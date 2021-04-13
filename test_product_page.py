import time
import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage



@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
##                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
##                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
##                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
##                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
##                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
##                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
##                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
##                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
##                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
            
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    alert = self.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    print("x="+x)
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    time.sleep(60)
##    
##    try:
##        alert = self.browser.switch_to.alert
##        alert_text = alert.text
##        print(f"Your code: {alert_text}")
##        alert.accept()
##    except NoAlertPresentException:
##        print("No second alert presented")




        ##    product = page.get_product_name_and_price()
##    page.add_to_basket()
##    page.should_be_added_to_basket(product.get('product_name'))
##    page.should_be_product_price(product.get('product_price'))

##
##@pytest.mark.need_review
##def test_guest_can_go_to_login_page_from_product_page(browser):
##    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
##    page = ProductPage(browser, link)
##    page.open()
##    page.go_to_login_page()
##    login_page = LoginPage(browser, browser.current_url)
##    login_page.should_be_login_page()
##
##
##@pytest.mark.need_review
##def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
##    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
##    page = ProductPage(browser, link)
##    page.open()
##    page.go_to_basket_page()
##    page = BasketPage(browser, browser.current_url)
##    page.should_be_no_items_in_basket()
##    page.should_be_text_empty_basket()
##
##
##def test_guest_cant_see_success_message(browser):
##    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear2019"
##    page = ProductPage(browser, link)
##    page.open()
##    page.should_not_be_success_message()
##
##
##@pytest.mark.xfail(reason="invalid test case")
##def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
##    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear2019"
##    page = ProductPage(browser, link)
##    page.open()
##    page.add_to_basket()
##    page.should_not_be_success_message()
##
##
##def test_guest_should_see_login_link_on_product_page(browser):
##    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
##    page = ProductPage(browser, link)
##    page.open()
##    page.should_be_login_link()
##
##
##@pytest.mark.xfail(reason="invalid test case")
##def test_message_disappeared_after_adding_product_to_basket(browser):
##    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear2019"
##    page = ProductPage(browser, link)
##    page.open()
##    page.add_to_basket()
##    page.should_be_disappeared()


##@pytest.mark.user_basket
##class TestUserAddToBasketFromProductPage():
####    @pytest.fixture(scope="function", autouse=True)
##    def setup(self, browser):
##        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
##        page = LoginPage(browser, link)
##        page.open()
##        email = str(time.time()) + "@fakemail.org"
##        password = str(time.time())
##        page.register_new_user(email, password)
##        page.should_be_authorized_user()
##
##    @pytest.mark.need_review
##    def test_user_can_add_product_to_basket(self, browser):
##        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear2019"
##        page = ProductPage(browser, link)
##        page.open()
##        product = page.get_product_name_and_price()
##        page.add_to_basket()
##        page.should_be_added_to_basket(product.get('product_name'))
##        page.should_be_product_price(product.get('product_price'))
##
##    def test_user_cant_see_success_message(self, browser):
##        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear2019"
##        page = ProductPage(browser, link)
##        page.open()
##        page.should_not_be_success_message()
