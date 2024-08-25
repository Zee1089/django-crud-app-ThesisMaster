# main_app/views.py

from django.shortcuts import render
from .models import ResearchPaper 
# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# views.py

# class ResearchPaper:
#     def __init__(self, title, authors, journal, publication_date, major_findings):
#         self.title = title
#         self.authors = authors
#         self.journal = journal
#         self.publication_date = publication_date
#         self.major_findings = major_findings

# # Create a list of ResearchPaper instances
# research_papers = [
#     ResearchPaper(
#         "Neural Mechanisms of Anorexia",
#         ["Dr. Jane Smith", "Dr. John Doe"],
#         "Journal of Neuroscience",
#         "2023-04-15",
#         "Identified altered activity in the hypothalamus linked to appetite suppression."
#     ),
#     ResearchPaper(
#         "Cognitive Behavioral Therapy for PTSD",
#         ["Dr. Emily Johnson", "Dr. Michael Lee"],
#         "Journal of Clinical Psychology",
#         "2022-10-20",
#         "Showed significant improvement in PTSD symptoms after 12 weeks of therapy."
#     ),
#     ResearchPaper(
#         "The Role of Gut Microbiota in Depression",
#         ["Dr. Susan Martinez", "Dr. Robert Brown"],
#         "Journal of Psychiatry & Neuroscience",
#         "2021-07-05",
#         "Demonstrated a correlation between gut microbiota composition and depressive behavior in mice."
#     ),
#     ResearchPaper(
#         "Genetic Variants Associated with Schizophrenia",
#         ["Dr. Linda Green", "Dr. Richard White"],
#         "Journal of Genetic Research",
#         "2020-11-30",
#         "Discovered several genetic variants significantly associated with an increased risk of schizophrenia."
#     )
# ]


# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>All of your Selected Research Articles Found Here</h1>')

# main_app/views.py

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