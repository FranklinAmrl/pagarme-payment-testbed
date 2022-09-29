from django.shortcuts import redirect

from ..views import gateway

from django.contrib import messages


from django.views.generic.edit import FormView

from payment.forms.user_registration_form import UserRegistrationForm


class MobilePhone:
    def __init__(self, country_code, area_code, number) -> None:
        self.country_code = country_code
        self.area_code = area_code
        self.number = number


class Phones:
    def __init__(self, mobile_phone) -> None:
        self.mobile_phone = mobile_phone


class Customer:
    def __init__(self, name, email, document, type, phones) -> None:
        self.name = name
        self.email = email
        self.document = document
        self.type = type
        self.phones = phones


class UserRegistrationFormView(FormView):
    template_name = "user_registration.html"
    form_class = UserRegistrationForm
    success_url = "/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        data = form.cleaned_data
        obj_mobile_phone = MobilePhone(
            country_code=data.get("country_code"),
            area_code=data.get("area_code"),
            number=data.get("number"),
        ).__dict__

        obj_phones = Phones(mobile_phone=obj_mobile_phone).__dict__

        payload = Customer(
            name=data.get("name"),
            email=data.get("email"),
            document=data.get("document"),
            type="individual",
            phones=obj_phones,
        ).__dict__

        try:
            gateway.insert_customer(payload)
        except Exception as e:
            messages.add_message(self.request, messages.ERROR, str(e))
            # form.add_error(None, str(e))
            return self.form_invalid(form)
        messages.add_message(
            self.request, messages.SUCCESS, message="Registro feito com sucesso."
        )
        return redirect(self.success_url)
