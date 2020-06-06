import graphene
from graphene_django import DjangoObjectType
from .models import Room
from users.types import UserType


class RoomType(DjangoObjectType):
    class Meta:
        model = Room

