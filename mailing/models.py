from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Message(models.Model):
    """Модель сообщения для рассылки"""
    header = models.CharField(max_length=100, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело письма')

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ('header',)

    def __str__(self):
        return self.header


class Mailing(models.Model):
    """Модель рассылки"""

    FREQUENCY = [
        ('DAY', 'раз в день'),
        ('WEEK', 'раз в неделю'),
        ('MONTH', 'раз в месяц')
    ]

    STATUS = [
        ('FINISH', 'завершена'),
        ('CREATE', 'создана'),
        ('START', 'запущена')
    ]

    time = models.TimeField(verbose_name='Время рассылки')
    frequency = models.CharField(max_length=100, choices=FREQUENCY, verbose_name='Периодичность')
    status = models.CharField(max_length=100, choices=STATUS, verbose_name='Статус')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, verbose_name='Сообщение', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='активность')

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('time',)

    def __str__(self):
        return f'Рассылка №{self.pk}'

    def delete(self, *args, **kwargs):
        """Функция, делающая пост не активным"""
        self.is_active = False
        self.save()


class MailingLogs(models.Model):
    """Модель логов рассылки"""
    STATUS = [
        ('Success', 'успешно'),
        ('Failure', 'отказ')
    ]

    data_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время отправки')
    status = models.CharField(max_length=100, choices=STATUS, verbose_name='Статус попытки')
    server_response = models.TextField(verbose_name='Ответ почтового сервера', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)
    mailing = models.ForeignKey(Mailing, on_delete=models.SET_NULL, verbose_name='Рассылка', **NULLABLE)
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, verbose_name='Сообщение', **NULLABLE)

    class Meta:
        verbose_name = 'лог отправки письма'
        verbose_name_plural = 'логи отправок писем'

    def __str__(self):
        return f'Лог {self.pk}'
