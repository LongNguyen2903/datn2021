import django_filters
from .models import *
from django_filters import CharFilter


class SearchFilter(django_filters.FilterSet):
    Pr_name = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['Pr_name', 'Pr_category']