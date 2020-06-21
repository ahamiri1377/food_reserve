from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import food_date, constructor, restaurant  
from .forms import apply, make_choices, order


def home_page(request):
    username = None
    group = None
    if request.user.is_authenticated:
        username = request.user.username
        group = request.user.groups.all()[0].name
    return render(request, 'foods/home.html', {'username':username, 'group':group})

def account_page(request):
    flag = False
    dt = None
    the_rest = None
    week = None
    if request.user.is_authenticated:
        form = order()
        if request.method == 'GET':
            rest = request.GET.get('restur_name')
            print(rest)
            rs = restaurant.objects.get(res_name='shila')
            fs = rs.foods_in_date.all()
            form.fields['f_name'].queryset = fs
            
        week = ['saturday', 'sunday', 'monday', 'thuesday', 'wendsday', 'thursday', 'friday']
        month = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
        t = datetime.today()    
        content = {
            'form':form, 
            'day':t, 
            'all_rest': restaurant.objects.all(), 
            'all_foods': food_date.objects.all(),
            'week':week,
            'month':month[t.month],
        }
        return render(request, 'foods/order.html', content)
    else:
        return redirect('\login')

def apply_food(request):
    form = None
    if request.user.is_authenticated:
        if request.user.groups.all()[0].name == 'admins':
            if request.method == 'POST':
                form = apply(request.POST)
                if form.is_valid():
                    fn = form.cleaned_data['food_name']
                    dt = form.cleaned_data['cooked_date']
                    q = food_date(food_name=fn, cook_date=dt)
                    q.save()

                    trt = form.cleaned_data['rest_name']
                    the_rest_name = make_choices(restaurant.objects.all())[int(trt) - 1][1]
                    the_rest = restaurant.objects.get(res_name=the_rest_name)
                    the_rest.foods_in_date.add(q)
            else:
                form = apply()
            return render(request, 'foods/apply_food.html', {'form': form})
        else:
            return HttpResponse('YOU ARE NOT ADMIN!!!!')
    else:
        return redirect('\login')
