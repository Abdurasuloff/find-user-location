# Generated by Django 4.1 on 2022-08-26 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_qrcode_qr_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="qrcode",
            name="name",
            field=models.CharField(max_length=300),
        ),
    ]
