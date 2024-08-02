from django.shortcuts import render, get_object_or_404, redirect
from Goods.models import Info
from Goods.forms import InfoForm

def info_list(request):
    infos = Info.objects.all()
    return render(request, 'infos/info_list.html', {'infos': infos})

def info_detail(request, id):
    info = get_object_or_404(Info, id=id)
    return render(request, 'infos/info_detail.html', {'info': info})

def info_create(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info_list')
    else:
        form = InfoForm()
    return render(request, 'infos/info_form.html', {'form': form})

def info_update(request, id):
    info = get_object_or_404(Info, id=id)
    if request.method == 'POST':
        form = InfoForm(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return redirect('info_list')
    else:
        form = InfoForm(instance=info)
    return render(request, 'infos/info_form.html', {'form': form})

def info_delete(request, id):
    info = get_object_or_404(Info, id=id)
    if request.method == 'POST':
        info.delete()
        return redirect('info_list')
    return render(request, 'infos/info_confirm_delete.html', {'info': info})
