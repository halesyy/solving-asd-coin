
# @Author Jack Hales

import json
from bs4 import BeautifulSoup

# Problem two solution space.
# Extracted from here:
# - https://www.asd.gov.au/75th-anniversary/events/commemorative-coin-challenge#no-back
raw_html = """
<div>
    B<strong>GOAMV</strong>OE<strong>I</strong>A<strong>TS</strong>IRL<strong>NGT</strong>T<strong>NE</strong>O<strong>GRER</strong>GXNT<strong>EAI</strong>F<strong>C</strong>ECA<strong>IE</strong>O<strong>AL</strong>EK<strong>FN</strong>R<strong>5L</strong>WE<strong>FCHDE</strong>EA<strong>EE</strong>E<strong>7N</strong>MD<strong>RX</strong>X<strong>5</strong>
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
