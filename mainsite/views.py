from django.shortcuts import render, redirect, get_object_or_404
from mainsite.models import OriginalStory, UserStoryParagraphs
from .forms import AddParagraphForm, UserRegistrationForm, StartStoryForm, EditProfileForm
from django.template.defaultfilters import slugify
from userprofile.models import AuthorProfile
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
# Home view

def home(request):
    new_paragraphs = UserStoryParagraphs.objects.order_by('-user_paragraph_date')
    home_stories = OriginalStory.objects.order_by('-story_publish_date')
    return render(request, 'home.html',
                  {'new_paragraphs': new_paragraphs, 'home_stories': home_stories})


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


# Watchers button

class WatcherCountRedirect(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        pk = self.kwargs.get("pk")
        print(pk)
        print(slug)
        obj = get_object_or_404(OriginalStory, pk=pk, slug=slug)
        url_ = obj.get_absolute_url()
        return url_

# Start a story form view

def start_a_story(request):
    if request.method == 'POST':
        start_story_form = StartStoryForm(request.POST)
        if start_story_form.is_valid():
            new_story = start_story_form.save(commit=False)
            new_story.slug = slugify(new_story.story_headline)
            new_story.story_paragraph_author = request.user
            new_story.save()
            start_story_form.save_m2m()
            return redirect('home')
    else:
        start_story_form = StartStoryForm()
    return render(request, 'start-a-story.html', {'start_story_form': start_story_form})


# All paragraphs section view
def all_paragraphs(request):
    all_paragraphs_list = OriginalStory.objects.all()
    author_image = AuthorProfile.objects.all()
    new_paragraphs_all = UserStoryParagraphs.objects.order_by('-user_paragraph_date')
    return render(request, 'all-paragraphs.html',
                  {'all_paragraphs_list': all_paragraphs_list, 'new_paragraphs_all': new_paragraphs_all,
                   'author_image': author_image})


# Registration form

def register(request):

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, request.FILES)

        if user_form.is_valid():
            new_user = user_form.save()
            return render(request, 'registration-complete.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


def register_complete(request):
    return render(request, 'registration/registration-complete.html')


# Edit profile form

@login_required
def edit_profile(request):
    if request.method == 'POST':
        edit_profile_form = EditProfileForm(instance=request.user, data=request.POST)
        if edit_profile_form.is_valid():
            edit_profile_form.save()
    else:
        edit_profile_form = EditProfileForm(instance=request.user)

    return render(request, 'registration/edit.html', {'edit_profile_form': edit_profile_form})


# Like a story
@login_required
def like_story(request):
    story_id = None
    if request.method == 'GET':
        story_id = request.GET['story_id']

    likes = 0
    if story_id:
        story = OriginalStory.objects.get(id=int(story_id))
        if story:
            likes = story.likes + 1
            story.likes =  likes
            story.save()

    return HttpResponse(likes)