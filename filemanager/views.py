from django.shortcuts import render, redirect
from filemanager.forms import DocumentForm


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('logout')
    else:
        form = DocumentForm()
    return render(request, 'templates/model_form_upload.html', {
        'form': form
    })