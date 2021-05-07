""" File containing mutations """

# Third party imports
import graphene

# Local application imports
from .objects import BusinessType
from .models import Business


class CreateBusinessMutation(graphene.Mutation):
    """ Mutation for adding new Business """
    business = graphene.Field(BusinessType)
    message = graphene.String()
    status = graphene.Int()

    class Arguments:
        name = graphene.String(required=True)
        owner = graphene.String(required=True)
        address = graphene.String(required=True)
        employee_count = graphene.Int(required=True)

    @classmethod
    def mutate(cls, root, info, name, owner, address, employee_count):
        queryset = Business.objects.filter(name=name)

        if len(queryset) != 0:
            msg = f'Business with name {name} already exists'
            status = 400
            obj = None
        else:
            obj = Business.objects.create(name=name, owner=owner, address=address, employee_count=employee_count)
            status = 200
            msg = 'Business Info successfully added'
        return cls(business=obj, message=msg, status=status)


class UpdateBusinessMutation(graphene.Mutation):
    """ Mutation for updating existing Business """
    business = graphene.Field(BusinessType)
    message = graphene.String()
    status = graphene.Int()

    class Arguments:
        name = graphene.String(required=True)
        owner = graphene.String()
        address = graphene.String()
        employee_count = graphene.Int()

    @classmethod
    def mutate(cls, root, info, name, **kwargs):
        queryset = Business.objects.filter(name=name)

        if len(queryset) != 0:
            queryset.update(**kwargs)
            obj = Business.objects.get(name=name)
            status = 200
            msg = 'Business Info successfully updated'
        else:
            msg = f'Business with name {name} does not exist'
            status = 400
            obj = None
        return cls(business=obj, message=msg, status=status)


class DeleteBusinessMutation(graphene.Mutation):
    """ Mutation for deleting existing Business """
    message = graphene.String()
    status = graphene.Int()

    class Arguments:
        name = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, name):
        queryset = Business.objects.filter(name=name)

        if len(queryset) != 0:
            queryset.delete()
            status = 200
            msg = 'Business Info successfully deleted'
        else:
            msg = f'Business with name {name} does not exist'
            status = 400
        return cls(message=msg, status=status)
