__author__ = 'mpetyx'


class OpeniPhoto:
    def __init__(self):
        """
        id	id	GET	id
url	-		post_url
object_type	-		type
service	-		-
from:id	from:id		blog:name
from:username	from:name		blog_name
from:url	-		blog:url
profile:title	name		title
profile:icon	icon		-
profile:format	-		format
time:created_time	created_time		date
location	-		timestamp
time:edited_time	updated_time		-
tags	name_tags		tags
width	width		-
height
        """

        self.id = None
        self.url = None
        self.object_type = None
        self.service = None
        self.from_ = None
        self.profile = None
        self.location = None
        self.time = None
        self.tags = None
        self.width = None
        self.height = None
        return 1

    def get(self):
        return self

    def delete(self):
        return 1

    def like(self):
        return 1