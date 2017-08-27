from django.shortcuts import render
# Create your views here.
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import  HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Recipe, RecipeIngredient, Ingredient, Step, Measurement, Image
from .forms import RecipeForm, RecipeIngredientForm, StepForm
from django.http import Http404
from django.utils import timezone

def index(request):
	
	try:
		r_form = RecipeForm(instance=Recipe())	

		if request.method == "POST":
			r_form = RecipeForm(request.POST, instance=Recipe()) 
		if r_form.is_valid():
			recipe = r_form.save(commit=False)
			recipe.recipe_name = request.POST.get('recipe_name')
			recipe.recipe_description = request.POST.get('recipe_description')
			recipe.pub_date = timezone.now()
			recipe.save()
			return HttpResponseRedirect('/recipemule')

		latest_recipe_list = {}
		latest_recipe_list['list'] = Recipe.objects.order_by('recipe_name')[:25]
		return render(request, 'recipemule/index.html', {'latest_recipe_list': latest_recipe_list, 'r_form' : r_form})
	
	except Recipe.DoesNotExist:
		
		raise Http404("Recipe does not exist")
	
	
def detail(request, recipe_id):

	try:
		recipe_details = {}
		recipe = get_object_or_404(Recipe, pk=recipe_id)
		recipe_details['frmRecipe'] = RecipeForm(request.POST or None, instance=recipe)
		recipe_details['frmRecipeIngredient'] = RecipeIngredientForm(instance=RecipeIngredient())
		recipe_details['frmStep'] = StepForm(instance=Step())
		recipe_details['RecipeMain'] = Recipe.objects.filter(id=recipe_id)
		recipe_details['RecipeIngredient'] = RecipeIngredient.objects.filter(recipe_id=recipe_id)
		recipe_details['RecipeStep'] = Step.objects.filter(recipe_id=recipe_id)

		if request.method == "POST":
			recipe_details['frmRecipe'] = RecipeForm(request.POST, instance=Recipe())	
			recipe_details['frmStep'] = StepForm(request.POST, instance=Step())	
			recipe_details['frmRecipeIngredient'] = RecipeIngredientForm(request.POST, instance=RecipeIngredient())			

		if recipe_details['frmRecipe'].is_valid():
			recipe.recipe_name = request.POST.get('recipe_name')
			recipe.pub_date = timezone.now()
			recipe.recipe_description = request.POST.get('recipe_description')
			recipe.save()
			return HttpResponseRedirect(reverse('detail', args=(recipe_id,)))

		if recipe_details['frmRecipeIngredient'].is_valid():
			recipe_i = recipe_details['frmRecipeIngredient'].save(commit=False)
		   	recipe_i.recipe_id = Recipe.objects.get(id=recipe_id)
		   	recipe_i.amount = request.POST.get('amount')
		   	recipe_i.measurement_id = Measurement.objects.get(id=request.POST.get('measurement_id'))
		   	recipe_i.ingredient_id = Ingredient.objects.get(id=request.POST.get('ingredient_id'))
		   	recipe_i.note_text = request.POST.get('note_text')	
		   	recipe_i.save() 
			return HttpResponseRedirect(reverse('detail', args=(recipe_id,)))

		if recipe_details['frmStep'].is_valid():
		
			recipe_s = recipe_details['frmStep'].save(commit=False)

			if request.POST.get('step_number'):
				recipe_s.step_number = request.POST.get('step_number')
			else:
				recipe_s.step_number = Step.objects.filter(recipe_id=recipe_id).count()
			
			recipe_s.recipe_id = Recipe.objects.get(id=recipe_id)
			recipe_s.step_instructions_text = request.POST.get('step_instructions_text')
			recipe_s.save() 
			return HttpResponseRedirect(reverse('detail', args=(recipe_id,)))
		
	except Recipe.DoesNotExist:
		
		raise Http404("Recipe does not exist")

	return render(request, 'recipemule/detail.html', {'recipe_details': recipe_details})


def recipe_new(request):
	
	if request.method == "POST":
		r_form = RecipeForm(request.POST, instance=Recipe()) 
	
	if r_form.is_valid():
		recipe = r_form.save(commit=False)
		recipe.recipe_name = request.POST.get('recipe_name')
		recipe.pub_date = timezone.now()
		recipe.save() 
		return render(request, 'recipemule/recipe_edit.html', {'r_form': r_form})
	
	else:
		r_form = RecipeForm(instance=Recipe())
		return render(request, 'recipemule/recipe_edit.html', {'r_form': r_form})

def recipe_ingredient_new(request, pk):

	if request.method == "POST":
		ri_form = RecipeIngredientForm(request.POST, instance=RecipeIngredient())
	
	if	([ri_form.is_valid() for ri in ri_form]):
		return render(request, 'recipemule/recipe_ingredient_edit.html', {'ri_form': ri_form})
	
	else:
		ri_form = RecipeIngredientForm(initial={'recipe_id': pk}) 
		ri_form.fields["recipe_id"].queryset = Recipe.objects.filter(pk=pk)

	return render(request, 'recipemule/recipe_ingredient_edit.html', {'ri_form': ri_form})


def step_new(request, pk):
  
	if request.method == "POST":
		s_form = StepForm(request.POST, instance=StepForm())
		s_form = StepForm(initial={'step_number': pk}) 

	if	([s_form.is_valid() for s in s_form]):
			return render(request, 'recipemule/recipe_step_edit.html', {'s_form': s_form})
	else:
		s_form = StepForm(initial={'step_number': (Step.objects.filter(recipe_id=pk).count()) + 1, 'recipe_id': pk}) 

	return render(request, 'recipemule/recipe_step_edit.html', {'s_form': s_form})


def recipe_delete(request, pk):

 	try: 
		recipe = get_object_or_404(Recipe, pk=pk)
		detail_id = recipe.id
		recipe.delete()
		return HttpResponseRedirect(reverse('index'))

	except RecipeIngredient.DoesNotExist:

		raise Http404("Recipe does not exist")

def recipe_ingredient_delete(request, pk):

 	try: 
		recipe_i = get_object_or_404(RecipeIngredient, pk=pk)
		detail_id = recipe_i.recipe_id.id
		recipe_i.delete()
		return HttpResponseRedirect(reverse('detail', args=(detail_id,)))

	except RecipeIngredient.DoesNotExist:

		raise Http404("Recipe does not exist")

def step_delete(request, pk):

 	try: 
		step_object = get_object_or_404(Step, pk=pk)
		detail_id = step_object.recipe_id.id
		step_object.delete()
		return HttpResponseRedirect(reverse('detail', args=(detail_id,)))

	except Step.DoesNotExist:

		raise Http404("Step does not exist")
