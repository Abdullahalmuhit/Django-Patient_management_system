from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import PatientReg
from .models import Patient,Cabin, Nurse
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        context = {
            'user':user
        }
        return render(request, 'index.html', context)
    else:
        return redirect('login')
def icons(request):
    return render(request, 'examples/icons.html')


def map(request):
    return render(request, 'examples/maps.html')


def profile(request):
    return render(request, 'examples/profile.html')


def table(request):
    return render(request, 'examples/tables.html')


def registration(request):
    return render(request, 'examples/register.html')


def patient_reg(request):
    print(request.POST)
    name = request.GET['p_name']
    email = request.GET['p_email']
    phone = request.GET['p_phone']
    ward = request.GET['p_ward_no']
    condition = request.GET['p_condition']
    disease = request.GET['p_disease']
    store = Patient(name=name, email=email, phone=phone, condition=condition, ward=ward, disease=disease)
    store.save()
    messages.success(request, 'Patient is successfully Created')
    return redirect('patient_list')


def nurse_reg(request):
    print(request.POST)
    name = request.GET['name']
    email = request.GET['email']
    phone = request.GET['phone']
    cabin_no = request.GET['cabin_no']
    store = Nurse(name=name, email=email, phone=phone, cabin_no=cabin_no)
    store.save()
    messages.success(request, 'Nurse is successfully Created')
    return redirect('nurse_list')


def cabin_reg(request):
    print(request.POST)
    name = request.GET['name']
    ward = request.GET['ward']
    room = request.GET['room']
    store = Cabin(name=name, ward=ward, room=room)
    store.save()
    messages.success(request, 'Cabin is successfully Created')
    return redirect('cabin_list')




def add_patient(request):
    return render(request, 'examples/add_patient.html')


def add_cabin(request):
    return render(request, 'examples/add_cabin.html')


def add_nurse(request):
    return render(request, 'examples/add_nurse.html')


def getlogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('index')
            else:
                messages.add_message(request, messages.ERROR, 'User Or Password Not Match!!')
                return render(request, 'examples/login.html')
    return render(request, 'examples/login.html')

def getlogout(request):
    logout(request)
    return redirect('login')

def base(request):
    return render(request, 'examples/base.html')


def nurse_list(request):
    list = Nurse.objects.all()
    context={
        'list':list
    }
    return render(request, 'examples/nurse_list.html', context)


def cabin_list(request):
    list = Cabin.objects.all()
    context={
        'list':list
    }
    return render(request, 'examples/cabin_list.html', context)

def patient_list(request):
    list = Patient.objects.all()
    context={
        'list':list
    }
    return render(request, 'examples/patient_list.html', context)


def list(request):
    return render(request,'examples/list.html')


def delete_nurse(request, pid):
    if request.user.is_authenticated:
        nurse = get_object_or_404(Nurse, id=pid)
        nurse.delete()
        messages.warning(request, 'Nurse is successfully deleted')
        return redirect('nurse_list')
    else:
        return redirect('login')


def delete_patient(request, pid):
    if request.user.is_authenticated:
        nurse = get_object_or_404(Patient, id=pid)
        nurse.delete()
        messages.warning(request, 'Patient is successfully deleted')
        return redirect('patient_list')
    else:
        return redirect('login')


def delete_cabin(request, pid):
    if request.user.is_authenticated:
        nurse = get_object_or_404(Cabin, id=pid)
        nurse.delete()
        messages.warning(request, 'Cabin is successfully deleted')
        return redirect('cabin_list')
    else:
        return redirect('login')

# cabin update

def cabin_edit(request, id):
    text = Cabin.objects.get(pk=id)
    return render(request, 'examples/cabin_update.html', {'text': text})

def cabin_update(request, id):
    if request.user.is_authenticated:
        text = Cabin.objects.get(pk=id)
        text.name = request.GET['name']
        text.ward = request.GET['ward']
        text.room = request.GET['room']
        text.save()
        messages.success(request, 'Cabin is successfully updated')
        return redirect("cabin_list")
    else:
        return redirect('login')

# end cabin update
# nurse update

def nurse_edit(request, id):
    text = Nurse.objects.get(pk=id)
    return render(request, 'examples/nurse_update.html', {'text': text})


def nurse_update(request, id):
    if request.user.is_authenticated:
        text = Nurse.objects.get(pk=id)
        text.name = request.GET['name']
        text.email = request.GET['email']
        text.phone = request.GET['phone']
        text.cabin_no = request.GET['cabin_no']
        text.save()
        messages.success(request, 'Nurse is successfully updated')
        return redirect("nurse_list")
    else:
        return redirect('login')



def patient_edit(request, id):
    text = Patient.objects.get(pk=id)
    return render(request, 'examples/patient_update.html', {'text': text})



def patient_update(request, id):
    if request.user.is_authenticated:
        text = Patient.objects.get(pk=id)
        text.name = request.GET['name']
        text.email = request.GET['email']
        text.phone = request.GET['phone']
        text.condition = request.GET['condition']
        text.ward = request.GET['ward']
        text.disease = request.GET['disease']
        text.save()
        messages.success(request, 'Patient is successfully updated')
        return redirect("patient_list")
    else:
        return redirect('login')