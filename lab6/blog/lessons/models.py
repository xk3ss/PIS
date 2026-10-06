from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LessonType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    experience = models.PositiveIntegerField(default=0, help_text="стаж в годах")
    subjects = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}".strip()


class Group(models.Model):
    name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    students_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lesson_type = models.ForeignKey(LessonType, on_delete=models.CASCADE)
    hours = models.PositiveIntegerField(default=0)
    rate_per_hour = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher} — {self.group} — {self.subject}"

    def get_total_payment(self):
        return self.hours * self.rate_per_hour