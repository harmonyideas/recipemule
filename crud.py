from crudbuilder.abstract import BaseCrudBuilder
from .models import Recipe, RecipeIngredient, Step

class RecipeCrud(BaseCrudBuilder):
	model=Recipe
	search_fields = ['recipe_text']
	tables2_fields = ('recipe_text',)
	tables2_css_class = "table table-bordered table-condensed"
	tables2_pagination = 20  # default is 10
    	modelform_excludes = ['created_by', 'updated_by']
	
	custom_templates = {
	'list': 'crudbuilder/recipe/list.html'
	}

#    	login_required=True
#    	permission_required=True

class RecipeIngredientCrud(BaseCrudBuilder):
	model=RecipeIngredient
	search_fields = ['ingredient_id__ingredient_text']
	tables2_fields = ('recipe_id','ingredient_id', 'amount', 'measurement_id', 'note_text')
	tables2_css_class = "table table-bordered table-condensed"
	tables2_pagination = 20  # default is 10
    	modelform_excludes = ['created_by', 'updated_by']
#    	login_required=True
#    	permission_required=True

class StepCrud(BaseCrudBuilder):
	model=Step
	search_fields = ['step_instructions_text']
	tables2_fields = ('step_number', 'step_instructions_text')
	tables2_css_class = "table table-bordered table-condensed"
	tables2_pagination = 20  # default is 10
    	modelform_excludes = ['created_by', 'updated_by']
#    	login_required=True
#    	permission_required=True
