#User is trying to import User model in blog/blog_main/forms.py. 
# Suggest adding the following import statement at the top of the file:
# User module has fields and methods to handle user authentication and management in Django.
from django.contrib.auth.models import User 

# UserCreationForm is a built-in form in Django that provides a way 
# to create new users with username and password fields.
# We created UserCreationForm to extend its functionality by adding an email field.
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username', 'password1', 'password2']
    