import graphene
from graphene_django import DjangoObjectType
from . import models


class UserType(DjangoObjectType):
    class Meta:
        model = models.User
        exclude = ("password", "is_superuser", "last_login")


class GetUserResponse(graphene.ObjectType):
    user = graphene.Field(UserType)


class CreateAccountResponse(graphene.ObjectType):
    ok = graphene.Boolean()
    error = graphene.String()


class MeResponse(graphene.ObjectType):
    user = graphene.Field(UserType)


class ToggleFavsResponse(graphene.ObjectType):
    ok = graphene.Boolean()


class EditProfileResponse(graphene.ObjectType):
    user = graphene.Field(UserType)
