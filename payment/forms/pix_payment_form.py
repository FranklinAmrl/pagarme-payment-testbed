from django import forms

from ..views import gateway


class PixPaymentForm(forms.Form):
    customer_id = forms.ChoiceField(label="Usuário comprador")
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

        customers_list = [(None, "Selecione o usuário comprador")]

        for customer in gateway.get_customers():
            customers_list.append((customer.get("id"), customer.get("name")))

        self.fields.get("customer_id").choices = tuple(customers_list)

    def check_amout_split(self, amount_split_for_company, amount_split_for_affiliate):
        total_amount_split = 100
        amount_split_for_company += amount_split_for_affiliate
        if total_amount_split < amount_split_for_company:
            return False
        return True
