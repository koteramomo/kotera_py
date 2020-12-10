import test_case.test_login,conf,common
import unittest

class running(test_case.test_login.loginRequest):
    def login(self):
       test_case.test_login.loginRequest.test_post(1)
       print("abc")

if __name__ == '__main__':
    unittest.main()