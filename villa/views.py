from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import ContactForm, FullContactForm, AddVillaForm, UserRegisterForm, UserLoginForm
from .models import *


def contact(request):
    return render(request, 'villa/contact.html')

class CategoryVilla(ListView):
    model = AllVilla
    context_object_name = 'all_villa'
    template_name = 'villa/category.html'
    paginate_by = 2

class GetCategory(ListView):
    context_object_name = 'all_villa'
    template_name = 'villa/category.html'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(*kwargs)
        return context

    def get_queryset(self):
        return AllVilla.objects.filter(category__slug=self.kwargs['slug'])

class GetVilla(DetailView):
    model = AllVilla
    template_name = 'villa/detail.html'
    context_object_name = 'all_villa'
    extra_context = {'populars': AllVilla.objects.order_by('-views')[:1]}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        return context

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['message'],
                'your send mail',
                ['your received mail'],
                fail_silently=True
            )
            if mail:
                return HttpResponse('<h2>Xabar Jo\'natildi</h2><p><a href="/">Home</a></p>')
            else:
                return HttpResponse('<h2>Xatolik yuz berdi</h2><p><a href="/">Home</a></p>')

    else:
        form = ContactForm()

    return render(request, 'villa/contact.html', {'form': form})


def fullcontent(request):
    all_villa = AllVilla.objects.all()
    if request.method == 'POST':
        form = FullContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(
                f"{form.cleaned_data['subject']} + {form.cleaned_data['name']}",
                f"{form.cleaned_data['message']} + {form.cleaned_data['email']}",
                'shaxboz.azamatov@inbox.ru',
                ['shaxboz9932@gmail.com'],
                fail_silently=True
            )
            if mail:
                return HttpResponse(f'<h2>Xabar Jo\'natildi</h2><p><a href="/">Home</a></p>')
            else:
                return HttpResponse('<h2>Xatolik yuz berdi</h2><p><a href="/">Home</a></p>')

    else:
        form = FullContactForm()

    return render(request, 'villa/index.html', {'form': form, 'all_villa': all_villa})

def add_villa(request):
    if request.user.is_authenticated:

        if request.method == 'POST':

                form = AddVillaForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect('home')
        else:
            form = AddVillaForm()
    else:
        return HttpResponse('<a href="/register">Ro\'yxatdan O\'ting</a> yoki <a href="/login">Kirish</a>')

    return render(request, 'villa/add_villa.html', {'form': form})

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
                form = UserRegisterForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Ro\'yxatdan Muvoffiqiyatli o\'tdingiz')
                    return redirect('register')
                else:
                    messages.error(request, 'Ro\'yxatdan o\'tishda xatolik yuz berdi')
        else:
            form = UserRegisterForm()
    else:
        return HttpResponse('Siz ro\'yxatdan o\'tgansiz\n<a href="/">Home</a>')
    return render(request, 'villa/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'villa/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


