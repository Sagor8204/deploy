from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import LubricantCategoryForm
from ..models import LubricantCategoryModel
redirecTo = 'showLubricantCategory'


@login_required(login_url="login")
def addLubricantCategory(request):
    if request.POST:
        form = LubricantCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = LubricantCategoryForm()
    return render(request, 'products/lubricant_category/create.html', {'form': form, 'active': 'lubricant_category'})



@login_required(login_url="login")
def showLubricantCategory(request):
    items = LubricantCategoryModel.objects.all().order_by('-id')
    return render(request, 'products/lubricant_category/show.html', {'items': items, 'active': 'lubricant_category'})



@login_required(login_url="login")
def editLubricantCategory(request, id):
    data = LubricantCategoryModel.objects.get(id=id)
    if request.POST:
        form = LubricantCategoryForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = LubricantCategoryForm(instance=data)
    return render(request, 'products/lubricant_category/create.html', {'form': form, 'active': 'lubricant_category', 'activity': 'edit'})


@login_required(login_url="login")
def deleteLubricantCategory(request, id):
    try:
        data = LubricantCategoryModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)