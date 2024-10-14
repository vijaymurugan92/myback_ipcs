from django.urls import path
from .views import *



urlpatterns=[
    path('', index, name='powerapp/index'),
    path('m/', My_view),
    path('about/', Myview.as_view()),
    path('create/', create.as_view(), name = "powerapp/createmodelmodel.html"),
    path('list', lmodellistview.as_view(), name = 'powerapp/listmodel_list'),
    path('<pk>/', DetailView.as_view() ,name ='powerapp/detailmodel_detail.html'),
    path('<pk>/update', UpdateView.as_view(), name='powerapp/updatemodel_form.html'),
    path('<pk>/delete', DeleteView.as_view(), name='powerapp/deletemodel_form.html'),
]