import graphene


class Query(graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    pass


schema = graphene.schema(query=Query, mutation=Mutation)
