from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from home.forms import ContactForm, MediaForm
from home.models import Media


# Create your views here.

def about(request):
    return render(request, "about/about.html")


def media(request):
    return render(request, "media/media.html")


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def thanks_view(request):
    return render(request, 'contact/thanks.html')


# media
def media_list(request):
    medias = Media.objects.all().order_by('-created_at')
    return render(request, 'media/media.html', {'medias': medias})


def media_detail(request, pk):
    media_ = get_object_or_404(Media, pk=pk)
    return render(request, 'media/media-detail.html', {'media': media_})


@login_required
def add_media(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            media_ = form.save(commit=False)
            media_.user = request.user
            media_.save()
            return redirect('media')
    else:
        form = MediaForm()
    return render(request, 'media/media-add.html', {'form': form})

