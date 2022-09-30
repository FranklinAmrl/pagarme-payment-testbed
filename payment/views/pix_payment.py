from django.conf import settings

from django.views.generic.edit import FormView

from payment.forms.pix_payment_form import PixPaymentForm

from ..views import gateway


class Options:
    def __init__(self, charge_processing_fee, charge_remainder_fee, liable) -> None:
        self.charge_processing_fee = charge_processing_fee
        self.charge_remainder_fee = charge_remainder_fee
        self.liable = liable


class Split:
    def __init__(self, options, type, amount, recipient_id) -> None:
        self.options = options
        self.type = type
        self.amount = amount
        self.recipient_id = recipient_id


class Pix:
    def __init__(self, expires_in) -> None:
        self.expires_in = expires_in


class Payments:
    def __init__(self, payment_method, pix, split) -> None:
        self.payment_method = payment_method
        self.pix = pix
        self.split = split


class Items:
    def __init__(self, amount, description, quantity, code) -> None:
        self.amount = amount
        self.description = description
        self.quantity = quantity
        self.code = code


class PixPayment:
    def __init__(self, customer_id, items, payments) -> None:
        self.customer_id = customer_id
        self.items = items
        self.payments = payments


class PixPaymentFormView(FormView):
    template_name = "pix_payment.html"
    form_class = PixPaymentForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        data = form.cleaned_data

        obj_options_org = Options(
            charge_processing_fee=True, charge_remainder_fee=True, liable=True
        ).__dict__

        obj_options_affiliate = Options(
            charge_processing_fee=False, charge_remainder_fee=False, liable=False
        ).__dict__

        obj_split_org = Split(
            options=obj_options_org,
            type="percentage",
            amount=str(data.get("amount_split_for_company")),
            recipient_id=settings.ORG_RECIPIENT_ID,
        ).__dict__

        obj_split_affiliate = Split(
            options=obj_options_affiliate,
            type="percentage",
            amount=str(data.get("amount_split_for_affiliate")),
            recipient_id=settings.AFFILIATE_RECIPIENT_ID,
        ).__dict__

        obj_payments = Payments(
            payment_method="pix",
            pix=Pix(expires_in="3600").__dict__,
            split=[obj_split_org, obj_split_affiliate],
        ).__dict__

        obj_items = Items(
            amount=data.get("amount"),
            description="Item de teste",
            quantity=100,
            code="123asd",
        ).__dict__

        list_items = [obj_items]
        list_payments = [obj_payments]

        payload = PixPayment(
            customer_id=data.get("customer_id"),
            items=list_items,
            payments=list_payments,
        ).__dict__

        response = gateway.insert_order(payload)

        qr_code = response["charges"][0]["last_transaction"]["qr_code"]
        qr_code_url = response["charges"][0]["last_transaction"]["qr_code_url"]
        self.success_url = (
            f"/qrcode-payment?qr_code={qr_code}&qr_code_url={qr_code_url}"
        )

        return super().form_valid(form)
