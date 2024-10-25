from company.models import CompanyProfile
from user.models import Address
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def CompanyRegister(request):
    if CompanyProfile.objects.filter(user=request.user).exists():
        return redirect('about')
    addresses = Address.objects.all()

    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        address_id = request.POST.get('address')
        capacity = request.POST.get('capacity')
        venue_type = request.POST.get('venue_type')
        image = request.FILES.get('image')
        video = request.FILES.get('video')

        address = Address.objects.get(id=address_id)

        CompanyProfile.objects.create(
            user=request.user,
            company_name=company_name,
            address=address,
            capacity=capacity,
            venue_type=venue_type,
            image=image,
            video=video
        )

        return redirect('about')

    return render(request, 'venue_register.html', {'addresses': addresses})


@login_required
def CompanyProfileView(request):
    user = request.user
    company_profile = CompanyProfile.objects.get(user=user)
    return render(request, 'venue_profile.html', {'user': user, 'company_profile': company_profile})


def Order(request):
    return render(request, 'order.html')
