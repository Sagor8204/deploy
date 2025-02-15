from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import BusinessSolutionsForm
from ..models import BusinessSolutionsModel
redirecTo = 'showBusinessSolutions'


@login_required(login_url="login")
def addBusinessSolutions(request):
    if request.POST:
        form = BusinessSolutionsForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = BusinessSolutionsForm()
    return render(request, 'lube/business_solutions/create.html', {'form': form, 'active': 'business_solutions'})



@login_required(login_url="login")
def showBusinessSolutions(request):
    items = BusinessSolutionsModel.objects.all().order_by('-id')
    return render(request, 'lube/business_solutions/show.html', {'items': items, 'active': 'business_solutions'})



@login_required(login_url="login")
def editBusinessSolutions(request, id):
    data = BusinessSolutionsModel.objects.get(id=id)
    if request.POST:
        form = BusinessSolutionsForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = BusinessSolutionsForm(instance=data)
    return render(request, 'lube/business_solutions/create.html', {'form': form, 'active': 'business_solutions', 'activity': 'edit'})


@login_required(login_url="login")
def deleteBusinessSolutions(request, id):
    try:
        data = BusinessSolutionsModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)