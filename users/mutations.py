import graphene

from . import models, types


class CreateAccountMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    Output = types.CreateAccountResponse

    def mutate(self, info, **kwargs):

        first_name = kwargs.get("first_name", None)
        last_name = kwargs.get("last_name", None)
        email = kwargs.get("email")
        password = kwargs.get("password")

        try:
            models.User.objects.get(email=email)
            return types.CreateAccountResponse(ok=False, error="User already exists.")
        except models.User.DoesNotExist:
            try:
                models.User.objects.create_user(email, email, password)
                return types.CreateAccountResponse(ok=True)
            except Exception:
                return types.CreateAccountResponse(ok=False, error="Can't create user.")
