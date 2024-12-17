from django.db import models


class Order(models.Model):
    customer = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Клиент')
    robot = models.ForeignKey('robots.Robot', on_delete=models.CASCADE, verbose_name='Робот')
    created_at = models.DateTimeField('Создан', auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.robot}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created_at',)
