from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import ResearchPaper, Comment, Theme
from .forms import CommentForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('researchpaper-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )
    
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def researchpaper_index(request):
    # Query all ResearchPaper objects from the database
    researchpapers = ResearchPaper.objects.filter(user=request.user)
    themes = Theme.objects.all()
    # Render the researchpapers/index.html template with the researchpapers data
    return render(request, 'researchpapers/index.html', {'researchpapers': researchpapers, 'themes': themes})

@login_required
def researchpaper_detail(request, researchpaper_id):
    researchpaper = ResearchPaper.objects.get(id=researchpaper_id)
    themes = Theme.objects.all()

     # Only get the toys the cat does not have
    # status_researchpaper_doesnt_have = Status.objects.exclude(id__in = researchpaper.status.all().values_list('id'))
 
    comment_form = CommentForm()
    return render(request, 'researchpapers/detail.html', {'researchpaper' : researchpaper, 'comment_form' : comment_form, 'themes': themes})

@login_required
def add_comment(request, researchpaper_id):
    # create a ModelForm instance using the data in request.POST
    form = CommentForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_comment = form.save(commit=False)
        new_comment.researchpaper_id = researchpaper_id
        new_comment.user = request.user
        new_comment.save()
    return redirect('researchpaper-detail', researchpaper_id=researchpaper_id)


class ResearchPaperCreate(LoginRequiredMixin, CreateView):
    model = ResearchPaper
    fields = ['title', 'authors', 'journal','publication_date', 'major_findings', 'url' , 'entire_paper']
    success_url = '/researchpapers/'
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)


class ResearchPaperUpdate(LoginRequiredMixin, UpdateView):
    model = ResearchPaper
    # Specify the fields that can be updated
    fields = ['title', 'authors', 'journal', 'publication_date', 'major_findings']

class ResearchPaperDelete(LoginRequiredMixin, DeleteView):
    model = ResearchPaper
    success_url = '/researchpapers/'  # Update the success URL to match your research papers' app

class ThemeCreate(LoginRequiredMixin, CreateView):
    model = Theme
    fields = '__all__'

class ThemeList(LoginRequiredMixin, ListView):
    model = Theme

class ThemeDetail(LoginRequiredMixin, DetailView):
    model = Theme

class ThemeUpdate(LoginRequiredMixin, UpdateView):
    model = Theme
    fields = ['theme_name', 'keywords']

class ThemeDelete(LoginRequiredMixin, DeleteView):
    model = Theme
    success_url = '/themes/'


@login_required
def associate_theme(request, researchpaper_id, theme_id):
    # Note that you can pass a toy's id instead of the whole object
    ResearchPaper.objects.get(id=researchpaper_id).themes.add(theme_id)
    return redirect('researchpaper-detail', researchpaper_id=researchpaper_id)

@login_required
def remove_theme(request, researchpaper_id, theme_id):
    ResearchPaper.objects.get(id=researchpaper_id).themes.remove(theme_id)
    return redirect('researchpaper-detail', researchpaper_id=researchpaper_id)

@login_required
def theme_detail(request, pk):
    theme = Theme.objects.get(pk=pk)
    researchpapers = ResearchPaper.objects.filter(themes=theme)
    return render(request, 'main_app/theme_detail.html', {'researchpapers': researchpapers, 'theme': theme})
