from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import LubricantCategoryYearForm
from ..models import LubricantCategoryYearModel
redirecTo = 'showLubricantYear'


@login_required(login_url="login")
def addLubricantYear(request):
    if request.POST:
        form = LubricantCategoryYearForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = LubricantCategoryYearForm()
    return render(request, 'products/lubricant_year/create.html', {'form': form, 'active': 'lubricant_year'})



@login_required(login_url="login")
def showLubricantYear(request):
    items = LubricantCategoryYearModel.objects.all().order_by('-id')
    return render(request, 'products/lubricant_year/show.html', {'items': items, 'active': 'lubricant_year'})



@login_required(login_url="login")
def editLubricantYear(request, id):
    data = LubricantCategoryYearModel.objects.get(id=id)
    if request.POST:
        form = LubricantCategoryYearForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = LubricantCategoryYearForm(instance=data)
    return render(request, 'products/lubricant_year/create.html', {'form': form, 'active': 'lubricant_year', 'activity': 'edit'})


@login_required(login_url="login")
def deleteLubricantYear(request, id):
    try:
        data = LubricantCategoryYearModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)