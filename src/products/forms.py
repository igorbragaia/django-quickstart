from django import forms

from .models import Product


class ProductModelForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "Your title"
    }))
    description = forms.CharField(required=False,widget=forms.Textarea(attrs={
        "placeholder": "Your description",
        "rows": 20,
        "cols": 100,
    }))

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
        ]

