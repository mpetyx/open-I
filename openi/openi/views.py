__author__ = 'mpetyx'

from sorl.thumbnail import get_thumbnail

im = get_thumbnail(my_file, '100x100', crop='center', quality=99)