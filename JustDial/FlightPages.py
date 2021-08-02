import time
from calendar import Calendar
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException, NoSuchWindowException, NoSuchFrameException, StaleElementReferenceException
from FlightLocators import FlightLocators
from FlightData import FlightData


class BaseFlightPage():

    def __init__(self,driver):
        self.driver = driver

    def click(self,by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    def enter_keys(self,by_locator,text):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def is_enabled(self,by_locator):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))

    def is_visible(self,by_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return bool (element)

    def hover_to(self,by_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()


class FlightHomePage(BaseFlightPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(FlightData.BASE_URL)

    def select_round_trip(self):
        self.driver.find_element(*FlightLocators.RoundTrip).click()


class SelectDestinations(BaseFlightPage):

    def __init__(self, driver):
        super().__init__(driver)

    def select_destinations(self):

        self.driver.find_element(*FlightLocators.From).send_keys("Mumbai")
        self.driver.find_element(*FlightLocators.Select_Mumbai).click()
        self.driver.find_element(*FlightLocators.To).send_keys("Delhi")
        self.driver.find_element(*FlightLocators.Select_Delhi).click()


class SelectDateRange(BaseFlightPage):

    def __init__(self, driver):
        super().__init__(driver)

    def select_daterange(self):
        calendar = self.driver.find_element(*FlightLocators.select_calendar)
        calendar.click()
        picker = self.driver.find_element(*FlightLocators.DatePicker)
        actions = ActionChains(self.driver)
        actions.move_to_element(picker)
        # perform the operation on the element
        actions.perform()
        fromdate = self.driver.find_element(*FlightLocators.From_Date)
        fromdate.click()
        todate = self.driver.find_element(*FlightLocators.To_Date)
        todate.click()


class SelectPassengerInfo(BaseFlightPage):

    def __init__(self, driver):
        super().__init__(driver)

    def select_passengers(self):
        selectadult = self.driver.find_element(*FlightLocators.Adults)
        adultcount = Select(selectadult)
        adultcount.select_by_value("2")
        selectchild = self.driver.find_element(*FlightLocators.Child)
        childcount = Select(selectchild)
        childcount.select_by_value("1")


class SearchFlight(BaseFlightPage):

    def __init__(self, driver):
        super().__init__(driver)

    def search_flight(self):
        self.driver.find_element(*FlightLocators.SearchFlight).click()
        time.sleep(3)


class BookFlight(BaseFlightPage):

    def __init__(self, driver):
        super().__init__(driver)

    def book_flight(self):

        #self.driver.find_element(*FlightLocators.BookButton).click()
        parent_window_handle = self.driver.current_window_handle
        print("Parent Window Handle is - ", parent_window_handle)
        book_flight = self.driver.find_element(*FlightLocators.BookButton)
        book_flight.click()
        time.sleep(5)
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
        except NoSuchWindowException:
            print("No Such Window Present")

    def standard_fare(self):
        time.sleep(6)
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.find_element(*FlightLocators.StandardFare).click()
        self.driver.execute_script("window.scrollTo(0, 1400)")
        time.sleep(3)
        self.driver.find_element(*FlightLocators.Continue).click()
        time.sleep(3)
        self.driver.find_element(*FlightLocators.select_seats).click()


class FlightDetails(BaseFlightPage):

    def __init__(self, driver):
        super().__init__(driver)

    def select_seats(self):

        time.sleep(3)
        seats = self.driver.find_elements(*FlightLocators.Seat)
        selectseats = []
        for x in (seats):
            selectseats.append(x)
            if len(selectseats)==3:
                break
        for y in selectseats:
            y.click()

        print("hello")
        time.sleep(4)
        self.driver.find_element(*FlightLocators.Done).click()
        self.driver.find_element(*FlightLocators.SaveNextSeats).click()

    def select_meals(self):

        time.sleep(3)
        self.driver.find_element(*FlightLocators.Meals).click()
        self.driver.find_element(*FlightLocators.MealsNext).click()
        self.driver.find_element(*FlightLocators.Next_menu).click()
        self.driver.find_element(*FlightLocators.MealsDone).click()
        self.driver.find_element(*FlightLocators.SaveNext).click()

    def select_baggage(self):

        time.sleep(3)
        self.driver.find_element(*FlightLocators.Baggage).click()
        self.driver.find_element(*FlightLocators.AddedLuggage).click()
        self.driver.find_element(*FlightLocators.LuggageDone).click()
        self.driver.find_element(*FlightLocators.SaveAndExit).click()
        self.driver.find_element(*FlightLocators.ContinueAfterLuggage).click()

    def contact_details(self):
        time.sleep(4)
        self.driver.find_element(*FlightLocators.MobileNumber).send_keys("9096914627")
        self.driver.find_element(*FlightLocators.Email).send_keys("isha.rth@gmail.com")
        time.sleep(3)
        self.driver.find_element(*FlightLocators.ContinueAfterContact).click()

    def traveler_details(self):
        time.sleep(3)
        self.driver.find_element(*FlightLocators.Adult1FN).send_keys("Mark")
        self.driver.find_element(*FlightLocators.Adult1LN).send_keys("Zuck")

        self.driver.find_element(*FlightLocators.Adult1G).click()
        self.driver.find_element(*FlightLocators.GenderM).click()

        self.driver.find_element(*FlightLocators.Adult2FN).send_keys("Mary")
        self.driver.find_element(*FlightLocators.Adult2LN).send_keys("Lane")

        self.driver.find_element(*FlightLocators.Adult2G).click()
        self.driver.find_element(*FlightLocators.GenderF).click()

        self.driver.find_element(*FlightLocators.ChildFN).send_keys("Rob")
        self.driver.find_element(*FlightLocators.ChildLN).send_keys("Zuck")

        self.driver.find_element(*FlightLocators.ChildG).click()
        self.driver.find_element(*FlightLocators.GenderM).click()

        self.driver.find_element(*FlightLocators.BirthD).send_keys("01/01/2012")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 3000)")
        try :
            a = self.driver.find_element_by_xpath("//label/p[contains(text(),'Use GSTIN details for this booking')]/parent::label/following-sibling::div[3]/div/button")
            time.sleep(2)
            a.click()

        except StaleElementReferenceException as e :
            raise e





























































