from django import forms
from ..views import gateway


class UserSelectForm(forms.Form):
    customer_id = forms.ChoiceField(label="Usuário comprador")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        customers_list = [(None, "Selecione o usuário comprador")]

        for customer in gateway.get_customers():
            customers_list.append((customer.get("id"), customer.get("name")))

        self.fields.get("customer_id").choices = tuple(customers_list)
