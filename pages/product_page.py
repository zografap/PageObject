from .base_page import BasePage
from .locators import ProductPageLocators

class PageObject(BasePage):
   def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()
        BasePage.solve_quiz_and_get_code(self) 
          
