from django.views.generic.edit import FormView

from payment.forms.pix_payment_form import PixPaymentForm


class PixPaymentFormView(FormView):
    template_name = "pix_payment.html"
    form_class = PixPaymentForm
    success_url = "/thanks/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)
