from django import forms

class NumbersInputForm(forms.Form):
    numbers = forms.CharField(
        label="Enter your numbers(comma-separated):",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "e.g. 1, 2, 3, 4",
                "class": "form-control",
            }
        ),
    )
    file = forms.FileField(
        label="Upload File (in a file, the number must have a comma to separate) ",
        required=False,
        widget=forms.ClearableFileInput(attrs={"class": "form-control"}),
    )

    def clean(self):
        cleaned = super().clean()
        if not cleaned.get("numbers") and not cleaned.get("file"):
            raise forms.ValidationError("Provide numbers or upload a file.")
        return cleaned
