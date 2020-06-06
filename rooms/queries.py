from . import models
from . import types


def resolve_get_room_list(self, info, page=1):
    if page < 1:
        page = 1
    page_size = 5
    skipping = page_size * (page - 1)
    taking = page_size * page
    rooms = models.Room.objects.all()[skipping:taking]
    total = models.Room.objects.count()
    return types.GetRoomListResponse(rooms=rooms, total=total)


def resolve_get_room_detail(self, info, **kwargs):
    uuid = kwargs.get("uuid")
    room = models.Room.objects.get(uuid=uuid)
    return types.GetRoomDetailResponse(room=room)
