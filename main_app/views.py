# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# views.py

class ResearchPaper:
    def __init__(self, title, authors, publication_date, major_findings):
        self.title = title
        self.authors = authors
        self.publication_date = publication_date
        self.major_findings = major_findings

# Create a list of ResearchPaper instances
research_papers = [
    ResearchPaper(
        "Neural Mechanisms of Anorexia",
        ["Dr. Jane Smith", "Dr. John Doe"],
        "2023-04-15",
        "Identified altered activity in the hypothalamus linked to appetite suppression."
    ),
    ResearchPaper(
        "Cognitive Behavioral Therapy for PTSD",
        ["Dr. Emily Johnson", "Dr. Michael Lee"],
        "2022-10-20",
        "Showed significant improvement in PTSD symptoms after 12 weeks of therapy."
    ),
    ResearchPaper(
        "The Role of Gut Microbiota in Depression",
        ["Dr. Susan Martinez", "Dr. Robert Brown"],
        "2021-07-05",
        "Demonstrated a correlation between gut microbiota composition and depressive behavior in mice."
    ),
    ResearchPaper(
        "Genetic Variants Associated with Schizophrenia",
        ["Dr. Linda Green", "Dr. Richard White"],
        "2020-11-30",
        "Discovered several genetic variants significantly associated with an increased risk of schizophrenia."
    )
]



# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>All of your Selected Research Articles Found Here</h1>')

# main_app/views.py

def about(request):
    return render(request, 'about.html')

# views.py

def researchpaper_index(request):
    # Render the researchpapers/index.html template with the researchpapers data
    return render(request, 'researchpapers/index.html', {'researchpapers': research_papers})