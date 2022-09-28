from django.urls import path
from payment.views.card_payment import CardPaymentFormView
from payment.views.card_registration import CardRegistrationFormView

from payment.views.home import HomeView
from payment.views.pix_payment import PixPaymentFormView
from payment.views.user_registration import UserRegistrationFormView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("pix-payment", PixPaymentFormView.as_view(), name="pix_payment"),
    path("card-payment", CardPaymentFormView.as_view(), name="card_payment"),
    path(
        "card-registration",
        CardRegistrationFormView.as_view(),
        name="card_registration",
    ),
    path(
        "user-registration",
        UserRegistrationFormView.as_view(),
        name="user_registration",
    ),
]
