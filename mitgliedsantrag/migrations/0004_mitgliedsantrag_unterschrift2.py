# Generated by Django 5.1.4 on 2025-05-24 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mitgliedsantrag', '0003_alter_mitgliedsantrag_unterschrift'),
    ]

    operations = [
        migrations.AddField(
            model_name='mitgliedsantrag',
            name='unterschrift2',
            field=models.ImageField(blank=True, null=True, upload_to='mitgliedsantrag/signaturen/', verbose_name='2. Unterschrift'),
        ),
    ]
