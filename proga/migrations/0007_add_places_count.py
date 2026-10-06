from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("proga", "0006_remove_university_field"),
    ]

    operations = [
        migrations.AddField(
            model_name="exchangeprogram",
            name="places_count",
            field=models.PositiveIntegerField(default=0, verbose_name="кількість місць"),
        ),
    ]