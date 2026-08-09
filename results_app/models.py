import random
import string

from django.db import models


def generate_pin():
    return "".join(random.choices(string.digits, k=6))


class Student(models.Model):
    reg_number = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=150)
    pin = models.CharField(max_length=6, default=generate_pin, editable=False)

    def __str__(self):
        return f"{self.reg_number} - {self.full_name}"


class Exam(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.year})"


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="results")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="results")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=5, blank=True)

    class Meta:
        unique_together = ("student", "exam", "subject")

    def save(self, *args, **kwargs):
        if not self.grade:
            self.grade = self.compute_grade()
        super().save(*args, **kwargs)

    def compute_grade(self):
        s = float(self.score)
        if s >= 70:
            return "A"
        if s >= 60:
            return "B"
        if s >= 50:
            return "C"
        if s >= 45:
            return "D"
        if s >= 40:
            return "E"
        return "F"

    def __str__(self):
        return f"{self.student.reg_number} - {self.subject} - {self.score}"