from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("proga", "0009_remove_old_places_field"),
    ]

    operations = [
        migrations.RenameField(
            model_name="exchangeprogram",
            old_name="places_count",
            new_name="places",
        ),
    ]