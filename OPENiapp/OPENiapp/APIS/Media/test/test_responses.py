from tastypie.test import TestApiClient

import datetime
from django.contrib.auth.models import User
from tastypie.test import ResourceTestCase
from ..Photo.models import OpeniPhoto

class PhotoResourceTest(ResourceTestCase):
    def setUp(self):
        super(PhotoResourceTest, self).setUp()

        # Create a user.
        self.username = 'daniel'
        self.password = 'pass'
        self.user = User.objects.create_user(self.username, 'daniel@example.com', self.password)

        # Fetch the ``OPENiPhoto`` object we'll use in testing.
        # Note that we aren't using PKs because they can change depending
        # on what other tests are running.
        photo = OpeniPhoto(1, 1, "1", "1", "1", "1", "2", "2", "3", "4")
        photo.save()
        self.entry_1 = OpeniPhoto.objects.get(id=1)

        self.maxDiff = None

        # We also build a detail URI, since we will be using it all over.
        # DRY, baby. DRY.
        self.detail_url = '/media/photo/{0}/'.format(self.entry_1.pk)

    def get_credentials(self):
        return self.create_basic(username=self.username, password=self.password)

    def test_get_list_unauthorzied(self):
        self.assertHttpUnauthorized(self.api_client.get('/media/photo/', format='json'))

    def test_get_list_json(self):
        resp = self.api_client.get('/media/photo/', format='json', authentication=self.get_credentials())
        self.assertValidJSONResponse(resp)

        # Scope out the data for correctness.
        self.assertEqual(len(self.deserialize(resp)['objects']), 1)
        # Here, we're checking an entire structure for the expected data.
        self.assertEqual(self.deserialize(resp)['objects'][0], {
            u'From': self.entry_1.From,
            u'facebook': {u'app1': {u'test': True}, u'app2': {u'test': True}},
            u'height': self.entry_1.height,
            u'id': self.user.pk,
            u'koukli': {'lol': 1},
            u'location': self.entry_1.location,
            u'object_type': self.entry_1.object_type,
            u'profile': self.entry_1.profile,
            u'resource_uri': "/media/photo/1/",
            u'service': self.entry_1.service,
            u'tags': self.entry_1.tags,
            u'time': self.entry_1.time,
            u'twitter': {u'app1': {u'test': True}, u'app2': {u'test': True}},
            u'url': self.entry_1.url,
            u'width': self.entry_1.width,
        })


#class EntryResourceTest(ResourceTestCase):
#    # Use ``fixtures`` & ``urls`` as normal. See Django's ``TestCase``
#    # documentation for the gory details.
#    fixtures = ['test_entries.json']

#    def setUp(self):
#        super(EntryResourceTest, self).setUp()

#        # Create a user.
#        self.username = 'daniel'
#        self.password = 'pass'
#        self.user = User.objects.create_user(self.username, 'daniel@example.com', self.password)

#        # Fetch the ``Entry`` object we'll use in testing.
#        # Note that we aren't using PKs because they can change depending
#        # on what other tests are running.
#        photo = OpeniPhoto(1, 1, "1", "1", "1", "1", "2", "2", "3", "4")
#        photo.save()
#        self.entry_1 = OpeniPhoto.objects.get(url="1")

#        self.maxDiff = None

#        # We also build a detail URI, since we will be using it all over.
#        # DRY, baby. DRY.
#        self.detail_url = '/media/photo/{0}/'.format(self.entry_1.pk)

#        # The data we'll send on POST requests. Again, because we'll use it
#        # frequently (enough).
#        self.post_data = {
#            url = models.TextField()
#            object_type = models.TextField()
#            service = models.TextField()
#            From = models.TextField()
#            profile = models.TextField()
#            location = models.TextField()
#            time = models.TextField()
#            tags = models.TextField()
#            width = models.TextField()
#            height = models.TextField()
#            'user': '/media/photo/{0}/'.format(self.user.pk),
#            'title': 'Second Post!',
#            'slug': 'second-post',
#            'created': '2012-05-01T22:05:12'
#        }

#    def get_credentials(self):
#        return self.create_basic(username=self.username, password=self.password)

