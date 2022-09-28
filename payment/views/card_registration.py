from django.views.generic.edit import FormView
from payment.forms.card_registration_form import CardRegistrationForm


class CardRegistrationFormView(FormView):
    template_name = "card_registration.html"
    form_class = CardRegistrationForm
    success_url = "/thanks/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)
