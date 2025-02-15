from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import LubricantSpecificationForm
from ..models import LubricantSpecificationModel
redirecTo = 'showLubricantSpecification'


@login_required(login_url="login")
def addLubricantSpecification(request):
    if request.POST:
        form = LubricantSpecificationForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = LubricantSpecificationForm()
    return render(request, 'products/lubricant_specification/create.html', {'form': form, 'active': 'lubricant_specification'})



@login_required(login_url="login")
def showLubricantSpecification(request):
    items = LubricantSpecificationModel.objects.all().order_by('-id')
    return render(request, 'products/lubricant_specification/show.html', {'items': items, 'active': 'lubricant_specification'})



@login_required(login_url="login")
def editLubricantSpecification(request, id):
    data = LubricantSpecificationModel.objects.get(id=id)
    if request.POST:
        form = LubricantSpecificationForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = LubricantSpecificationForm(instance=data)
    return render(request, 'products/lubricant_specification/create.html', {'form': form, 'active': 'lubricant_specification', 'activity': 'edit'})


@login_required(login_url="login")
def deleteLubricantSpecification(request, id):
    try:
        data = LubricantSpecificationModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)