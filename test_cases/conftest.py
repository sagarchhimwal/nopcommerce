import pytest
import undetected_chromedriver as uc
from selenium import webdriver
#from pytest_metadata import metadata_key


##########for pytest html reports ############
##hook for adding environment info in html reports


# def pytest_configure(config):
#      config.stash[metadata_key] ['Project name'] = 'Ecommerce Project, nopcommerce'
#      config.stash[metadata_key] ['Test Module name'] = 'Admin Login Tests'
#      config.stash[metadata_key] ['Tester Name'] = "Sagar"

####hook for delete/modify environment info in html report.
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('Plugins', None)
    metadata.pop('Platform', None)




@pytest.fixture()
def browser(request):
    return request.config.option("--browser")








@pytest.fixture()
def setup():
    driver = uc.Chrome()
    return driver








