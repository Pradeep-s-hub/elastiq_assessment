from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TableSearch:
    search_box_xpath = "//div[@id='example_filter']/label/input"
    rows = "//table[@id='example']/tbody/tr"
    def __init__(self,driver):
        self.driver = driver
    def search_box(self,search_value):
        self.driver.find_element(By.XPATH,self.search_box_xpath).send_keys(search_value)
    def rows_items(self):
        rows_ele = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,self.rows)))
        return rows_ele







