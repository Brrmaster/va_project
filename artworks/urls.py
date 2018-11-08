from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='artworks' ),
	path('<int:artwork_id>', views.listing, name='artwork'),
]