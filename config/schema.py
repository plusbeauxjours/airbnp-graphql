import graphene
import graphql_jwt

from users import schema as user_schema
from rooms import schema as room_schema


class Query(user_schema.Query, room_schema.Query, graphene.ObjectType):
    pass


class Mutation(user_schema.Mutation, room_schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
