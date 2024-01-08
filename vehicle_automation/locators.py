""" /* File:
    Objective: The objective of this page is Automating the file about Unit of Measure page of the TMS module.


    Description: This page configures the unit of measure of the product.

                 For all these functions I have automated using selenium scripts with all the negative cases.


Initiated By:Devi Abirami on 05th December
Modification History

--------------------------------------------------------------------------------------------------------------------
DATE         |   AUTHOR       |   Modification Request No.                    | Remarks / Detail of Changes
--------------------------------------------------------------------------------------------------------------------
05-Dec-2023  |  Devi Abirami      |   Devi Abirami on 25th April 2023                 |        Created mock script
             |  Devi Abirami      |   Devi Abirami on 25th April 2023                 |       Completed the full script

--------------------------------------------------------------------------------------------------------------------
This is what the change that you have to done to run the automation file

For Addition(only valid case) -> The name has to be unique
For Edit(only valid case) -> The name has to be unique
"""

import time

from selenium.webdriver.common.by import By


class Locators:
    """
    List all element selectors used to test, by this way If any element is changed
    then can change in this (one) file.
    """

    # Login Module
    LOGIN_LINK = (By.XPATH, 'https://royal-dev.techgenzi.com/')
    USERNAME = (By.ID, 'Username')
    PASSWORD = (By.ID, 'Password')
    EYE_BUTTON = (By.ID, 'Eye_Button')
    LOGIN_SUBMIT_BUTTON = (By.ID, "Login_Button")

    PROFILE = (By.ID, 'Popup_Button')
    MY_ACCOUNT = (By.ID, 'User_Profile_Button')
    DOWNLOAD_APPS = (By.ID, 'Download_Apk_Button')
    USER_HISTORY = (By.ID, 'User_History_Button')
    CONFIGURE_COMPANY = (By.ID, 'Company_Code_Button')
    CONFIGURE_COMPANY_CODE_CHANGE = (By.ID, 'Company_Code_Change')
    CLOSE_BUTTON = (By.ID, 'Close_Button')
    LOGOUT_BUTTON = (By.ID, 'Logout_Button')

    USERNAME_ALERT = (By.XPATH, '//*[@id="mui-5-helper-text"]')
    PASSWORD_ALERT = (By.XPATH, '//*[@id="mui-6-helper-text"]')

    # SIDEBARS
    MENU = (By.ID, "Drawer_Button")
    CLOSE_MENU = (By.XPATH, '//*[@id="Vehicle_sidebar"]/div/div/div[1]/button')
    DASHBOARD = (By.XPATH, "//ul[@id='Menus_Dashboard']")
    HEALTH_DASHBOARD = (By.XPATH, "//ul[@id='Menus_Health Dashboard']")
    REPORTS = (By.ID, "Menus_Reports")
    USER_AND_ROLES = (By.XPATH, '//*[@id="jo_sidebar"]/div/div/div[2]/a[3]/ul/li')
    COMPANY = (By.XPATH, '//*[@id="jo_sidebar"]/div/div/div[2]/a[4]/ul')
    PLAYBACK = (By.ID, 'Menus_Playback')

    CONFIGURE = (By.ID, 'Menus_Configure')
    time.sleep(2)
    VEHICLE = (
        By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[1]")
    STUDENT = (
        By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[2]")
    STUDENT_ASSIGN = (
        By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[3]")
    ROUTE = (
        By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[5]")
    PARENT = (
        By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[4]")
    DRIVER = (
        By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[6]")
    CONDUCTOR = (
        By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[7]")
    SUPERVISOR = (
        By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[8]")
    HELPER = (
        By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/div[9]")
    ASSIGN = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[1]/div/div/div[2]/nav/div[10]')

    # BUTTONS
    CHECKBOX = (By.XPATH, '//div[@ref="eCheckbox"]')
    ADD = (By.ID, 'Add_Button')
    EDIT = (By.ID, 'Edit_Button')
    DELETE = (By.ID, 'Delete_Button')
    DOWNLOAD = (By.ID, 'Export_Button')
    PDF = (By.XPATH, '//*[@id="basic-menu"]/div[3]/ul/li[1]')
    EXCEL = (By.XPATH, '//*[@id="basic-menu"]/div[3]/ul/li[2]')
    SUBMIT = (By.ID, 'Submit_Button')
    CANCEL = (By.ID, 'Cancel_Button')
    OK_BUTTON = (By.ID, "Ok_Button")
    GO_BACK = (By.XPATH, '//header/div[1]/div[2]/div[1]/button[1]')

    # VEHICLE
    VEH_SITE_NAME = (By.NAME, 'asset_attributes.site_id')
    VEH_NUMBER = (By.NAME, 'asset_identifier')
    VEH_NAME = (By.ID, 'Vehicle_Name')
    VEH_ENGINE_NUMBER = (By.ID, 'Engine_No')
    VEH_CHASSIS_NUMBER = (By.ID, 'Chassis_No')
    VEH_RC_NUMBER = (By.ID, 'RC_No')
    VEH_FC_NUMBER = (By.ID, 'FC_No')
    VEH_TAX_RECEIPT_NUMBER = (By.ID, "Tax_Recepit_No")
    VEH_PERMIT_NUMBER = (By.ID, 'Permit_No')
    VEH_SEAT_CAPACITY = (By.ID, 'Seat_Capacity')
    VEH_FUEL_CAPACITY = (By.ID, 'Fuel_Tank_Capacity')
    FUEL_TYPE = (By.ID, 'Fuel_Type')
    SPEEDLIMIT = (By.ID, 'Speed_Limit')
    ATTACHMENTS = (By.XPATH,
                   "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[6]/div[1]/div[1]/div[1]/table[1]/tr[1]/td[1]/span[1]")
    RC_EXP_DATE = (By.ID, 'RC_Exp_date')
    FC_EXP_DATE = (By.ID, 'FC_Exp_date')
    EMISSION_EXP_DATE = (By.ID, 'Emission_Exp_Date')
    INSURANCE_EXP_DATE = (By.ID, 'Insurance_Exp_Date')
    TAX_EXP_DATE = (By.ID, 'Tax_Exp_Date')
    PERMIT_EXP_DATE = (By.ID, 'Permit_expiry_date')

    VEHICLE_SITE_ALERT = (By.ID, "mui-2-helper-text")
    VEH_NUMBER_ALERT = (By.ID, "mui-3-helper-text")
    VEH_SUBMIT_BUTTON = (By.ID, "Submit_Button")
    VEH_CANCEL_BUTTON = (By.ID, "Cancel_Button")

    # STUDENT
    STUDENT_SITE_NAME = (By.ID, "Site_Name")
    STUDENT_NAME = (By.ID, 'Student_Name')
    STUDENT_IDCARD = (By.ID, 'Id_Card_No')
    DOB = (By.ID, 'D_O_B')
    CLASS_NAME = (By.ID, 'Class_Name')
    SECTION = (By.ID, 'Section_Name')
    FATHER_NAME = (By.ID, 'Fater_Name')
    MOTHER_NAME = (By.ID, 'Mother_Name')
    CONTACT_NUMBER = (By.ID, 'Contact_No')
    ADDRESS = (By.ID, 'Address_No')

    # STUDENT ROUTE ASSIGN
    STUDENT_NAME_ASSIGN = (By.NAME, "ipss_asset_id")
    ASSIGN_ROUTE_NAME = (By.NAME, 'details[0].route_id')
    ASSIGN_STOP_NAME = (By.NAME, 'details[0].stop_id')
    ADD_ROUTE_BUTTON = (By.ID, 'Add_Button')
    DELETE_ROUTE_BUTTON = (By.ID, 'Delete_Button_1')
    STUDENT_SUBMIT_BUTTON = (By.ID, 'Submit_Button')
    STUDENT_CANCEL_BUTTON = (By.ID, 'Cancel_Button')

    # PARENT
    PARENT_SITE_NAME = (By.ID, 'Site_Name')
    PARENT_NAME = (By.ID, 'Name')
    MOBILE_NUMBER = (By.ID, 'Phone_No')
    LOGIN_REQUIRED = (By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div/div[4]/label')
    CLOSE = (By.ID, 'close')
    SITE_ALERT = (By.ID, 'mui-2-helper-text')
    PARENT_NAME_ALERT = (By.ID, 'title-helper-text')
    PARENT_MOBILE_NUMBER_ALERT = (By.ID, 'description-helper-text')
    PARENT_SUBMIT_BUTTON = (By.ID, 'Submit_Button')
    PARENT_CANCEL_BUTTON = (By.ID, 'Cancel_Button')

    # ROUTE
    ROUTE_SITE_NAME = (By.NAME, 'routeno')
    ROUTE_NAME = (By.ID, 'name')
    ROUTE_ACTIVE = (By.ID, 'demo-simple-select')
    STOP_NAME = (By.ID, 'details[0].stop_name')
    LOCATION = (By.ID, 'details[0].location')
    LATITUDE = (By.ID, 'details[0].stop_lat')
    LONGITUDE = (By.ID, 'details[0].stop_lng')
    DEPARTURE_TIME = (By.ID, 'details[0].depart_time_up')
    ARRIVAL_TIME = (By.ID, 'details[1].arrival_time_up')
    LOCATORS_row1 = [
        (By.ID, 'details[0].stop_name'),
        (By.ID, 'details[0].location'),
        (By.ID, 'details[0].stop_lat'),
        (By.ID, 'details[0].stop_lng'),
        (By.ID, 'details[0].depart_time_up')
    ]
    ADD_STOP = (By.ID, 'Add Stop')

    LOCATORS_row2 = [
        (By.ID, 'details[1].stop_name'),
        (By.ID, 'details[1].location'),
        (By.ID, 'details[1].stop_lat'),
        (By.ID, 'details[1].stop_lng'),
        (By.ID, 'details[1].arrival_time_up'),
        (By.ID, 'details[1].depart_time_up')
    ]
    LOCATORS_row3 = [
        (By.ID, 'details[2].stop_name'),
        (By.ID, 'details[2].location'),
        (By.ID, 'details[2].stop_lat'),
        (By.ID, 'details[2].stop_lng'),
        (By.ID, 'details[2].arrival_time_up')
    ]

    # DRIVER
    DRIVER_SITE_NAME = (By.XPATH, 'asset_attributes.site_id')
    DRIVER_NAME = (By.NAME, 'title')
    DRIVER_MOBILE_NO = (By.ID, 'description')

    # CONDUCTOR
    CONDUCTOR_SITE_NAME = (By.NAME, 'asset_attributes.site_id')
    CONDUCTOR_NAME = (By.NAME, 'title')
    CONDUCTOR_MOBILE_NO = (By.ID, 'description')

    # SUPERVISOR
    SUPERVISOR_SITE_NAME = (By.NAME, 'asset_attributes.site_id')
    SUPERVISOR_NAME = (By.NAME, 'title')
    SUPERVISOR_MOBILE_NO = (By.ID, 'description')

    # HELPER
    HELPER_SITE_NAME = (By.NAME, 'asset_attributes.site_id')
    HELPER_NAME = (By.NAME, 'title')
    HELPER_MOBILE_NO = (By.ID, 'description')

    # ASSIGN
    RESET_BUTTON = (By.XPATH, '//header/div[1]/div[2]/div[1]/button[1]')
    SELECT_1 = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
    selection_1 = (By.XPATH, '//li[text()="Vehicle"]')
    SELECT_1_VALUE = (By.ID, 'combo-box-demo')
    SELECT_2 = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]")
    selection_2 = (By.XPATH, '//li[text()="Route"]')
    SELECT_TO_ASSIGN = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[4]/div/div[1]/div/div[3]/li')
    ASSIGN_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[4]/div/div[2]/div[1]/button[1]')
    DEASSIGN_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[4]/div/div[2]/div[1]/button[2]')
    SELECT_TO_DEASSIGN = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[4]/div/div[3]/div/div[3]/li')

    # ALERTS
    ALERT_MSG = (By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div")

    # DASHBOARD
    STATUS_TAB = (By.ID, "Status_tab")
    FILTER_TAB = (By.ID, 'Filter_tab')

    ALL_VEHICLES = (By.ID, 'All Vehicles_Card')
    GPS_INSTALLED = (By.ID, 'GPS Installed_Card')
    RUNNING_VEHICLES = (By.ID, 'Running Vehicles_Card')
    STOPPED_VEHICLES = (By.ID, 'Stopped Vehicles_Card')
    IDLE_VEHICLES = (By.ID, 'Idle Vehicles_Card')
    OUT_OF_NETWORK = (By.ID, 'Out of Network_Card')
    CLOSE_CARD = (By.ID, 'Close_Button')

    PDF_DOWNLOAD = (By.ID, 'PDF_Download')
    EXCEL_DOWNLOAD = (By.ID, 'Excel_Download')

    FILTER_MENU = (By.ID, 'Collabsive_Button')
    FILTER_BUTTON = (By.ID, 'Filter_Button')
    SITE = (By.ID, 'Site_Select')
    SITE_SELECT = [(By.ID, 'Select_All_Site'),
                   (By.ID, 'Menu_0',),
                   (By.ID, 'Menu_1'),
                   (By.ID, 'Menu_2')]

    DEVICE_STATUS = (By.ID, 'Status_Select')
    STATUS_SELECT = [(By.ID, 'Select_All_Device'),
                     (By.ID, 'Menu_0',),
                     (By.ID, 'Menu_1'),
                     (By.ID, 'Menu_2'),
                     (By.ID, 'Menu_3')]
    ROUTES = (By.ID, 'Routes_Select')
    ROUTES_SELECT = [(By.ID, 'Select_All_Routes'),
                     (By.ID, 'Menu_0'),
                     (By.ID, 'Menu_1'),
                     (By.ID, 'Menu_2'),
                     (By.ID, 'Menu_3')]
    SEARCH_VEHICLE = (By.ID, 'Search_Vehicles')
    FILTERED_VEHICLES = ([
        (By.ID, 'Vehicle_0'),
        (By.ID, 'Vehicle_1'),
        (By.ID, 'Vehicle_2'),
        (By.ID, 'Vehicle_3')
    ])

    # COMPANY CONFIGURATION
    COMPANY_CODE_TAB = (
        By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]")
    COMPANY_CODE_ASSIGN = (
        By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]")
    COMPANY_NAME = (By.ID, 'CompanyName')
    COMPANY_CODE = (By.ID, 'compcode')
    COMPANY_ADDRESS = (By.ID, 'address')
    COMPANY_ADD_BUTTON = (By.ID, 'Allocate_config_Add-Button')
    COMPANY_EDIT_BUTTON = (By.ID, 'Allocate_config_Edit-Button')
    COMPANY_DELETE_BUTTON = (By.ID, 'Allocate_config_Delete-Button ')
    SUBMIT_BUTTON = (By.ID, 'Submit')
    CANCEL_BUTTON = (By.ID, 'Cancel')
    YES_BUTTON = (By.XPATH, "Yes_Button")
    NO_BUTTON = (By.ID, "No_Button")

    # REPORTS
    LOGIN_LOGOUT_TAB = (By.XPATH, '//button[contains(text(),"Login/Logout")]')

    OVERSPEED_TAB = (By.XPATH, '//button[contains(text(),"Overspeed")]')
    GEOFENCE_TAB = (By.XPATH, '//button[contains(text(),"Geofence")]')
    NOTIFICATION_TAB = (By.XPATH, '//button[contains(text(),"Notification")]')
    DAYWISE_TAB = (By.XPATH, '//button[contains(text(),"Daywise")]')
    SUMMARY_TAB = (By.XPATH, '//button[contains(text(),"Summary")]')
    NON_WORKING_HOURS_TAB = (
        By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[7]/button[1]")
    NOT_TRACKING_TAB = (By.XPATH, '//button[contains(text(),"Not Tracking")]')
    FILLTOFILL_TAB = (By.XPATH, '//button[contains(text(),"Fill to Fill Report")]')
    MANAGEMENT_REPORT = (By.XPATH, '//button[contains(text(),"Management Report")]')
    TRIP_REPORT = (By.XPATH, '//button[contains(text(),"Trip Report")]')
    FUELFILL_TAB = (By.XPATH, '//button[contains(text(),"Fuel Fill Report")]')
    GATEPASS_TAB = (By.XPATH, '//button[contains(text(),"Gate Pass")]')
    REPORT_DASHBOARD = (By.XPATH, '//button[contains(text(),"Report Dashboard")]')

    REPORT_PERIOD = (By.ID, 'demo-multiple-name')
    REPORT_PDF = (By.ID, 'PDF_Button')
    EXCEL_PDF = (By.ID, 'Excel_Button')

    # PLABACK
    PLAYBACK_SITE = (
        By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]")
    PLAYBACK_VEHICLE = (By.XPATH,
                        "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]")
    PLAYBACK_DATE = (By.XPATH, '//*[@id="mui-3-label"]')
    PLAYBACK_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div[2]/button')
