from django.shortcuts import render, get_object_or_404, redirect
from Goods.models import Banner
from Goods.forms import BannerForm

def banner_list(request):
    banners = Banner.objects.all()
    return render(request, 'banner/banner_list.html', {'banners': banners})

def banner_detail(request, id):
    banner = get_object_or_404(Banner, id=id)
    return render(request, 'banner/banner_detail.html', {'banner': banner})

def banner_create(request):
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('banner_list')
    else:
        form = BannerForm()
    return render(request, 'banner/banner_form.html', {'form': form})

def banner_update(request, id):
    banner = get_object_or_404(Banner, id=id)
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            form.save()
            return redirect('banner_list')
    else:
        form = BannerForm(instance=banner)
    return render(request, 'banner/banner_form.html', {'form': form})

def banner_delete(request, id):
    banner = get_object_or_404(Banner, id=id)
    if request.method == 'POST':
        banner.delete()
        return redirect('banner_list')
    return render(request, 'banner/banner_confirm_delete.html', {'banner': banner})
