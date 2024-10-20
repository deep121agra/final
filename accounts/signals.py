from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from .models import User,UserProfile
@receiver(post_save, sender=User)
def post_save_create_profile_reciver(sender,instance,created, **kwargs) :
    if created:
        UserProfile.objects.create(user=instance)

    else:
        try:
            profile=UserProfile.objects.get(user=instance)
            profile.save()
        except:
            UserProfile.objects.get(user=instance)
@receiver(pre_save, sender=User)
def pre_save_profile_reciver(sender,instance,**kwargs):
    print(instance.username,'this user is being saved ')  