from django.views.generic.edit import FormView

from payment.forms.card_payment_form import CardPaymentForm


class CardPaymentFormView(FormView):
    template_name = "card_payment.html"
    form_class = CardPaymentForm
    success_url = "/thanks/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)
