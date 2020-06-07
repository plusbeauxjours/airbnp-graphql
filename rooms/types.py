import graphene
from graphql_jwt.decorators import login_required
from graphene_django import DjangoObjectType
from . import models


class RoomType(DjangoObjectType):

    is_fav = graphene.Boolean()

    class Meta:
        model = models.Room

    @login_required
    def resolve_is_fav(self, info):
        user = info.context.user
        return self in user.favs.all()


class GetRoomListResponse(graphene.ObjectType):
    rooms = graphene.List(RoomType)
    total = graphene.Int()


class GetRoomDetailResponse(graphene.ObjectType):
    room = graphene.Field(RoomType)
