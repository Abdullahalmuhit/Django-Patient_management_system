from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),

    path('getlogin/', views.getlogin, name='login'),
    path('profile/', views.profile, name='profile'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.getlogout, name="logout"),
    path('base/', views.base, name="base"),
    path('add_patient/', views.add_patient, name="add_patient"),
    path('patient_reg/', views.patient_reg, name="patient_reg"),
    path('add_cabin/', views.add_cabin, name="add_cabin"),
    path('cabin_reg/', views.cabin_reg, name="cabin_reg"),
    path('add_nurse/', views.add_nurse, name="add_nurse"),
    path('nurse_reg/', views.nurse_reg, name="nurse_reg"),
    path('nurse_list/', views.nurse_list, name="nurse_list"),
    path('cabin_list/', views.cabin_list, name="cabin_list"),
    path('patient_list/', views.patient_list, name="patient_list"),
    path('list/', views.list, name="list"),
    path('delete_nurse/<int:pid>', views.delete_nurse, name="delete_nurse"),
    path('delete_patient/<int:pid>', views.delete_patient, name="delete_patient"),
    path('delete_cabin/<int:pid>', views.delete_cabin, name="delete_cabin"),
    path('cabin_edit/<id>', views.cabin_edit, name="cabin_edit"),
    path('cabin_update/<id>', views.cabin_update, name='cabin_update'),
    path('nurse_edit/<id>', views.nurse_edit, name='nurse_edit'),
    path('nurse_update/<id>', views.nurse_update, name='nurse_update'),
    path('patient_edit/<id>', views.patient_edit, name='patient_edit'),
    path('patient_update/<id>', views.patient_update, name='patient_update'),
]
