import re

text = "Call +91-987-654-3210 or 987-654-3210"

phone_numbers = re.findall(r"(?:\+?\d{1,3}[-.\s]?)?\d{3}[-.\s]?\d{3}[-.\s]?\d{4}", text)
print(phone_numbers)
