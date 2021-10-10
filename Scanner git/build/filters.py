import django_filters
from .models import *

class TrackerScannerFilter(django_filters.FilterSet):
    class Meta:
        model = TrackerScanner
        fields = '__all__'
        exclude = ['first_name']