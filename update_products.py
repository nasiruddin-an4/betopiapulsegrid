import os
import re

file_path = 'products.html'

with open(file_path, 'r') as f:
    content = f.read()

# Replace any Lithium (LiFePO4) Battery</li> with Lithium (LiFePO4) Battery</li>\n                    <li>Backup Time: 2-4 hours</li>
if 'Backup Time: 2-4 hours' not in content:
    content = re.sub(
        r'(Lithium \(LiFePO4\) Battery</li>)',
        r'\1\n                    <li>Backup Time: 2-4 hours</li>',
        content
    )
    with open(file_path, 'w') as f:
        f.write(content)
    print("Updated products.html")
else:
    print("Already updated products.html")
