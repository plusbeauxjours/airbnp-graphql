import graphene
from graphql_jwt.decorators import login_required

from rooms import models as room_models
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


class ToggleFavsMutation(graphene.Mutation):
    class Arguments:
        uuid = graphene.String(required=True)

    Output = types.ToggleFavsResponse

    @login_required
    def mutate(self, info, **kwargs):

        user = info.context.user
        uuid = kwargs.get("uuid")

        try:
            room = room_models.Room.objects.get(uuid=uuid)
            if room in user.favs.all():
                user.favs.remove(room)
            else:
                user.favs.add(room)
            return types.ToggleFavsResponse(ok=True)

        except room_models.Room.DoesNotExist:
            return types.ToggleFavsResponse(ok=False)
