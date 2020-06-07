import graphene
from graphql_jwt.decorators import login_required

from . import models, types


class CreateRoomMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        address = graphene.String(required=True)
        price = graphene.Int(required=True)
        beds = graphene.Int()
        lat = graphene.Float(required=True)
        lng = graphene.Float(required=True)
        bedrooms = graphene.Int()
        bathrooms = graphene.Int()
        check_in = graphene.Time()
        check_out = graphene.Time()
        instant_book = graphene.Boolean()

    Output = types.CreateRoomResponse

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        name = kwargs.get("name")
        address = kwargs.get("address")
        price = kwargs.get("price")
        beds = kwargs.get("beds", "1")
        lat = kwargs.get("lat")
        lng = kwargs.get("lng")
        bedrooms = kwargs.get("bedrooms", 1)
        bathrooms = kwargs.get("bathrooms", 1)
        check_in = kwargs.get("check_in", "16:00:00")
        check_out = kwargs.get("check_out", "11:00:00")
        instant_book = kwargs.get("instant_book", False)

        try:
            room = models.Room.objects.create(
                user=user,
                name=name,
                address=address,
                price=price,
                beds=beds,
                lat=lat,
                lng=lng,
                bedrooms=bedrooms,
                bathrooms=bathrooms,
                check_in=check_in,
                check_out=check_out,
                instant_book=instant_book,
            )
            return types.CreateRoomResponse(room=room)

        except Exception:
            return types.CreateRoomResponse(room=None)


class EditRoomMutation(graphene.Mutation):
    class Arguments:
        uuid = graphene.String(required=True)
        name = graphene.String()
        address = graphene.String()
        price = graphene.Int()
        beds = graphene.Int()
        lat = graphene.Float()
        lng = graphene.Float()
        bedrooms = graphene.Int()
        bathrooms = graphene.Int()
        check_in = graphene.Time()
        check_out = graphene.Time()
        instant_book = graphene.Boolean()

    Output = types.EditRoomResponse

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        uuid = kwargs.get("uuid")
        name = kwargs.get("name", None)
        address = kwargs.get("address", None)
        price = kwargs.get("price", None)
        beds = kwargs.get("beds", None)
        lat = kwargs.get("lat", None)
        lng = kwargs.get("lng", None)
        bedrooms = kwargs.get("bedrooms", None)
        bathrooms = kwargs.get("bathrooms", None)
        check_in = kwargs.get("check_in", None)
        check_out = kwargs.get("check_out", None)
        instant_book = kwargs.get("instant_book", None)

        try:
            room = models.Room.objects.get(uuid=uuid)

            if check_in == check_out:
                return types.EditRoomResponse(
                    room=None, error="Not enough time between changes"
                )

            else:
                if name:
                    room.name = name
                if address:
                    room.address = address
                if price:
                    room.price = price
                if beds:
                    room.beds = beds
                if lat:
                    room.lat = lat
                if lng:
                    room.lng = lng
                if bedrooms:
                    room.bedrooms = bedrooms
                if bathrooms:
                    room.bathrooms = bathrooms
                if check_in:
                    room.check_in = check_in
                if check_out:
                    room.check_out = check_out
                if instant_book:
                    room.instant_book = instant_book

                room.save()
                return types.EditRoomResponse(room=room, error=None)

        except models.Room.DoesNotExist:
            return types.EditRoomResponse(room=None, error=None)
