from django.db import models


class Todo(models.Model):
  title = models.CharField(max_length=150)
  description = models.TextField(null=True, blank=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey('auth.User')

  def __unicode__(self):
    return '%s has to do %s' % (self.author, self.title)
