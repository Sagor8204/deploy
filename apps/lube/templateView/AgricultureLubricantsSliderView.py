from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import AgricultureLubricantsSliderForm
from ..models import AgricultureLubricantsSliderModel
redirecTo = 'showAgricultureLubricantsSlider'


@login_required(login_url="login")
def addAgricultureLubricantsSlider(request):
    if request.POST:
        form = AgricultureLubricantsSliderForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = AgricultureLubricantsSliderForm()
    return render(request, 'lube/agriculture_lubricants_slider/create.html', {'form': form, 'active': 'agriculture_lubricants_slider'})



@login_required(login_url="login")
def showAgricultureLubricantsSlider(request):
    items = AgricultureLubricantsSliderModel.objects.all().order_by('-id')
    return render(request, 'lube/agriculture_lubricants_slider/show.html', {'items': items, 'active': 'agriculture_lubricants_slider'})



@login_required(login_url="login")
def editAgricultureLubricantsSlider(request, id):
    data = AgricultureLubricantsSliderModel.objects.get(id=id)
    if request.POST:
        form = AgricultureLubricantsSliderForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = AgricultureLubricantsSliderForm(instance=data)
    return render(request, 'lube/agriculture_lubricants_slider/create.html', {'form': form, 'active': 'agriculture_lubricants_slider', 'activity': 'edit'})


@login_required(login_url="login")
def deleteAgricultureLubricantsSlider(request, id):
    try:
        data = AgricultureLubricantsSliderModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)