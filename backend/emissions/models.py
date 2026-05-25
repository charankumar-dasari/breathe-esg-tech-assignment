from django.db import models


class EmissionRecord(models.Model):
    SOURCE_CHOICES = [
        ('SAP', 'SAP'),
        ('UTILITY', 'UTILITY'),
        ('TRAVEL', 'TRAVEL'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'PENDING'),
        ('APPROVED', 'APPROVED'),
        ('REJECTED', 'REJECTED'),
    ]

    source_type = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    activity_type = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)
    co2e = models.FloatField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    is_flagged = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity_type


class AuditLog(models.Model):
    record = models.ForeignKey(EmissionRecord, on_delete=models.CASCADE, related_name='audit_logs')
    action = models.CharField(max_length=100)
    old_status = models.CharField(max_length=20)
    new_status = models.CharField(max_length=20)
    changed_by = models.CharField(max_length=100, default='analyst')
    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.record.activity_type} - {self.action}"