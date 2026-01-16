from pydantic import BaseModel, Field, model_validator
from typing import Optional, Literal
from enum import Enum

class PaymentType(str, Enum):
    TILL = "till"
    PAYBILL = "paybill"
    BANK = "bank"

class TemplateStyle(str, Enum):
    MODERN = "modern"
    CLASSIC = "classic"
    MINIMAL = "minimal"
    PROFESSIONAL = "professional"

class TemplateRequest(BaseModel):
    payment_type: PaymentType
    business_name: str = Field(..., min_length=1, max_length=100)
    
    # Till number fields
    till_number: Optional[str] = Field(None, pattern=r'^\d{5,7}$')
    
    # Paybill fields
    paybill_number: Optional[str] = Field(None, pattern=r'^\d{5,7}$')
    account_number: Optional[str] = Field(None, max_length=50)
    
    # Bank fields
    bank_business_number: Optional[str] = Field(None, max_length=50)
    bank_account_number: Optional[str] = Field(None, max_length=50)
    
    # Common fields
    amount: Optional[float] = Field(None, gt=0)
    reference: Optional[str] = Field(None, max_length=200)
    instructions: Optional[str] = Field(None, max_length=500)
    template_style: TemplateStyle = TemplateStyle.MODERN
    include_qr: bool = True
    
    @model_validator(mode='after')
    def validate_payment_fields(self):
        """Validate required fields based on payment type"""
        if self.payment_type == PaymentType.TILL and not self.till_number:
            raise ValueError('Till number is required for till payments')
        
        if self.payment_type == PaymentType.PAYBILL:
            if not self.paybill_number:
                raise ValueError('Paybill number is required for paybill payments')
            if not self.account_number:
                raise ValueError('Account number is required for paybill payments')
        
        if self.payment_type == PaymentType.BANK:
            if not self.bank_business_number:
                raise ValueError('Business number is required for bank payments')
            if not self.bank_account_number:
                raise ValueError('Account number is required for bank payments')
        
        return self

class TemplateResponse(BaseModel):
    success: bool
    message: str
    filename: Optional[str] = None