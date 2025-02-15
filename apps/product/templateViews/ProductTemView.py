from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import ProductForm
from ..models import ProductModel
redirecTo = 'showProduct'


@login_required(login_url="login")
def addProduct(request):
    if request.POST:
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = ProductForm()
    return render(request, 'products/product/create.html', {'form': form, 'active': 'product'})



@login_required(login_url="login")
def showProduct(request):
    items = ProductModel.objects.all().order_by('-id')
    return render(request, 'products/product/show.html', {'items': items, 'active': 'product'})



@login_required(login_url="login")
def editProduct(request, id):
    data = ProductModel.objects.get(id=id)
    if request.POST:
        form = ProductForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = ProductForm(instance=data)
    return render(request, 'products/product/create.html', {'form': form, 'active': 'product', 'activity': 'edit'})


@login_required(login_url="login")
def deleteProduct(request, id):
    try:
        data = ProductModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)