from app.models.schemas import TemplateRequest, PaymentType, TemplateStyle

# Test 1: Valid Till payment
try:
    till_request = TemplateRequest(
        payment_type=PaymentType.TILL,
        business_name="Test Shop",
        till_number="123456"
    )
    print("✓ Till request valid:", till_request.model_dump())
except Exception as e:
    print("✗ Till request failed:", e)

# Test Invalid Till 
try:
    invalid_till = TemplateRequest(
        payment_type=PaymentType.TILL,
        business_name="Test Shop"
    )
    print("✗ Should have failed but didn't")
except Exception as e:
    print("✓ Correctly rejected:", str(e))

# Test Valid Paybill
try:
    paybill_request = TemplateRequest(
        payment_type=PaymentType.PAYBILL,
        business_name="ABC Company",
        paybill_number="400200",
        account_number="ACC001",
        amount=5000
    )
    print("✓ Paybill request valid:", paybill_request.model_dump())
except Exception as e:
    print("✗ Paybill request failed:", e)

# Test Valid Bank payment
try:
    bank_request = TemplateRequest(
        payment_type=PaymentType.BANK,
        business_name="My Business",
        bank_business_number="247247",
        bank_account_number="0123456789",
        amount=10000
    )
    print("✓ Bank request valid:", bank_request.model_dump())
except Exception as e:
    print("✗ Bank request failed:", e)

# TestInvalid Bank
try:
    invalid_bank = TemplateRequest(
        payment_type=PaymentType.BANK,
        business_name="My Business",
        bank_business_number="247247"
    )
    print("✗ Should have failed but didn't")
except Exception as e:
    print("✓ Correctly rejected:", str(e))