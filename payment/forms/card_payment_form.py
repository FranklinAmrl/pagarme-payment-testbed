from django import forms
from ..views import gateway

from ..views import card_payment


class CardPaymentForm(forms.Form):
    card_id = forms.ChoiceField(label="Cartão para pagamento")
    cvv = forms.CharField(
        label="CVV",
        widget=forms.TextInput(
            attrs={
                "onkeypress": "return event.charCode >= 48 && event.charCode <= 57",
                "placeholder": "Código de segurança do cartão.",
            }
        ),
        max_length=4,
    )
    amount = forms.DecimalField(label="Valor do item")
    amount_split_for_company = forms.IntegerField(
        label="Percentual da comissão para organização", max_value=100
    )
    amount_split_for_affiliate = forms.IntegerField(
        label="Percentual da comissão para o afiliado", max_value=100
    )

    def get_customer_id(self, request):
        customer_id = request.GET.get("customer_id")
        return customer_id

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        cards_list = [(None, "Selecione o cartão para pagamento")]

        customer_id = str(self.get_customer_id("customer_id"))

        cards = gateway.get_cards(customer_id=customer_id)

        for card in cards:
            cards_list.append(card.get("id"))
        self.fields.get("card_id").choices = tuple(cards_list)
