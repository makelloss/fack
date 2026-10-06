from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("proga", "0008_convert_places_to_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="exchangeprogram",
            name="places",
        ),
    ]