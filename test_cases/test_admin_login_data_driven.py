from selenium.webdriver.common.by import By

from utilities.custom_logger import Log_maker
from utilities.read_properties import Read_Config


class Test_02_Admin_Login_data_driven:
    admin_page_url = Read_Config.get_admin_page_url()
    logger = Log_maker.log_gen()


