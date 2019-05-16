import logging
from typing import Union
from uuid import uuid4

import requests

logging.basicConfig(filename='bot.log', datefmt="%Y-%m-%d-%H-%M-%S",
                    level=logging.DEBUG)


class Bot:
    def __init__(self, api_url, number_of_users, max_posts_per_user,
                 max_likes_per_user):
        self.api_url = api_url
        self.number_of_users = number_of_users
        self.max_posts_per_user = max_posts_per_user
        self.max_likes_per_user = max_likes_per_user

    def sign_up(self, email: str, password: str) -> Union[str, None]:
        if email and password:
            url = f'{self.api_url}/users/auth/signup'
            r = requests.post(url, {'email': email, 'password': password})
            if r.status_code == 201:
                return r.json()['token']
            elif r.json()['email'][0] == 'Email already exists.':
                logging.info('Method: sign_up - %s' % r.json())
                return None
            logging.info('Method: sign_up - %s' % r.json())
            return None
        logging.info('Method: sign_up - parameter email or password is '
                     'required.')
        return None

    def create_post(self, user_id, access_token: str) -> Union[bool, None]:
        url = f'{self.api_url}/posts/create'
        r = requests.post(url,
                          {'user_id': user_id, 'title': str(uuid4()),
                           'description': str(uuid4())},
                          headers={
                              'Authorization': f'JWT {access_token}'})
        if r.status_code == 201:
            logging.info('Post created by user id - %s' % user_id)
            return r.json()['id']
        logging.info('Method: create_post - %s' % r.json())
        return None

    def like_post(self, post_id: int, access_token: str):
        url = f'{self.api_url}/posts/{post_id}/like'
        r = requests.post(url, {'id': post_id}, headers={
            'Authorization': f'JWT {access_token}'})
        if r.status_code == 200:
            return True
        return r.json()
