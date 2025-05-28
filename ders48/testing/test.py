# Testing is a per production phase of developing
import unittest
import main # test edecegimiz dosyanin ismi



# class TestMain(unittest.TestCase):
#     def test_do_stuff(self):
#         test_param = 10
#         result = main.do_stuff(test_param) # here results comes from our main.py file
#         self.assertEqual(result,15)



# unittest.main()

# # Beklenen cikti:
# # ----------------------------------------------------------------------
# # Ran 1 test in 0.000s

# # OK


# -----------------if-we-change-15-to-anything-else--------------

# class TestMain(unittest.TestCase):
#     def test_do_stuff(self):
#         test_param = 10
#         result = main.do_stuff(test_param) # here results comes from our main.py file
#         self.assertEqual(result,20)



# unittest.main()


#cikti:

# F
# ======================================================================
# FAIL: test_do_stuff (__main__.TestMain.test_do_stuff)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/Users/mamooth/Desktop/sql/testing/test.py", line 30, in test_do_stuff
#     self.assertEqual(result,20)
#     ~~~~~~~~~~~~~~~~^^^^^^^^^^^
# AssertionError: 15 != 20 ❌

# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# FAILED (failures=1)



# ======================================

# 2
# class TestMain(unittest.TestCase):
#     def test_do_stuff(self):
#         test_param = 10
#         result = main.do_stuff(test_param) # here results comes from our main.py file
#         self.assertEqual(result,15)

#     # bu durumda bizim test.py fail aliyor ,main.py degil
#     def test_do_stuff(self):
#         test_param = 'lkdjflksjfd'
#         result = main.do_stuff(test_param) # here results comes from our main.py file
#         self.assertEqual(result,ValueError)


# unittest.main()


# bu durumda ValueError aliriz ama bu hala bir insertion error degil
# E
# ======================================================================
# ERROR: test_do_stuff (__main__.TestMain.test_do_stuff)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/Users/mamooth/Desktop/sql/testing/test.py", line 68, in test_do_stuff
#     result = main.do_stuff(test_param) # here results comes from our main.py file
#   File "/Users/mamooth/Desktop/sql/testing/main.py", line 9, in do_stuff
#     return int(num) + 5
#            ~~~^^^^^
# ValueError: invalid literal for int() with base 10: 'lkdjflksjfd'

# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# FAILED (errors=1


# ====================================
# 3


# class TestMain(unittest.TestCase):
#     def test_do_stuff(self):
#         test_param = 10
#         result = main.do_stuff(test_param) # here results comes from our main.py file
#         self.assertEqual(result,15)

#     # bu durumda bizim test.py fail aliyor ,main.py degil
#     def test_do_stuff(self):
#         test_param = 'lkdjflksjfd'
#         result = main.do_stuff(test_param) # here results comes from our main.py file
#         self.assertEqual(result,ValueError)


# unittest.main()


# this time we'll get the assertionError

# F
# ======================================================================
# FAIL: test_do_stuff (__main__.TestMain.test_do_stuff)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/Users/mamooth/Desktop/sql/testing/test.py", line 108, in test_do_stuff
#     self.assertEqual(result,ValueError)
#     ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
# AssertionError: ValueError("invalid literal for int() with base 10: 'lkdjflksjfd'") != <class 'ValueError'>

# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# FAILED (failures=1)

# ====================================

# 4 - to fix this test we should use assertTrue
# cunku result bu durumda kendisi ValueError degil , ValueError ornegidir(instance)


# class TestMain(unittest.TestCase):
#     def test_do_stuff(self):
#         test_param = 10
#         result = main.do_stuff(test_param) # here results comes from our main.py file
#         self.assertEqual(result,15)

#     # bu durumda bizim test.py fail aliyor ,main.py degil
#     def test_do_stuff(self):
#         test_param = 'lkdjflksjfd'
#         result = main.do_stuff(test_param) # here results comes from our main.py file
#         # self.assertTrue(isinstance(result,ValueError))
#         self.assertIsInstance(result,ValueError)
        


# unittest.main()


# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK

# ======================================

# 5

class TestMain(unittest.TestCase):
    def test_do_stuff1(self):
        test_param = 10
        result = main.do_stuff(test_param) # here results comes from our main.py file
        self.assertEqual(result,15)

    # bu durumda bizim test.py fail aliyor ,main.py degil
    def test_do_stuff2(self):
        test_param = 'lkdjflksjfd'
        result = main.do_stuff(test_param) # here results comes from our main.py file
        # self.assertTrue(isinstance(result,ValueError))
        self.assertIsInstance(result,ValueError)
    
    def test_do_stuff3(self):        
        test_param = None
        result = main.do_stuff(test_param) 
        self.assertEqual(result,"enter a number")
    

unittest.main() #buradaki main dosyayla bir alakasi yok.
