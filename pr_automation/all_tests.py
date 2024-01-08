import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from pr_automation.pr_test_cases.authentication.logout import Logout
from pr_automation.pr_test_cases.configuration.deduction import Deduction
from pr_automation.pr_test_cases.configuration.earned_leave import Earned_Leave
from pr_automation.pr_test_cases.configuration.employee_salary import Employee_Salary
from pr_automation.pr_test_cases.configuration.negative_cases import Negative_cases
from pr_automation.pr_test_cases.configuration.other_deduction import Other_Deduction
from pr_automation.pr_test_cases.taxslabs.professional_tax import Professional_tax
from pr_automation.test_base import TestBase
from pr_test_cases.authentication.login import Login
from pr_test_cases.configuration.earning import Earning


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

    # for login and logout only

    def test_authentication(self):
        self.login = Login(self.driver)
        self.login.do_login()
        time.sleep(3)
        self.logout = Logout(self.driver)
        self.logout.do_logout()

    def test_earningConfig(self):
        self.login = Login(self.driver)
        self.login.do_login()
        time.sleep(3)
        self.earning = Earning(self.driver)
        self.earning.add_earning()

    def test_deductionConfig(self):
        self.login = Login(self.driver)
        self.login.do_login()
        time.sleep(3)
        self.deduction = Deduction(self.driver)
        self.deduction.add_deduction()

    def test_employeeSalaryConfig(self):
        self.login = Login(self.driver)
        self.login.do_login()
        time.sleep(3)
        self.es = Employee_Salary(self.driver)
        self.es.add_employee_salary()

    def test_otherDeductionConfig(self):
        self.login = Login(self.driver)
        self.login.do_login()
        time.sleep(3)
        self.od = Other_Deduction(self.driver)
        self.od.add_otherDeduction()

    def test_PT(self):
        self.login = Login(self.driver)
        self.login.do_login()
        time.sleep(3)
        self.pt = Professional_tax(self.driver)
        self.pt.add_professional_tax()

    def test_earnedLeave(self):
        self.login = Login(self.driver)
        self.login.do_login()
        time.sleep(3)
        self.el = Earned_Leave(self.driver)
        self.el.add_earnedLeave()

    def test_negatives(self):
        self.login = Login(self.driver)
        self.login.do_login()
        time.sleep(3)
        self.neg = Negative_cases(self.driver)
        self.neg.check_popup()
        time.sleep(3)


if __name__ == '__main__':
    # Run test cases
    test_suite = unittest.TestSuite()
    test_suite.addTest(AllTests('test_login'))
    unittest.main(testRunner=HTMLTestRunner(output="Reports", open_in_browser=True, verbosity=2,
                                            report_name="Reports"))
    unittest.TextTestRunner().run(test_suite)
