from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import ProductRangeForm
from ..models import ProductRangeModel
redirecTo = 'showProductRange'


@login_required(login_url="login")
def addProductRange(request):
    if request.POST:
        form = ProductRangeForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = ProductRangeForm()
    return render(request, 'products/product_range/create.html', {'form': form, 'active': 'product_range'})



@login_required(login_url="login")
def showProductRange(request):
    items = ProductRangeModel.objects.all().order_by('-id')
    return render(request, 'products/product_range/show.html', {'items': items, 'active': 'product_range'})



@login_required(login_url="login")
def editProductRange(request, id):
    data = ProductRangeModel.objects.get(id=id)
    if request.POST:
        form = ProductRangeForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = ProductRangeForm(instance=data)
    return render(request, 'products/product_range/create.html', {'form': form, 'active': 'product_range', 'activity': 'edit'})


@login_required(login_url="login")
def deleteProductRange(request, id):
    try:
        data = ProductRangeModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)