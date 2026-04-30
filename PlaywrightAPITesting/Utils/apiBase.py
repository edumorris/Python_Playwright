import os

from playwright.sync_api import Playwright

class APIUtils:

    def getToken(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url=os.environ['client_api_base_url'])

        data = {
            'userEmail': os.environ['client_api_email'],
            'userPassword': os.environ['client_api_pwd'],
        }

        response = api_request_context.post('/api/ecom/auth/login',
                                 data = data)

        assert  response.ok

        return response.json()['token']

    def createOrder(self, playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url=os.environ['client_api_base_url'])

        orderData = {
            'orders': [
                {
                    'country': 'India',
                    'productOrderedId': '6960eac0c941646b7a8b3e68'
                }
            ]
        }

        headers = {
            'Authorization': self.getToken(playwright),
            'Content-Type': 'application/json'
        }

        response = api_request_context.post('/api/ecom/order/create-order',
                                 data = orderData,
                                 headers = headers)

        response_body = response.json()

        assert response.status == 201

        return response_body["orders"][0]