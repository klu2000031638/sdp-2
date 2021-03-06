from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from .forms import ContactForm



class HomePageView(TemplateView):
    template_name = 'home.html'


class Profile(TemplateView):
    template_name = 'profile.html'

class About(TemplateView):
    template_name = 'about.html'

class Drone(TemplateView):
    template_name = 'drone.html'




# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['techbyone@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})

def successView(request):
    return render(request, "success.html", {})
