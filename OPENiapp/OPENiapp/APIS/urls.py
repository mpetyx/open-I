__author__ = 'mpetyx'

from tastypie.api import Api



api = Api(api_name='v.01')

# Media
from .Media.Audio.Resources import AudioResource
from .Media.Photo.Resources import PhotoResource
from .Media.Video.Resources import VideoResource

api.register(AudioResource())
api.register(PhotoResource())
api.register(VideoResource())

# Location
from .Location.Event.Resources import EventResource
from .Location.Place.Resources import PlaceResource
from .Location.Route.Resources import RouteResource

api.register(EventResource())
api.register(PlaceResource())
api.register(RouteResource())



urlpatterns = api.urls
