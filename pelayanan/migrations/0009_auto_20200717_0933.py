# Generated by Django 3.0.8 on 2020-07-17 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelayanan', '0008_pengaduans_respon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengaduan',
            name='respon',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pengaduans',
            name='respon',
            field=models.TextField(blank=True, null=True),
        ),
    ]
