from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from company.forms import AddressForm
from company.models import CompanyProfile, CompanyOrderAcceptance
from user.models import Address
from datetime import datetime

@login_required
def CompanyRegister(request):
    if CompanyProfile.objects.filter(user=request.user).exists():
        return redirect('about')

    if request.method == 'POST':
        addressForm = AddressForm(request.POST, request.FILES)
        if addressForm.is_valid():
            address = addressForm.save()

            company_name = request.POST.get('company_name')
            capacity = request.POST.get('capacity')
            venue_type = request.POST.get('venue_type')
            image = request.FILES.get('image')
            video = request.FILES.get('video')

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
    else:
        addressForm = AddressForm()

    return render(request, 'venue_register.html', {'addressForm': addressForm})

@login_required
def CompanyProfileView(request):
    user = request.user
    try:
        company_profile = CompanyProfile.objects.get(user=user)
    except CompanyProfile.DoesNotExist:
        company_profile = None
    return render(request, 'venue_profile.html', {'user': user, 'company_profile': company_profile})

@login_required
def Order(request):
    try:
        company = request.user.companyprofile
    except CompanyProfile.DoesNotExist:
        return render(request, 'order.html', {'orders': [], 'error': 'No company profile found for the user.'})

    orders = CompanyOrderAcceptance.objects.filter(venue=company)
    return render(request, 'order.html', {'orders': orders, 'error': None})

@login_required
def accept_order(request, order_id):
    order = get_object_or_404(CompanyOrderAcceptance, pk=order_id)
    if not order.accepted:
        order.accepted = True
        order.accepted_date = datetime.now()
        order.save()
    return redirect('order')
