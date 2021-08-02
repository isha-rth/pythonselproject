import unittest
from selenium import webdriver
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir + r'\resources')
sys.path.insert(0, parentdir + r'\resources\PO')
from FlightData import FlightData
from FlightLocators import FlightLocators
from FlightPages import FlightHomePage, SelectDestinations, SelectDateRange, SelectPassengerInfo, SearchFlight,BookFlight,FlightDetails


class Test_ClearTrip_Url(unittest.TestCase):

    def setUp(self):

        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(FlightData.CHROME_EXECUTABLE_PATH, options=chrome_options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class Test_ClearTrip(Test_ClearTrip_Url):

    def setUp(self):
        super().setUp()

    def test_home_page_loaded_successfully(self):
        self.homePage = FlightHomePage(self.driver)
        self.assertIn(FlightData.HOME_PAGE_TITLE, self.homePage.driver.title)

    def test_user_should_be_able_to_selectTrip(self):
        self.homePage = FlightHomePage(self.driver)
        self.homePage.select_round_trip()

    def test_user_should_be_able_to_select_destinations(self):
        self.homePage = FlightHomePage(self.driver)
        self.homePage.select_round_trip()
        self.destinations = SelectDestinations(self.driver)
        self.destinations.select_destinations()

    def test_user_should_be_able_to_select_dates(self):
        self.homePage = FlightHomePage(self.driver)
        self.homePage.select_round_trip()
        self.destinations = SelectDestinations(self.driver)
        self.destinations.select_destinations()
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.daterange = SelectDateRange(self.driver)
        self.daterange.select_daterange()

    def test_user_should_be_able_to_select_passengerinfo(self):
        self.homePage = FlightHomePage(self.driver)
        self.homePage.select_round_trip()
        self.destinations = SelectDestinations(self.driver)
        self.destinations.select_destinations()
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.daterange = SelectDateRange(self.driver)
        self.daterange.select_daterange()
        self.passengerinfo = SelectPassengerInfo(self.driver)
        self.passengerinfo.select_passengers()

    def test_searchflight(self):
        self.homePage = FlightHomePage(self.driver)
        self.homePage.select_round_trip()
        self.destinations = SelectDestinations(self.driver)
        self.destinations.select_destinations()
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.daterange = SelectDateRange(self.driver)
        self.daterange.select_daterange()
        self.passengerinfo = SelectPassengerInfo(self.driver)
        self.passengerinfo.select_passengers()
        self.searchflight = SearchFlight(self.driver)
        self.searchflight.search_flight()
        self.assertTrue(self.searchflight.is_visible(FlightLocators.pageassertion))

    def test_bookbutton(self):
        self.homePage = FlightHomePage(self.driver)
        self.homePage.select_round_trip()
        self.destinations = SelectDestinations(self.driver)
        self.destinations.select_destinations()
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.daterange = SelectDateRange(self.driver)
        self.daterange.select_daterange()
        self.passengerinfo = SelectPassengerInfo(self.driver)
        self.passengerinfo.select_passengers()
        self.searchflight = SearchFlight(self.driver)
        self.searchflight.search_flight()
        self.assertTrue(self.searchflight.is_visible(FlightLocators.pageassertion))
        self.book = BookFlight(self.driver)
        self.book.book_flight()

    def test_flight_details(self):
        self.homePage = FlightHomePage(self.driver)
        self.homePage.select_round_trip()
        self.destinations = SelectDestinations(self.driver)
        self.destinations.select_destinations()
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.daterange = SelectDateRange(self.driver)
        self.daterange.select_daterange()
        self.passengerinfo = SelectPassengerInfo(self.driver)
        self.passengerinfo.select_passengers()
        self.searchflight = SearchFlight(self.driver)
        self.searchflight.search_flight()
        self.assertTrue(self.searchflight.is_visible(FlightLocators.pageassertion))
        self.book = BookFlight(self.driver)
        self.book.book_flight()
        self.book.standard_fare()
        self.flightdetails = FlightDetails(self.driver)
        self.flightdetails.select_seats()
        self.flightdetails.select_meals()
        self.flightdetails.select_baggage()
        self.flightdetails.contact_details()
        self.flightdetails.traveler_details()
        self.assertTrue(self.flightdetails.is_visible(FlightLocators.PaymentAssert))










