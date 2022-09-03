
# Going to be maninupating/testing this to
# get an idea for the structure/info behind
# it.
assumed_hex = """
E3B
8287D4
290F723381
4D7A47A291DC
0F71B2806D1A53B
311CC4B97A0E1CC2B9
3B31068593332F10C6A335
2F14D1B27A3514D6F7382F1A
D0B0322955D1B83D3801CDB2
287D05C0B82A311085A03329
1D85A3323855D6BC333119D
6FB7A3C11C4A72E3C17CCB
B33290C85B6343955CCBA3
B3A1CCBB62E341ACBF72
E3255CAA73F2F14D1B27A
341B85A3323855D6BB33
3055C4A53F3C55C7B22
E2A10C0B97A291DC0F
73E3413C3BE392819
D1F73B331185A33
23855CCBA2A3
206D6BE383
1108B
"""

chunks = lambda li, size=2: [li[i:i+2] for i in range(0, len(li), size)]

xor_part = "A5D75"

# Manipulate into proper format.
assumed_hex = assumed_hex.strip()
assumed_hex = "".join(assumed_hex.split("\n"))
hex_pairs = chunks(assumed_hex, 2)

print(f"> Hex is '{len(assumed_hex)}' long")
# print(f"> Pairs:", hex_pairs)

# A quick google showed that XOR bitwise is ^ in Python.
# So, I tried using hexadecimal raw types in Python
# by opening up a REPL and doing:
# int(0xE) ^ int(0xA) which resulted in 4, which is
# not large enough to be a ascii-readable integer, but
# when using pairs, we get 70 and 111 respectively, which
# map to "Fo" in ascii each characters.
# But, using pairs will eventually fail since we don't have
# a pair for 5 onwards, so either duplicate it to map, or
# iteratively use modula. Anyway, let's give it a go.

iter_xor_keys = [
    "A5",
    "D7",
    "5A",
    "5D",
    "75"
]
pointer = 0
results = ""
for pair in hex_pairs:
    value = int(pair, 16) # base-16
    # Key retrieval, and casting.
    select_xor_key = iter_xor_keys[pointer % 5] # using 5-based pointer
    select_xor_val = int(select_xor_key, 16)
    # Bitwise compile using xor + hex.
    bitwise_result = value ^ select_xor_val
    result_character = chr(bitwise_result)
    results += result_character
    pointer += 1

print(results)
