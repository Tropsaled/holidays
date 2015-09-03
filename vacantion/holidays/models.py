from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Worker(models.Model):
    user = models.OneToOneField(User)
    supervisors = models.ManyToManyField(User, related_name='worker_supervisors')
    days_left = models.IntegerField()

    def __unicode__(self):
        return u"{} {}".format(self.user.first_name, self.user.last_name)

class Vacantion(models.Model):
    worker = models.ForeignKey(Worker)
    days = models.IntegerField()
    start = models.DateField()
    end = models.DateField()

    def __unicode__(self):
        return u"{} {}: {} - {}".format(self.worker.user.first_name, self.worker.user.last_name, self.start, self.end)


    def save(self, *args, **kwargs):
        self.worker.days_left -= self.days
        self.worker.save()
        super(Vacantion, self).save(*args, **kwargs)