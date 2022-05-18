from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'created_by', 'created_at', 'updated_at']
