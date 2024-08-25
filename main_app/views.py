from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import ResearchPaper, Comment, Status
from .forms import CommentForm

class ResearchPaperCreate(CreateView):
    model = ResearchPaper
    fields = '__all__'
    success_url = '/researchpapers/'

class ResearchPaperUpdate(UpdateView):
    model = ResearchPaper
    # Specify the fields that can be updated
    fields = ['title', 'authors', 'journal', 'publication_date', 'major_findings']

class ResearchPaperDelete(DeleteView):
    model = ResearchPaper
    success_url = '/researchpapers/'  # Update the success URL to match your research papers' app

class StatusCreate(CreateView):
    model = Status
    fields = '__all__'

class StatusList(ListView):
    model = Status

class StatusDetail(DetailView):
    model = Status

class StatusUpdate(UpdateView):
    model = Status
    fields = ['date', 'status']

class StatusDelete(DeleteView):
    model = Status
    success_url = '/status/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def researchpaper_index(request):
    # Query all ResearchPaper objects from the database
    researchpapers = ResearchPaper.objects.all()
    # Render the researchpapers/index.html template with the researchpapers data
    return render(request, 'researchpapers/index.html', {'researchpapers': researchpapers})

def researchpaper_detail(request, researchpaper_id):
    researchpaper = ResearchPaper.objects.get(id=researchpaper_id)
    comment_form = CommentForm()
    return render(request, 'researchpapers/detail.html', {'researchpaper' : researchpaper, 'comment_form' : comment_form})

def add_comment(request, researchpaper_id):
    # create a ModelForm instance using the data in request.POST
    form = CommentForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_comment = form.save(commit=False)
        new_comment.researchpaper_id = researchpaper_id
        new_comment.save()
    return redirect('researchpaper-detail', researchpaper_id=researchpaper_id)
