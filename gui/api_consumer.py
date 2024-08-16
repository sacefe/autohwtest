
import requests
import logging
import coloredlogs
import json

coloredlogs.install(level="INFO")


class ApiSettings:
    def __init__(self):
        self.__server = "http://127.0.0.1:8000/"
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__logger.setLevel(logging.INFO)

    def partnumbers(self):
        try:
            response = requests.get(self.__server + "api/partnumbers/")
            self.__logger.info(f"part numbers {response.status_code} ")
            part_numbers_data = response.json().get('PartNumber')
            column_name = "partnumber"  # TODO  no mame must be arguments
            # part_number_list = list(filter(lambda x:x[column_name], part_numbers_data))
            part_number_list = list(x[column_name] for x in part_numbers_data)

            # for data_dict in part_numbers_data:
            #     # data = data_dict.values()
            #     # part_number_list.append(list(data))
            #     data = data_dict.get(column_name)
            #     part_number_list.append(data)
            return part_number_list, column_name
        except BaseException as e:
            self.__logger.error(f"an exception occurred during the <get_part_numbers_from_api>: {e}")
            pass

