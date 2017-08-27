from django import forms
from django.db import models
from django.utils.encoding import force_text

from django_select2.forms import (
    HeavySelect2MultipleWidget, HeavySelect2Widget, ModelSelect2TagWidget,
    ModelSelect2Widget, Select2Widget, Select2TagWidget
)

from .models import Recipe, RecipeIngredient, Ingredient, Step

from django.contrib.admin import widgets

class RecipeForm(forms.ModelForm):
	recipe_description = forms.CharField( widget=forms.Textarea)
	class Meta:
		model = Recipe
		exclude = ['pub_date']
		labels = {
			'recipe_name': ('Recipe Name'),
		}
		
class MyWidget(ModelSelect2Widget):
	search_fields = [
	'ingredient_text__icontains',
	]

class RecipeIngredientForm(forms.ModelForm):
	
	class Meta:
		model = RecipeIngredient
		exclude = ['recipe_id']
		labels = {'ingredient_id': ('Ingredient'), 'measurement_id': ("Unit of Measure"),'note_text': ("Notes") }
		widgets = {
			'ingredient_id': MyWidget,
		}

class StepForm(forms.ModelForm):
	step_instructions_text = forms.CharField(label='Instructions', widget=forms.Textarea)
        class Meta:
		model = Step
		exclude = ['recipe_id','step_number']

