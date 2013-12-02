__author__ = 'mpetyx'


from facepy import GraphAPI
from allauth.socialaccount.models import SocialApp

# For testing purposes go to https://developers.facebook.com/tools/explorer/ and play
class provider:
    """ This class is used to:
        1. Make the connection to the Graph API
        2. Get user's Photos
        3. Get OPENi album Photos
        4. Post Photos to OPENi album
    """
    def __init__(self, access_token, data):
        """ Initiate the graph and find the OPENi album """
        self.graph = GraphAPI(access_token)
        self.find_album_openi = self.graph.fql('SELECT object_id  FROM album WHERE owner=me() AND name="OPENi photos"')
        self.data = data

    def get_photos(self):
        """ Return user's photos """
        result = self.graph.get('me/photos', limit=1)
        return result

    def get_photos_since(self, since="now"):
        """ Return user's photos since.. """
        result = self.graph.get('me/photos', limit=1, since=since)
        return result

    def get_photos_until(self, until="now"):
        """ Return user's photos until.. """
        result = self.graph.get('me/photos', limit=1, until=until)
        return result

    def post_photo(self, path):
        """ Post a photo to OPENi album """
        return self.graph.post(path = 'me/photos', source = open(path, 'rb'))

    def get_album_photos(self):
        """ If there is an OPENi album return its first photo, else return nada """
        if not self.find_album_openi['data']:
            return []
        else:
            result = self.graph.get('/' + self.find_album_openi['data'][0]['object_id'] + '/photos', limit=1)
            return result

    def get_album_photos_before(self, before):
        """ If there is an OPENi album return its first photo before.., else return nada """
        if not self.find_album_openi['data']:
            return []
        else:
            result = self.graph.get('/' + self.find_album_openi['data'][0]['object_id'] + '/photos', limit=1,
                                    before=before)
            return result

    def get_album_photos_after(self, after):
        """ If there is an OPENi album return its first photo after.., else return nada """
        if not self.find_album_openi['data']:
            return []
        else:
            result = self.graph.get('/' + self.find_album_openi['data'][0]['object_id'] + '/photos', limit=1,
                                    after=after)
            return result

    def delete_album_photo(self, id):
        """ Delete an Album Photo by its facebook id. Unfortunately not allowed. """
        # NOT ALLOWED
        #print self.graph.fql('SELECT can_delete FROM photo WHERE object_id='+id)
        #self.graph.fql('DELETE FROM photo WHERE object_id='+id)
        #self.graph.delete()



    # This should be just right!

    # PHOTO API
    def get_photo(self):
        """ Get a photo by its id """
        return self.graph.get(self.data.photo_id)
    
    def get_all_photos_for_account(self):
        """ Get all photos for an account """
        return self.graph.get(self.data.user_id+'/photos')

    def post_photo_to_account(self):
        """ Post a photo to a simple account """
        return self.graph.post(path = self.data.user_id+'/photos', source = open(self.data.path_string, 'rb'))

    def post_photo_to_account(self):
        """ Post a photo to an album """
        return self.graph.post(path = self.data.album_id+'/photos', source = open(self.data.path_string, 'rb'))

    def share_photo(self):
        """ Share a photo """
        return {'result': 'Not applicable'}

    def edit_photo_object(self):
        """ Edit a photo object """
        return {'result': 'Not applicable'}

    def delete_photo_object(self):
        """ Delete a photo object """
        return self.graph.delete(self.data.photo_id)

    
    def get_comments(self):
        """ Get comments for a photo by its id """
        return self.graph.get(self.data.photo_id+'/comments')
    
    def post_comment(self):
        """ Post a comment to a photo by its id """
        return self.graph.post(path = self.data.photo_id+'/comments', data = self.data.comment)
    
    def delete_comment(self):
        """ Delete a comment by its id """
        return self.graph.delete(self.data.comment_id)
    
    def edit_comment(self):
        """ Edit a comment by its id """
        # This would be possible only by deleting the comment and creating a new one.
        return {'result': 'Not applicable'}
    
    def like_photo(self):
        """ Like a photo by its id """
        return self.graph.post(self.data.photo_id + '/likes')
    
    def get_likes_for_photo(self):
        """ Get like for a photo by its id """
        return self.graph.get(self.data.photo_id + '/likes')
    
    def unlike_photo(self):
        """ Unlike a photo by its id """
        return self.graph.delete(self.data.photo_id + '/likes')
    
    def dislike_photo(self):
        """ Dislike a photo by its id """
        return {'result': 'Not applicable'}
    
    def get_dislikes_for_article(self):
        """ Get dislikes for an article """
        return {'result': 'Not applicable'}
    
    def delete_photo_from_article(self):
        """ Delete a photo from an article """
        return {'result': 'Not applicable'}