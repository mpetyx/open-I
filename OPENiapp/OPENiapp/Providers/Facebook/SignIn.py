__author__ = 'mpetyx'

from django.utils.cache import patch_response_headers
from django.shortcuts import render

import requests

from allauth.socialaccount.models import SocialAccount, SocialLogin, SocialToken
from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.helpers import render_authentication_error
from allauth.socialaccount.adapter import get_adapter
from allauth.socialaccount import providers
from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter,
                                                          OAuth2LoginView,
                                                          OAuth2CallbackView)

from allauth.socialaccount.providers.facebook.provider import FacebookProvider


def fb_complete_login(app, token):
    resp = requests.get('https://graph.facebook.com/me',
                        params={'access_token': token.token})
    extra_data = resp.json()
    uid = extra_data['id']
    user = get_adapter() \
        .populate_new_user(email=extra_data.get('email'),
                           username=extra_data.get('username'),
                           first_name=extra_data.get('first_name'),
                           last_name=extra_data.get('last_name'))
    account = SocialAccount(uid=uid,
                            provider=FacebookProvider.id,
                            extra_data=extra_data,
                            user=user)
    return SocialLogin(account)


def fb_complete_login2(app, token):
    resp = requests.get('https://graph.facebook.com/me',
                        params={'access_token': token})
    extra_data = resp.json()
    uid = extra_data['id']
    user = get_adapter() \
        .populate_new_user(email=extra_data.get('email'),
                           username=extra_data.get('username'),
                           first_name=extra_data.get('first_name'),
                           last_name=extra_data.get('last_name'))
    account = SocialAccount(uid=uid,
                            provider=FacebookProvider.id,
                            extra_data=extra_data,
                            user=user)
    return SocialLogin(account)


class FacebookOAuth2Adapter(OAuth2Adapter):
    provider_id = FacebookProvider.id

    authorize_url = 'https://www.facebook.com/dialog/oauth'
    access_token_url = 'https://graph.facebook.com/oauth/access_token'
    expires_in_key = 'expires'

    def complete_login(self, request, app, access_token, **kwargs):
        return fb_complete_login(app, access_token)


oauth2_login = OAuth2LoginView.adapter_view(FacebookOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(FacebookOAuth2Adapter)


def channel(request):
    provider = providers.registry.by_id(FacebookProvider.id)
    locale = provider.get_locale_for_request(request)
    response = render(request, 'facebook/channel.html',
                      {'facebook_jssdk_locale': locale})
    cache_expire = 60 * 60 * 24 * 365
    patch_response_headers(response, cache_expire)
    response['Pragma'] = 'Public'
    return response


def login_by_token(request, access_token):
    ret = None
    if request.method == 'POST':
        try:
            app = providers.registry.by_id(FacebookProvider.id) \
                .get_app(request)
            access_token = access_token
            token = SocialToken(app=app,
                                token=access_token)
            login = fb_complete_login(app, token)
            login.token = token
            login.state = SocialLogin.state_from_request(request)
            ret = complete_social_login(request, login)
        except:
            # FIXME: Catch only what is needed
            pass
    if not ret:
        ret = render_authentication_error(request)
    return ret


# from openiHeroku.providers.facebook.SignIn import fb_complete_login2
#
# sample_token = 'BAACOmM5Td2ABAFCCrp1s8HlVWSjCwrUagZBHsoY70ptSBflfYJvJlwQWLpJiFFR42FHig797rI7YTjvRwadrclTecbp7gwNkDEJ8QZAJ6y0u7ZBHwxMkZBlN7ZBtb480ZD'
#
# user2 = fb_complete_login2(None, sample_token)

from django.test import RequestFactory

request_factory = RequestFactory()
request = request_factory.get('/path', data={'name': u'test'},
                              session={"access_token": '1234',
                                       "access_token_secret": '1234'})