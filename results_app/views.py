from django.shortcuts import render

from .forms import ResultLookupForm
from .models import Student


def check_result(request):
    results = None
    student = None
    error = None

    if request.method == "POST":
        form = ResultLookupForm(request.POST)
        if form.is_valid():
            reg_number = form.cleaned_data["reg_number"].strip()
            pin = form.cleaned_data["pin"].strip()
            try:
                student = Student.objects.get(reg_number__iexact=reg_number, pin=pin)
                results = student.results.select_related("exam", "subject").order_by(
                    "exam__year", "subject__name"
                )
                if not results.exists():
                    error = "No results have been published for this student yet."
            except Student.DoesNotExist:
                error = "Registration number or PIN is incorrect. Please try again."
    else:
        form = ResultLookupForm()

    return render(
        request,
        "results/lookup.html",
        {"form": form, "results": results, "student": student, "error": error},
    )