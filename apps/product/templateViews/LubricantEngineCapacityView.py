from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import LubricantEngineCapacityForm
from ..models import LubricantEngineCapacityModel
redirecTo = 'showLubricantEngineCapacity'


@login_required(login_url="login")
def addLubricantEngineCapacity(request):
    if request.POST:
        form = LubricantEngineCapacityForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = LubricantEngineCapacityForm()
    return render(request, 'products/lubricant_engine_capacity/create.html', {'form': form, 'active': 'lubricant_engine_capacity'})



@login_required(login_url="login")
def showLubricantEngineCapacity(request):
    items = LubricantEngineCapacityModel.objects.all().order_by('-id')
    return render(request, 'products/lubricant_engine_capacity/show.html', {'items': items, 'active': 'lubricant_engine_capacity'})



@login_required(login_url="login")
def editLubricantEngineCapacity(request, id):
    data = LubricantEngineCapacityModel.objects.get(id=id)
    if request.POST:
        form = LubricantEngineCapacityForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = LubricantEngineCapacityForm(instance=data)
    return render(request, 'products/lubricant_engine_capacity/create.html', {'form': form, 'active': 'lubricant_engine_capacity', 'activity': 'edit'})


@login_required(login_url="login")
def deleteLubricantEngineCapacity(request, id):
    try:
        data = LubricantEngineCapacityModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)