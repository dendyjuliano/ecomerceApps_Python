import django_filters
from Ecomerce.models import Product,Category
from django import forms

class OrderProduct(django_filters.FilterSet):
    name = django_filters.CharFilter(label= '',lookup_expr='icontains',widget=forms.TextInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Search Here ......',
            'autocomplete':'off'
        }
    ))
    category = django_filters.ModelMultipleChoiceFilter(label='',queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs = {
                'class':'check-input',
            }
        ))

    class Meta:
        model = Product
        fields = ['name']

class SearchProduct(django_filters.FilterSet):
    name = django_filters.CharFilter(label= '',lookup_expr='icontains',widget=forms.TextInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Search Here ......',
            'autocomplete':'off',
            'aria-describedby':'inputGroup-sizing-default',
            'aria-label':'Sizing example input',
        }
    ))

    class meta:
        model = Product
        fields = ['name']