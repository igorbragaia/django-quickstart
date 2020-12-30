from django import forms

from .models import Course


class CourseForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "Your title"
    }))
    description = forms.CharField(required=False,widget=forms.Textarea(attrs={
        "placeholder": "Your description",
        "rows": 20,
        "cols": 100,
    }))

    class Meta:
        model = Course
        fields = [
            'title',
            'description',
            'price',
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" not in title:
            raise forms.ValidationError("This is not a valid title (must contain CFE)")

        return title


class RawCourseForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
