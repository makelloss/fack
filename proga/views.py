from .models import Department, ExchangeProgram, HomePageContent, Program
from django.shortcuts import get_object_or_404, render

from .models import Department, HomePageContent, Program


def home(request):
    content = HomePageContent.get_solo()
    return render(request, "proga/home.html", {"content": content})


def program_list(request):
    programs = Program.objects.select_related("department").all()
    return render(request, "proga/program_list.html", {"programs": programs})


def program_detail(request, pk):
    program = get_object_or_404(
        Program.objects.select_related("department").prefetch_related("disciplines"),
        pk=pk,
    )
    return render(request, "proga/program_detail.html", {"program": program})


def department_list(request):
    departments = Department.objects.prefetch_related("programs").all()
    return render(request, "proga/department_list.html", {"departments": departments})


def department_detail(request, pk):
    department = get_object_or_404(
        Department.objects.prefetch_related("programs", "teachers"), pk=pk
    )
    return render(request, "proga/department_detail.html", {"department": department})

def exchange_list(request):
    programs = ExchangeProgram.objects.order_by("deadline")
    return render(request, "proga/exchange_list.html", {"programs": programs})