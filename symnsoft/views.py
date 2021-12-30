from django.shortcuts import render, get_object_or_404
from symnsoft.models import pageModel

# Create your views here.

def index(request):
    singlepage = pageModel.objects.all()[:4]
    return render(request, 'index.html', context={
        'singlepage': singlepage,
    })

def singlepage(request, slug):
    singlepage = pageModel.objects.all()
    page = get_object_or_404(pageModel, slug=slug)
    return render(request, 'singlepage.html', context={
        'singlepage': singlepage,
        'page': page,
    })