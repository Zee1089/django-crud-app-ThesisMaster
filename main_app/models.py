from django.db import models
from django.urls import reverse

class ResearchPaper(models.Model):
    title = models.CharField(max_length=250)
    authors = models.CharField(max_length=500) 
    journal = models.CharField(max_length=250)  # Added field for journal name
    publication_date = models.DateField()  # Changed to DateField to store dates
    major_findings = models.TextField()  # Changed to TextField for textual data

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
    # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('researchpaper-detail', kwargs={'researchpaper_id': self.id})