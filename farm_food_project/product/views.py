from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from farm_food_project.product.forms import EditProductForm
from farm_food_project.product.models import Product


class ListProductsView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'


class ProductDetailsView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product/product_details.html'
    context_object_name = 'product'


class CreateProductView(CreateView):
    model = Product
    template_name = 'product/create_product.html'
    fields = ('product_type', 'name', 'quantity', 'price', 'product_image',)
    success_url = reverse_lazy('list products')

    # def get_success_url(self):
    #     product_id = self.kwargs['pk']
    #     return reverse_lazy('product details', kwargs={'pk': product_id})

    def form_valid(self, form):
        product = form.save(commit=False)
        product.producer_profile = self.request.user.produceruserprofile
        product.save()
        return super().form_valid(form)


class EditProductView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'product/edit_product.html'
    form_class = EditProductForm

    def get_success_url(self):
        product_id = self.kwargs['pk']
        return reverse_lazy('product details', kwargs={'pk': product_id})


class DeleteProductView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('list products')