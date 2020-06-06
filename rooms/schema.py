import graphene
from . import types, queries, mutations


class Query(object):

    get_room_list = graphene.Field(
        types.GetRoomListResponse,
        resolver=queries.resolve_get_room_list,
        required=True,
    )
    get_room_detail = graphene.Field(
        types.GetRoomDetailResponse,
        resolver=queries.resolve_get_room_detail,
        required=True,
        args={"uuid": graphene.String(required=True)},
    )


class Mutation(object):
    
    pass
