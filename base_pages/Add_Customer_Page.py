



class Add_Customer_Page:

    #locators from add customer page
    link_customers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_menuoption_xpath = "//li[@class='nav-item']//p[normalize-space(text())='Customer']"
    link_add_new_xpath = "//a[@class='btn btn-primary']"
    text_email_id = "//input[@id='Email']"
    text_password_id = "//input[@id='Password']"
    text_first_name_id = "//input[@id='FirstName']"
