# that displays a number with a comma (,)
# as the thousands' separator (US and UK format)
# and with a period(.) as the thousands' separator (EU format).

number = int(float(input("Enter a number in the thousands:")))
new_number = f'{number:,}'
print(new_number)
print(new_number.replace(',', '.'))

