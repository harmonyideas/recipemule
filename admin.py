from django.contrib import admin

# Register your models here.
from .models import Recipe, RecipePart, Ingredient, Course, RecipeCourse, FoodCategory, RecipeFoodCategory, Measurement, RecipeIngredient, Step, Image

admin.site.register(Recipe)
admin.site.register(RecipePart)
admin.site.register(Step)
admin.site.register(Ingredient)
admin.site.register(Course)
admin.site.register(RecipeCourse)
admin.site.register(FoodCategory)
admin.site.register(RecipeFoodCategory)
admin.site.register(Measurement)
admin.site.register(RecipeIngredient)
admin.site.register(Image)
