from helpers.config import get_settings,Settings
import os
import random
import string

class BaseDataModel:

    def __init__(self, db_client: object):
        self.db_client = db_client
        self.app_settings = get_settings()
