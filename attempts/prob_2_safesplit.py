
# @Author Jack Hales

import json
from bs4 import BeautifulSoup

# Problem two solution space.
# Extracted from here:
# - https://www.asd.gov.au/75th-anniversary/events/commemorative-coin-challenge#no-back
raw_html = """
<div>
    <u>.</u><strong>D</strong>VZIV<u>Z</u>FWZX<strong>R</strong><u>L</u><strong>FHRM</strong>X<u>L</u>MX<strong>VKG</strong><u>ZM</u>W<strong>NV</strong><u>G</u><strong>RXF</strong><u>O</u>L<strong>FHR</strong><u>M</u><strong>V</strong>C<u>V</u><strong>X</strong>F<strong>GR</strong><u>L</u>M<strong>.UR</strong><u>M</u><strong>W</strong><u>X</u><strong>O</strong>Z<strong>I</strong><u>R</u>G<u>B</u><strong>R</strong>M7<strong>D</strong><u>R</u><strong>W</strong>G<u>S</u><strong>C</strong>5<strong>W</strong><u>V</u>K<strong>G</strong>S</p>
</div>
"""

# Fill iteratively, so it can be used on both problems.
groups = {}

# Interpet as soup.
soup = BeautifulSoup(raw_html, "html.parser")
cont = soup.find("div")
for child in cont.children:
    name = child.name or "normal"
    text = child.text.strip() # Assumption.
    # Ignore empty text. Assumption.
    if text == "":
        continue
    # Create group.
    if name not in groups:
        groups[name] = ["", 0]
    # Add text to group.
    groups[name][0] += text

# Populate the length of the values.
groups = {k: [v[0], len(v[0])] for k, v in groups.items()}

print(json.dumps(groups, indent=4))
