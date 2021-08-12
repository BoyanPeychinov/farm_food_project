from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, UpdateView

from farm_food_project.product.models import Product
from farm_food_project.profiles.forms import ProducerProfileForm, ConsumerProfileForm, EditProducerProfileForm, \
    EditConsumerProfileForm
from farm_food_project.profiles.models import ProducerUserProfile, ConsumerUserProfile


class ListProducersProfilesView(ListView):
    template_name = 'profiles/list_producers.html'
    context_object_name = 'producers'
    model = ProducerUserProfile


class ProducerDetailsFromListView(LoginRequiredMixin, DetailView):
    model = ProducerUserProfile
    template_name = 'profiles/producer_profile_from_list.html'
    context_object_name = 'producer'
    login_url = 'sign in'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        producer = context['producer']

        is_user = producer.user == self.request.user

        context['is_user'] = is_user

        return context

    def get_permission_denied_message(self):
        self.permission_denied_message = "You must log in to see farm's details"
        return self.permission_denied_message


class ProducerProfileDetailsView(LoginRequiredMixin, FormView):
    form_class = ProducerProfileForm
    template_name = 'profiles/producer_profile.html'
    success_url = reverse_lazy('producer details')
    object = None

    def get(self, request, *args, **kwargs):
        self.object = ProducerUserProfile.objects.get(pk=request.user.id)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = ProducerUserProfile.objects.get(pk=request.user.id)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object.name = form.cleaned_data['name']
        self.object.description = form.cleaned_data['description']
        self.object.location = form.cleaned_data['location']
        self.object.phone_number = form.cleaned_data['phone_number']
        self.object.profile_image = form.cleaned_data['profile_image']
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        is_user = self.object.user == self.request.user

        context['products'] = Product.objects.filter(id=self.request.user.id)
        context['is_user'] = is_user
        context['producer'] = self.object

        return context


class EditProducerProfileView(LoginRequiredMixin, UpdateView):
    model = ProducerUserProfile
    form_class = EditProducerProfileForm
    template_name = 'profiles/edit_producer.html'
    success_url = reverse_lazy('producer details')


class ConsumerProfileDetailsView(LoginRequiredMixin, FormView):
    form_class = ConsumerProfileForm
    template_name = 'profiles/customer_profile.html'
    success_url = reverse_lazy('consumer details')
    object = None

    def get(self, request, *args, **kwargs):
        self.object = ConsumerUserProfile.objects.get(pk=request.user.id)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = ConsumerUserProfile.objects.get(pk=request.user.id)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        self.object.profile_image = form.cleaned_data['profile_image']
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['consumer'] = self.object

        return context


class EditConsumerProfileView(LoginRequiredMixin, UpdateView):
    model = ConsumerUserProfile
    form_class = EditConsumerProfileForm
    template_name = 'profiles/edit_consumer.html'
    success_url = reverse_lazy('list products')