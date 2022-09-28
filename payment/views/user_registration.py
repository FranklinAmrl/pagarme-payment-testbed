from django.views.generic.edit import FormView

from payment.forms.user_registration_form import UserRegistrationForm


class UserRegistrationFormView(FormView):
    template_name = "user_registration.html"
    form_class = UserRegistrationForm
    success_url = "/thanks/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)
