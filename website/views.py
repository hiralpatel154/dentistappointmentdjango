from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact, Appointment
from Dentist.settings import EMAIL_HOST_USER as emailfrom
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views import View


def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        return render(request, 'confirmcontact.html', {'name': contact.name})
    else:
        return render(request, 'contact.html')


def about(request):
    return render(request, 'home.html')


class Appoint(View):
    def get(self, *args, **kwargs):
        return render(self.request, "appointment.html")

    def post(self, *args, **kwargs):
        try:
            appoint = Appointment()
            name = self.request.POST.get('name')
            date = self.request.POST.get('date')
            time = self.request.POST.get('time')
            email = self.request.POST.get('email')
            phone_number = self.request.POST.get('phone_number')
            appoint.name = name
            appoint.date = date
            appoint.time = time
            appoint.email = email
            appoint.phone_number = phone_number
            data = self.request.POST.get
            appoint.save()
            res = send_mail("Appointment Successful",
                            "Patient Name: {}\n Date of Appointment : {}\n Time of appointment : {}\n Your contact number : {}".format(appoint.name,appoint.date, appoint.time, appoint.phone_number), emailfrom, [data("email")])
            return render(self.request, 'appointdetail.html', {
            'name': appoint.name,
            'date': appoint.date,
            'time': appoint.time,
            'phone_number': appoint.phone_number, })
        except Exception as exe:
            return HttpResponse(exe)


def blog(request):
    return render(request, 'blog.html')


def blogsingle(request):
    return render(request, 'blog-single.html')


def department(request):
    return render(request, 'department.html')


def price(request):
    return render(request, 'pricing.html')
