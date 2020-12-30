from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import ProductModelForm
from .models import Product


class ProductObjectMixin(object):
    model = Product

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj


class ProductCreateView(View):
    template_name = "products/create.html"

    def get(self, request, *args, **kwargs):
        form = ProductModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)


class ProductDeleteView(ProductObjectMixin, View):
    template_name = "products/delete.html"

    def get(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('../../')
        return render(request, self.template_name, context)


class ProductUpdateView(ProductObjectMixin, View):
    template_name = "products/create.html"

    def get(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = ProductModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = ProductModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)


class ProductListView(View):
    template_name = "products/list.html"
    queryset = Product.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)


class ProductDetailView(ProductObjectMixin, View):
    template_name = "products/detail.html"

    def get(self, request, id=None, *args, **kwargs):
        context = {'object': self.get_object()}
        return render(request, self.template_name, context)
