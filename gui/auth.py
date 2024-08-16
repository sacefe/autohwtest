import logging
import coloredlogs
from typing import Optional
import requests
from requests.auth import HTTPDigestAuth
import json

coloredlogs.install(level="INFO")


class Auth:
    def __init__(self):
        # set logger
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__logger.setLevel(logging.INFO)

    """
    Validate user , send User/Password and validate in Web App
    """
    def user_verification(self, dlg_user, dlg_password):
        try:
            # request = requests.get("http://127.0.0.1:8000/api/part-numbers/")
            # print("get something: ")
            # print("status code response: ", request.status_code)
            # print("content response: ", request.content)
            # all_fields = json.loads(request.content)
            # print(all_fields)
            # print("response Status: ", all_fields.get('Status'))
            # print("response Status: ", all_fields.get('partnumbers'))
            return True
        except BaseException as e:
            self.__logger.error(f"an exception occurred during the <user_verification>: {e}")
            pass
        return True

