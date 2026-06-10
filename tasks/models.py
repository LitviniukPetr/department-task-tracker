from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва підрозділу")

    class Meta:
        verbose_name = "Підрозділ"
        verbose_name_plural = "Підрозділи"

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активне'),
        ('done', 'Виконане'),
    ]

    title = models.CharField(max_length=300, verbose_name="Назва завдання")
    description = models.TextField(blank=True, verbose_name="Опис")
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        related_name='tasks', verbose_name="Підрозділ"
    )
    deadline = models.DateField(verbose_name="Дедлайн")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES,
        default='active', verbose_name="Статус"
    )
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, verbose_name="Створив"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Завдання"
        verbose_name_plural = "Завдання"
        ordering = ['deadline']

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name="Підрозділ"
    )
    is_manager = models.BooleanField(default=False, verbose_name="Менеджер")
    is_supervisor = models.BooleanField(default=False, verbose_name="Supervisor (всі підрозділи)")

    class Meta:
        verbose_name = "Профіль"
        verbose_name_plural = "Профілі"

    def __str__(self):
        return f"{self.user.username} — {self.department}"