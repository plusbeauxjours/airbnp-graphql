import graphene
from graphene_django.types import DjangoObjectType


class ResponseField(graphene.AbstracType):
    ok = graphene.Boolean(required=True)
    error = graphene.String()
