#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 8:34
# @Author  : qiubin
# @File    : baidu_test.py
# @Software: PyCharm
import unittest
import os
import time
from selenium import webdriver


class Baidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = 'http://uatcas.cre.com.hk/dmp-fresh-frontend'
        cls.driver = webdriver.Chrome(executable_path="D:\\chromedriver\\chromedriver.exe")
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def setUp(self):
    #     self.url = 'http://devcas.cre.com.hk/osp-mtmsg-front/#/login'
    #     self.driver = webdriver.Chrome(executable_path="D:\\chromedriver\\chromedriver.exe")
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(10)
    #
    # def tearDown(self):
    #     self.driver.close()

    def test_login(self):
        driver = self.driver
        time.sleep(10)
        driver.find_element_by_name('username').clear()
        driver.find_element_by_name('username').send_keys('chenxiaojun56')
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys('cxj123456')
        driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/button').click()
        id_element = driver.find_element_by_xpath('//*[@id="app"]/div/ul/div[3]/div/p')
        print(driver.title)
        self.assertEqual(id_element.text, "欢迎您：水产系统管理员!", msg='登录账号不正确')


