__author__ = 'mpetyx'

from tastypie.api import Api

from .Audio.Resources import AudioResource
from .Photo.Resources import PhotoResource
from .Video.Resources import VideoResource


api = Api(api_name='')
api.register(AudioResource())
api.register(PhotoResource())
api.register(VideoResource())

urlpatterns = api.urls
