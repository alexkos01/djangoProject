from django.shortcuts import render, redirect
from notes.forms import NotesForm
from notes.models import Notes


def index(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        form = NotesForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    data = Notes.objects.all()
    return render(request, "show.html", {'data': data})


def edit(request, id):
    data = Notes.objects.get(id=id)
    return render(request, 'edit.html', {'data': data})


def update(request, id):
    data = Notes.objects.get(id=id)
    form = NotesForm(request.POST, instance=data)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'data': data})


def delete(request, id):
    data = Notes.objects.get(id=id)
    data.delete()
    return redirect("/show")



