from django.shortcuts import render, redirect, get_object_or_404
from mainsite.models import OriginalStory, UserStoryParagraphs
from .forms import AddParagraphForm, UserRegistrationForm, StartStoryForm
from django.template.defaultfilters import slugify
from userprofile.models import AuthorProfile
from django.db.models import Count


# Story detail view with paragraph form submission
def story(request, pk, slug):
    story = get_object_or_404(OriginalStory, pk=pk)
    story_user_paragraphs = story.paragraphs.all()
    if request.method == 'POST':
        add_paragraph_form = AddParagraphForm(request.POST)
        if add_paragraph_form.is_valid():
            add_para = add_paragraph_form.save(commit=False)
            add_para.story_belongs_to = story
            add_para.paragraph_author = request.user
            add_para.save()
            return redirect('story', pk=story.pk, slug=story.slug)
    else:
        add_paragraph = AddParagraphForm()

    return render(request, 'story_detail.html',
                  {'story': story, 'story_user_paragraphs': story_user_paragraphs, 'add_paragraph': add_paragraph})


# Start a story form view

def start_a_story(request):
    if request.method == 'POST':
        start_story_form = StartStoryForm(request.POST)
        if start_story_form.is_valid():
            new_story = start_story_form.save(commit=False)
            new_story.slug = slugify(new_story.story_headline)
            new_story.story_paragraph_author = request.user
            new_story.save()
            return redirect('home')
    else:
        start_story_form = StartStoryForm()
    return render(request, 'start-a-story.html', {'start_story_form': start_story_form})


# Home view

def home(request):
    home_list = OriginalStory.objects.all()
    new_paragraphs = UserStoryParagraphs.objects.order_by('-user_paragraph_date')[:6]
    home_stories = OriginalStory.objects.order_by('-story_publish_date')
    return render(request, 'home.html',
                  {'home_list': home_list, 'new_paragraphs': new_paragraphs, 'home_stories': home_stories})


# Registration form

def register(request):

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, request.FILES)

        if user_form.is_valid():
            new_user = user_form.save()
            return render(request, 'registration-complete.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


def register_complete(request):
    return render(request, 'registration-complete.html')


# All paragraphs section view
def all_paragraphs(request):
    all_paragraphs_list = OriginalStory.objects.all()
    author_image = AuthorProfile.objects.all()
    new_paragraphs_all = UserStoryParagraphs.objects.order_by('-user_paragraph_date')
    return render(request, 'all-paragraphs.html',
                  {'all_paragraphs_list': all_paragraphs_list, 'new_paragraphs_all': new_paragraphs_all,
                   'author_image': author_image})
