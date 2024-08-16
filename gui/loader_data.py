import logging
import coloredlogs
from typing import Optional, List, Tuple, Any
import csv
from api_consumer import ApiSettings
import requests
from requests.auth import HTTPDigestAuth

coloredlogs.install(level="INFO")


class LoaderData:
    def __init__(self,
                 station_fp: Optional[str] = "config/station.csv",
                 part_numbers_fp: Optional[str] = "config/part_numbers.csv",
                 ):
        # set logger
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__logger.setLevel(logging.INFO)
        self.apis = ApiSettings()
        # fp
        self.station_fp = station_fp
        self.part_numbers_fp = part_numbers_fp

    def get_station_info(self):
        station_info_dict, columns_name_ste = self.__reader_csv(self.station_fp)
        return station_info_dict, columns_name_ste

    # def get_part_numbers_from_api(self) -> tuple[list[Any], str]:
    #     try:
    #         part_number_data, column_name = self.apis.partnumbers()
    #         # response = requests.get("http://127.0.0.1:8000/api/partnumbers/")
    #         # self.__logger.info(f"part numbers {response.status_code} ")
    #         # # part_numbers_data = json.loads(response.content).get('PartNumber')
    #         # part_numbers_data = response.json().get('PartNumber')
    #         part_number_list = []
    #         # column_name = "partnumber"   # TODO  no mame must be arguments
    #         for data_dict in part_number_data:
    #             # data = data_dict.values()
    #             # part_number_list.append(list(data))
    #             data = data_dict.get(column_name)
    #             part_number_list.append(data)
    #         return part_number_list, column_name
    #     except BaseException as e:
    #         self.__logger.error(f"an exception occurred during the <get_part_numbers_from_api>: {e}")
    #         pass

    def get_part_numbers(self):
        # Read API data if fail read from file
        # part_number_list, columns_name_pn = self.get_part_numbers_from_api()
        part_number_list, columns_name_pn = self.apis.partnumbers()
        if not part_number_list:
            part_numbers_data, _ = self.__reader_csv(self.part_numbers_fp)
            for data_dict in part_numbers_data:
                # data = data_dict.values()
                # part_number_list.append(list(data))
                data = data_dict.get(columns_name_pn)   # TODO  no mame must be arguments? double check
                part_number_list.append(data)
        return part_number_list, columns_name_pn

    def get_testplan(self, testplan_fp):
        testplan_dict, columns_name_tp = self.__reader_csv(testplan_fp)
        return testplan_dict, columns_name_tp

    def get_test_exec(self, test_exec_fp):
        testplan_dict, columns_name_tp = self.__reader_csv(
            test_exec_fp, {'VALUE': ' ', 'RESULTS': ' '})
        return testplan_dict, columns_name_tp

    def update_all_test_exec(selfself,
                             current_results: list,
                             new_results: list):
        for i in range(len(current_results)):
            for key in new_results[i].keys():
                current_results[i][key] = new_results[i][key]
        return current_results

    def update_test_exec(self, index: int,
                         current_results: list,
                         new_result: list):
        for key in new_result[0].keys():
            current_results[index][key] = new_result[0][key]
        return current_results

    def __reader_csv(self,
                     file_pointer,
                     extra_elements: Optional[dict] = None
                     ):
        try:
            list_dicts = []
            with open(file_pointer, mode='r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    row_norm = {key.lower(): value for key, value in row.items()}
                    list_dicts.append(row_norm)
                    if extra_elements is not None:
                        extra_norm = {key.lower(): value for key, value in extra_elements.items()}
                        list_dicts[-1].update(extra_norm)
            columns = csv_reader.fieldnames
            if extra_elements is not None:
                columns = columns + list(extra_elements.keys())
            columns_name = [col.lower() for col in columns]
            return list_dicts, columns_name
        except BaseException as e:
            self.__logger.error(f"an exception occurred during the <get_testplan>: {e}")
            pass

    def __writer_csv(self, file_pointer):
        try:
            list_dicts = []
            with open(file_pointer, mode='w') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    row_norm = {key.upper(): value for key, value in row.items()}
                    list_dicts.append(row_norm)
            #              if extra_elements is not None:
            #                  extra_norm = {key.upper(): value for key, value in extra_elements.items()}
            #                  list_dicts[-1].update(extra_norm)
            columns = csv_reader.fieldnames
            #      if extra_elements is not None:
            #          columns = columns + list(extra_elements.keys())
            columns_name = [col.upper() for col in columns]
            return list_dicts, columns_name
        except BaseException as e:
            self.__logger.error(f"an exception occurred during the <get_testplan>: {e}")
            pass
