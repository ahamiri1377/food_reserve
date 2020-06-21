from django.contrib import admin
from .models import *

admin.site.register(constructor)
admin.site.register(restaurant)
admin.site.register(food_date)

class con_admin(admin.ModelAdmin):
    list_display = ('food_name' ,'food_count', 'cooked_date', 'delivery',)
    # def queryset(self, request):
    #     qs = super(con_admin, self).queryset(request)
    #     qs = qs.distinct('food_name')
    #     return qs

    def food_name(self, obj):
        fn = obj.food.food_name
        return fn
    
    def food_count(self, obj):
        r = Reserved.objects.all()
        rf = [i.food for i in r]
        rfn = [j.food_name for j in rf]
        ct = 0
        for q in rfn:
            if q == obj.food.food_name:
                ct += 1
        return ct

    def cooked_date(self, obj):
        return obj.food.cook_date
    
    def delivery(self, obj):
        return obj.deliverd
    
        

admin.site.register(Reserved, con_admin)


class food_numb(admin.ModelAdmin):
    list_display = ('food_name', 'cook_date', 'number_to_cook','number_of_delivery',)

    def food_name(self, obj):
        return obj.food.food_name

    def cook_date(self, obj):
        return obj.food.cook_date

    def number_to_cook(self, obj):
        r = Reserved.objects.all()
        rf = [i.food for i in r]
        w = restaurant.objects.all()
        st = ''
        for u in w:
            res = 0
            for q in r:
                if q.rest_name == u and q.food == obj.food:
                    res += 1
            st += u.res_name + ': ' + str(res) + ' ,  '

        ct = 0
        for q in rf:
            if q == obj.food:
                ct += 1
        return 'Total: ' + str(ct), st
    
    def number_of_delivery(self, obj):
        r = Reserved.objects.all()
        ct = 0
        for q in r:
            if q.deliverd:
                ct += 1
        return ct

admin.site.register(Foodscount, food_numb)
