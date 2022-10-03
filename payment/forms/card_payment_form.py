from django import forms
from ..views import gateway


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

    amount = forms.IntegerField(
        label="Valor do item",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Percentual da comissão para organização.",
            }
        ),
    )

    amount_split_for_company = forms.IntegerField(
        label="Percentual da comissão para organização",
        max_value=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Percentual da comissão para organização.",
            }
        ),
    )
    amount_split_for_affiliate = forms.IntegerField(
        label="Percentual da comissão para o afiliado",
        max_value=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Percentual da comissão para o afiliado.",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["card_id"].choices = kwargs["initial"]["card_list"]
