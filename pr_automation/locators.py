from selenium.webdriver.common.by import By


class Locators:
    """
    List all element selectors used to test, by this way If any element is changed
    then can change in this (one) file.
    """
    # Login Module
    USERNAME_INPUT = (By.NAME, 'username')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_SUBMIT_BUTTON = (By.XPATH, '//button[text()="Log in"]')
    INVALID_USER = (By.ID, 'mui-1-helper-text')

    # Logout Module
    PROFILE_CLICK = (By.XPATH, "//*[contains(concat(' ', normalize-space(@class), ' '), ' MuiAvatar-root')]")
    LOGOUT_BUTTON = (By.XPATH, '//li[contains(text(),"Logout")]')

    PAYROLL_CARD = (By.XPATH, "//div[p[@class='app-name' and text()='Payroll']]")

    # bar_links
    configuration = (By.XPATH, '//span[contains(text(),"Configuration")]')
    earning = (By.XPATH, '//span[contains(text(),"Earning")]')
    deduction = (By.XPATH, '//span[contains(text(),"Deduction")]')
    other_deduction = (By.XPATH, '//span[contains(text(),"Other Deduction")]')
    employee_salary = (By.XPATH, "//span[contains(text(),'Employee Salary')]")
    tax_slab = (By.XPATH, '//span[contains(text(),"Tax Slab")]')
    salary_structure = (By.ID, '//span[contains(text(),"Salary Structure")]')
    payroll_settings = (By.ID, '//span[contains(text(),"Payroll Settings")]')
    reports = (By.ID, '//span[contains(text(),"Reports")]')
    earned_leave = (By.XPATH, '//span[contains(text(),"Configure Earned Leave")]')
    noOfDays = (By.ID, 'no_of_days')

    # icons abd buttons
    add_icon = (By.XPATH, '//*[@id="add"]')
    edit_icon = (By.ID, 'edit')
    delete_icon = (By.ID, 'delete')
    upload_icon = (By.ID, 'Upload')
    download_icon = (By.ID, 'download')
    submit = (By.ID, 'submit')
    cancel = (By.ID, 'cancel')
    next = (By.XPATH, '//button[contains(text(),"Next")]')

    # add and edit  fields
    name = (By.NAME, 'component_name')
    payslip = (By.CSS_SELECTOR, "input[name='payslip_name']")
    calc = (By.ID, 'calculation_type')
    pf = (By.ID, 'is_pf')
    description = (By.ID, 'description')
    tax_type = (By.ID, 'is_taxable')
    pay_type = (By.ID, 'pay_type')
    active = (By.ID, 'is_active')
    esi = (By.ID, 'is_esi')
    flexible = (By.ID, 'is_flexible')
    deduction_type = (By.XPATH, '//input[@name="tax_type"]')
    other_det = (By.ID, 'other_ded')
    emp_id = (By.ID, 'emp_id')
    deduction_name = (By.ID, 'deduction_mast_id')
    pay_month = (By.ID, "pay_month")
    description_od = (By.XPATH, '//input[contains(@name, ".description")]')
    amount_od = (By.XPATH, '//input[contains(@name, ".amount")]')
    # amount = (By.ID, 'deduction_mast_id[0].deduct_amount')
    # date = (By.ID, 'effective_date')
    tds = (By.NAME, "tds")
    regime = (By.NAME, 'regime')
    pt = (By.NAME, 'pt')
    salary_structure_name = (By.NAME, 'salary_structure_id')
    pay_Wage_type = (By.NAME, 'wage_type')
    effect_date = (By.NAME, 'effective_date')
    monthly_amount = (By.XPATH, '//input[contains(@name, ".monthly_amount")]')
    component_type = (By.XPATH, '//input[contains(@name, ".component_type")]')

    # no id/class for tags
    emp_add = (By.XPATH, '//header/div[1]/div[2]/div[1]/div[1]/button[1]/*[1]')
    emp_edit = (By.XPATH, '//header/div[1]/div[2]/div[1]/div[2]/button[1]/*[1]')
    emp_delete = (By.XPATH, '//header/div[1]/div[2]/div[1]/div[3]/button[1]/*[1]')
    emp_upload = (By.XPATH, '//header/div[1]/div[2]/div[1]/div[4]/button[1]/*[1]')
    emp_download = (By.XPATH, '//header/div[1]/div[2]/div[1]/div[5]/button[1]/*[1]')
    emp_emp_id = (By.NAME, 'emp_id')
    pop_del = (By.XPATH, '//button[contains(text(),"Yes")]')
    submit1 = (By.XPATH, '//button[contains(text(),"submit")]')

    # Tax Slab
    professional_tax = (By.XPATH, '//button[contains(text(), "Professional Tax")]')
    income_tax = (By.XPATH, "//button[contains(text(), 'Income Tax')]")
    edit_prof = (By.ID, "//body/div[@id='root']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div["
                        "1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/*[1]")

    # Checkbox
    checkbox = (By.XPATH, '//div[@ref="eCheckbox"]')


    # negative data
    neg_name = (By.ID, 'component_name-helper-text')
    neg_payslip = (By.ID, 'payslip_name-helper-text')
    neg_calc = (By.ID, 'calculation_type-helper-text')
    neg_pf = (By.ID, 'is_pf-helper-text')
    neg_tax = (By.ID, 'is_taxable-helper-text')
    neg_deduction_type = (By.XPATH, '//input[@name="tax_type"]')
    neg_pay = (By.ID, 'pay_type-helper-text')
    neg_active = (By.ID, 'is_active-helper-text')
    neg_esi = (By.ID, 'is_esi-helper-text')
    neg_flexible = (By.ID, 'is_flexible-helper-text')
    neg_emp_id = (By.ID, 'emp_id-helper-text')
    neg_deduction_name = (By.ID, 'deduction_mast_id-helper-text')
    neg_amount = (By.ID, 'amount-helper-text')
    neg_date = (By.ID, 'effective_date-helper-text')
