# Generated by Django 2.0.4 on 2018-10-10 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("marksapp", "0011_profile")]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="visibility",
            field=models.CharField(
                choices=[("PB", "Public"), ("PV", "Private")],
                default="PB",
                max_length=2,
            ),
        )
    ]
