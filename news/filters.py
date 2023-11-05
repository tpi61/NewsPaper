from django_filters import FilterSet, ModelChoiceFilter, CharFilter, DateFilter
from django.forms import DateInput
from .models import Post, Category

class PostsFilter(FilterSet):
    
    title = CharFilter(
        label = 'Title',
        field_name = 'postHead',
        lookup_expr = 'icontains'
    )

    category = ModelChoiceFilter(
        label = 'Post category',
        field_name = 'postCategory',
        queryset = Category.objects.all(),
        empty_label = 'All categories'
    )

    date = DateFilter(
        field_name='createTime', 
        lookup_expr='gt',
        label = 'From date',
        widget = DateInput(
            attrs={
                'type':'date'
            }
        )
    )

    class Meta:
        model = Post

        fields = {
            # 'postHead': ['icontains'],
            # 'postCategory': ['exact'],
        }


