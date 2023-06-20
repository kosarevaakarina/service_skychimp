from django.urls import reverse_lazy
from django.views import generic
from mailing.models import *


class MailingListView(generic.ListView):
    model = Mailing
    extra_context = {'title': 'Рассылки'}

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset


class MailingDetailView(generic.DetailView):
    model = Mailing


class MailingCreateView(generic.CreateView):
    model = Mailing
    fields = '__all__'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingUpdateView(generic.UpdateView):
    model = Mailing
    fields = '__all__'
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDeleteView(generic.DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')
