from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from blood.models import Donor


class DonorList(ListView):
    model = Donor


class DonorDetail(DetailView):
    model = Donor


class DonorCreate(CreateView):
    model = Donor
    fields = ['first_name', 'last_name']


class DonorUpdate(UpdateView):
    model = Donor
    fields = ['first_name', 'last_name']


class DonorDelete(DeleteView):
    model = Donor
    success_url = reverse_lazy('donor_list')