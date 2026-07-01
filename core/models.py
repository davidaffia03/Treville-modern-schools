from django.db import models


class GalleryPhoto(models.Model):
    image = models.ImageField(upload_to="gallery/")
    caption = models.CharField(max_length=120, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return self.caption or f"Photo {self.pk}"


class NewsEvent(models.Model):
    NEWS = "news"
    EVENT = "event"
    TYPE_CHOICES = [(NEWS, "News"), (EVENT, "Event")]

    title = models.CharField(max_length=150)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=NEWS)
    date_label = models.CharField(max_length=60, help_text="e.g. 12 July 2026")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=150, help_text="Email or phone")
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.name} — {self.submitted_at:%d %b %Y}"
