import re

from django.db import migrations



def extract_number(text):
    match = re.search(r"\d+", text)
    return int(match.group()) if match else 0


def convert_forward(apps, schema_editor):
    ExchangeProgram = apps.get_model("proga", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        program.places_count = extract_number(program.places)
        program.save(update_fields=["places_count"])


def convert_backward(apps, schema_editor):
    ExchangeProgram = apps.get_model("proga", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        program.places = str(program.places_count)
        program.save(update_fields=["places"])


class Migration(migrations.Migration):

    dependencies = [
        ("proga", "0007_add_places_count"),
    ]

    operations = [
        migrations.RunPython(convert_forward, convert_backward),
    ]