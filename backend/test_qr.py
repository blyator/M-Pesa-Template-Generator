from app.services.qr_generator import generate_qr_code

# Generate a QR code for Till payment
qr_data = "Till: 123456\nAmount: KES 1,000"
qr_buffer = generate_qr_code(qr_data, size=400)

# Save it 
with open("test_qr.png", "wb") as f:
    f.write(qr_buffer.getvalue())

print("✓ QR code generated! Check test_qr.png")
print("Try scanning it with your phone camera!")
