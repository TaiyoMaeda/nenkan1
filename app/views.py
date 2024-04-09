from django.shortcuts import render
from django.views.generic import FormView
from .forms import SeisakuForm
from django.core.mail import EmailMessage

def index(request):
    return render(request, 'index.html')

class Contactview(FormView):
    template_name = 'mail.html'
    success_url = '/'
    form_class = SeisakuForm

    def form_valid(self,form):
         name = form.cleaned_data['name']
         inquiry = form.cleaned_data['inquiry']
         emailMessage = EmailMessage(
        to=['fko2347063@stu.o-hara.ac.jp'],
        subject = name,
        body = inquiry)
         emailMessage.send()
         return super().form_valid(form)
         
