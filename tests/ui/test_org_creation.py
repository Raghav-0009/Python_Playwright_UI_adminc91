import pytest
from pages.org_creation_page import OrgCreationPage
from utils.data_generator import generate_test_data


@pytest.mark.smoke
def test_create_org(page):
    test_data = generate_test_data()
    org = OrgCreationPage(page)

    org.click_new_business()
    org.select_org_type("primary")

    org.enter_basic_details(
        test_data["display_name"],
        test_data["business_name"]
    )

    org.enter_bank_details(
        test_data["account_number"],
        "FINO0000121"
    )

    org.enter_pan(test_data["pan"])

    org.enter_primary_address(
        test_data["Primary_house_number"],
        test_data["Primary_street_name"],
        test_data["Primary_landmark"],
        test_data["Primary_pincode"],
        test_data["Primary_city"],
        test_data["Primary_state"]
    )

    org.enter_registered_address(
        test_data["Register_house_number"],
        test_data["Register_street_name"],
        test_data["Register_landmark"],
        test_data["Register_pincode"],
        test_data["Register_city"],
        test_data["Register_state"]
    )

    org.authorize_signature(
        test_data["AdminName"],
        test_data["AdminMobile"],
        test_data["AdminEmail"]
    )

    # save() validates creation internally
    org.save()


def test_org_approval(page):
    org = OrgCreationPage(page)

    org.send_for_approval()

    assert org.is_org_approved_successfully(), "Organization approval failed"