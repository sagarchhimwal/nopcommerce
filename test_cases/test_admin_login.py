import time
import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_maker

class Test_01_Admin_Login:

    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_maker.log_gen()

    @pytest.mark.regression
    def test_title_verification(self,setup):
        self.logger.info("***********Test_01_Admin_Login**************")
        self.logger.info("***********Verification of Title*********")
        self.driver = setup
        self.driver.get(self.admin_page_url)

        act_title = self.driver.title
        print(act_title)
        time.sleep(5)
        exp_title = "nopCommerce demo store. Login"

        if act_title == exp_title:
            self.logger.info("************Test_Title_Verification Title matched**********")
            assert True
            self.driver.close()
        else:

            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("**********Title_Unmatched********")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_admin_login(self,setup):
        self.logger.info("**********Test_valid_admin_login_started*********")
        self.driver = setup
        self.driver.get(self.admin_page_url)

        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        time.sleep(10)
        act_dashboard_txt = self.driver.find_element(By.XPATH, "//div[@class= 'content-header']/h1").text

        if act_dashboard_txt == "Dashboard":
            self.logger.info("***********Valid Admin********")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.logger.info("***********Invalid Admin**********")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_invalid_admin_login(self,setup):
        self.logger.info("**************Test_Invalid_admin_Login****************")
        self.driver = setup
        self.driver.get(self.admin_page_url)

        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()

        error_message = self.driver.find_element(By.XPATH, "//li").text
        time.sleep(5)
        if error_message == "No customer account found":
            self.logger.info("***********Valid Username/email*********")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.logger.info("***************Invalid username**********")
            self.driver.close()
            assert False

