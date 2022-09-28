from django import forms


class CardRegistrationForm(forms.Form):
    item_value = forms.DecimalField(label="Valor do item")
    amount_split = forms.IntegerField(
        label="Percentual da comissão para você", max_value=100
    )
    name = forms.CharField(label="Nome")
    email = forms.EmailField()
    cpf = forms.CharField(
        label="CPF",
        widget=forms.TextInput(
            attrs={"onkeypress": "return event.charCode >= 48 && event.charCode <= 57"}
        ),
        max_length=11,
    )
    phone = forms.IntegerField(label="Telefone")
