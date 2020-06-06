import graphene
from graphene_django import DjangoObjectType
from . import models


class RoomType(DjangoObjectType):

    class Meta:
        model = models.Room


class GetRoomListResponse(graphene.ObjectType):
    rooms = graphene.List(RoomType)
    total = graphene.Int()


class GetRoomDetailResponse(graphene.ObjectType):
    room = graphene.Field(RoomType)
