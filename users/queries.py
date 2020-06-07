from . import models, types
from graphql_jwt.decorators import login_required


def resolve_get_user(self, info, **kwargs):
    uuid = kwargs.get("uuid")
    user = models.User.objects.get(uuid=uuid)
    return types.GetUserResponse(user=user)


@login_required
def resolve_me(self, info):
    user = info.context.user
    return types.MeResponse(user=user)
