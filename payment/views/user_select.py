from django.conf import settings
from django.shortcuts import redirect

from django.views.generic.edit import FormView

from payment.forms.user_select_form import UserSelectForm

from ..views import gateway


class UserSelectFormView(FormView):
    template_name = "user_select.html"
    form_class = UserSelectForm

    def form_valid(self, form):
        data = form.cleaned_data

        customer_id = str(data.get("customer_id"))

        self.success_url = f"/card-payment?customer_id={customer_id}"

        return redirect(self.success_url)
