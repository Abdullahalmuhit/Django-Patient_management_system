from django.db import models


class Nurse(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    profile_picture = models.FileField()
    assign_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    phone = models.CharField(max_length=200)
    cabin_no = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cabin(models.Model):
    #nurse_name = models.ForeignKey(Nurse, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    ward = models.CharField(max_length=50)
    room = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Patient(models.Model):
    #cabin_name = models.ForeignKey(Cabin, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    condition = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)
    admited_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    release_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


