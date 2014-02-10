__author__ = 'mpetyx'

from tastypie.api import Api

from .Media.Audio.Resources import AudioResource
from .Media.Photo.Resources import PhotoResource
from .Media.Video.Resources import VideoResource


from .Location.Event.Resources import EventResource


api = Api(api_name='v.01')

# Media
api.register(AudioResource())
api.register(PhotoResource())
api.register(VideoResource())

# Location
api.register(EventResource())


urlpatterns = api.urls
