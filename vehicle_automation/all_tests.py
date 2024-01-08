import os
import unittest
import HTMLTestRunner
from vehicle_automation.test_base import TestBase
from vehicle_automation.vehicle_test_cases.authentication.logout import Logout
from vehicle_automation.vehicle_test_cases.configure.assign import Assign
from vehicle_automation.vehicle_test_cases.configure.assignStudentRoute import Configure_studentRouteAssign
from vehicle_automation.vehicle_test_cases.configure.configurations import Configurations
from vehicle_automation.vehicle_test_cases.configure.parent import Configure_parent
from vehicle_automation.vehicle_test_cases.configure.route import Configure_route
from vehicle_automation.vehicle_test_cases.configure.student import Configure_student
from vehicle_automation.vehicle_test_cases.configure.vehicle import Configure_vehicle
from vehicle_automation.vehicle_test_cases.live_check.flow_check import flow_check
from vehicle_automation.vehicle_test_cases.pages.company_code_configuration import Company_code_config
from vehicle_automation.vehicle_test_cases.pages.dashboard import Dashboard
from vehicle_automation.vehicle_test_cases.pages.playback import Playback
from vehicle_automation.vehicle_test_cases.pages.profile_settings import Profile_settings
from vehicle_test_cases.authentication.login import Login


class AllTests(TestBase):
    """
    Run all test cases here
    """

    def setUp(self) -> None:
        """
        Chrome driver setup from Base class
        :return:
        """
        super().setUp()

    def test_assets(self):
        Login(self.driver).do_login()

        Configurations(self.driver).driver_config()
        Configurations(self.driver).conductor_config()
        Configurations(self.driver).supervisor_config()
        Configurations(self.driver).helper_config()
        Assign(self.driver).assign_config()
        Configure_route(self.driver).route_config()

    def test_vehicle(self):
        Login(self.driver).do_login()
        Configure_vehicle(self.driver).add_new_vehicle()
        Configure_vehicle(self.driver).update_existing_vehicle()
        Configure_vehicle(self.driver).download_vehicle_reports()

    def test_student(self):
        Login(self.driver).do_login()
        Configure_student(self.driver).add_new_student()
        Configure_student(self.driver).update_existing_student()

    def test_studentRouteAssign(self):
        Login(self.driver).do_login()
        Configure_studentRouteAssign(self.driver).add_studentRouteAssign()
        Configure_studentRouteAssign(self.driver).edit_studentRouteAssign()
        Configure_studentRouteAssign(self.driver).delete_studentRouteAssign()

    def test_parent(self):
        Login(self.driver).do_login()
        Configure_parent(self.driver).add_new_parent()
        Configure_parent(self.driver).edit_existing_parent()

    def test_dashboard(self):
        Login(self.driver).do_login()
        Dashboard(self.driver).test_dashboard()
        Dashboard(self.driver).check_filters()

    def test_profileSettings(self):
        Login(self.driver).do_login()
        # Profile_settings(self.driver).my_account()
        Company_code_config(self.driver).config_comp_code()

    def test_authentication(self):
        Login(self.driver).do_login()
        Logout(self.driver).do_logout()

    def test_logout(self):
        self.logout = Logout(self.driver)
        self.logout.do_logout()

    def test_workflow(self):
        # Login(self.driver).do_login()
        flow_check(self.driver).check_flow()

    def test_playback(self):
        Login(self.driver).do_login()
        Playback(self.driver).playback()

    def tearDown(self):
        """
        Clean up after the test suite.
        """
        super().tearDown()  # Close the browser session


if __name__ == '__main__':
    # Create a test suite
    test_suite = unittest.TestSuite()

    # Add your test cases to the suite
    test_suite.addTest(AllTests("test_assets"))
    test_suite.addTest(AllTests("test_vehicle"))
    test_suite.addTest(AllTests("test_student"))
    test_suite.addTest(AllTests("test_studentRouteAssign"))
    test_suite.addTest(AllTests("test_parent"))
    test_suite.addTest(AllTests("test_dashboard"))
    test_suite.addTest(AllTests("test_profileSettings"))
    test_suite.addTest(AllTests("test_authentication"))
    test_suite.addTest(AllTests("test_logout"))
    test_suite.addTest(AllTests("test_workflow"))
    test_suite.addTest(AllTests("test_playback"))

    # Configure the HTMLTestRunner
    html_report_path = "D:/VehicleAutomation/vehicle_automation/vehicle_test_cases/html_reports"
    print("HTML Report Path:", html_report_path)

    if not os.path.exists(html_report_path):
        os.makedirs(html_report_path)
        print("HTML Report Path:", html_report_path)

    html_test_runner = HTMLTestRunner.HTMLTestRunner(
        output=html_report_path,
        open_in_browser=True,
        verbosity=2,
        report_name="Vehicle"
    )

    # Run the suite with HTMLTestRunner
    html_test_runner.run(test_suite)
