from django.shortcuts import render, get_object_or_404
from .models import Amlak

def index(request):
    amlak   =   list(Amlak.objects.all().order_by('-list_date'))
    count   =   len(amlak)
    context =   {
        'amlak':amlak,
        'count':count,
    }
    
    return render(request, template_name='amlak/index.html', context=context)


def details(request, melk_id):
    melk       =   get_object_or_404(Amlak, id=melk_id)
    context     =   {
        'melk':melk,
    }
    return render(request, template_name='amlak/details.html', context=context)


def search(request):
    amlak   =   Amlak.objects.all()
    if 'bedroom' in request.GET:
        print('\n'*4)
        print(request.GET)
        print('\n'*4)
        bedroom =   request.GET['bedroom']
        amlak   =  amlak.filter(bedroom=bedroom)

    context =   {
        'amlak':amlak,

    }
    return render(request, template_name='amlak/index.html', context=context)
