# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact
import os


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(300)

    def test_add_contact(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_contact_page(wd)
        self.add_personal_information(wd, Contact(first_name="alex",
                                      middle_name="wellington",
                                      last_name="Andressen",
                                      nickname="Andy",
                                      title="test",
                                      company="wb",
                                      address="SPb",
                                      home="home",
                                      mobile="secret",
                                      work="QA",
                                      fax="none_none",
                                      email_1="dmitriydzd@gmail.com",
                                      email_2="dmitriydzk@gmail.com",
                                      email_3="dmitrosnachos@gmail.com",
                                      homepage="yandex.ru",
                                      day_of_birth="30",
                                      month_of_birth="June",
                                      year_of_birth="1997",
                                      anniversary_day="30",
                                      anniversary_month="June",
                                      anniversary_year="2027"))
        self.sumbit_contact_creation(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")
    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def add_personal_information(self, wd, contact):
        # name fields
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # photo field not used - doesn't work
        # wd.find_element_by_name('photo').send_keys(os.getcwd() + '/testy.jpg')
        # contact information
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").send_keys(contact.fax)
        # email fields
        wd.find_element_by_name("email").send_keys(contact.email_1)
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("email3").send_keys(contact.email_3)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # date of birth field
        wd.find_element_by_name("bday").send_keys(contact.day_of_birth)
        wd.find_element_by_name("bmonth").send_keys(contact.month_of_birth)
        wd.find_element_by_name("byear").send_keys(contact.year_of_birth)
        # anniversary field
        wd.find_element_by_name("aday").send_keys(contact.anniversary_day)
        wd.find_element_by_name("amonth").send_keys(contact.anniversary_month)
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        wd.find_element_by_name("theform").click()

    def test_add_empty_contact(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_contact_page(wd)
        self.add_personal_information(wd, Contact(first_name="",
                                      middle_name="",
                                      last_name="",
                                      nickname="",
                                      title="",
                                      company="",
                                      address="",
                                      home="",
                                      mobile="",
                                      work="",
                                      fax="",
                                      email_1="",
                                      email_2="",
                                      email_3="",
                                      homepage="",
                                      day_of_birth="",
                                      month_of_birth="",
                                      year_of_birth="",
                                      anniversary_day="",
                                      anniversary_month="",
                                      anniversary_year=""))
        self.sumbit_contact_creation(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def sumbit_contact_creation(self, wd):
        wd.find_element_by_name("submit").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
