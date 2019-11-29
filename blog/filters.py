from .models import Post
import django_filters

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')
    date_posted__gt = django_filters.NumberFilter(field_name='date_posted', lookup_expr='year__gte')
    date_posted__lt = django_filters.NumberFilter(field_name='date_posted', lookup_expr='year__lte')
    class Meta:
        model = Post
        fields = ['title','content','date_posted','author',]
