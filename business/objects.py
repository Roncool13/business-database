""" Graphene Objects Definition File """

# Third party imports
from graphene_django import DjangoObjectType
from graphene import relay

# Local application imports
from .models import Business


class BusinessType(DjangoObjectType):
    class Meta:
        model = Business
        fields = ('name', 'owner', 'employee_count', 'address')


class BusinessNode(DjangoObjectType):
    class Meta:
        model = Business
        filter_fields = {
            'name': ['iexact', 'icontains', 'istartswith'],
            'owner': ['iexact', 'icontains', 'istartswith'],
            'address': ['iexact', 'icontains', 'istartswith'],
            'employee_count': ['lt', 'gt'],
        }
        interfaces = (relay.Node, )
