from selenium.common.exceptions import NoAlertPresentException # ג םאקאכו פאיכא

def solve_quiz_and_get_code(self):
    alert = self.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")
        

def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    product = page.get_product_name_and_price()
    page.add_to_basket()
    page.should_be_added_to_basket(product.get('product_name'))
    page.should_be_product_price(product.get('product_price'))

