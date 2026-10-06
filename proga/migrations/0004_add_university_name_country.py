from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("proga", "0003_seed_exchangeprogram_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="exchangeprogram",
            name="university_name",
            field=models.CharField(default="", max_length=255, verbose_name="назва університету"),
        ),
        migrations.AddField(
            model_name="exchangeprogram",
            name="country",
            field=models.CharField(default="", max_length=100, verbose_name="країна"),
        ),
    ]