from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import DistributionPointForm
from ..models import DistributionPointModel
redirecTo = 'showDistributionPoint'


@login_required(login_url="login")
def addDistributionPoint(request):
    if request.POST:
        form = DistributionPointForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = DistributionPointForm()
    return render(request, 'lube/distribution_point/create.html', {'form': form, 'active': 'distribution_point'})



@login_required(login_url="login")
def showDistributionPoint(request):
    items = DistributionPointModel.objects.all().order_by('-id')
    return render(request, 'lube/distribution_point/show.html', {'items': items, 'active': 'distribution_point'})



@login_required(login_url="login")
def editDistributionPoint(request, id):
    data = DistributionPointModel.objects.get(id=id)
    if request.POST:
        form = DistributionPointForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = DistributionPointForm(instance=data)
    return render(request, 'lube/distribution_point/create.html', {'form': form, 'active': 'distribution_point', 'activity': 'edit'})


@login_required(login_url="login")
def deleteDistributionPoint(request, id):
    try:
        data = DistributionPointModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)