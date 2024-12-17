from django.db import models


class RobotSerial(models.Model):
    serial = models.CharField('Серия робота', max_length=6, primary_key=True)

    def __str__(self):
        return self.serial

    class Meta:
        verbose_name = 'Серия робота'
        verbose_name_plural = 'Серии роботов'


class RobotModel(models.Model):
    model = models.CharField('Модель робота', max_length=6, primary_key=True)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Модель робота'
        verbose_name_plural = 'Модели роботов'


class Robot(models.Model):
    serial = models.ForeignKey(RobotSerial, on_delete=models.CASCADE, verbose_name='Серия')
    model = models.ForeignKey(RobotModel, on_delete=models.CASCADE, verbose_name='Модель')
    version = models.CharField('Версия', max_length=2)
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    quantity = models.PositiveIntegerField('Количество роботов в наличии', default=0)

    def __str__(self):
        return f'{self.serial_id} {self.model_id}'

    class Meta:
        verbose_name = 'Робот'
        verbose_name_plural = 'Роботы'
        ordering = ('-created_at',)
        unique_together = [('serial_id', 'model_id')]
