from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from goodcreator import models
from goodcreator.rest.serializers import CategorySerializer, EntrySerializer, UserSerializer, GroupSerializer



class ArchiveViewSetMixin:
  def perform_destroy(self, instance):
        instance.archive = True
        instance.save()

class UserViewSet(viewsets.ModelViewSet, ArchiveViewSetMixin):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet, ArchiveViewSetMixin):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class EntryViewSet(ArchiveViewSetMixin,viewsets.ModelViewSet):
    queryset = models.Entry.objects.filter(archive=False).all()
    serializer_class = EntrySerializer

class CategoryViewSet(ArchiveViewSetMixin, viewsets.ModelViewSet):
    queryset = models.Category.objects.filter(archive=False).all()
    serializer_class = CategorySerializer
