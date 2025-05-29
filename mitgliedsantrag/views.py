import io
import base64
import datetime
from django.shortcuts import render, redirect
from .forms import MitgliedsantragForm
from .models import Mitgliedsantrag
from django.core.files.base import ContentFile
from django.conf import settings

from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PyPDF2 import PdfReader, PdfWriter


def mitgliedsantrag_view(request):
    beitrags_range = range(5, 105, 5)  # 5 bis 100 in 5er-Schritten

    if request.method == "POST":
        form = MitgliedsantragForm(request.POST, request.FILES)
        unterschrift_data = request.POST.get("unterschrift_data")
        unterschrift_data_2 = request.POST.get("unterschrift_data_2")

        if form.is_valid() and unterschrift_data:
            antrag = form.save(commit=False)

            # Erste Unterschrift speichern
            format, imgstr = unterschrift_data.split(';base64,')
            unterschrift_file = ContentFile(base64.b64decode(imgstr), name=f"unterschrift_{antrag.name}.png")
            antrag.unterschrift = unterschrift_file

            # Zweite Unterschrift (optional)
            if unterschrift_data_2:
                format, imgstr = unterschrift_data_2.split(';base64,')
                zweite_unterschrift_file = ContentFile(base64.b64decode(imgstr), name=f"unterschrift2_{antrag.name}.png")
                antrag.unterschrift2 = zweite_unterschrift_file

            # PDF generieren
            packet = io.BytesIO()
            can = canvas.Canvas(packet)

            # Textfelder platzieren (Koordinaten anpassen!)
            can.drawString(300, 660, antrag.name)
            can.drawString(300, 620, antrag.adresse)
            can.drawString(300, 580, antrag.mobilnummer)
            can.drawString(300, 540, antrag.kontoinhaber)
            can.drawString(300, 500, antrag.iban)
            can.drawString(300, 460, antrag.bic)
            can.drawString(350, 415, f"{antrag.beitrag} EUR")
            if antrag.zahlungstermin == "1.":
                can.drawString(215, 380, "X")
            elif antrag.zahlungstermin == "15.":
                can.drawString(350, 380, "X")
            can.drawString(70, 140, datetime.date.today().strftime("%d.%m.%Y"))

            # Erste Unterschrift
            signature_image = ImageReader(antrag.unterschrift)
            can.drawImage(signature_image, 140, 120, width=150, height=50, mask='auto')

            # Zweite Unterschrift 150 px rechts daneben
            if unterschrift_data_2:
                zweite_signature_image = ImageReader(antrag.unterschrift2)
                can.drawImage(zweite_signature_image, 290, 120, width=150, height=50, mask='auto')

            can.save()

            # PDF zusammenführen
            packet.seek(0)
            overlay = PdfReader(packet)
            existing_pdf = PdfReader(open(settings.BASE_DIR / "static/pdf/Mitgliedsantrag_Neu_2024.pdf", "rb"))
            output = PdfWriter()

            page = existing_pdf.pages[0]
            page.merge_page(overlay.pages[0])
            output.add_page(page)

            output_stream = io.BytesIO()
            output.write(output_stream)
            antrag.pdf_datei.save(f"mitgliedsantrag_{antrag.name}.pdf", ContentFile(output_stream.getvalue()))

            antrag.save()

            # PDF-URL in Session speichern für Erfolgseite
            request.session['pdf_url'] = antrag.pdf_datei.url

            return redirect("mitgliedsantrag_success")
    else:
        form = MitgliedsantragForm()

    return render(request, "mitgliedsantrag/formular.html", {
        "form": form,
        "beitrags_range": beitrags_range,
    })


def mitgliedsantrag_success(request):
    pdf_url = request.session.pop('pdf_url', None)
    return render(request, "mitgliedsantrag/erfolg.html", {"pdf_url": pdf_url})
