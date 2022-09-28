from django.urls import path

from payment.views.home import HomeView
from payment.views.pix_payment import PixPaymentFormView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("pix-payment", PixPaymentFormView.as_view(), name="pix_payment"),
]
