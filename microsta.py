import requests
import json


class InstagramGraph():

    def __init__(self, access_token, client_id, client_secret, page_id, instagram_account_id, graph_domain='https://graph.facebook.com/', graph_version='v14.0', debug='no') -> None:
        self.access_token = access_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.graph_domain = graph_domain
        self.graph_version = graph_version
        self.debug = debug
        self.page_id = page_id
        self.instagram_account_id = instagram_account_id
        self.endpoint_base = self.graph_domain + self.graph_version + '/'


    def getCreds(self) :
        creds = dict()
        creds['access_token'] = self.access_token
        # 'long lived'AbNrriZA4g4BAHvsiU2JCDppLScxXZC1mnElywxW0Sa0aGYmsTljlrhB79kYpMnS3QIsM9AMjgFmA5Fzqwouk1y9ZCI6ZAfHhtQOvehNhbZANiA52M7swhdPGX5InyHp4LzWpMNyUyuzOZCyUm4phhorMqzlj42uZC6HyNDzo2iUrHnQNcpxlu
        # 'EAAbNrriZA4g4BAGJBU6Qy0IB8NtyRgsW4MUBWmZABZAeaPmf5G7CdmbYzvh1Rh7s8ogy3ygyCjKqfsKYwO6lBOB9p5ftAZB80BNnHPkBZCCcGIL3tQbFZCZCgZBwNiYSTBuferTG1bS8q5qojqWMwXpvZCzxdvL1luAEEOBAk9ddOhcW5L15cZAOIb'
        # old
        # 'EAAbNrriZA4g4BAC0eOrRHU96q4ZAKgI7QjTHYAzyBeOO8bIZCYgR1OaucMnsBdzpGMAlvjDilNsLblhIecPpzl6CHQYZB66kgyU06vGN2DUj3u5q0oC20OwJNFgFHXxGDmOszZA5QGYJAdYHYaE5mLSuTEfLlH5A9UZAEgveTAPhES1ZAflzZB0y6p4FwXk7cD1YtKFlXu9NZBZCZAjxnINbnrZAIt0XCVhZBvfAZD'
        creds['client_id'] = self.client_id
        creds['client_secret'] = self.client_secret
        creds['graph_domain'] = self.graph_domain
        creds['graph_version'] = self.graph_version
        creds['endpoint_base'] = self.endpoint_base
        creds['debug'] = self.debug
        creds['page_id'] = self.page_id
        creds['instagram_account_id'] = self.instagram_account_id
        return creds

    def makeApiCall(self, url, endpointParams, debug='no'):
        data = requests.get(url, endpointParams)
        response = dict()
        response['url'] = url
        response['endpoint_params'] = endpointParams
        response['endpoint_params_pretty'] = json.dumps(endpointParams, indent=4)
        response['json_data'] = json.loads(data.content)
        response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)
        return response

    def getAccount(self, params, username):
        endpointParams = dict()
        endpointParams['fields'] = 'business_discovery.username(' + username + '){name,username,followers_count,follows_count,media_count,profile_picture_url,biography, ig_id, id, website}'
        endpointParams['access_token'] = params['access_token']
        url = params['endpoint_base'] + params['instagram_account_id']
        return self.makeApiCall(url, endpointParams, params['debug'])

    def getMedia(self, params, username):
        endpointParams = dict()
        endpointParams['fields'] = 'business_discovery.username(' + username + '){media{caption, comments_count, like_count, media_url,permalink,media_product_type, media_type, timestamp, id}}'
        endpointParams['access_token'] = params['access_token']
        url = params['endpoint_base'] + params['instagram_account_id']
        return selfmakeApiCall(url, endpointParams, params['debug'])

