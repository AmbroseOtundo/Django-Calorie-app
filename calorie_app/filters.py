import django_filters
from django_filters import CharFilter
from .models import *


# The FoodFilter class is a subclass of django_filters.FilterSet. 
# It has a CharFilter that filters the Food model's name field using the icontains lookup expression. 
# The CharFilter is given the label 'search food items'.
class FoodFilter(django_filters.FilterSet):
    food_name = CharFilter(field_name = 'name',lookup_expr = 'icontains',label='search food items')
    class Meta:
        model = Food
        fields = ['food_name']