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


class BusinessTest(TestCase):
    fixtures = ['business.json']

    def setUp(self) -> None:
        file_path = os.path.join(settings.BASE_DIR, 'tests', 'test_business.json')
        with open(file_path, 'r') as fp:
            self.data_dict = json.load(fp)

    def test_create_business_mutation(self):
        """ Testing Mutation for creation of Business normally """
        mutation = '''
            mutation CreateBusinessMutation{
              createBusiness(name: "Eichiba Inc", owner: "Anweshan Guha", address: "San Jose, California, United States", employeeCount:10){
                business{
                  name,
                  owner,
                  address,
                  employeeCount
                }
                message,
                status
              }
            }
        '''
        result = schema.execute(mutation)
        assert result is not None
        result_dict = result.to_dict()
        assert result_dict['data']['createBusiness']['status'] == 200
        assert result_dict['data']['createBusiness']['message'] == 'Business Info successfully added'
        assert result_dict['data']['createBusiness']['business']['name'] == 'Eichiba Inc'
        assert result_dict['data']['createBusiness']['business']['owner'] == 'Anweshan Guha'
        assert result_dict['data']['createBusiness']['business']['address'] == 'San Jose, California, United States'
        assert result_dict['data']['createBusiness']['business']['employeeCount'] == 10

    def test_create_business_already_exists_mutation(self):
        """ Testing Mutation for creation of Business that already exists in records"""
        mutation = '''
            mutation CreateBusinessMutation{
              createBusiness(name: "Zomato", owner: "Gaurav Gupta", address: "Gurgaon, Haryana, India", employeeCount:5001){
                business{
                  name,
                  owner,
                  address,
                  employeeCount
                }
                message,
                status
              }
            }
        '''
        result = schema.execute(mutation)
        assert result is not None
        result_dict = result.to_dict()
        assert result_dict['data']['createBusiness']['status'] == 400
        assert result_dict['data']['createBusiness']['message'] == 'Business with name Zomato already exists'
        assert result_dict['data']['createBusiness']['business'] is None

    def test_update_business_mutation(self):
        """ Testing Mutation for updation of Business normally """
        mutation = '''
            mutation UpdateBusinessMutation{
              updateBusiness(name: "Zomato", owner: "Deepinder Goyal", address: "Gurgaon, Haryana, India", employeeCount:5001){
                business{
                  name,
                  owner,
                  address,
                  employeeCount
                }
                message,
                status
              }
            }
        '''
        result = schema.execute(mutation)
        assert result is not None
        result_dict = result.to_dict()
        assert result_dict['data']['updateBusiness']['status'] == 200
        assert result_dict['data']['updateBusiness']['message'] == 'Business Info successfully updated'
        assert result_dict['data']['updateBusiness']['business']['owner'] == 'Deepinder Goyal'

    def test_update_business_does_not_exist_mutation(self):
        """ Testing Mutation for updation of Business that does not exist in records """
        mutation = '''
            mutation UpdateBusinessMutation{
              updateBusiness(name: "CoinSwitch Kuber", owner: "Ashish Singhal", address: "Bangalore, Karnataka, India", employeeCount:2000){
                business{
                  name,
                  owner,
                  address,
                  employeeCount
                }
                message,
                status
              }
            }
        '''
        result = schema.execute(mutation)
        assert result is not None
        result_dict = result.to_dict()
        assert result_dict['data']['updateBusiness']['status'] == 400
        assert result_dict['data']['updateBusiness']['message'] == 'Business with name CoinSwitch Kuber does not exist'
        assert result_dict['data']['updateBusiness']['business'] is None

    def test_delete_business_mutation(self):
        """ Testing Mutation for deletion of Business normally """
        mutation = '''
            mutation DeleteBusinessMutation{
              deleteBusiness(name: "Zomato"){
                message,
                status
              }
            }
        '''
        result = schema.execute(mutation)
        assert result is not None
        result_dict = result.to_dict()
        assert result_dict['data']['deleteBusiness']['status'] == 200
        assert result_dict['data']['deleteBusiness']['message'] == 'Business Info successfully deleted'

    def test_delete_business_does_not_exist_mutation(self):
        """ Testing Mutation for deletion of Business that does not exist in records """
        mutation = '''
            mutation DeleteBusinessMutation{
              deleteBusiness(name: "CoinSwitch Kuber"){
                message,
                status
              }
            }
        '''
        result = schema.execute(mutation)
        assert result is not None
        result_dict = result.to_dict()
        assert result_dict['data']['deleteBusiness']['status'] == 400
        assert result_dict['data']['deleteBusiness']['message'] == 'Business with name CoinSwitch Kuber does not exist'
