import logging

from django import forms
from django.core.mail import EmailMessage
from django.http import HttpResponse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from nocaptcha_recaptcha.fields import NoReCaptchaField

logger = logging.getLogger(__name__)


class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=100, required=True)
    email = forms.EmailField(max_length=150, label="E-mail", required=True)
    message = forms.CharField(label="Consulta", required=True, widget=forms.Textarea)
    captcha = NoReCaptchaField()

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Enviar", css_class="btn-block", style=""))
        self.helper.form_tag = True
        self.helper.form_action = "/contact/"

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        try:
            email = self.cleaned_data.get("email")
            name = self.cleaned_data.get("name")
            msg = self.cleaned_data.get("message")

            content = (
                f"Holas! Tenes un nuevo contacto en filosofes.com.ar. {name} escribio en la web contacto"
                f"lo siguiente: {msg}\n"
                f"Si querés escribirle su mail es {email}"
            )

            email = EmailMessage("Nuevo contacto", content, email, ["eduardo.a.enriquez@gmail.com"])
            email.send()
            logger.info("Email sent")

        except Exception:
            logger.exception("Email problems")
            return HttpResponse("Something wrong happened")
