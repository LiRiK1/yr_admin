from django.db import models
from django.utils import timezone


class User(models.Model):
    telegram_id = models.BigIntegerField(null=False)
    user_name = models.CharField(max_length=255, null=False)
    tg_name = models.CharField(max_length=255, null=False)
    user_phone = models.CharField(max_length=255, blank=True, null=True)
    user_mail = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField(default=1)
    user_coin = models.IntegerField(default=0)
    wallet = models.IntegerField(default=0)
    date_register = models.DateField(default=timezone.now)

    class Meta:
        managed = True
        db_table = 'users'

    def __str__(self):
        return self.user_name


class JuristName(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    specialization = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    rating = models.FloatField(default=0.0)

    class Meta:
        managed = True
        db_table = 'juristName'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PaymentStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    COMPLETED = "completed", "Completed"
    FAILED = "failed", "Failed"


class Payment(models.Model):
    user = models.ForeignKey(User, related_name='payments', on_delete=models.CASCADE)
    jurist = models.ForeignKey(JuristName, related_name='payments', on_delete=models.CASCADE)
    amount = models.FloatField(null=False)
    currency = models.CharField(max_length=10, default='RUB')
    status = models.CharField(
        max_length=10,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING,
    )
    date_created = models.DateField(default=timezone.now, null=False)
    date_completed = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'payments'

    def __str__(self):
        return f"Payment {self.id} - {self.status}"


class Document(models.Model):
    user = models.ForeignKey(User, related_name='documents', on_delete=models.CASCADE)
    jurist = models.ForeignKey(JuristName, related_name='documents', on_delete=models.CASCADE)
    document_path = models.CharField(max_length=255, null=False)
    upload_date = models.DateField(default=timezone.now, null=False)

    class Meta:
        managed = True
        db_table = 'documents'

    def __str__(self):
        return self.document_path
