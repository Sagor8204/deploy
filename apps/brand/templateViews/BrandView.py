from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import BrandForm
from ..models import BrandModel
redirecTo = 'showBrand'


@login_required(login_url="login")
def addBrand(request):
    if request.POST:
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = BrandForm()
    return render(request, 'Brand/brand/create.html', {'form': form, 'active': 'brand'})



@login_required(login_url="login")
def showBrand(request):
    items = BrandModel.objects.all().order_by('-id')
    return render(request, 'Brand/brand/show.html', {'items': items, 'active': 'brand'})



@login_required(login_url="login")
def editBrand(request, id):
    data = BrandModel.objects.get(id=id)
    if request.POST:
        form = BrandForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = BrandForm(instance=data)
    return render(request, 'Brand/brand/create.html', {'form': form, 'active': 'brand', 'activity': 'edit'})


@login_required(login_url="login")
def deleteBrand(request, id):
    try:
        data = BrandModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)