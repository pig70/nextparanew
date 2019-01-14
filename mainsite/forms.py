from django import forms
from .models import UserStoryParagraphs,OriginalStory
from userprofile.models import AuthorProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Add a paragraph form on a story
class AddParagraphForm(forms.ModelForm):
    user_paragraph = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'user-paragraph-field'}))

    class Meta:
        model = UserStoryParagraphs
        fields = ('user_paragraph',)

# Start a story form
class StartStoryForm(forms.ModelForm):
    story_headline = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'class': 'form-field'}))
    story_first_paragraph = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-field'}))


    class Meta:
        model = OriginalStory
        exclude = ('story_publish_date', 'slug', 'story_paragraph_author')


# Registration form

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-field'}))
    password2 = forms.CharField(label='Confirm password',
                                       widget=forms.PasswordInput(attrs={'class': 'form-field'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-field'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-field'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-field'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-field'}))
    author_image = forms.ImageField(label="Profile image")

    class Meta(UserCreationForm.Meta):
        model = AuthorProfile
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'author_image')

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match')
        return cd['password2']