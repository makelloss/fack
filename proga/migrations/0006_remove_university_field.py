from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("proga", "0005_split_university_into_name_and_country"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="exchangeprogram",
            name="university",
        ),
    ]