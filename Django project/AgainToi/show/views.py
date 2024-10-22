from django.shortcuts import render, redirect
from .models import Host, Photographer, CameraOperator, Dancer, Singer, ShowProfile
from .forms import HostForm,PhotographerForm,CameraOperatorForm, DancerForm, DancerForm, SingerForm, ShowProfileForm

def all_profiles_list(request):
    hosts = Host.objects.all()
    photographers = Photographer.objects.all()
    camera_operators = CameraOperator.objects.all()
    dancers = Dancer.objects.all()
    singers = Singer.objects.all()

    context = {
        'hosts': hosts,
        'photographers': photographers,
        'camera_operators': camera_operators,
        'dancers': dancers,
        'singers': singers,
    }

    return render(request, 'all_profiles_list.html', context)

def add_host(request):
    if request.method == 'POST':
        form = HostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_profiles_list')
    else:
        form = HostForm()
    return render(request, 'events/add_host.html', {'form': form})

def add_photographer(request):
    if request.method == 'POST':
        form = PhotographerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_profiles_list')
    else:
        form = PhotographerForm()
    return render(request, 'events/add_photographer.html', {'form': form})

def add_camera_operator(request):
    if request.method == 'POST':
        form = CameraOperatorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_profiles_list')
    else:
        form = CameraOperatorForm()
    return render(request, 'events/add_camera_operator.html', {'form': form})

def add_dancer(request):
    if request.method == 'POST':
        form = DancerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_profiles_list')
    else:
        form = DancerForm()
    return render(request, 'events/add_dancer.html', {'form': form})

def add_singer(request):
    if request.method == 'POST':
        form = SingerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_profiles_list')
    else:
        form = SingerForm()
    return render(request, 'events/add_singer.html', {'form': form})

def add_show_profile(request):
    if request.method == 'POST':
        form = ShowProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_profiles_list')
    else:
        form = ShowProfileForm()
    return render(request, 'events/add_show_profile.html', {'form': form})
