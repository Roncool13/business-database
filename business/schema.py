# Third-party imports
import graphene

# Local application imports
from .mutations import CreateBusinessMutation, UpdateBusinessMutation, DeleteBusinessMutation
from .queries import BusinessQuery


# class BusinessSerializerMutation(SerializerMutation):
#     class Meta:
#         serializer_class = BusinessSerializer
#         model_operations = ['create', 'update', 'delete']
#         lookup_field = 'id'


class BusinessMutation(graphene.ObjectType):
    create_business = CreateBusinessMutation.Field()
    update_business = UpdateBusinessMutation.Field()
    delete_business = DeleteBusinessMutation.Field()


schema = graphene.Schema(query=BusinessQuery, mutation=BusinessMutation)
