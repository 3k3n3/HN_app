import django_filters
from .models import Base
# from django_filters import CharFilter

class BaseFilter(django_filters.FilterSet):


    class Meta:
        model = Base
        fields = {
            'title' : ['icontains']
        }