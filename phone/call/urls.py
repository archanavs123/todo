from django.urls import path
from . import views
urlpatterns = [
    path('',views.base,name='base'),
    path('add/',views.add,name='add'),
    path('view_details/',views.view_details,name='view'),
    path('individual/',views.individual,name='individual'),
    path('update/',views.update,name='update'),
    path('delete/',views.delete,name='delete'),






]