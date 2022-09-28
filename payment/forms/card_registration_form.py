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
    holber_name = forms.CharField(label="Nome do títular do cartão")
    exp_month = forms.IntegerField(label="Mẽs de expiração (Exemplo: XX)", max_value=12)
    exp_year = forms.IntegerField(
        label="Ano de expiração (Exemplo: XX ou XXXX)",
        validators=[MaxLengthValidator(4)],
    )
    cvv = forms.CharField(
        label="CVV (Código de segurança do cartão)",
        widget=forms.TextInput(
            attrs={"onkeypress": "return event.charCode >= 48 && event.charCode <= 57"}
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
