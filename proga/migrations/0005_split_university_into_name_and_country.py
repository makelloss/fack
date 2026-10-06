import re

from django.db import migrations



def split_university(value):
    value = value.strip()
    match = re.match(r"^(.*)\((.*)\)\s*$", value)
    if match:
        return match.group(1).strip().rstrip(","), match.group(2).strip()
    if " - " in value:
        name, country = value.split(" - ", 1)
        return name.strip(), country.strip()
    if "," in value:
        name, country = value.rsplit(",", 1)
        return name.strip(), country.strip()
    return value, ""


def split_forward(apps, schema_editor):
    ExchangeProgram = apps.get_model("proga", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        name, country = split_university(program.university)
        program.university_name = name
        program.country = country
        program.save(update_fields=["university_name", "country"])


def split_backward(apps, schema_editor):
    ExchangeProgram = apps.get_model("proga", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        program.university = f"{program.university_name}, {program.country}"
        program.save(update_fields=["university"])


class Migration(migrations.Migration):

    dependencies = [
        ("proga", "0004_add_university_name_country"),
    ]

    operations = [
        migrations.RunPython(split_forward, split_backward),
    ]