import configparser
import os

env = os.environ

config = configparser.ConfigParser()
config.read('config.ini')

API_URL = config.get('BACKEND', 'api_url')
PATH_TO_EMAILS = config.get('BACKEND', 'path_to_emails')
NUMBER_OF_USERS = int(config.get('BOT', 'number_of_users'))
MAX_POSTS_PER_USER = int(config.get('BOT', 'max_posts_per_user'))
MAX_LIKES_PER_USER = int(config.get('BOT', 'max_likes_per_user'))

JWT_SECRET_KEY = env.get('JWT_SECRET_KEY', 'secret-key')
JWT_ALGORITHMS = env.get('JWT_ALGORITHMS', 'HS256')
