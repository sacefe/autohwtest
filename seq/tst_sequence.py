from seq.tst_case import Test
from threading import Thread, Lock, Semaphore
import logging
from time import sleep
from typing import Optional
from enum import Enum
import traceback
from datetime import datetime
 
 
class State(Enum):
    '''
    State Machine - Using strings b/c we can relatively easily look
    for valid substrings to give more information in a concise way.
    For instance, one may be looking for the substring 'ready', but
    another function may look for the substring 'abort'.
    valid states:
        - starting      - ready              - aborting
        - exiting       - complete / ready   - "aborted / ready" 
    ?->    - setting up
        - executing tests
        - tearing down
    '''
    starting= "starting"
    ready= "ready"
    exiting= "exiting"
    aborting= "aborting"
    aborted_ready= "aborted / ready" 
    complete_ready= "complete / ready" 
    
class TestSequence(Thread):
    """
    The sequence or ``Test`` objects to execute.
    The TestSequence will "init" the sequence together by taking the test \
    objects and appropriately passing them through the automated testing \
    process.
    :param sequence: a list of Tests
    :param auto_run: an integer that determines how many times a test \
     sequence will be executed before stopping
    :param setup: function to call before the test sequence
    :param loglevel: the logging level

    :param archive_manager: an instance of ``ArchiveManager`` which will \
    contain the path and data_format-specific information
    :param callback: function to call on each test sequence completion; \
    callback will be required to accept one parameter, which is the \
    dictionary of values collected over that test iteration
    :param teardown: function to call after the test sequence is complete, \
    even if there was a problem; common to have safety issues addressed here
    :param on_close: function to call when the functionality is complete; \
    for instance, when a GUI closes, test hardware may need to be de-allocated
    """
    def __init__(self,
        sequence: list[Test],
        auto_run: Optional[int],
        setup: Optional[callable]= None,
        # teardown: Optional[callable] = None,
        loglevel: Optional[callable]= logging.INFO
        ):
        Thread.__init__(self)
        self._logger= logging.getLogger(self.__class__.__name__)
        self._logger.setLevel(loglevel)
        self._sequence= sequence
        self._auto_run= auto_run
        self._state= State.ready.value
        
        self._test_data = {
            "datetime": str(datetime.now()),
            "pass": True,
            "failed": [],
        }
        self._current_test_name= "test-0"
        self._current_test_number= 0 
        self._setup= setup
        self._teardown = None
        self.semaphore= Semaphore(2)        
        self._thread= Thread(target=self._run_sequence, daemon=True) #, args=(semaphoro))
        self._thread.start()   
    
    @property
    def tests(self) -> list[Test]:
        """
        Returns instances of all tests contained within the ``TestSequence``
        :return: all tests as a list
        """
        return [test for test in self._sequence]
    
    @property
    def test_names(self) -> list[Test]:
        """
        Returns instances of all test names within Test Sequence
        :return: all test names as a list
        """
        return [test.nickname for test in self._sequence]
    
    @property
    def in_progress(self) -> bool:
        """
        Returns True if the test sequence is currently in progress, else False.

        :return: True if the test sequence is currently in progress, else False
        """
        # return State.ready not in self._state
        return State.ready.value not in self._state
    @property
    def is_passing(self) -> bool:
        """
        Returns True if the test sequence is currently passing, else False
        :return: True or False
        """
        return self._test_data.get("pass")
    
    @property
    def get_state(self) -> str:
        """
        return status of the current Thread seq test"""    
        return self._state
    
#TODO
    # def ready(self) -> bool:
    # def is_aborted(self) -> bool:    
    # def failed_tests(self) -> list[str]:
    # def progress(self) -> tuple[int, int]:
    # def close(self):
           
    #private Methods
