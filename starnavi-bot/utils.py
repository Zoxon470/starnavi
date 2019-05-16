import logging
from typing import Union

import jwt

from config import JWT_SECRET_KEY, JWT_ALGORITHMS

logging.basicConfig(filename='bot.log', datefmt="%Y-%m-%d-%H-%M-%S",
                    level=logging.DEBUG)


def decode_access_token(access_token: str) -> str:
    try:
        return jwt.decode(access_token, JWT_SECRET_KEY,
                          algorithms=[JWT_ALGORITHMS])
    except jwt.exceptions.InvalidSignatureError:
        logging.error('Method: decode_access_token - Signature '
                      'verification failed.')
        return 'Signature verification failed.'


def parse_emails(path_to_file: str) -> Union[list, bool]:
    if path_to_file:
        with open(path_to_file, 'r') as f:
            email_list = f.read().splitlines()
            return email_list
    logging.error('Method: parse_emails - parameter path_to_file is '
                  'required.')
    return False
