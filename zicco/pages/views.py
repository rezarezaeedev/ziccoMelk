from django.shortcuts import render
from .models import About_us

def index(request):
    return render(request=request, template_name='page/index.html')


def about_page(request):
    abouts  =   About_us.objects.all()
    context =   {
        'abouts':abouts,
    }
    return render(request=request, template_name='page/about.html', context=context)