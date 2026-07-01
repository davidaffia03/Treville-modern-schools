from django.contrib import admin
from .models import GalleryPhoto, NewsEvent, ContactMessage


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ("caption", "uploaded_at")


@admin.register(NewsEvent)
class NewsEventAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "date_label", "created_at")
    list_filter = ("type",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "contact_info", "submitted_at")
    readonly_fields = ("name", "contact_info", "message", "submitted_at")