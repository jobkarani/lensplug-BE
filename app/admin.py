from django.contrib import admin

from app.models import *

# Register your models here.

class VehicleLightsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

class VehicleLightsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}  

class AccessoriesCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}  

class BulbsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

class BulbsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}  

class GrillesCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

class GrillesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}  

class BumperAndPartsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

class BumperAndPartsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}    

admin.site.register(VehicleLightsCategory, VehicleLightsCategoryAdmin )
admin.site.register(VehicleLights, VehicleLightsAdmin)
admin.site.register(AccessoriesCategory, AccessoriesCategoryAdmin )
admin.site.register(Accessories, AccessoriesAdmin)
admin.site.register(BulbsCategory, BulbsCategoryAdmin )
admin.site.register(Bulbs, BulbsAdmin)
admin.site.register(GrillesCategory, GrillesCategoryAdmin )
admin.site.register(Grilles, GrillesAdmin)
admin.site.register(BumperAndPartsCategory, BumperAndPartsCategoryAdmin )
admin.site.register(BumperAndParts, BumperAndPartsAdmin)