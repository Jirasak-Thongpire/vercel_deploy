from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'simple.html')

def about(request):
    context = {
        'about_page': True,
        'title': 'About Us',
        'content': 'This is the about page of our Django application deployed on Vercel.'
    }
    return render(request, 'simple.html', context)
