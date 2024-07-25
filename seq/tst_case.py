from typing import Optional, Union
from numbers import Number
import logging
from enum import Enum
from __init__ import *

class Status(Enum):
    waiting= "waiting"
    running= "running"
    aborted= "aborted"
    complete= "complete"

class Test():
    """
    The most basic unit of an executing test sequence.
    Within a test, we may have a setup(), execute(), and \
    teardown() method.  Only the `execute()` method is required \
    to be overridden.
    - Properties:  criteria, abort, is_passing
    - Status: waiting, running, aborted, complete
    :param nickname: a shortcut name for this particular test
    :param min_value: the minimum value that is to be considered a pass, if defined
    :param max_value: the maximum value that is to be considered a pass, if defined
    :param pass_if: the value that must be present in order to pass, if defined
    :param loglevel: the logging level to apply such as `logging.INFO`    
    :param decimal_position: the number of significant decimals appropriate to the measurement
    """
    def __init__(
        self, 
        nickname: str,
        pass_if: Optional[Union[str, bool, int]]= None,
        min_value: Optional[Number]= None,
        max_value: Optional[Number]= None,
        decimal_position: Optional[int] = 4,
        loglevel= logging.INFO,
        ):
        self._logger= logging.getLogger(self.__class__.__name__)
        self._logger.setLevel(loglevel)
        
        criteria={}
        if pass_if is not None:
            criteria["pass_if"]= pass_if
        if max_value is not None:
            criteria["max"]= max_value
        if min_value is not None:
            criteria["min"]= min_value
        self.__criteria= criteria if criteria else None
        self.decimal_position = decimal_position
                
        self.nickname= nickname
        self._test_is_passing= None
        self.test_result= None
        self.aborted= False 
        self.status= Status.waiting.value
        self.saved_data = {}
    
    #Properties criteria, aborted, is_passing
    @property
    def criteria(self):
        """
        Returns the test criteria as a `dict`
        return: test criteria as a `dict`
        """        
        return self.__criteria
        
    @property
    def is_passing(self):
        """
        input:
        return: `True` if passing, else `False`
        """
        return self._test_is_passing
    
    #Protected methods 
    def _teardown(self, is_passing: bool):
        """
        Pre-execution method used for logging and housekeeping.

        :param is_passing: True if the test sequence is passing up to \
        this point, else False
        :return:
        """
        if self.aborted:
            self.status = "aborted"
            self._logger.warning("aborted, not executing")
            return

        self._logger.info(f'tearing down "{self.nickname}"')

        self.teardown(is_passing)
        self.status = "complete"
        
        
    def _setup(self, is_passing: bool):
        """
        Pre-execution method used for logging and housekeeping.
        :param is_passing: True if the test sequence is passing up to this \
        point, else False
        :return:
        """
        try:
            self._logger.info((f'setting up "{self.nickname}"')) 
        
            self._test_is_passing= True
            self.test_result= None
            self.status= Status.running.value if not self.aborted else Status.aborted.value
            
            self.aborted= False
            if not self.setup(is_passing=is_passing):
                self.status= Status.aborted.value    
            self.status= Status.running.value if not self.aborted else Status.aborted.value
        except Exception as e:
            self._logger.critical(f"crirtial error {e}") 
        
    def _execute(self, is_passing:bool):
        """
        Pre-execution method used for logging and housekeeping.

        :param is_passing: True if the test sequence is passing up to this \
        point, else False
        :return: Test result 
        """   
        try:    
            self.status= Status.running.value if not self.status else Status.aborted.value
            if self.aborted:
                self._logger.info("aborted, not executing")
                return
            self._logger.info(f'executing test "{self.nickname}"')
            value= self.execute(is_passing=is_passing)
            self.test_result= value
            if self.__criteria is not None:
                if self.__criteria.get("pass_if") is not None:
                    if self.test_result != self.__criteria["pass_if"]:
                        self._logger.warning(
                            f'FAIL => "{self.test_result}" != pass_if requirement '
                            f'"{self.__criteria["pass_if"]}", failing'
                        )
                        self.fail()
                    else:
                        self._logger.info(
                            f'PASS => "{self.test_result}" == pass_if requirement '
                            f'"{self.__criteria["pass_if"]}"'
                        )

                if self.__criteria.get("min") is not None:
                    if self.test_result < self.__criteria["min"]:
                        self._logger.warning(
                            f'FAIL => "{self.test_result}" is below the minimum '
                            f'"{self.__criteria["min"]}", failing'
                        )
                        self.fail()
                    else:
                        self._logger.info(
                            f'PASS => "{self.test_result}" is above the minimum '
                            f'"{self.__criteria["min"]}"'
                        )

                if self.__criteria.get("max") is not None:
                    if self.test_result > self.__criteria["max"]:
                        self._logger.warning(
                            f'FAIL => "{self.test_result}" is above the maximum '
                            f'"{self.__criteria["max"]}"'
                        )
                        self.fail()
                    else:
                        self._logger.info(
                            f'PASS => "{self.test_result}" is below the maximum '
                            f'"{self.__criteria["max"]}"'
                        )       
            return self.test_result
        except Exception as e:
            self._logger.critical(f"crirtial error {e}")     
            
    #Public methods 
#TODO
#    def save_dict(self, data: dict):

    def reset(self) -> None:
        """
        Reset the test status
        :return: None
        """
        self.status= Status.waiting.value        

    def abort(self):
        """
        Causes current test status to abort
        :return: True/False
        """
        self.aborted= True
    
    def fail(self):
        """
        When called, will cause the test to fail.
        :return: None
        """        
        self._test_is_passing= False

        
    #Abstract methods setup(), execute(), and teardown()
    def setup(self, is_passing:bool):
        """
        Abstract method intended to be overridden by subclass

        :param is_passing: True if the test sequence is passing up to this \
        point, else False
        :return: None
        """        
        pass
    
    def execute(self, is_passing:bool):
        """
        Abstract method intended to be overridden by subclass

        :param is_passing: True if the test sequence is passing up to this \
        point, else False
        :return: value to be appended to the sequence dictionary
        """    
        raise NotImplementedError
    
    def teardown(self, is_passing:bool):
        """
        Abstract method intended to be overridden by subclass

        :param is_passing: True if the test sequence is passing up to this \
        point, else False
        :return: None
        """
        pass 