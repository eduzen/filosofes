from . import forms
from django.views.generic import TemplateView
from django.views.generic.edit import FormView


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = forms.ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ThanksView(TemplateView):
    template_name = "contact/thanks.html"
