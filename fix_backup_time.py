import re

with open('products.html', 'r') as f:
    content = f.read()

content = re.sub(r'>\d+-\d+ hours of backup<', '>2-4 hours of backup<', content)

with open('products.html', 'w') as f:
    f.write(content)

print("Updated backup times in products.html")
