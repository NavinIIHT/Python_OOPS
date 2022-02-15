import unittest
import sys, os
sys.path.append("..")

import part_c, part_d

file_path = os.path.dirname(os.path.realpath(__file__)) + '/../output_exception_revised.txt'

class ExceptionalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(file_path,"w"):
            pass

    def test_partc_correctCalc_div_by_zero(self):

        try:
            x, y = 8.4, 0
            ob1 = part_c.MainClass(x)
            ob2 = part_c.MainClass(y)

            with open(file_path,"a") as f:
                f.write("TestPartbCorrectCalcDivByZero=True\n")
                print("TestPartbCorrectCalcDivByZero = Passed")
        except:
            with open(file_path,"a") as f:
                f.write("TestPartbCorrectCalcDivByZero=False\n")
                print("TestPartbCorrectCalcDivByZero = Failed")
                assert False

    def test_partd_div_by_zero(self):
        try:
            x, y = 8.4, 0
            m_obj = part_d.Main()
            ops = m_obj.get_operations(x, y)

            if y==0:
                assert set(ops) == set([x+y, x-y, x*y, -1, -1])
            else:
                assert set(ops) == set([x+y, x-y, x*y, x/y, x%y]) 

            with open(file_path,"a") as f:
                f.write("TestPartdDivByZero=True\n")
                print("TestPartdDivByZero = Passed")
        except:
            with open(file_path,"a") as f:
                f.write("TestPartdDivByZero=False\n")
                print("TestPartdDivByZero = Failed")
                assert False