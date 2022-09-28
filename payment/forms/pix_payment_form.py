from django import forms
from pagarme_integration.payment_gateway import PaymentGatewayClass


class PixPaymentForm(forms.Form):
    customer_id = forms.ChoiceField(label="Usuário comprador")
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

        gateway = PaymentGatewayClass(key="sk_M7Vep2XtDCNp5yKz")

        for customer in gateway.get_customers():
            customers_list.append((customer.get("id"), customer.get("name")))

        self.fields.get("customer_id").choices = tuple(customers_list)
