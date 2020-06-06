import graphene
from . import types


class EditProfile(graphene.Mutation):

    Output = types.GetRoomListResponse

    def mutate(self, info, **kwargs):
        pass