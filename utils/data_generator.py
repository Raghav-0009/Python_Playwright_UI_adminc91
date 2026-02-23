import random
import string


# ───────────── Basic Info ─────────────

def generate_display_name():
    first = ["Tech", "Global", "Digital", "Smart", "Inno", "Alpha", "Beta", "Prime", "Elite", "Pro"]
    last = ["Solutions", "Systems", "Labs", "Works", "Hub", "Net", "Core", "Max", "Plus"]
    return f"{random.choice(first)} {random.choice(last)} {random.randint(100, 999)}"


def generate_business_name():
    prefixes = ["Advanced", "Premium", "Super", "Mega", "Ultra", "Elite", "Pro", "Smart", "Digital", "Global"]
    suffixes = ["Pvt Ltd", "Ltd", "Inc", "Corp", "LLC", "Enterprises", "Industries", "Group", "Holdings"]
    return f"{random.choice(prefixes)} {random.choice(prefixes)} {random.choice(suffixes)}"


# ───────────── Bank Details ─────────────

def generate_account_number():
    return ''.join(random.choices(string.digits, k=14))


def generate_client_id():
    return f"{random.choice(['A', 'B', 'C', 'D'])}{''.join(random.choices(string.digits, k=5))}"


# ───────────── Address Helpers ─────────────

def generate_house_number(min_val=1):
    return str(random.randint(min_val, 9999))


def generate_street_name():
    return random.choice([
        "Main St", "Oak Ave", "Park Rd", "Elm St",
        "Maple Dr", "Cedar Ln", "Pine St", "Walnut Ave"
    ])


def generate_landmark():
    return random.choice([
        "Near Metro Station", "Opp Mall", "City Center",
        "Tech Park", "Bus Stand", "Railway Station"
    ])


def generate_pincode():
    return str(random.randint(100000, 999999))


def generate_city():
    return random.choice([
        "Bangalore", "Mumbai", "Delhi", "Chennai",
        "Kolkata", "Hyderabad", "Pune", "Ahmedabad",
        "Jaipur", "Lucknow"
    ])


def generate_state():
    return random.choice(["KA", "MH", "DL", "TN", "WB", "TS", "GJ", "RJ", "UP", "PB"])


# ───────────── PAN & Admin ─────────────

def generate_pan():
    return (
            ''.join(random.choices(string.ascii_uppercase, k=5)) +
            ''.join(random.choices(string.digits, k=4)) +
            random.choice(string.ascii_uppercase)
    )


def generate_admin_name():
    first = ["Ravi", "Amit", "Neha", "Ankit", "Priya", "Rahul", "Karan", "Pooja"]
    last = ["Sharma", "Verma", "Gupta", "Singh", "Mehta", "Patel"]
    return f"{random.choice(first)} {random.choice(last)}"


def generate_mobile():
    return ''.join(random.choices("6789", k=1) + random.choices(string.digits, k=9))


def generate_email():
    return ''.join(random.choices(string.ascii_lowercase, k=10)) + "@mailinator.com"


# ───────────── Final Test Data ─────────────

def generate_test_data():
    return {
        # Basic
        "display_name": generate_display_name(),
        "business_name": generate_business_name(),

        # Bank
        "account_number": generate_account_number(),
        "client_id": generate_client_id(),

        # Primary Address
        "Primary_house_number": generate_house_number(),
        "Primary_street_name": generate_street_name(),
        "Primary_landmark": generate_landmark(),
        "Primary_pincode": generate_pincode(),
        "Primary_city": generate_city(),
        "Primary_state": generate_state(),

        # Registered Address
        "Register_house_number": generate_house_number(min_val=10),
        "Register_street_name": generate_street_name(),
        "Register_landmark": generate_landmark(),
        "Register_pincode": generate_pincode(),
        "Register_city": generate_city(),
        "Register_state": generate_state(),

        # PAN
        "pan": generate_pan(),

        # Authorized Signatory
        "AdminName": generate_admin_name(),
        "AdminMobile": generate_mobile(),
        "AdminEmail": generate_email(),
    }