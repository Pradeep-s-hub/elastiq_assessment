# elastiq_assessment
### using below cmd to Run the script:
  - pytest .\qa_selenium_test.py -s -v
### Project info
  - Used pytest framework with page object model approch
  - Programming language used Python
### what it do
  - Navigates to the[Selenium Playground Table Search Dem](https://www.lambdatest.com/selenium-playground/table-sort-search-demo).
  - Locates and interacts with the search box to search for "New York".
  - Validates that the search results show 5 entries out of 24 total entries.
### qa_selenium_test.py
  - This file contains Test_SeleniumPlayGround class and test_city_results method in it.
  - test_city_results is a instance method which takes below two peraamater:
     - **setup:** which is already taken from **conftest.py** file
     - **city:** which is passed form  @pytest.mark.parametrize('city',[("New York")])
  -  Created object for class **TableSearch** which is imported from tableSearchObj.py and used methods in this class.
  -  Send "New York" to searchbox and validate number of rows
### conftest.py file
   - This file contains setup part which can be used if any other file if we include in feature.
### pytest.ini
  -  we used to ignore warnings
  -  We can also include diffrent markers and for ordering and grouping testcases
### testSearchObj.py
  - Created different methods that have diffrent methods which can access diffrent elements in search page. 
  
