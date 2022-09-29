from django.shortcuts import redirect, render

from django.contrib import messages

from django.views.generic.edit import FormView

from payment.forms.card_registration_form import CardRegistrationForm

from ..views import gateway


class BillingAddress:
    def __init__(self, country, state, city, zip_code, line_1) -> None:
        self.country = country
        self.state = state
        self.city = city
        self.zip_code = zip_code
        self.line_1 = line_1


class Card:
    def __init__(
        self,
        number,
        holder_name,
        exp_month,
        exp_year,
        cvv,
        billing_address,
    ) -> None:
        self.number = number
        self.holder_name = holder_name
        self.exp_month = exp_month
        self.exp_year = exp_year
        self.cvv = cvv
        self.billing_address = billing_address


class CardRegistrationFormView(FormView):
    template_name = "card_registration.html"
    form_class = CardRegistrationForm
    success_url = "/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        data = form.cleaned_data
        obj_billing_address = BillingAddress(
            country=data.get("country"),
            state=data.get("state"),
            city=data.get("city"),
            zip_code=data.get("zip_code"),
            line_1=data.get("line_1"),
        ).__dict__

        payload = Card(
            number=data.get("number"),
            holder_name=data.get("holder_name"),
            exp_month=int(data.get("exp_month")),
            exp_year=int(data.get("exp_year")),
            cvv=data.get("cvv"),
            billing_address=obj_billing_address,
        ).__dict__

        customer_id = data.get("customer_id")

        try:
            gateway.insert_card(customer_id=customer_id, payload=payload)
        except Exception as e:
            messages.add_message(self.request, messages.ERROR, str(e))
            # form.add_error(None, str(e))
            return self.form_invalid(form)

        messages.add_message(
            self.request, messages.SUCCESS, message="Registro feito com sucesso."
        )
        return redirect(self.success_url)
