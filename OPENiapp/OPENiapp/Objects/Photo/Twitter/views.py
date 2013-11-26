__author__ = 'romdim'

from twitter import TWprovider as TWprovider


def make_tw_connection(request, app):
    """ Use Twython to make an API call """
    return TWprovider(
        app, request.user)