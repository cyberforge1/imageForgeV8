from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.conf import settings

from django.shortcuts import render
import subprocess
from django.http import HttpResponse
import os
from imageGeneration.models import Prompt



def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

# Addition of imageForge Views

@login_required
def generation(request):
    """Show generation page."""
    return render(request, 'learning_logs/generation.html')

def gallery(request):
    """Show gallery page."""
    return render(request, 'learning_logs/gallery.html')

def user_history(request):
    """Show user history page."""
    return render(request, 'learning_logs/user_history.html')

def about(request):
    """Show the about page."""
    return render(request, 'learning_logs/about.html')

def prompt(request):
    most_recent_prompt = Prompt.objects.latest('date_added')
    context = {'prompt': most_recent_prompt}
    return render(request, 'learning_logs/prompt.html', context)


# Script execution on button click

def run_prompt_script(request):
    script_path = os.path.join(settings.BASE_DIR, 'newPromptInstance.py')
    subprocess.run(["python", script_path], cwd=settings.BASE_DIR)
    return redirect('learning_logs:prompt')

def run_image_script(request):
    script_path = os.path.join(settings.BASE_DIR, 'newImageInstance.py')
    subprocess.run(["python", script_path], cwd=settings.BASE_DIR)
    return redirect('imageForge:gallery')








