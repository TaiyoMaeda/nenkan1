from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import PostModel
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render



class ListClass(ListView):
    template_name = 'list.html'
    model = PostModel

class FormClass(CreateView):
    template_name = 'toukou.html'
    model = PostModel
    fields = ('title','memo')
    success_url = reverse_lazy('list')

def touroku(request):
        title = request.POST['title']
        memo = request.POST['memo']
        PostMode2 = PostModel(title=title,memo=memo)
        PostMode2.save()
        return HttpResponseRedirect(reverse('toukou:list'))


def post(request):
    title = request.POST['title']
    memo = request.post['memo']
    # ここを変えた
    return HttpResponseRedirect(reverse('toukou:toukou'))



