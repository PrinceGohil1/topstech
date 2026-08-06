#Given a list of order IDs like ['ORD1234', 'ORD5678', 'ORD9999', 'ORD0001'], use re.match() to filter and print only those IDs that end with an even number.<br><br><em><strong>Hint:</strong> Use a regular expression that checks if the last digit is 0, 2, 4, 6, or 8.</em>

import re

orders = ["ORD1234", "ORD5678", "ORD9999", "ORD0001"]

pattern = r"ORD\d*[02468]$"

for order in orders:
    if re.match(pattern, order):
        print(order)