from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from farm_food_project.profiles.forms import ProfileForm
from farm_food_project.profiles.models import ProducerUserProfile


class ListProducersProfilesView(ListView):
    template_name = 'profiles/list_producers.html'
    context_object_name = 'producers'
    model = ProducerUserProfile


# @login_required
# def producer_profile_details(request):
#     profile = ProducerUserProfile.objects.get(pk=request.user.id)
#     if request.method == 'POST':
#         form = ProfileForm(
#             request.POST,
#             request.FILES,
#             instance=profile,
#         )
#         if form.is_valid():
#             form.save()
#             return redirect('producer details')
#     else:
#         form = ProfileForm(instance=profile)
#
#     # user_pets = Pet.objects.filter(user_id=request.user.id)
#
#     context = {
#         'form': form,
#         # 'pets': user_pets,
#         'profile': profile,
#     }
#
#     return render(request, 'profiles/producer_details.html', context)

class ProducerProfileDetailsView(LoginRequiredMixin, DetailView):
#     form_class = ProfileForm
#     template_name = 'profiles/producer_details.html'
#     success_url = reverse_lazy('producer details')
#     object = None
#
#     def get(self, request, *args, **kwargs):
#         self.object = ProducerUserProfile.objects.get(pk=request.user.id)
#         return super().get(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         self.object = ProducerUserProfile.objects.get(pk=request.user.id)
#         return super().post(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         self.object.name = form.cleaned_data['name']
#         self.object.description = form.cleaned_data['description']
#         self.object.location = form.cleaned_data['location']
#         self.object.phone_number = form.cleaned_data['phone_number']
#         self.object.profile_image = form.cleaned_data['profile_image']
#         self.object.save()
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['pets'] = Pet.objects.filter(user_id=self.request.user.id)
#         context['profile'] = self.object
#
#         return context
    model = ProducerUserProfile
    template_name = 'profiles/producer_profile.html'
    context_object_name = 'producer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        producer = context['producer']

        is_user = producer.user == self.request.user

        context['is_user'] = is_user

        return context


