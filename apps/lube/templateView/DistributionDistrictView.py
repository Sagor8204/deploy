from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import DistributionDistrictForm
from ..models import DistributionDistrictModel
redirecTo = 'showDistrict'


@login_required(login_url="login")
def addDistrict(request):
    if request.POST:
        form = DistributionDistrictForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = DistributionDistrictForm()
    return render(request, 'lube/district/create.html', {'form': form, 'active': 'district'})



@login_required(login_url="login")
def showDistrict(request):
    items = DistributionDistrictModel.objects.all().order_by('-id')
    return render(request, 'lube/district/show.html', {'items': items, 'active': 'district'})



@login_required(login_url="login")
def editDistrict(request, id):
    data = DistributionDistrictModel.objects.get(id=id)
    if request.POST:
        form = DistributionDistrictForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = DistributionDistrictForm(instance=data)
    return render(request, 'lube/district/create.html', {'form': form, 'active': 'district', 'activity': 'edit'})


@login_required(login_url="login")
def deleteDistrict(request, id):
    try:
        data = DistributionDistrictModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)