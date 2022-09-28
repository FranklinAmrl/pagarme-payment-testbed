from django import forms
from django.core.validators import MaxLengthValidator


class CardRegistrationForm(forms.Form):
    number = forms.CharField(
        label="Número do cartão",
        widget=forms.TextInput(
            attrs={"onkeypress": "return event.charCode >= 48 && event.charCode <= 57"}
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
        widget=forms.TextInput(
            attrs={
                "placeholder": "Exemplo: XX.",
            }
        ),
    )
    exp_year = forms.IntegerField(
        label="Ano de expiração",
        validators=[MaxLengthValidator(4)],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Exemplo: XX ou XXXX.",
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
    country = forms.CharField(label="País")
    state = forms.CharField(label="Estado")
    city = forms.CharField(label="Cidade", max_length=64)
    zip_code = forms.CharField(
        label="CEP",
        widget=forms.TextInput(
            attrs={
                "onkeypress": "return event.charCode >= 48 && event.charCode <= 57",
                "size": "40",
            }
        ),
        max_length=16,
    )
    line_1 = forms.CharField(label="Endereço", max_length=256)
