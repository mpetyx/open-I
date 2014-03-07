__author__ = 'mpetyx'

from tastypie.api import Api



api = Api(api_name='v.04')

# Media
from .Media.Audio.Resources import AudioResource
from .Media.Photo.Resources import PhotoResource
from .Media.Video.Resources import VideoResource
from .Media.File.Resources import FileResource
from .Media.Article.Resources import ArticleResource


api.register(AudioResource())
api.register(PhotoResource())
api.register(VideoResource())
api.register(FileResource())
api.register(ArticleResource())

# Location
from .Location.Event.Resources import EventResource
from .Location.Place.Resources import PlaceResource
from .Location.Route.Resources import RouteResource

api.register(EventResource())
api.register(PlaceResource())
api.register(RouteResource())

# Activity
from .Activity.Badge.Resources import BadgeResource
from .Activity.Checkin.Resources import CheckinResource
from .Activity.Event.Resources import ActivityEventResource
from .Activity.Game.Resources import GameResource
from .Activity.Measurement.Resources import MeasurementResource
from .Activity.Note.Resources import NoteResource
from .Activity.Nutrition.Resources import NutritionResource
from .Activity.Question.Resources import QuestionResource
from .Activity.Sleep.Resources import SleepResource
from .Activity.Status.Resources import StatusResource
from .Activity.Workout.Resources import WorkoutResource



api.register(BadgeResource())
api.register(CheckinResource())
api.register(EventResource())
api.register(GameResource())
api.register(MeasurementResource())
api.register(NoteResource())
api.register(NutritionResource())
api.register(QuestionResource())
api.register(SleepResource())
api.register(StatusResource())
api.register(WorkoutResource())


# Product and Services
from .Products_and_Services.Card.Resources import CardResource
from .Products_and_Services.Product.Resources import ProductResource
from .Products_and_Services.Service.Resources import ServiceResource
from .Products_and_Services.Shop.Resources import ShopResource


api.register(CardResource())
api.register(ProductResource())
api.register(ServiceResource())
api.register(ShopResource())


# Profile
from .Profile.Account.Resources import AccountResource
from .Profile.Application.Resources import ApplicationResource
from .Profile.Contact.Resources import ContactResource
from .Profile.Device.Resources import DeviceResource
from .Profile.User.Resources import UserResource


api.register(AccountResource())
api.register(ApplicationResource())
api.register(ContactResource())
api.register(DeviceResource())
api.register(UserResource())

# Builder
from .Builder.Application.Resources import CBSResource

api.register(CBSResource())



urlpatterns = api.urls
