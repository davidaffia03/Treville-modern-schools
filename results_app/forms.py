from django import forms


class ResultLookupForm(forms.Form):
    reg_number = forms.CharField(
        label="Registration Number",
        max_length=20,
        widget=forms.TextInput(attrs={"placeholder": "e.g. STU-2026-001", "autofocus": True}),
    )
    pin = forms.CharField(
        label="PIN",
        max_length=6,
        widget=forms.PasswordInput(attrs={"placeholder": "6-digit PIN"}),
    )