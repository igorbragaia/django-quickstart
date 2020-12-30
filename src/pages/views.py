from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    print(request.user)
    my_context = {
        "my_text": "This is the homep age",
        "my_number": 123,
        "my_list": [123, 456, 789],
    }
    return render(request, "home.html", my_context)


def contact_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "contact.html", {})