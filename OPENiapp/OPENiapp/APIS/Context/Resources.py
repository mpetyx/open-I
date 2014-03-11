from .models import OpeniContext
from OPENiapp.APIS.OpeniGenericResource import GenericResource

__author__ = 'amertis'

class ContextResource(GenericResource):
    class Meta:
        queryset = OpeniContext.objects.all()