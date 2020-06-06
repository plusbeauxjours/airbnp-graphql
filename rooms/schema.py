import graphene
from users import schema as user_schema
from rooms import schema as room_schema


class Query(user_schema.Query, room_schema.Query):
    pass


class Mutation(user_schema.Mutation, room_schema.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