#    def test_get_list_unauthorized(self):
#        self.assertHttpUnauthorized(self.api_client.get('/api/v1/entries/', format='json'))

#    def test_get_list_json(self):
#        resp = self.api_client.get('/media/photo/', format='json', authentication=self.get_credentials())
#        self.assertValidJSONResponse(resp)

#        # Scope out the data for correctness.
#        self.assertEqual(len(self.deserialize(resp)['objects']), 1)
#        # Here, we're checking an entire structure for the expected data.
#        self.assertEqual(self.deserialize(resp)['objects'][0], {
#            u'From': self.entry_1.From,
#            u'facebook': {u'app1': {u'test': True}, u'app2': {u'test': True}},
#            u'height': self.entry_1.height,
#            u'id': self.user.pk,
#            u'koukli': {'lol': 1},
#            u'location': self.entry_1.location,
#            u'object_type': self.entry_1.object_type,
#            u'profile': self.entry_1.profile,
#            u'resource_uri': "/media/photo/1/",
#            u'service': self.entry_1.service,
#            u'tags': self.entry_1.tags,
#            u'time': self.entry_1.time,
#            u'twitter': {u'app1': {u'test': True}, u'app2': {u'test': True}},
#            u'url': self.entry_1.url,
#            u'width': self.entry_1.width,
#        })

#    def test_get_list_xml(self):
#        self.assertValidXMLResponse(self.api_client.get('/api/v1/entries/', format='xml', authentication=self.get_credentials()))

#    def test_get_detail_unauthenticated(self):
#        self.assertHttpUnauthorized(self.api_client.get(self.detail_url, format='json'))

#    def test_get_detail_json(self):
#        resp = self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials())
#        self.assertValidJSONResponse(resp)

#        # We use ``assertKeys`` here to just verify the keys, not all the data.
#        self.assertKeys(self.deserialize(resp), ['created', 'slug', 'title', 'user'])
#        self.assertEqual(self.deserialize(resp)['name'], 'First post')

#    def test_get_detail_xml(self):
#        self.assertValidXMLResponse(self.api_client.get(self.detail_url, format='xml', authentication=self.get_credentials()))

#    def test_post_list_unauthenticated(self):
#        self.assertHttpUnauthorized(self.api_client.post('/api/v1/entries/', format='json', data=self.post_data))

#    def test_post_list(self):
#        # Check how many are there first.
#        self.assertEqual(Entry.objects.count(), 5)
#        self.assertHttpCreated(self.api_client.post('/api/v1/entries/', format='json', data=self.post_data, authentication=self.get_credentials()))
#        # Verify a new one has been added.
#        self.assertEqual(Entry.objects.count(), 6)

#    def test_put_detail_unauthenticated(self):
#        self.assertHttpUnauthorized(self.api_client.put(self.detail_url, format='json', data={}))

#    def test_put_detail(self):
#        # Grab the current data & modify it slightly.
#        original_data = self.deserialize(self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials()))
#        new_data = original_data.copy()
#        new_data['title'] = 'Updated: First Post'
#        new_data['created'] = '2012-05-01T20:06:12'

#        self.assertEqual(Entry.objects.count(), 5)
#        self.assertHttpAccepted(self.api_client.put(self.detail_url, format='json', data=new_data, authentication=self.get_credentials()))
#        # Make sure the count hasn't changed & we did an update.
#        self.assertEqual(Entry.objects.count(), 5)
#        # Check for updated data.
#        self.assertEqual(Entry.objects.get(pk=25).title, 'Updated: First Post')
#        self.assertEqual(Entry.objects.get(pk=25).slug, 'first-post')
#        self.assertEqual(Entry.objects.get(pk=25).created, datetime.datetime(2012, 3, 1, 13, 6, 12))

#    def test_delete_detail_unauthenticated(self):
#        self.assertHttpUnauthorized(self.api_client.delete(self.detail_url, format='json'))

#    def test_delete_detail(self):
#        self.assertEqual(Entry.objects.count(), 5)
#        self.assertHttpAccepted(self.api_client.delete(self.detail_url, format='json', authentication=self.get_credentials()))
#        self.assertEqual(Entry.objects.count(), 4)