from django.shortcuts import render

def tower_about(request):
    return render(request, 'tower_about.html', {'current_page': 'about'})

def tower_contact(request):
    return render(request, 'tower_contact.html', {'current_page': 'contact'})

def tower_home(request):    
    return render(request, 'tower_home.html', {'current_page': 'home'})

def tower_services(request):
    return render(request, 'tower_services.html', {'current_page': 'services'})