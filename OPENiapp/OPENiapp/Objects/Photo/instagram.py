__author__ = 'mpetyx'


class connector:

    def Get_comments(self):

        """

        GET API_PATH/[PHOTO_ID]/comments
        GET graph.facebook.com/[PHOTO_ID]/comments
        """

    def Post_comment(self):

        """POST API_PATH/[PHOTO_ID]/comments
    POST graph.facebook.com/[PHOTO_ID]/comments
    """


    def Delete_comment (self):

        """
    DELETE API_PATH/[COMMENT_ID]
    DELETE graph.facebook.com/[COMMENT_ID]
    """


    def Edit_comment(self):
        """PUT API_PATH/[COMMENT_ID]
POST graph.facebook.com/[COMMENT_ID]
"""


    def Like_Photo(self):

        """POST API_PATH/[PHOTO_ID]/likes
POST graph.facebook.com/[PHOTO_ID]/likes
POST api.tumblr.com/v2/user/like
"""


    def Get_Likes_for_a_photo(self):
        """GET API_PATH/[PHOTO_ID]/likes
GET graph.facebook.com/[PHOTO_ID]/likes
GET api.tumblr.com/v2/blog/{base-hostname}/likes
"""

    """return Unimplemented()"""

# Unlike Photo	DELETE API_PATH/[PHOTO_ID]/likes
# DELETE graph.facebook.com/[PHOTO_ID]/likes
# -
# Dislike Photo	POST API_PATH/[PHOTO_ID]/dislikes	-	-
# Get Dislikes for an Article	GET API_PATH/[PHOTO_ID]/dislikes	-	-
# Delete Photo from Article