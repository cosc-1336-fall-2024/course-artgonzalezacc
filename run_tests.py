import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
#from tests.examples.b_input_process_output import tests_input_process_output
from tests.examples.f_files_exception import tests_files_exception

suite = unittest.TestLoader().loadTestsFromModule(tests_files_exception)
unittest.TextTestRunner(verbosity=2).run(suite)
