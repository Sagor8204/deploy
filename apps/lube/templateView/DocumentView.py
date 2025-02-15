from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import DocumentForm
from ..models import DocumentModel
redirecTo = 'showDocument'


@login_required(login_url="login")
def addDocument(request):
    if request.POST:
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = DocumentForm()
    return render(request, 'lube/document/create.html', {'form': form, 'active': 'document'})



@login_required(login_url="login")
def showDocument(request):
    items = DocumentModel.objects.all().order_by('-id')
    return render(request, 'lube/document/show.html', {'items': items, 'active': 'document'})



@login_required(login_url="login")
def editDocument(request, id):
    data = DocumentModel.objects.get(id=id)
    if request.POST:
        form = DocumentForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = DocumentForm(instance=data)
    return render(request, 'lube/document/create.html', {'form': form, 'active': 'document', 'activity': 'edit'})


@login_required(login_url="login")
def deleteDocument(request, id):
    try:
        data = DocumentModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)