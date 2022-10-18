 # A signal that is sent when an object is saved.post_save
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile

    # """
    # "If a user is created, create a profile for that user."
    
    # # HTML
    # {% if user.is_authenticated %}
    #     &lt;a href="{% url 'profile' %}"&gt;Profile&lt;/a&gt;
    # {% else %}
    #     &lt;a href="{% url 'login' %}"&gt;Login&lt;/a&gt;
    # {% endif %}
    
    # sender: The model class
    # instance: The instance being saved
    # created: A boolean; True if a new record was created
    # """
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(person_of=instance)
        print("profile created")
post_save.connect(create_profile,sender=User)