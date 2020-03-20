from django.contrib import admin
from .models import Camera, ShortDefenition, ShortDefenitionImage, Characteristic, Category, Filter, Accessory


# Register your models here.

class FilterInLine(admin.TabularInline):
	model = Filter
	extra = 1

class ShortDefenitionImageInLine(admin.TabularInline):
	model = ShortDefenitionImage
	extra = 1

class CharacteristicInLine(admin.TabularInline):
	model = Characteristic
	extra = 1

class ShortDefenitionInLine(admin.TabularInline):
	model = ShortDefenition
	extra = 1



class CameraAdmin(admin.ModelAdmin):
    inlines = [ShortDefenitionImageInLine, ShortDefenitionInLine, CharacteristicInLine, FilterInLine]



admin.site.register(Camera, CameraAdmin)
admin.site.register(ShortDefenition)
admin.site.register(ShortDefenitionImage)
admin.site.register(Characteristic)
admin.site.register(Category)
admin.site.register(Filter)
admin.site.register(Accessory)