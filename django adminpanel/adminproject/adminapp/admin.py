from django.contrib import admin
from .models import Nurse,Cabin,Patient

# Register your models here.
class AuthorNurse(admin.ModelAdmin):
    list_display = ["__str__", 'name', 'email', 'phone']
    search_fields = ["__str__", 'name']
    list_filter = ['assign_date']
    class Meta:
        model = Nurse
admin.site.register(Nurse, AuthorNurse)

class AuthorPatient(admin.ModelAdmin):
    list_display = ["__str__", 'name', 'condition']
    search_fields = ["__str__", 'name']
    list_filter = ['admited_on']
    class Meta:
        model = Patient
admin.site.register(Patient, AuthorPatient)


class AuthorCabin(admin.ModelAdmin):
    list_display = ["__str__", 'ward', 'room']
    search_fields = ["__str__", 'name']
    list_filter = ['name']
    class Meta:
        model = Cabin
admin.site.register(Cabin, AuthorCabin)
