from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import ViscosityForm
from ..models import ViscosityModel
redirecTo = 'showViscosity'


@login_required(login_url="login")
def addViscosity(request):
    if request.POST:
        form = ViscosityForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = ViscosityForm()
    return render(request, 'products/viscosity/create.html', {'form': form, 'active': 'viscosity'})



@login_required(login_url="login")
def showViscosity(request):
    items = ViscosityModel.objects.all().order_by('-id')
    return render(request, 'products/viscosity/show.html', {'items': items, 'active': 'viscosity'})



@login_required(login_url="login")
def editViscosity(request, id):
    data = ViscosityModel.objects.get(id=id)
    if request.POST:
        form = ViscosityForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = ViscosityForm(instance=data)
    return render(request, 'products/viscosity/create.html', {'form': form, 'active': 'viscosity', 'activity': 'edit'})


@login_required(login_url="login")
def deleteViscosity(request, id):
    try:
        data = ViscosityModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)