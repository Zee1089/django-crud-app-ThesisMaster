from django.contrib import admin
from .models import ResearchPaper, Comment, Status

admin.site.register(ResearchPaper)
admin.site.register(Comment)
admin.site.register(Status)


