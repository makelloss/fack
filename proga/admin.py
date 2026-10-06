from django.contrib import admin

from .models import Department, Discipline, ExchangeProgram, HomePageContent, Program, Teacher


class TeacherInline(admin.TabularInline):
    model = Teacher
    extra = 1


class ProgramInline(admin.TabularInline):
    model = Program
    extra = 0
    fields = ("code", "name")
    show_change_link = True


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "head")
    search_fields = ("name", "head")
    inlines = [TeacherInline, ProgramInline]


class DisciplineInline(admin.TabularInline):
    model = Discipline
    extra = 1


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "department", "coordinator_name")
    list_filter = ("department",)
    search_fields = ("name", "code")
    inlines = [DisciplineInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "degree", "department")
    list_filter = ("department",)
    search_fields = ("name",)


@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ("title",)

    def has_add_permission(self, request):
        return not HomePageContent.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ExchangeProgram)
class ExchangeProgramAdmin(admin.ModelAdmin):
    list_display = ("university_name", "country", "places", "deadline")
    list_filter = ("country",)
    search_fields = ("university_name", "country")