# Write a function called get_vat() with 2 parameters, price and vat percentage
# It calculates and returns the VAT (value-added tax).
# YOUR CODE STARTS HERE

def get_vat(price, vat_percentage):
    VAT = price * vat_percentage / 100

    return VAT