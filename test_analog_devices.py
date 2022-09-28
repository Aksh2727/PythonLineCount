""" Importing Modules"""
import unittest
# pylint: disable=E1120

from analog_devices import line_count_func

class TestCountFunction(unittest.TestCase):
    """ Testing class"""
    def test_line_count_func(self):
        """ Testing function"""
        list_to_check = ['./folder_1/file1.txt : 6', './folder_1/folder_2/file2.txt : 0',
        './folder_1/folder_2/file3.txt : 1', './folder_1/folder_3/file4.txt : 3',
        'Number of files found : 4', 'Total number of lines : 10', 'Average lines per file : 2.50']



        self.assertEqual(line_count_func('',),['No file present'])
        self.assertEqual(line_count_func('','.txt'),['No file present'])
        self.assertEqual(line_count_func('.',),list_to_check)
        self.assertEqual(line_count_func('.','.txt'),list_to_check)
        with self.assertRaises(TypeError):
            line_count_func()
