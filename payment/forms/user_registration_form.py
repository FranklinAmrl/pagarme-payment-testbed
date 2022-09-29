from django import forms
from django.core.validators import MaxLengthValidator


class UserRegistrationForm(forms.Form):
    name = forms.CharField(
        label="Nome",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Escreva seu nome completo.",
            }
        ),
        max_length=256,
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(attrs={"placeholder": "Escreva o seu email."}),
    )
    cpf = forms.CharField(
        label="CPF",
        widget=forms.TextInput(
            attrs={
                "onkeypress": "return event.charCode >= 48 && event.charCode <= 57",
                "placeholder": "Escreva o seu CPF. Exemplo: XXXXXXXXXXX.",
            }
        ),
        max_length=11,
    )
    country_code = forms.CharField(
        label="Discagem Direta Internacional (DDI)",
        widget=forms.TextInput(
            attrs={
                "onkeypress": "return event.charCode >= 48 && event.charCode <= 57",
                "placeholder": "Escreva o código do país. Exemplo: Se for Brasil, escreva 55.",
            }
        ),
        max_length=3,
    )
    area_code = forms.CharField(
        label="Discagem Direta à distância (DDD)",
        widget=forms.TextInput(
            attrs={
                "onkeypress": "return event.charCode >= 48 && event.charCode <= 57",
                "placeholder": "Escreva o código telefônico do estado. Exemplo: Se for Pernambuco, escreva 081.",
            }
        ),
        max_length=3,
    )
    number = forms.CharField(
        label="Número",
        widget=forms.TextInput(
            attrs={
                "onkeypress": "return event.charCode >= 48 && event.charCode <= 57",
                "placeholder": "Escreva o seu número de telefone.",
            }
        ),
        max_length=9,
    )
