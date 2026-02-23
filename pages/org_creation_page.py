from utils.base_page import BasePage
from playwright.sync_api import expect


class OrgCreationPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        # ───────── Buttons / Toggles ─────────
        self.new_business_btn = page.get_by_role("button", name="New Business")
        self.primary_org_toggle = page.locator(
            'label[data-v-2385cbd4][for="create-business-primary"]'
        )

        # ───────── Basic Details ─────────
        self.display_name_input = page.locator("[data-test='displayName']")
        self.business_name_input = page.locator("[data-test='businessName']")

        # ───────── Bank Details ─────────
        self.account_number_input = page.get_by_role("textbox", name="account number")
        self.ifsc_code_input = page.get_by_role("textbox", name="ifsc code")

        # ───────── PAN ─────────
        self.document_type_dropdown = page.locator("[id^='document-select']").first
        self.pan_option = page.get_by_text("PAN Document", exact=True)
        self.add_document_btn = page.get_by_role("button", name="Add Document")

        # ───────── Primary Address ─────────
        self.primary_house_input = page.locator('#__BVID__315')
        self.primary_street_input = page.locator('#__BVID__317')
        self.primary_landmark_input = page.locator('#__BVID__319')
        self.primary_pincode_input = page.locator('#pinCode').first
        self.primary_city_input = page.locator('#__BVID__323')
        self.primary_state_input = page.locator('#__BVID__325')

        # ───────── Registered Address ─────────
        self.registered_house_input = page.locator('#__BVID__327')
        self.registered_street_input = page.locator('#__BVID__329')
        self.registered_landmark_input = page.locator('#__BVID__331')
        self.registered_pincode_input = page.locator('#pinCode').nth(1)
        self.registered_city_input = page.locator('#__BVID__335')
        self.registered_state_input = page.locator('#__BVID__337')

        # ───────── Authorized Signatory ─────────
        self.auth_sign_name_input = page.locator('#authSignName')
        self.auth_sign_mobile_input = page.locator('#authSignMobile')
        self.auth_sign_email_input = page.locator('#authSignEmail')

        # ───────── Save / Approval ─────────
        self.save_btn = page.get_by_role("button", name="Save")
        self.send_for_approval_icon = page.locator("#action-send-approval-icon")
        self.approval_success_msg = page.get_by_text("sent for approval", exact=False)

    # ───────── Actions ─────────

    def click_new_business(self):
        self.click(self.new_business_btn)
        expect(self.display_name_input).to_be_visible()

    def select_org_type(self, org_type):
        if org_type.lower() == "primary":
            self.click(self.primary_org_toggle)

    def enter_basic_details(self, display_name, business_name):
        self.fill(self.display_name_input, display_name)
        self.fill(self.business_name_input, business_name)

    def enter_bank_details(self, account_no, ifsc):
        self.fill(self.account_number_input, account_no)
        self.fill(self.ifsc_code_input, ifsc)

    def enter_pan(self, pan_value):
        self.click(self.document_type_dropdown)
        self.click(self.pan_option)
        self.click(self.add_document_btn)

        pan_input = (
            self.page.get_by_label("PAN")
            .or_(self.page.get_by_placeholder("PAN"))
            .or_(self.page.locator("[data-test*='pan']"))
            .first
        )

        expect(pan_input).to_be_visible()
        self.fill(pan_input, pan_value)

    def enter_primary_address(self, house, street, landmark, pincode, city, state):
        self.fill(self.primary_house_input, house)
        self.fill(self.primary_street_input, street)
        self.fill(self.primary_landmark_input, landmark)
        self.fill(self.primary_pincode_input, pincode)
        self.fill(self.primary_city_input, city)
        self.fill(self.primary_state_input, state)

    def enter_registered_address(self, house, street, landmark, pincode, city, state):
        self.fill(self.registered_house_input, house)
        self.fill(self.registered_street_input, street)
        self.fill(self.registered_landmark_input, landmark)
        self.fill(self.registered_pincode_input, pincode)
        self.fill(self.registered_city_input, city)
        self.fill(self.registered_state_input, state)

    def authorize_signature(self, name, mobile, email):
        self.fill(self.auth_sign_name_input, name)
        self.fill(self.auth_sign_mobile_input, mobile)
        self.fill(self.auth_sign_email_input, email)

    def save(self):
        self.click(self.save_btn)
        expect(self.send_for_approval_icon).to_be_visible(timeout=15000)

    def send_for_approval(self):
        expect(self.send_for_approval_icon).to_be_visible(timeout=15000)
        self.click(self.send_for_approval_icon)

    def is_org_approved_successfully(self):
        try:
            expect(self.approval_success_msg).to_be_visible(timeout=15000)
            return True
        except Exception:
            return False