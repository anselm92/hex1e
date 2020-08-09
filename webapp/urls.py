from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from hex1e import settings
from webapp.views import BlogListView, RaffleListView, RaffleParticipantView

app_name = 'webapp'

urlpatterns = [

  path('index/', BlogListView.as_view(), name='blog-list'),
  path('index/<int:month>/<int:year>', BlogListView.as_view(), name='blog-list'),

  path('raffles/', RaffleListView.as_view(), name='raffle-list'),
  path('raffles/<int:raffle_id>/subscribe/', RaffleParticipantView.as_view(), name='raffle-participant-create'),

  path('success/', TemplateView.as_view(template_name='webapp/success.html'), name='success'),
  path('privacy-policy/', TemplateView.as_view(template_name='webapp/privacy-policy.html'), name='privacy-policy'),
  path('impressum/', TemplateView.as_view(template_name='webapp/impressum.html'), name='impressum'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
