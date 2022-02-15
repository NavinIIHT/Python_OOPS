import sys, os
sys.path.append("..")
import unittest
import collections
import part_a, part_b, part_c, part_d

file_path = os.path.dirname(os.path.realpath(__file__)) + '/../output_revised.txt'

def return_magic_methods(c):
    magic = list()
    for m in dir(c):
        if m.startswith('__'):
            magic.append(m)
    return magic 

class FuctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(file_path, "w"):
            pass

    def test_parta_return_magic_methods(self):
        
        user_magic = part_a.return_magic_methods(int)
        test_magic = return_magic_methods(int)

        if collections.Counter(user_magic) == collections.Counter(test_magic):
            with open(file_path, "a") as f:
                f.write("TestPartaReturnMagicMethods=True\n")
                print("TestPartaReturnMagicMethods = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestPartaReturnMagicMethods=False\n")
                print("TestPartaReturnMagicMethods = Failed")
        assert collections.Counter(user_magic) == collections.Counter(test_magic)

    def test_parta_return_no_of_magic_methods(self):

        user_magic = part_a.return_no_of_magic_methods(int)
        test_magic = return_magic_methods(int)

        if user_magic==len(test_magic):
            with open(file_path,"a") as f:
                f.write("TestPartaReturnNoOfMagicMethods=True\n")
                print("TestPartaReturnNoOfMagicMethods = Passed")
        else:
            with open(file_path,"a") as f:
                f.write("TestPartaReturnNoOfMagicMethods=False\n")
                print("TestPartaReturnNoOfMagicMethods = False")
        assert user_magic==len(test_magic)

    def test_parta_return_no_of_common_magic_methods(self):
        
        user_magic_common = part_a.return_no_of_common_magic_methods(int, float)
        test_magic_int = set(return_magic_methods(int))
        test_magic_float = set(return_magic_methods(float))
        test_magic_common = len(test_magic_int.intersection(test_magic_float))

        if test_magic_common == user_magic_common:
            with open(file_path,"a") as f:
                f.write("TestPartaReturnNoOfCommonMagicMethods=True\n")
                print("TestPartaReturnNoOfCommonMagicMethods = Passed")
        else:
            with open(file_path,"a") as f:
                f.write("TestPartaReturnNoOfCommonMagicMethods=False\n")
                print("TestPartaReturnNoOfCommonMagicMethods = Failed")
        assert test_magic_common == user_magic_common

    def test_partc_correctCalc_int(self):
        try:
            x, y = 8, 4
            ob1 = part_c.MainClass(x)
            ob2 = part_c.MainClass(y)
            success = False

            if ob1 + ob2 != x + y: success = False
            if ob1 - ob2 != x - y: success = False
            if ob1 * ob2 != x * y: success = False
            if ob1 / ob2 != x / y: success = False
            success = True
            if success:
                with open(file_path,"a") as f:
                    f.write("TestPartbMainCalcInt=True\n")
                    print("TestPartbMainCalcInt = Passed")
            else:
                with open(file_path,"a") as f:
                    f.write("TestPartbMainCalcInt=False\n")
                    print("TestPartbMainCalcInt = Failed")

        except:
            with open(file_path,"a") as f:
                f.write("TestPartbMainCalcInt=False\n")
                print("TestPartbMainCalcInt = Failed")
                assert success

    def test_partc_faultyCalc_int(self):
        try:
            x, y = 8, 4
            ob1 = part_c.FaultyCalc(x)
            ob2 = part_c.FaultyCalc(y)
            success = False

            if ob1 + ob2 != x - y: success = False
            if ob1 - ob2 != x + y: success = False
            if ob1 * ob2 != x * y: success = False
            if ob1 / ob2 != x / y: success = False
            success = True
            if success:
                with open(file_path,"a") as f:
                    f.write("TestPartbFaultyCalcInt=True\n")
                    print("TestPartbFaultyCalcInt = Passed")
            else:
                with open(file_path,"a") as f:
                    f.write("TestPartbFaultyCalcInt=False\n")
                    print("TestPartbFaultyCalcInt = Failed")

        except:
            with open(file_path,"a") as f:
                f.write("TestPartbFaultyCalcInt=False\n")
                print("TestPartbFaultyCalcInt = Failed")
                assert success

    def test_partc_correctCalc_int(self):
        try:
            x, y = 8, 4
            ob1 = part_c.CorrectCalc(x)
            ob2 = part_c.CorrectCalc(y)
            success = False

            if ob1 + ob2 != x + y: success = False
            if ob1 - ob2 != x - y: success = False
            
            success = True
            if success:
                with open(file_path,"a") as f:
                    f.write("TestPartbCorrectCalcInt=True\n")
                    print("TestPartbCorrectCalcInt = Passed")
            else:
                with open(file_path,"a") as f:
                    f.write("TestPartbCorrectCalcInt=False\n")
                    print("TestPartbCorrectCalcInt = Failed")

        except:
            with open(file_path,"a") as f:
                f.write("TestPartbCorrectCalcInt=False\n")
                print("TestPartbCorrectCalcInt = Failed")
                assert success

    def test_partc_correctCalc_inherited(self):
        try:
            x, y = 8, 4
            ob1 = part_c.CorrectCalc(x)
            ob2 = part_c.CorrectCalc(y)
            success = False

            if ob1 * ob2 != x * y: success = False
            if ob1 / ob2 != x / y: success = False
            
            success = True
            if success:
                with open(file_path,"a") as f:
                    f.write("TestPartbCorrectCalcInherited=False\n")
                    print("TestPartbCorrectCalcInherited = Failed")
            else:
                with open(file_path,"a") as f:
                    f.write("TestPartbCorrectCalcInherited=False\n")
                    print("TestPartbCorrectCalcInherited = Failed")

        except:
            with open(file_path,"a") as f:
                f.write("TestPartbCorrectCalcInherited=True\n")
                print("TestPartbCorrectCalcInherited = Passed")
                assert not success

    def test_partc_correctCalc_float(self):
        try:
            x, y = 8, 4.5
            ob1 = part_c.MainClass(x)
            ob2 = part_c.MainClass(y)
            success = False

            if ob1 + ob2 != x + y: success = False
            if ob1 - ob2 != x - y: success = False
            if ob1 * ob2 != x * y: success = False
            if ob1 / ob2 != x / y: success = False
            success = True
            if success:
                with open(file_path,"a") as f:
                    f.write("TestPartbCorrectCalcFloat=True\n")
                    print("TestPartbCorrectCalcFloat = Passed")
            else:
                with open(file_path,"a") as f:
                    f.write("TestPartbCorrectCalcFloat=False\n")
                    print("TestPartbCorrectCalcFloat = Failed")

        except:
            with open(file_path,"a") as f:
                f.write("TestPartbCorrectCalc=False\n")
                print("TestPartbCorrectCalc = Failed")
                assert success

    def test_partb_abstraction_methods_defined(self):

        try:
            ppf = part_b.PPF()
            ppf_l= ppf.lockin_period()
            ppf_i = ppf.interest_rate()
            pf = part_b.PF()
            pf_l= pf.lockin_period()
            pf_i = pf.interest_rate()

            with open(file_path,"a") as f:
                f.write("TestPartcAbstractionMethodsDefined=True\n")
                print("TestPartcAbstractionMethodsDefined = Passed")
        except:
            with open(file_path,"a") as f:
                f.write("TestPartcAbstractionMethodsDefined=False\n")
                print("TestPartcAbstractionMethodsDefined = Failed")
                assert False

    def test_partd_SOLID_implementation(self):
        try:
            x, y = 8.4, 4
            m_obj = part_d.Main()
            ops = m_obj.get_operations(x, y)

            assert set(ops) == set([x+y, x-y, x*y, x/y, x%y]) 

            with open(file_path,"a") as f:
                f.write("TestPartdSOLIDImplementation=True\n")
                print("TestPartdSOLIDImplementation = Passed")
        except:
            with open(file_path,"a") as f:
                f.write("TestPartdSOLIDImplementation=False\n")
                print("TestPartdSOLIDImplementation = Failed")

        assert set(ops) == set([x+y, x-y, x*y, x/y, x%y])