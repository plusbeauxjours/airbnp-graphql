from . import models, types


def resolve_get_user(self, info, **kwargs):
    uuid = kwargs.get("uuid")
    user = models.User.objects.get(uuid=uuid)
    return types.GetUserResponse(user=user)
