from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import SectorsForm
from ..models import SectorsModel
redirecTo = 'showSectors'


@login_required(login_url="login")
def addSectors(request):
    if request.POST:
        form = SectorsForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = SectorsForm()
    return render(request, 'products/sectors/create.html', {'form': form, 'active': 'sectors'})



@login_required(login_url="login")
def showSectors(request):
    items = SectorsModel.objects.all().order_by('-id')
    return render(request, 'products/sectors/show.html', {'items': items, 'active': 'sectors'})



@login_required(login_url="login")
def editSectors(request, id):
    data = SectorsModel.objects.get(id=id)
    if request.POST:
        form = SectorsForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = SectorsForm(instance=data)
    return render(request, 'products/sectors/create.html', {'form': form, 'active': 'sectors', 'activity': 'edit'})


@login_required(login_url="login")
def deleteSectors(request, id):
    try:
        data = SectorsModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)