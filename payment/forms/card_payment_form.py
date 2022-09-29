from django import forms
from ..views import gateway


class CardPaymentForm(forms.Form):
    customer_id = forms.ChoiceField(label="Usuário comprador")
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        customers_list = [(None, "Selecione o usuário comprador")]
        cards_list = [(None, "Selecione o cartão para pagamento")]

        for customer in gateway.get_customers():
            customers_list.append((customer.get("id"), customer.get("name")))

        self.fields.get("customer_id").choices = tuple(customers_list)

        self.fields.get("card_id").choices = tuple(cards_list)
