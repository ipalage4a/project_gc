from django.urls import include, path
from goodcreator import views

entries_patch = ([
    path('', views.EntryIndexView, name="list"),
    path('<str:pk>', views.EntryDetailView.as_view(), name="detail"),
], 'entries')

categories_patch = ([
    path('', views.CategoryIndexView, name="list"),
    path('<str:pk>', views.CategoryDetailView.as_view(), name="detail"),
], 'categories')

urlpatterns = [
    path('', views.index, name="index"),
    path('entries/', include(entries_patch)),
    path('categories/', include(categories_patch))
]