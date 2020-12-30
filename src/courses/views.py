from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CourseForm, RawCourseForm
from .models import Course


def course_create_view(request):
    obj = Course.objects.get(id=1)
    form = CourseForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = CourseForm()

    context = {
        'form': form
    }

    return render(request, "courses/create.html", context)


def course_detail_view(request, id):
    try:
        obj = Course.objects.get(id=id)
    except Course.DoesNotExist:
        raise Http404

    context = {
        "object": obj
    }
    return render(request, "courses/detail.html", context=context)


def course_delete_view(request, id):
    try:
        obj = Course.objects.get(id=id)
    except Course.DoesNotExist:
        raise Http404

    if request.method == "POST":
        obj.delete()
        return redirect('../../')

    context = {
        "object": obj
    }
    return render(request, "courses/delete.html", context=context)


def course_list_view(request):
    queryset = Course.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "courses/list.html", context)