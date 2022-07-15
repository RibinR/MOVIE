from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import movieform
from .models import movie


def index(request):
    temp = movie.objects.all()
    return render(request, 'index.html', {'movie_list': temp})


def detail(request, movie_id):
    obj = movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie': obj})


def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        adding = movie(name=name, desc=desc, year=year, img=img)
        adding.save()
    return render(request, 'admin_data.html')


def update(request, id):
    v_movie = movie.objects.get(id=id)
    v_form = movieform(request.POST or None, request.FILES, instance=v_movie)
    if v_form.is_valid():
        v_form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': v_form, 'movie': v_movie})


def delete(request, id):
    d_movie = movie.objects.get(id=id)
    if request.method == 'POST':
         d_movie.delete()
         return redirect('/')
    return render(request, 'delete.html')



