from django.db import models

# Create your models here.
from django.db import models

class ResearchPaper(models.Model):
    title = models.CharField(max_length=250)
    authors = models.TextField()  # Changed to TextField for potentially longer author lists
    journal = models.CharField(max_length=250)  # Added field for journal name
    publication_date = models.DateField()  # Changed to DateField to store dates
    major_findings = models.TextField()  # Changed to TextField for textual data

    def __str__(self):
        return self.title