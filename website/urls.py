from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.auth.models import User

def temp_reset_password(request):
    try:
        user = User.objects.get(username="trevilleadmin")
        user.set_password("jessytres")  # <-- change this to your new password
        user.save()
        return HttpResponse("Password changed successfully.")
    except User.DoesNotExist:
        return HttpResponse("User not found.")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("temp-reset-x92k4/", temp_reset_password),  # <-- our secret temporary URL
    path("", include("core.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)