import os
import glob
import re

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r') as file:
        content = file.read()
    
    modified = False

    # Update Pricing Plan List
    if 'Lithium (LiFePO4) Battery\n                </li>' in content and 'Backup time 2-4 hours' not in content:
        content = content.replace(
            'Lithium (LiFePO4) Battery\n                </li>',
            'Lithium (LiFePO4) Battery\n                </li>\n                <li class="list-unstyled d-flex align-items-start gap-2 text-small text-color-1">\n                  <i class="bi bi-check2 text-heading-color-1"></i> Backup time 2-4 hours\n                </li>'
        )
        content = re.sub(
            r'<li class="list-unstyled d-flex align-items-start gap-2 text-small text-color-1">(\s*<i.*?Lithium \(LiFePO4\) Battery\n                </li>)',
            r'<li class="list-unstyled mb-2 d-flex align-items-start gap-2 text-small text-color-1">\1',
            content
        )
        modified = True

    # Update Calculator Array
    if '["Battery",      pkg.bat],' in content and '"Backup Time"' not in content:
        content = content.replace(
            '["Battery",      pkg.bat],',
            '["Battery",      pkg.bat],\n      ["Backup Time",  "2-4 hours"],'
        )
        modified = True

    if modified:
        with open(f, 'w') as file:
            file.write(content)
        print(f"Updated {f}")
