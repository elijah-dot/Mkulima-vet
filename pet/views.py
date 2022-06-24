from django.shortcuts import render, redirect,reverse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView
from .models import Vet


class hospitalView(TemplateView):
    template_name = 'index.html'
    
# def hospitalView(request):
#     return render(request, 'index.html')

# def DoctorListView(request):
#     queryset = Doctor.objects.all()
#     return render(request, 'doctor-team.html', {'queryset': queryset})
    


class DoctorListView(ListView):
    queryset = Vet.objects.all()
    template_name = 'doctor-team.html'



# class ContactView(TemplateView):
#     template_name = 'contact.html'
#     # return render(request, 'contact/contact.html', context)
#         # name = request.POST.get('name')
#         # email_from = request.POST.get('email')
#         # subject = request.POST.get('subject')
#         # message = request.POST.get('message')

#         # if subject == '':
#         #     subject = 'Healthcae Contact'     

#         # if name and message and email_from:
#         #     send_mail(
#         #         subject+ " - " + name,
#         #         message+ 
#         #         email_from,
#         #         ['yourname@gmail.com',],
#         #         fail_silently=False,
#         #     )
#         #     messages.success(request, f'Your message has been sent. Thank you {name}!')

#         return redirect('contact')
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # return render(request, 'contact/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)



@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home.html')

def profile(request, username):
    return render(request, 'profile.html')

def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm()
    return render(request, 'editprofile.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def pet(request):
    #check the form is submitted or not
    if request.method == 'POST':
        pet = PetForm(request.POST)
        #check the form data are valid or not
        if pet.is_valid():
            #Read the submitted values
            name = request.POST.get('name')
            age = request.POST.get('age')
            kind = request.POST.get('kind')
            user = request.user
            pet = Pet(name=name, age=age, kind=kind, user=user)
            
            
            
            pet.save()
            #merge the values
            data = ['Your pet registration is completed successfully.<br />', 'Name:', name, '<br />','Age:', age, '<br />', 'Kind:', kind, '<br />','User:', user]
            #return form values as response
            return HttpResponse(data)
        else:
            #display the petform
            form = PetForm()
            return render(request,"pet.html",{'form':form})
            
    form = PetForm()        
    return render(request,"pet.html",{'form':form})


def available(request):
    vets = Vet.objects.all()


    context = {'vets': vets,'user':request.user}
    return render(request,'pet/available.html', context=context)

def booking(request,vetName):
    form = AppointmentForm()
    
    pets = Pet.objects.all().filter(user_id=request.user)
    form.fields['pet'].queryset = pets
    try:
        vet = Vet.objects.get(pk=vetName)
        context = {'form': form, 'vet':vet,'user':request.user}
    except Vet.DoesNotExist:
        return Http404
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        # print(form.errors)
        if form.is_valid():
          new_appointment = Appointment(pet=form.cleaned_data['pet'], vet=vet, time_booked=form.cleaned_data['time_booked'],service=form.cleaned_data['service'], date=form.cleaned_data['date'],when_the_booking_was_done=datetime.now(),pet_owner=request.user)
          new_appointment.save()
          print(new_appointment)




          return HttpResponseRedirect (reverse('available'))
        return render(request,'pet/booking.html')
    return render(request,'pet/booking.html',context=context)

def user_appointments(request):
    print(request.user)
    try:
        logged_user = User.objects.get(username=request.user)
        
        print(logged_user)
        appointments = Appointment.objects.all().filter(pet_owner=logged_user)
        context = {'appointments': appointments,'user':request.user}
    except Exception as e:
        message = 'You do not have any Appointments'
        context = {'message': message,'user':request.user}
        return render(request,'pet/appointments.html',context=context)

    context = {'appointments': appointments,'user':request.user}
    
    

    return render(request,'pet/appointments.html',context=context)

    




def vet_appointments(request):
    try:
        appointments = Appointment.objects.all().filter(vet=request.user)
    except Exception as e:
        message = 'You do not have any Appointments'
        context = {'message': message}
        return render(request,'pet/appointments.html',context=context)

    context = {'appointments': appointments,'user':request.user}

    return render(request,'pet/appointments.html',context=context)

def delete_appointment(request,appointment):
    app = Appointment.objects.get(pk=appointment)
    app.delete()
    return HttpResponseRedirect(reverse('user_appointments'))





