import requests
import json
from base64 import b64encode

def get_request(logger, url, headers=None, parameters=None, auth=None, return_json=False, verify=True):
    result = {}
    result['status_code'] = -1
    try:
        r = requests.get(url,headers=headers, params=parameters, auth=auth, verify=verify)
        result['status_code'] = r.status_code

        if r.status_code >= 200 and r.status_code <= 202:
            if return_json:
                result['content'] = r.json()
            else:
                result['content'] = r.content
        else: 
            logger.error(f'Failed to run get request to {r.url} - Error {r.status_code}: {r.content}')
    except:
        logger.exception(f'Failed to run get request to {url}')

    return result

def post_request(logger, url, headers=None, data=None, auth=None, return_json=False, verify=True):
    result = {}
    result['status_code'] = -1
    try:
        r = requests.post(url, headers=headers, data=data, auth=auth, verify=verify)
        result['status_code'] = r.status_code

        if r.status_code >= 200 and r.status_code <= 202:
            if return_json:
                result['content'] = r.json()
            else:
                result['content'] = r.content
        else: 
            logger.error(f'Error {r.status_code}: {r.content}')
    except:
        logger.exception(f'Failed to run get request to {url}')

    return result


def get_json_headers(logger, bearer_token=None, basic_auth=None):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    if bearer_token:
        headers['Authorization'] = 'Bearer ' + bearer_token

    if basic_auth:
        user_and_pass = b64encode(bytes(basic_auth,'utf-8')).decode("ascii")
        headers['Authorization'] = 'Basic ' + user_and_pass

    return headers


def check_url_ok(logger, url):
    try:
        r = requests.get(url)
        return r.status_code == 200
    except:
        logger.error(f'Failed to connect to url: {url}')
        return False
