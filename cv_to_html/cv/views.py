# cv/views.py
from django.shortcuts import render
from .models import Profile, Experience, Education, Skill

def cv_view(request):
    # Fetch all the data from the database
    # .first() assumes you only have one profile.
    profile = Profile.objects.first()
    experiences = Experience.objects.all().order_by('-start_date')
    educations = Education.objects.all().order_by('-graduation_year')
    skills = Skill.objects.all()

    # Pack the data into a context dictionary
    context = {
        'profile': profile,
        'experiences': experiences,
        'educations': educations,
        'skills': skills,
    }

    # Render the template with the context
    return render(request, 'cv/resume.html', context)