from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path(
        'peliculas',
        views.PeliculasCreate.as_view(),
        name='peliculas_create'
    ),
        path(
        'socios',
        views.SociosCreate.as_view(),
        name='socios_create'
    ),
    path(
        'alquiler',
        views.AltaCreate.as_view(),
        name='alquiler_create'
    ),
        path(
        'estadisticas',
        views.AltaEstadistica.as_view(),
        name='estadisticas_create'
    ),
]