# Third party imports
import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

# Local application imports
from .models import Business
from .objects import BusinessType, BusinessNode


class BusinessQuery(graphene.ObjectType):
    all_business = graphene.List(BusinessType)
    business = relay.Node.Field(BusinessNode)
    search_business = DjangoFilterConnectionField(BusinessNode)
    business_by_name = graphene.Field(BusinessType, name=graphene.String(required=True))
    business_by_owner = graphene.Field(BusinessType, owner=graphene.String(required=True))

    def resolve_all_business(root, info):
        return Business.objects.all()

    # def resolve_business_by_name(root, info, name):
    #     """ Searching Business by name """
    #     try:
    #         return Business.objects.get(name__iexact=name)
    #     except Business.DoesNotExist:
    #         return None
    #
    # def resolve_business_by_owner(root, info, owner):
    #     """ Searching Business by owner """
    #     try:
    #         return Business.objects.get(owner__iexact=owner)
    #     except Business.DoesNotExist:
    #         return None
