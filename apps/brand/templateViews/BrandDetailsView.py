from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import BrandDetailsForm
from ..models import BrandDetailsModel
redirecTo = 'showBrandDetails'


@login_required(login_url="login")
def addBrandDetails(request):
    if request.POST:
        form = BrandDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = BrandDetailsForm()
    return render(request, 'Brand/brand_details/create.html', {'form': form, 'active': 'brand_details'})



@login_required(login_url="login")
def showBrandDetails(request):
    items = BrandDetailsModel.objects.all().order_by('-id')
    return render(request, 'Brand/brand_details/show.html', {'items': items, 'active': 'brand_details'})



@login_required(login_url="login")
def editBrandDetails(request, id):
    data = BrandDetailsModel.objects.get(id=id)
    if request.POST:
        form = BrandDetailsForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = BrandDetailsForm(instance=data)
    return render(request, 'Brand/brand_details/create.html', {'form': form, 'active': 'brand_details', 'activity': 'edit'})


@login_required(login_url="login")
def deleteBrandDetails(request, id):
    try:
        data = BrandDetailsModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)