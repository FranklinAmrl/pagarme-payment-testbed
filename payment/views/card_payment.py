import re
from django.shortcuts import render
from django.views.generic import TemplateView

from payment.forms.card_payment_form import CardPaymentForm

from django.conf import settings

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


class Card:
    def __init__(self, cvv) -> None:
        self.cvv = cvv


class CreditCard:
    def __init__(self, capture, statement_descriptor, card_id, card) -> None:
        self.capture = capture
        self.statement_descriptor = statement_descriptor
        self.card_id = card_id
        self.card = card


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


class CardPayment:
    def __init__(self, customer_id, items, payments) -> None:
        self.customer_id = customer_id
        self.items = items
        self.payments = payments


class CardPaymentFormView(TemplateView):
    template_name = "card_payment.html"
    success_url = "/"

    def get(self, request, *args, **kwargs):
        customer_id = request.GET.get("customer_id")
        cards = gateway.get_cards(customer_id=customer_id)
        cards_list = [(None, "Selecione o cartão para pagamento")]
        for card in cards:
            cards_list.append(
                (card.get("id"), f'**** **** **** {card.get("last_four_digits")}')
            )
        form = CardPaymentForm(initial={"card_list": tuple(cards_list)})
        context = {}
        context["form"] = form
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form = CardPaymentForm(request.POST)

        if form.is_valid():
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

            obj_card = Card(card=str(data.get("cvv"))).__dict__

            obj_credit_card = CreditCard(
                capture=True,
                statement_descriptor=str(data.get("statement_descriptor")),
                card_id=str(data.get("card_id")),
                card=obj_card,
            ).__dict__

            obj_payments = Payments(
                payment_method="credit_card",
                credit_card=obj_credit_card,
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

            payload = CardPayment(
                customer_id=self.request.GET.get("customer_id"),
                items=list_items,
                payments=list_payments,
            ).__dict__

            gateway.insert_order(payload)

        context = self.get_context_data()
        return render(request, self.template_name, context)
