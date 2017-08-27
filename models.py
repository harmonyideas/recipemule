from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import select2.fields
import select2.models

# Create your models here.

@python_2_unicode_compatible
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image_filename = models.CharField(max_length=256, default="default.jpg")
    recipe_description = models.CharField(max_length=500, default=None)
    def __str__(self):
	return self.recipe_name

class Image(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=256, default="default.jpg")
    image_filename = models.CharField(max_length=256)
    image_text = models.CharField(max_length=100)

class RecipePart(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    recipe_id_part = models.IntegerField()
    recipe_part_text = models.CharField(max_length=100)

    def __str__(self):
	return self.recipe_part_text

class Ingredient(models.Model):
    ingredient_text = models.CharField(max_length=256)
    active = models.CharField(max_length=25)
    class Meta:
	ordering = ('ingredient_text',)
    def __unicode__(self):
	return self.ingredient_text


class Course(models.Model):
    course_text = models.CharField(max_length=100)
    active = models.CharField(max_length=25)

    def __str__(self):
	return self.course_text

class RecipeCourse(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE) 
    course_id = models.ForeignKey(Course)

class FoodCategory(models.Model):
    food_category_text = models.CharField(max_length=100)
    active = models.CharField(max_length=25)

    def __str__(self):
	return self.food_category_text

class RecipeFoodCategory(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    food_category_id = models.ForeignKey(FoodCategory)

class Measurement(models.Model):
    measurement_text = models.CharField(max_length=50)
    abbreviation_text = models.CharField(max_length=10)
    active = models.CharField(max_length=25)

    def __str__(self):
	return self.measurement_text

class Step(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step_instructions_text = models.CharField(max_length=400)
    step_number = models.IntegerField(blank=True)

    def __str__(self):
	return self.step_instructions_text

class RecipeIngredient(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.FloatField()
    measurement_id = models.ForeignKey(Measurement)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    note_text = models.CharField(max_length=400) 
    def __unicode__(self):
        return self.note_text
