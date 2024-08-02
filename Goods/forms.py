from django import forms
from .models import ProductEnter,Banner

class ProductEnterForm(forms.ModelForm):
    class Meta:
        model = ProductEnter
        fields = ['product', 'quantity', 'old_quantity', 'date', 'description']

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['title', 'sub_title', 'img', 'is_active']


from django import forms
from .models import Info

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['name', 'email']