#TODO
    # def __validate_sequence(sequence: list[Test]):
       
                
    #protected Methods
    def _sequence_teardown(self): 
        """
        Finishes up a test sequence by saving data, executing teardown \
        sequence, along with user callbacks.
        :return:
        """
        if "abort" not in self._state:
            self._state = "tearing down"
        self._logger.info("-" * 80)
        self._logger.info("test sequence complete")
        self._logger.debug(f"test results: {self._test_data}")

        if self._teardown is not None:
            try:
                self._teardown()
            except Exception as e:
                self._logger.critical(
                    f"an exception has occurred which "
                    f"may result in an unsafe condition "
                    f"during sequence teardown: {e}"
                )
#TODO callback
        # if self._callback is not None:
        #     self._logger.info(
        #         f"executing user-supplied callback function " f'"{self._callback}"'
        #     )
        #     try:
        #         self._callback(self._test_data)
        #     except Exception as e:
        #         self._logger.warning(
        #             f"an exception occurred during the callback sequence: {e}"
        #         )
                
                    
    def _sequence_executing_tests(self): 
        if State.aborting.value in self._state:
            return
        
        #start test process
        for i, test in enumerate(self._sequence):
            self._current_test_number= i
            self._current_test_name= test.nickname
            self._logger.info("-" * 80)  
            try:
                test._setup(is_passing= self.is_passing)
            except Exception as e:
                self._logger.critical(f"critical error during setup of  {test} : {e}")
                self._logger.critical(str(traceback.format_exc()))
                self.abort()
                test.fail()
                                
            try:
                test._execute(is_passing= self.is_passing)
            except Exception as e:
                self._logger.critical(f"critical error during execution of  {test} : {e}")
                self._logger.critical(str(traceback.format_exc()))
                self.abort()
                test.fail()
                
            try:
                test._teardown(is_passing=self.is_passing)
            except Exception as e:
                self._logger.critical(
                    f"critical error during " f'teardown of "{test}": {e}'
                )
                self._logger.critical(str(traceback.format_exc()))
                self.abort()
                test.fail()
                
        if "abort" in self._state:
            self._test_data["pass"] = None
        
    def _sequence_setup(self):
        """
        Finishes up a test sequence by saving data, executing teardown \
        sequence, along with user callbacks.
        :return:
        """   
        if "abort" in self._state:
            return

        self._state = "setting up"
        self._logger.info("=" * 80)
        self._test_data = {
            "datetime": str(datetime.now()),
            "pass": True,
            "failed": [],
        }

        self._current_test_number = 0

        for test in self._sequence:
            test.reset()

        if self._setup is not None:
            self._setup()
                     
        
    def _run_sequence(self):
    # def _run_sequence(self, semaphore):
    # def run(self):
        """
        Runs one instance of the test sequence.
        :return: None
        """
        with self.semaphore:    
            while self._state != State.exiting.value:
                # wait until ready
                while State.ready.value in self._state:
                    if self._auto_run and "abort" not in self._state:
                        self._logger.info(
                            '"auto_run" flag is set, ' "beginning test sequence"
                        )
                        self.startTests()
                    else:
                        sleep(0.1)
                
                if self._state == "exiting":
                    self._sequence_teardown()
                    return   
                       
                self._sequence_setup()
                self._sequence_executing_tests()
                self._sequence_teardown()

                if self._auto_run:
                    self._auto_run -=1
        
                if State.aborting.value in self._state:
                    self._state = State.aborted_ready.value
                else:
                    self._state = State.complete_ready.value
            
    #public Methods
    def startTests(self) -> None:
        """
        Start a test sequence.  Will only work if a test sequence isn't already in progress.
        :return: None
        """
        if self.in_progress:
            self._logger.warning(f"cannot begin another test when test is  \
                { self._current_test_name} currently in progress")
            return
        self._state= State.starting.value

        
    def close(self) -> None:
        """
        Allows higher level code to call the close functionality.
        """
        self._state= State.exiting.value
        
    def abort(self) -> None:
        """
        Abort the current test sequence.
        :return: None
        """          
        self._state= State.aborting.value
        [test.abort() for test in self._sequence]
                

            
        