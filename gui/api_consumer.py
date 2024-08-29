
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
            column_names = ["id", "partnumber", "description"]  # TODO  no mame must be arguments
            # part_numbers_list = list(filter(lambda x:x[column_name], part_numbers_data))
            # part_numbers_list = list(x[column_names] for x in part_numbers_data)
            # part_numbers_list = [{x[key] for key in column_names} for x in part_numbers_data]
            # for data_dict in part_numbers_data:
            #     # data = data_dict.values()
            #     # part_number_list.append(list(data))
            #     data = data_dict.get(column_name)
            #     part_numbers_list.append(data)
            return part_numbers_data, column_names
        except BaseException as e:
            self.__logger.error(f"an exception occurred during the <get_part_numbers_from_api>: {e}")
            return None, None

    def test_matrix(self):  # TODO  Get test martix from Database
        try:
            str_get = f"{self.__server}api/testmatrix/"
            response = requests.get(str_get)
            self.__logger.info(f"test matrix {response.status_code} ")
            test_matrix_data = response.json().get('TestMatrix')
            column_names = ["partnumber_fk", "sibling_lname_fk", "testplan_name"]  # TODO  no mame must be arguments
            new_response = [{key: x[key] for key in column_names} for x in test_matrix_data]
            return new_response, column_names
            # return None, None
        except BaseException as e:
            self.__logger.error(f"an exception occurred during the <get_part_numbers_from_api>: {e}")
            return None, None

    def testplan(self):  # TODO  Get test martix from Database
        try:
            partnumber_fk, sibling_lname_fk = 1, 1 #TODO partnumber_fk and sibling_lname_fk  must be arguments
            str_get = f"{self.__server}api/testmatrix/{partnumber_fk},{sibling_lname_fk}"
            response = requests.get(str_get)
            self.__logger.info(f"test matrix {response.status_code} ")
            test_matrix_data = response.json().get('TestMatrix')
            column_name = "testplan_name"  # TODO  no mame must be arguments
            testplan_name = test_matrix_data.get(column_name)
            return testplan_name
            # return None
        except BaseException as e:
            self.__logger.error(f"an exception occurred during the <get_part_numbers_from_api>: {e}")
            return None
