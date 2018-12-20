from django.shortcuts import render, redirect, get_object_or_404
from mainsite.models import OriginalStory, UserStoryParagraphs
from .forms import AddParagraphForm, UserRegistrationForm
from userprofile.models import AuthorProfile

"""
Story detail view with paragraph form submission
"""


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


# Home view
def home(request):
    home_list = OriginalStory.objects.all()
    author_image = AuthorProfile.objects.all()
    new_paragraphs = UserStoryParagraphs.objects.order_by('-user_paragraph_date')
    return render(request, 'home.html',
                  {'home_list': home_list, 'new_paragraphs': new_paragraphs, 'author_image': author_image})


# Registration form

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration-complete.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


def register_complete(request):
    return render(request, 'registration-complete.html')
