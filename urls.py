from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<recipe_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^r_new/$', views.recipe_new, name='recipe_new'),
    url(r'^ri_new/(?P<pk>\d+)$', views.recipe_ingredient_new, name='recipe_ingredient_new'),
    url(r'^s_new/(?P<pk>\d+)$', views.step_new, name='step_new'),
	url(r'^recipe_delete/(?P<pk>\d+)/$', views.recipe_delete, name='recipe_delete'),
	url(r'^ri_delete/(?P<pk>\d+)/$', views.recipe_ingredient_delete, name='recipe_ingredient_delete'),
	url(r'^step_delete/(?P<pk>\d+)/$', views.step_delete, name='step_delete'),
]


