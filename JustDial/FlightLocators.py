from selenium.webdriver.common.by import By

class FlightLocators():

    RoundTrip = (By.XPATH,"//div/p[@class='fs-3 fw-600 c-neutral-900'][contains(text(),'Round trip')]")
    From = (By.XPATH,"//div/input[@class='field bw-1 bs-solid w-100p p-2 box-border br-4 fs-2 c-neutral-900 h-8 "
                     "bc-neutral-100 c-neutral-900 focus:bc-secondary-500 flex flex-middle flex-between t-all fs-2 "
                     "focus:bc-secondary-500 bg-transparent bc-neutral-100 pr-2 pl-3 pt-2 pb-2 ba br-4 h-8 null']")
    Suggestions = (By.XPATH,"//div[@class='bg-white br-4 elevation-5 p-1 p-absolute mt-1 z-50 l-0']")
    To = (By.XPATH,"//div/input[@class='field bw-1 bs-solid w-100p p-2 box-border br-4 fs-2 c-neutral-900 h-8 bc-neutral-100 "
                   "c-neutral-900 focus:bc-secondary-500 flex flex-middle flex-between t-all fs-2 focus:bc-secondary-500 bg-transparent"
                   " bc-neutral-100 pr-2 pl-3 pt-2 pb-2 ba br-4 h-8']")

    DatePicker = (By.XPATH,"//div[@class='bg-white br-4 elevation-5 p-1 p-absolute mt-1 z-50 l-0 t-8']")

    Select_Mumbai = (By.XPATH,"//li/p[@class='to-ellipsis o-hidden ws-nowrap c-inherit fs-3'][contains(text(),'Mumbai')]")

    Select_Delhi = (By.XPATH,"//li/p[@class='to-ellipsis o-hidden ws-nowrap c-inherit fs-3'][contains(text(),'Delhi')]")

    select_calendar = (By.XPATH,"//div/button[@class='flex flex-middle flex-between t-all fs-2 focus:bc-secondary-500 bg-transparent bc-neutral-100 c-pointer pr-2 pl-3 pt-2 pb-2 ba br-4 h-8 c-neutral-900']/preceding-sibling::button")

    #select_calendar = (By.XPATH,"//div[@class='flex flex-middle p-relative homeCalender']")

    From_Date = (By.XPATH,"//div[@aria-label='Sat Aug 07 2021']")
    To_Date = (By.XPATH,"//div[@aria-label='Mon Aug 09 2021']")
    Adults = (By.XPATH,"//div/h4[contains(text(),'Adults')]//following-sibling::select")
    Child = (By.XPATH,"//div/h4[contains(text(),'Children')]//following-sibling::select")

    SearchFlight = (By.XPATH,"//div/button[@class='px-7 bg-primary-500 hover:bg-primary-600 c-white bc-transparent c-pointer w-100p py-2 px-5 h-10 fs-4 fw-600 t-all button bs-solid tp-color td-500 bw-1 br-4 lh-solid box-border']")

    pageassertion = (By.XPATH,"//div/input[@value='BOM - Mumbai, IN ']")

    BookButton = (By.XPATH,"//div/button[@class='bg-primary-500 hover:bg-primary-600 c-white bc-transparent c-pointer py-1 px-3 h-8 fs-3 fw-600 t-all button bs-solid tp-color td-500 bw-1 br-4 lh-solid box-border']")

    StandardFare = (By.XPATH,"//div/div[@data-testid='fareCard0']")

    Continue = (By.XPATH,"//div[@class='d-inline-block']")

    select_seats = (By.XPATH,"//div[contains(text(),'Choose the seat you want')]/parent::div/following-sibling::div/button")

    SeatAssert = (By.XPATH,"//div/div[contains(text(),'Need extra legroom? Choose your seats now')]")

    Seat = (By.XPATH,"//div/div[@style='border-width: 0.5px; background-color: rgb(164, 205, 255);']")


    Next = (By.XPATH,"//button[@class='px-5 bg-secondary-500 hover:bg-secondary-600 c-white bc-transparent c-pointer py-1 px-3 h-8 fs-3 fw-600 t-all button bs-solid tp-color td-500 bw-1 br-4 lh-solid box-border']")


    Done = (By.XPATH,"//div/button[@class='px-5 bc-secondary-500 hover:bc-secondary-600 c-secondary-500 hover:c-secondary-600 bg-transparent c-pointer py-1 px-3 h-8 fs-3 fw-600 t-all button bs-solid tp-color td-500 bw-1 br-4 lh-solid box-border']")

    SaveNextSeats = (By.XPATH,"//div/span[@class='fs-2 c-secondary-300 ml-6 fw-500 c-pointer hover:td-underline']")

    Meals = (By.XPATH,"//div[contains(text(),'Add delicious meals')]/parent::div/following-sibling::div/button")

    select_menu = (By.XPATH,"//div[@class='flex flex-right']/*[name()='svg'][@data-testid='incrementCoconut water']")


    MealsNext = (By.XPATH,"//div/button[@class='px-5 bg-secondary-500 hover:bg-secondary-600 c-white bc-transparent c-pointer py-1 px-3 h-8 fs-3 fw-600 t-all button bs-solid tp-color td-500 bw-1 br-4 lh-solid box-border']")

    Next_menu = (By.XPATH,"//div[@class='flex flex-right']/*[name()='svg'][@data-testid='incrementVeg Diabetic Meal']")

    MealsDone = (By.XPATH,"//div/button[@class='px-5 bg-secondary-500 hover:bg-secondary-600 c-white bc-transparent c-pointer py-1 px-3 h-8 fs-3 fw-600 t-all button bs-solid tp-color td-500 bw-1 br-4 lh-solid box-border']")
    SaveNext = (By.XPATH,"//div/span[contains(text(),'Save and Exit')]")

    Baggage = (By.XPATH,"//div[contains(text(),'Baggage is cheaper when pre-booked')]/parent::div/following-sibling::div/button")

    AddedLuggage = (By.XPATH,"//div[@class='flex flex-right']/*[name()='svg'][@data-testid='increment5 KG']")

    LuggageDone = (By.XPATH,"//div/button[@class='px-5 bc-secondary-500 hover:bc-secondary-600 c-secondary-500 hover:c-secondary-600 bg-transparent c-pointer py-1 px-3 h-8 fs-3 fw-600 t-all button bs-solid tp-color td-500 bw-1 br-4 lh-solid box-border']")
    SaveAndExit = (By.XPATH,"//div/span[@data-testid='saveAndExit']")

    ContinueAfterLuggage = (By.XPATH,"//button[@class='px-7 mr-2 bg-primary-500 hover:bg-primary-600 c-white bc-transparent c-pointer py-2 px-5 h-10 fs-4 fw-600 t-all button bs-solid tp-color td-500 bw-1 br-4 lh-solid box-border'][contains(text(),'Continue')]")
    MobileNumber = (By.XPATH,"//div/input[@data-testid='mobileNumber']")
    Email = (By.XPATH,"//div/input[@data-testid='email']")
    ContinueAfterContact = (By.XPATH,"//label/p[contains(text(),'Send me travel offers, deals, and news by email')]/parent::label/following-sibling::div[2]")
    Adult1FN = (By.XPATH,"//div/h4[contains(text(),'Adult 1')]/following-sibling::div[2]/div/div/input[@data-testid='firstName']")
    Adult1LN = (By.XPATH,"//div/h4[contains(text(),'Adult 1')]/following-sibling::div[2]/div[2]/div/input[@data-testid='lastName']")
    Adult1G = (By.XPATH,"//div/h4[contains(text(),'Adult 1')]/following-sibling::div[2]/div[3]/div/div/button/div[contains(text(),'Gender')]")
    GenderM = (By.XPATH,"//div/ul/li[contains(text(),'Male')]")
    GenderF = (By.XPATH,"//div/ul/li[contains(text(),'Female')]")


    Adult2FN = (By.XPATH,"//div/h4[contains(text(),'Adult 2')]/following-sibling::div[2]/div/div/input[@data-testid='firstName']")
    Adult2LN = (By.XPATH,"//div/h4[contains(text(),'Adult 2')]/following-sibling::div[2]/div[2]/div/input[@data-testid='lastName']")
    Adult2G = (By.XPATH,"//div/h4[contains(text(),'Adult 2')]/following-sibling::div[2]/div[3]/div/div/button/div[contains(text(),'Gender')]")
    ChildFN = (By.XPATH,"//div/h4[contains(text(),'Child 1')]/following-sibling::div[2]/div/div/input[@data-testid='firstName']")
    ChildLN = (By.XPATH,"//div/h4[contains(text(),'Child 1')]/following-sibling::div[2]/div[2]/div/input[@data-testid='lastName']")
    ChildG = (By.XPATH,"//div/h4[contains(text(),'Child 1')]/following-sibling::div[2]/div[3]/div/div/button/div[contains(text(),'Gender')]")
    BirthD = (By.XPATH,"//div/input[@placeholder='DD / MM / YYYY']")
    Payment = (By.XPATH,"//label/p[contains(text(),'Use GSTIN details for this booking')]/parent::label/following-sibling::div[3]/div/button")
    PaymentAssert = (By.XPATH,"//div/p[@class='fs-3 c-secondary-500 fw-500 fw-600']")











