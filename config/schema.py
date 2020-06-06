import graphene
from users import schema as user_schema
from rooms import schema as room_schema


class Query(user_schema.Query, room_schema.Query, graphene.ObjectType):
    pass


class Mutation(user_schema.Mutation, room_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
