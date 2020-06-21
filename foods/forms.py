from django import forms
from .models import restaurant, food_date

def food_list(foo):
    foods = []
    numb = 1
    for f in foo:
        foods.append((numb, str(f.food_name)))
        numb += 1
    return foods

def make_choices(rests):
    res_choices = []
    for r in rests:
        foods = r.foods_in_date.all()
        res_choices.append((str(r.res_name), food_list(foods)))
    return res_choices

def make_choices_res(rests):
    res_choices = []
    numb = 1
    for r in rests:
        res_choices.append((numb, str(r.res_name)))
        numb += 1
    return res_choices


class apply(forms.Form):
    food_name = forms.CharField(label='food name', max_length=100)
    cooked_date = forms.DateField(label='date', widget=forms.SelectDateWidget())
    rest_name = forms.ChoiceField(choices=make_choices_res(restaurant.objects.all()))

class order(forms.Form):
    date = forms.DateField(label='date', widget=forms.SelectDateWidget())
    restur_name = forms.ChoiceField(choices=make_choices_res(restaurant.objects.all()))
    f_name = forms.ChoiceField(choices=make_choices(restaurant.objects.all()))
    



