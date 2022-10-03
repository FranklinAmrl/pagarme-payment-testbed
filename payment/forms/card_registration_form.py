from django import forms
from django.core.validators import MaxLengthValidator
from pagarme_integration.payment_gateway import PaymentGatewayClass


class CardRegistrationForm(forms.Form):
    customer_id = forms.ChoiceField(label="Usuário comprador")
    statement_descriptor = forms.CharField(
        label="Número do cartão",
        widget=forms.TextInput(
            attrs={
                "onkeypress": "return event.charCode >= 48 && event.charCode <= 57",
                "placeholder": "Escreva igual como está impresso no cartão.",
            }
        ),
        max_length=19,
    )
    holder_name = forms.CharField(
        label="Nome do títular do cartão",
        widget=forms.TextInput(
            attrs={"placeholder": "Escreva igual como está impresso no cartão."}
        ),
    )
    exp_month = forms.IntegerField(
        label="Mẽs de expiração",
        max_value=12,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Escreva igual como está impresso no cartão. Exemplo: XX.",
            }
        ),
    )
    exp_year = forms.IntegerField(
        label="Ano de expiração",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Escreva igual como está impresso no cartão. Exemplo: XX ou XXXX.",
            }
        ),
    )
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
    country = forms.CharField(
        label="País",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Escreva o seu país de naturalidade.",
            }
        ),
        max_length=2,
    )
    state = forms.CharField(
        label="Estado",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Escreva o estado que você nasceu.",
            }
        ),
        max_length=6,
    )
    city = forms.CharField(
        label="Cidade",
        max_length=64,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Escreva a cidade que você nasceu.",
            }
        ),
    )
    zip_code = forms.CharField(
        label="CEP",
        widget=forms.TextInput(
            attrs={
                "onkeypress": "return event.charCode >= 48 && event.charCode <= 57",
                "size": "40",
                "placeholder": "Escreva o código postal do seu logradouro.",
            }
        ),
        max_length=16,
    )
    line_1 = forms.CharField(label="Endereço", max_length=256)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        customers_list = [(None, "Selecione o usuário comprador")]

        gateway = PaymentGatewayClass(key="sk_M7Vep2XtDCNp5yKz")

        for customer in gateway.get_customers():
            customers_list.append((customer.get("id"), customer.get("name")))

        self.fields.get("customer_id").choices = tuple(customers_list)

        
