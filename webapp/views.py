from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView
from django.views.generic.base import ContextMixin

from webapp.forms import RaffleForm
from webapp.models import Raffle, Blog, RaffleParticipant


class BaseView(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['archive_dates'] = Blog.objects.dates('date_posted', 'month', order='DESC')
        return context


class BlogListView(BaseView, ListView):
    model = Blog

    def get_queryset(self):
        return super().get_queryset().filter(
            date_posted__year=self.kwargs['year'],
            date_posted__month=self.kwargs['month']
        ) if {'year', 'month'}.issubset(self.kwargs) else super().get_queryset()


class RaffleListView(ListView):
    model = Raffle
    value = 1


class RaffleParticipantView(CreateView):
    model = RaffleParticipant
    form_class = RaffleForm
    success_url = reverse_lazy('webapp:success')

    def form_valid(self, form):
        raffle = get_object_or_404(Raffle, pk=self.kwargs['raffle_id'], active=True)
        form.instance.raffle = raffle
        try:
            valid = super(RaffleParticipantView, self).form_valid(form)
            messages.success(self.request, "Thanks for participating in this raffle. We'll notify the winner "
                                           "via e-mail")
            return valid
        except IntegrityError:
            messages.error(self.request, "You've already participated in this raffle.")
            return super(RaffleParticipantView, self).form_invalid(form)
