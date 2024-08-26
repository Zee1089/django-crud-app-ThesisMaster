from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

class Theme(models.Model):
    theme_name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    keywords = models.CharField(max_length=50)

    def __str__(self):
        return self.theme_name

    def get_absolute_url(self):
        return reverse('theme-detail', kwargs={'pk': self.id})

class ResearchPaper(models.Model):
    title = models.CharField(max_length=250)
    authors = models.CharField(max_length=500) 
    journal = models.CharField(max_length=250)  
    publication_date = models.DateField() 
    major_findings = models.TextField(max_length=800)
    themes = models.ManyToManyField(Theme)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
    # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('researchpaper-detail', kwargs={'researchpaper_id': self.id})


class Comment(models.Model):
    date = models.DateField(auto_now_add=True)
    note = models.TextField(max_length=400)
    researchpaper = models.ForeignKey(ResearchPaper, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"Comment by {self.user.username} on {self.date}"
        
    class Meta:
        ordering = ['-date']  # This line makes the newest feedings appear first

