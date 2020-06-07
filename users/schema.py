import graphene
import graphql_jwt
from . import types, queries, mutations


class Query(object):

    get_user = graphene.Field(
        types.GetUserResponse,
        resolver=queries.resolve_get_user,
        required=True,
        args={"uuid": graphene.String(required=True)},
    )


class Mutation(object):

    create_account = mutations.CreateAccountMutation.Field(required=True)
    log_in = graphql_jwt.ObtainJSONWebToken.Field(required=True)
