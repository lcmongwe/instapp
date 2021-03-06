from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from django.forms import ModelForm
from .models import Profile,Image,Comment






# create upload from
class UploadImageForm(ModelForm):
    class Meta:
        model= Image
        # fields= "__all__"
        fields=('image', 'img_name', 'imge_caption',   )

        labels={
            'img_name':'name',
            'imge_caption':'caption',     
        }

        widgets={
           'img_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'  name '}),
           
           'imge_caption':forms.TextInput(attrs={'class': 'form-control','placeholder':'caption'}),

        }



# create a profile form
class ProfileForm(ModelForm):
    class Meta:
        model= Profile
        # fields= "__all_"
        fields=('name', 'username', 'profile_photo',  'bio',  )

        labels={
            'name':'name',
            'username':'username',
            'profile_photo':'photo',
            'bio':'bio',
        }

        widgets={
           'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'name '}),
           'username':forms.TextInput(attrs={'class': 'form-control','placeholder':' username'}),
           
           'bio':forms.Textarea(attrs={'class': 'form-control','placeholder':'bio'}),
          
        }



# create a comment form
class CommentForm(ModelForm):
    class Meta:
        model= Comment
        # fields= "__all__"
        fields=('comment',   )

        labels={
            'comment':'',

        }

        widgets={
           'comment': forms.TextInput(attrs={'placeholder':' post a comment '}),
        }









# authentication forms
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email','password1','password2')

    def __init__(self, *args,**kwargs):
        super(RegisterUserForm, self).__init__(*args,**kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
