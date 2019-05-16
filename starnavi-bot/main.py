import logging
from random import randint
from uuid import uuid4

from bot import Bot
from config import (
    PATH_TO_EMAILS, API_URL, NUMBER_OF_USERS,
    MAX_POSTS_PER_USER, MAX_LIKES_PER_USER
)
from utils import decode_access_token, parse_emails

logging.basicConfig(filename='bot.log', datefmt="%Y-%m-%d-%H-%M-%S",
                    level=logging.DEBUG)


def main():
    bot = Bot(
        API_URL,
        NUMBER_OF_USERS,
        MAX_POSTS_PER_USER,
        MAX_LIKES_PER_USER
    )
    emails = parse_emails(PATH_TO_EMAILS)
    for email in emails[:int(NUMBER_OF_USERS)]:
        random_password = str(uuid4()).replace('-', '')
        access_token = bot.sign_up(email, random_password)
        if access_token:
            decoded_access_token = decode_access_token(access_token)
            for post in range(randint(1, MAX_POSTS_PER_USER)):
                post_id = bot.create_post(decoded_access_token['user_id'],
                                          access_token)
                print(post_id)
                if post_id:
                    for _ in range(randint(1, MAX_LIKES_PER_USER)):
                        bot.like_post(post_id, access_token)


if __name__ == '__main__':
    main()
