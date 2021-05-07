# Standard library imports
import json
import logging
import sys
import os

# Third party imports
import pytest
from django.test import TestCase
from django.conf import settings
from graphene_django.utils.testing import graphql_query

# Local application imports
from business.schema import schema


logger = logging.getLogger(__file__)


# @pytest.fixture
# def client_query(client):
#     def func(*args, **kwargs):
#         return graphql_query(*args, **kwargs, client=client)
#
#     return func
#
#
# def test_allbusiness_query(db, client_query):
#     response = client_query(
#         '''
#         query {
#             searchBusiness(address_Icontains: "China"){
#             edges{
#               node{
#                 name,
#                 owner,
#                 address,
#                 employeeCount
#               }
#             }
#           }
#         }
#         '''
#     )
#     content = json.loads(response.content)
#     assert 'errors' not in content


class BusinessTest(TestCase):
    fixtures = ['business.json']

    def setUp(self) -> None:
        file_path = os.path.join(settings.BASE_DIR, 'tests', 'test_business.json')
        with open(file_path, 'r') as fp:
            self.data_dict = json.load(fp)

    def test_all_business_query(self):
        """ Test allBusiness Query to get all the records"""
        query = '''
            query{
              allBusiness{
                name,
                owner,
                address,
                employeeCount
              }
            }
        '''
        result = schema.execute(query)
        assert result is not None
        assert result.to_dict() == self.data_dict

    def test_search_business_by_exact_name_query(self):
        """ Test searchBusiness Query to get business record for specific name """
        query = '''
            query {
              searchBusiness(name_Iexact: "zomato"){
                edges{
                  node{
                    name,
                    owner,
                    address,
                    employeeCount
                  }
                }
              }
            }
        '''
        result = schema.execute(query)
        assert result is not None
        result_dict = result.to_dict()
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['name'] == 'Zomato'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['owner'] == 'Gaurav Gupta'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['address'] == 'Gurgaon, Haryana, India'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['employeeCount'] == 5001

    def test_search_business_by_name_contains_query(self):
        """ Test searchBusiness Query to get business record for name containing specific keyword """
        query = '''
            query {
              searchBusiness(name_Icontains: "bank"){
                edges{
                  node{
                    name,
                    owner,
                    address,
                    employeeCount
                  }
                }
              }
            }
        '''
        result = schema.execute(query)
        assert result is not None
        result_dict = result.to_dict()
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['name'] == 'SoftBank'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['owner'] == 'Masayoshi Son'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['address'] == 'Tokyo, Japan'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['employeeCount'] == 10001

    def test_search_business_by_name_startswith_query(self):
        """ Test searchBusiness Query to get business record for name starting with certain keyword """
        query = '''
            query {
              searchBusiness(name_Istartswith: "fire"){
                edges{
                  node{
                    name,
                    owner,
                    address,
                    employeeCount
                  }
                }
              }
            }
        '''
        result = schema.execute(query)
        assert result is not None
        result_dict = result.to_dict()
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['name'] == 'Fireblocks'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['owner'] == 'Idan Ofrat'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['address'] == 'New York, New York, United States'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['employeeCount'] == 250

    def test_search_business_by_exact_address_query(self):
        """ Test searchBusiness Query to get business record for specific address """
        query = '''
            query {
              searchBusiness(address_Iexact: "New York, New York, United States"){
                edges{
                  node{
                    name,
                    owner,
                    address,
                    employeeCount
                  }
                }
              }
            }
        '''
        result = schema.execute(query)
        assert result is not None
        result_dict = result.to_dict()
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['name'] == 'Fireblocks'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['owner'] == 'Idan Ofrat'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['address'] == 'New York, New York, United States'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['employeeCount'] == 250

    def test_search_business_by_address_contains_query(self):
        """ Test searchBusiness Query to get business record for address containing specific keyword """
        query = '''
            query {
              searchBusiness(address_Icontains: "India"){
                edges{
                  node{
                    name,
                    owner,
                    address,
                    employeeCount
                  }
                }
              }
            }
        '''
        result = schema.execute(query)
        assert result is not None
        result_dict = result.to_dict()
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['name'] == 'Zomato'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['owner'] == 'Gaurav Gupta'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['address'] == 'Gurgaon, Haryana, India'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['employeeCount'] == 5001

    def test_search_business_by_address_startswith_query(self):
        """ Test searchBusiness Query to get business record for address starting with certain keyword """
        query = '''
            query {
              searchBusiness(address_Istartswith: "Tokyo"){
                edges{
                  node{
                    name,
                    owner,
                    address,
                    employeeCount
                  }
                }
              }
            }
        '''
        result = schema.execute(query)
        assert result is not None
        result_dict = result.to_dict()
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['name'] == 'SoftBank'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['owner'] == 'Masayoshi Son'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['address'] == 'Tokyo, Japan'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['employeeCount'] == 10001

    def test_search_business_by_exact_owner_query(self):
        """ Test searchBusiness Query to get business record for specific owner """
        query = '''
            query {
              searchBusiness(owner_Iexact: "Idan Ofrat"){
                edges{
                  node{
                    name,
                    owner,
                    address,
                    employeeCount
                  }
                }
              }
            }
        '''
        result = schema.execute(query)
        assert result is not None
        result_dict = result.to_dict()
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['name'] == 'Fireblocks'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['owner'] == 'Idan Ofrat'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['address'] == 'New York, New York, United States'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['employeeCount'] == 250

    def test_search_business_by_owner_contains_query(self):
        """ Test searchBusiness Query to get business record for owner containing specific keyword """
        query = '''
            query {
              searchBusiness(owner_Icontains: "Gaurav"){
                edges{
                  node{
                    name,
                    owner,
                    address,
                    employeeCount
                  }
                }
              }
            }
        '''
        result = schema.execute(query)
        assert result is not None
        result_dict = result.to_dict()
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['name'] == 'Zomato'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['owner'] == 'Gaurav Gupta'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['address'] == 'Gurgaon, Haryana, India'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['employeeCount'] == 5001

    def test_search_business_by_owner_startswith_query(self):
        """ Test searchBusiness Query to get business record for owner starting with certain keyword """
        query = '''
            query {
              searchBusiness(owner_Istartswith: "Masa"){
                edges{
                  node{
                    name,
                    owner,
                    address,
                    employeeCount
                  }
                }
              }
            }
        '''
        result = schema.execute(query)
        assert result is not None
        result_dict = result.to_dict()
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['name'] == 'SoftBank'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['owner'] == 'Masayoshi Son'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['address'] == 'Tokyo, Japan'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['employeeCount'] == 10001

    def test_search_business_by_lessthan_employeeCount_query(self):
        """ Test searchBusiness Query to get employeeCount less than specific number """
        query = '''
            query {
              searchBusiness(employeeCount_Lt: 500){
                edges{
                  node{
                    name,
                    owner,
                    address,
                    employeeCount
                  }
                }
              }
            }
        '''
        result = schema.execute(query)
        assert result is not None
        result_dict = result.to_dict()
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['name'] == 'Fireblocks'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['owner'] == 'Idan Ofrat'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['address'] == 'New York, New York, United States'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['employeeCount'] == 250

    def test_search_business_by_greaterthan_employeeCount_query(self):
        """ Test searchBusiness Query to get employeeCount greater than specific number """
        query = '''
            query {
              searchBusiness(employeeCount_Gt: 4500){
                edges{
                  node{
                    name,
                    owner,
                    address,
                    employeeCount
                  }
                }
              }
            }
        '''
        result = schema.execute(query)
        assert result is not None
        result_dict = result.to_dict()
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['name'] == 'SoftBank'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['owner'] == 'Masayoshi Son'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['address'] == 'Tokyo, Japan'
        assert result_dict['data']['searchBusiness']['edges'][0]['node']['employeeCount'] == 10001
        assert result_dict['data']['searchBusiness']['edges'][1]['node']['name'] == 'Zomato'
        assert result_dict['data']['searchBusiness']['edges'][1]['node']['owner'] == 'Gaurav Gupta'
        assert result_dict['data']['searchBusiness']['edges'][1]['node']['address'] == 'Gurgaon, Haryana, India'
        assert result_dict['data']['searchBusiness']['edges'][1]['node']['employeeCount'] == 5001