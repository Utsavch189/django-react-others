from .models import SignalTest
from django.db.models.signals import pre_save,post_save

from django.dispatch import receiver

"""
wake before save data
"""
@receiver(pre_save,sender=SignalTest)
def pre_signals(sender,instance,**kwargs):
    print('pre_save>>>>>>')
    if sender.objects.filter(email=instance.email).exists():
        print("sender(before value in db) : ",sender.objects.get(email=instance.email).name)
        print("instance(after value in db) : ",instance.name)

"""
wake after save data
"""
@receiver(post_save,sender=SignalTest)
def post_signals(sender,instance,**kwargs):
    print('post_save>>>>>>')
    print("after save : ",sender.objects.get(email=instance.email).name)

