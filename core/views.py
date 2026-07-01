from django.shortcuts import render, redirect
from django.contrib import messages as flash
from .models import GalleryPhoto, NewsEvent, ContactMessage


def home(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        contact_info = request.POST.get("contact_info", "").strip()
        message = request.POST.get("message", "").strip()
        if name and contact_info and message:
            ContactMessage.objects.create(
                name=name, contact_info=contact_info, message=message
            )
            flash.success(
                request, "Thank you — your message has been received. We'll get back to you soon."
            )
        else:
            flash.error(request, "Please fill in every field before sending.")
        return redirect("home")

    context = {
        "gallery_photos": GalleryPhoto.objects.all()[:8],
        "news_items": NewsEvent.objects.all()[:6],
    }
    return render(request, "home.html", context)
