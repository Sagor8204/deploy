from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import OilTypeForm
from ..models import OilTypeModel
redirecTo = 'showOilType'


@login_required(login_url="login")
def addOilType(request):
    if request.POST:
        form = OilTypeForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = OilTypeForm()
    return render(request, 'products/oil_type/create.html', {'form': form, 'active': 'oil_type'})



@login_required(login_url="login")
def showOilType(request):
    items = OilTypeModel.objects.all().order_by('-id')
    return render(request, 'products/oil_type/show.html', {'items': items, 'active': 'oil_type'})



@login_required(login_url="login")
def editOilType(request, id):
    data = OilTypeModel.objects.get(id=id)
    if request.POST:
        form = OilTypeForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = OilTypeForm(instance=data)
    return render(request, 'products/oil_type/create.html', {'form': form, 'active': 'oil_type', 'activity': 'edit'})


@login_required(login_url="login")
def deleteOilType(request, id):
    try:
        data = OilTypeModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)