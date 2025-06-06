# Generated by Django 5.1.4 on 2025-05-10 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VorstandMitglied',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('aufgabe', models.TextField()),
                ('rolle', models.CharField(choices=[('leiter', 'Leiter'), ('verwaltung', 'Verwaltung'), ('vorstand', 'Vorstand')], max_length=20)),
                ('geschlecht', models.CharField(choices=[('maennlich', 'Männlich'), ('weiblich', 'Weiblich')], max_length=10)),
                ('bild', models.ImageField(blank=True, null=True, upload_to='vorstandsbilder/')),
            ],
            options={
                'verbose_name': 'Vorstandsmitglied',
                'verbose_name_plural': 'Vorstandsmitglieder',
                'ordering': ['rolle', 'name'],
            },
        ),
    ]
