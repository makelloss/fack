from django.db import models
from django.utils import timezone


class Department(models.Model):

    name = models.CharField("назва кафедри", max_length=255)
    head = models.CharField("завідувач кафедри", max_length=255)
    description = models.TextField("опис кафедри", blank=True)

    class Meta:
        verbose_name = "кафедра"
        verbose_name_plural = "кафедри"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Program(models.Model):

    name = models.CharField("назва спеціальності", max_length=255)
    code = models.CharField("код спеціальності", max_length=20)
    description = models.TextField("опис спеціальності")
    coordinator_name = models.CharField("ім'я координатора набору", max_length=255)
    coordinator_contact = models.CharField("контакт координатора набору", max_length=255)
    department = models.ForeignKey(
        Department,
        verbose_name="випускова кафедра",
        related_name="programs",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "спеціальність"
        verbose_name_plural = "спеціальності"
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} {self.name}"

    def short_description(self, word_count=50):
        words = self.description.split()
        if len(words) <= word_count:
            return self.description
        return " ".join(words[:word_count]) + "…"


class Discipline(models.Model):

    name = models.CharField("назва дисципліни", max_length=255)
    program = models.ForeignKey(
        Program,
        verbose_name="спеціальність",
        related_name="disciplines",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "дисципліна"
        verbose_name_plural = "дисципліни"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Teacher(models.Model):

    name = models.CharField("ім'я", max_length=255)
    position = models.CharField("посада", max_length=255)
    degree = models.CharField("науковий ступінь", max_length=255, blank=True)
    department = models.ForeignKey(
        Department,
        verbose_name="кафедра",
        related_name="teachers",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "викладач"
        verbose_name_plural = "викладачі"
        ordering = ["name"]

    def __str__(self):
        return self.name


class HomePageContent(models.Model):

    title = models.CharField("назва факультету", max_length=255)
    intro = models.TextField("короткий опис факультету")
    about = models.TextField("основна інформація про факультет")
    address = models.CharField("адреса", max_length=255, blank=True)
    phone = models.CharField("телефон", max_length=50, blank=True)
    email = models.EmailField("email", blank=True)
    website = models.URLField("сайт", blank=True)

    class Meta:
        verbose_name = "текст головної сторінки"
        verbose_name_plural = "текст головної сторінки"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(
            pk=1,
            defaults={
                "title": "Назва факультету",
                "intro": "Інформація ще не додана.",
                "about": "Інформація ще не додана.",
            },
        )
        return obj


class ExchangeProgram(models.Model):

    university_name = models.CharField("назва університету", max_length=255)
    country = models.CharField("країна", max_length=100)
    languages = models.CharField("мови навчання", max_length=255)
    places = models.PositiveIntegerField("кількість місць")
    deadline = models.DateField("дедлайн подачі")
    description = models.TextField("опис")

    class Meta:
        verbose_name = "програма обміну"
        verbose_name_plural = "програми обміну"

    def __str__(self):
        return f"{self.university_name} ({self.country})"

    @property
    def is_open(self):
        return self.deadline >= timezone.localdate()