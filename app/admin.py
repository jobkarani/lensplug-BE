from django.contrib import admin

from app.models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

class BabyShowerCakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}    

class BridalShowerCakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

class ChristmasCakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

class EasterCakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

class FathersDayCakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

class MothersDayCakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

class GraduationCakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

class ValentinesCakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

class RuracioCakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

class EngagementCakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

class CoporateCakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

class AnniversaryCakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

class BaptismalCakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

class ChristeningCakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

class WeddingCakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

class BirthdayCakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(BabyShowerCakes, BabyShowerCakesAdmin )
admin.site.register(BirthdayCakes, BirthdayCakesAdmin )
admin.site.register(BridalShowerCakes, BridalShowerCakesAdmin )
admin.site.register(ChristmasCakes, ChristmasCakesAdmin )
admin.site.register(EasterCakes, EasterCakesAdmin )
admin.site.register(FathersDayCakes, FathersDayCakesAdmin )
admin.site.register(MothersDayCakes, MothersDayCakesAdmin )
admin.site.register(GraduationCakes, GraduationCakesAdmin )
admin.site.register(ValentinesCakes, ValentinesCakesAdmin )
admin.site.register(RuracioCakes, RuracioCakesAdmin )
admin.site.register(EngagementCakes, EngagementCakesAdmin )
admin.site.register(CoporateCakes, CoporateCakesAdmin )
admin.site.register(AnniversaryCakes, AnniversaryCakesAdmin )
admin.site.register(BaptismalCakes, BaptismalCakesAdmin )
admin.site.register(ChristeningCakes, ChristeningCakesAdmin )
admin.site.register(WeddingCakes, WeddingCakesAdmin )
admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blogs)