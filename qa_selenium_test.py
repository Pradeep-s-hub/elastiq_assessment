import pytest
from tableSearchObj import TableSearch
class Test_SeleniumPlayGround:
    @pytest.mark.parametrize('city',[("New York")])
    def test_city_results(self,setup,city):
        '''This testcase send "New York" to searchbox and validate number of rows'''
        self.driver = setup
        self.driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
        table_page_obj = TableSearch(self.driver)
        table_page_obj.search_box(city)
        new_york_elements = len(table_page_obj.rows_items())
        if new_york_elements == 5:
            print(f"The office's location  with {city} is", str(new_york_elements))
        else:
            raise Exception(f"The office's location with {city} should be 5 but, we got ", str(new_york_elements))
        self.driver.close()
        self.driver.quit()