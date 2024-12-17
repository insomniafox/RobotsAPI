from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = "admin"
    MANAGER = "manager"
    CUSTOMER = "customer"

    ROLES_CHOICES = (
        (ADMIN, "Администратор"),
        (MANAGER, "Менеджер"),
        (CUSTOMER, "Клиент"),
    )

    role = models.CharField('Роль', max_length=32, choices=ROLES_CHOICES)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
