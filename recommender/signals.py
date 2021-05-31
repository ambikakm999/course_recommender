from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Student


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(username=instance)
        print('Profile created!')


post_save.connect(create_profile, sender=User)

#@receiver(post_save, sender=User)
#def update_profile(sender, instance, created, **kwargs):
    #if created == False:
        #instance.profile.save()
        #print('Profile updated!')

# post_save.connect(update_profile, sender=User)