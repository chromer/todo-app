from rest_framework import viewsets

from models import Todo
from serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer

  def pre_save(self, obj):
    obj.author = self.request.user

  def get_queryset(self):
    if self.request.user.is_authenticated():
      return Todo.objects.filter(author=self.request.user)
    return Todo.objects.none()
