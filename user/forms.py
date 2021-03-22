from django import forms 
from django.contrib.auth.models import User   
from django.contrib.auth.forms import UserCreationForm
class tourist_DB(UserCreationForm):
    
    email = forms.EmailField()
    
    class Meta:
        model = User  
        fields = ['username', 'email', 'password', 'password2' ] 

# {% extends 'app1/base.html' %}
# {% load crispy_forms_tags %}
# {% load static %}
# {% block content%}

# <link rel="stylesheet" href="{% static 'app1/register.css' %}">
# <div class="regist">
#     <div class="cotntent-section">
#         <form method="POST">
#             {% csrf_token %} 
#             <fieldset class = "form-group">
#                 <legend class="border-bottom mb-4">Join Today</legend>
#                 {{ form| crispy }}
#             </fieldset>
#             <div class="form-group">
#                 <button class="btn btn-outline-info" type="submit">Sign Up</button>
#             </div>
#         </form>
#         <div class="border-top pt3">
#             <small class = "text-muted">
#                 Already Have An Account <a href= "#" class="ml-2">Sign In</a>
#             </small>
#         </div>
#     </div>
# </div>
    
# {% endblock content %}