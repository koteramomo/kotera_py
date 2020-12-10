import requests,conf

class requestMsg(conf.config):
    def login_data(self):
        url1 = conf.config.setConfig.base_url()
        data1 = conf.conf.config.setConfig.user_data()
        return url1,data1