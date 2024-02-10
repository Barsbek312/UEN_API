from django.db import models
from user.models import User, Organization

class Event(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    place = models.CharField(max_length=300)
    capacity = models.IntegerField(default=0)
    description = models.TextField()
    status = models.CharField(max_length=300)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="organization_name")
    
    def __str__(self) -> str:
        return self.name
    

class EventVideo(models.Model):
    video = models.FileField(upload_to='event_videos/')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_video')
    

class EventImages(models.Model):
    image = models.ImageField(upload_to='event_images/')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_image')
    

class EventFile(models.Model):
    file = models.FileField(upload_to='event_files/')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_file')
    

STATUSES = [
    ("CS", "Consideration"),
    ("RJ", "Rejected"),
    ("AC", "Accepted"),
]


class EventInvitations(models.Model):
    status = models.CharField(max_length=3, choices=STATUSES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_invitation')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_invitation')