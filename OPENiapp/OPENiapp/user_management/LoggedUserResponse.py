__author__ = 'mpetyx'

from OPENiapp.OPENiapp.models import Person


def profileJson(person, secret, function=""):
    """

    @param person:
    @param initial:
    @return:

    >>> from OPENiapp.api.v2.Person.Profile import *
    >>> profileJson(2,3)

    """

    response = {}

    if type(person) == int:
        person = Person.objects.get(id=person)

    response["id"] = person.id
    response["name"] = person.user.first_name
    response["surname"] = person.user.last_name
    response["username"] = person.user.username

    response["authentication"] = {}
    response["authentication"]["secret"] = secret
    # response["is_available"] = False # Needs to be changed

    # if Friendship.objects.filter(from_friend=initial,to_friend=person).exists():
    #     response["is_followed"] = True
    # else:
    #     response["is_followed"] = False

    return response