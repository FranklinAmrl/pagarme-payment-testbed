from pagarme_integration.payment_gateway import PaymentGatewayClass

from django.conf import settings

gateway = PaymentGatewayClass(key=settings.KEY_GATEWAY)
