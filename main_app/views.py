from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ResearchPaper 

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



def about(request):
    return render(request, 'about.html')

# views.py

def researchpaper_index(request):
    # Query all ResearchPaper objects from the database
    researchpapers = ResearchPaper.objects.all()
    # Render the researchpapers/index.html template with the researchpapers data
    return render(request, 'researchpapers/index.html', {'researchpapers': researchpapers})

def researchpaper_detail(request, researchpaper_id):
    researchpaper = ResearchPaper.objects.get(id=researchpaper_id)
    return render(request, 'researchpapers/detail.html', {'researchpaper' : researchpaper})