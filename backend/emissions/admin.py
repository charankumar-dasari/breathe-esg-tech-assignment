from django.contrib import admin
from .models import EmissionRecord, AuditLog


@admin.register(EmissionRecord)
class EmissionRecordAdmin(admin.ModelAdmin):
    list_display = (
        'source_type',
        'activity_type',
        'quantity',
        'unit',
        'status',
        'is_flagged',
        'uploaded_at'
    )

    list_filter = ('source_type', 'status', 'is_flagged')

    search_fields = ('activity_type',)


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = (
        'record',
        'action',
        'old_status',
        'new_status',
        'changed_by',
        'changed_at'
    )