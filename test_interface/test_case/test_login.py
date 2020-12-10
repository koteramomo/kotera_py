import requests,unittest
import conf.config,common



class loginRequest(conf.config.setConfig,unittest.TestCase):
    # 登录接口路径
    def test_url(self):
        host = conf.config.setConfig.base_url(1)
        endpoint = 'login.json'
        url_login = ''.join([host, endpoint])
        return url_login

    # case1：正确用户名+正确密码
    def test_case1(self):
        correct_data = conf.config.setConfig.user_data(1)
        res_login = requests.post(loginRequest.test_url(1),correct_data)
        print('response:',res_login.json())
        try:
            self.assertEqual(res_login.status_code,200,"登录失败")and self.assertIn('token',res_login.json(),'登录失败')
            print("case1 success")
        except(RuntimeError,TypeError,ConnectionError):
            pass
        except:
            print("case1 fail")

    # case2：正确用户名+错误密码
    def test_case2(self):
        res_login2 = requests.post(loginRequest.test_url(1),'a123456')
        print('case2返回:',res_login2.json())
        try:
            self.assertIn('token', res_login2.json()) and self.assertIn('displayName',res_login2.json(),'login failed')
            print("case2 success")
        except(RuntimeError, TypeError, ConnectionError):
            pass
        except:
            print("case2 fail")

    # case3：错误用户名+错误密码
    def test_case3(self):
        res_login3 = requests.post(loginRequest.test_url(1), 'a123456')
        print('case3返回:', res_login3.json())

        try:
            self.assertIn('token', res_login3.json())
            print("case3 success")
        except(RuntimeError, TypeError, ConnectionError):
            pass
        except:
            print("case3 fail")


