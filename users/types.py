import graphene
from graphene_django import DjangoObjectType
from .models import User
from rooms.types import RoomType


class UserType(DjangoObjectType):
    class Meta:
        model = User
