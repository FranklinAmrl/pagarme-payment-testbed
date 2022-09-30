from django.views.generic import TemplateView
from requests import request

from payment.views.pix_payment import PixPaymentFormView

# Create your views here.


class QrcodePayment(TemplateView):
    template_name = "qrcode_payment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qr_code"] = self.request.GET.get("qr_code")
        context["qr_code_url"] = self.request.GET.get("qr_code_url")
        return context
