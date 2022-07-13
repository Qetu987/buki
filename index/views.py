from django.shortcuts import render
from tutor.models import Subject

# Create your views here.
def main_page(r):
    subjects = Subject.objects.filter(is_active=True)
    return render(r, 'main_page.html', {'subjects': subjects})