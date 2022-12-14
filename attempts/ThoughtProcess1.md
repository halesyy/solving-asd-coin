
Begun at 11:24am, 3rd of September.

# Start

12 sides to this coin.
Design is in thirds.
Think about braile, hexadecimal, binary.

I'm guessing each third is a layer, the
outer layer is a layer, and Side B is a layer. No this doesn't seem true, as there's little info in two of the thirds.

--

Outer ring, 3-bit encoding.

.

--

Inner ring, 2-bit encoding.

-----------

# Problem 1:

Side A (SA) has dots under each letter, in a matrix which seems to max out at 2x2. The matrix for the given letters is defined as:

B    T    H    A    S    A
1 1  1 0  1 1  1 0  1 0  1 1
0 0  1 0  1 0  0 0  0 1  0 1

B    T    H    A    S    A
X X  1 0  X X  X 0  X 0  X X
0 0  X 0  X 0  0 0  0 X  0 X

Parsed as 1/2/3/4 grid vals.
B = 1 2   = 2
T = 1 3   = 4
H = 1 2 3 = 6
A = 1     = 1
S = 1 3   = 4
A = 1 2 4 = 7
= A B T/S H A

Parsed as Binary.
    8 4 2 1
B = 1 1 0 1 = 13
T = 1 0 1 0 = 10
H = 1 1 1 0 = 14 (wikipedia 14 commonwealth counties?)
A = 1 0 0 0 = 1
S = 1 0 0 1 = 9
A = 1 1 0 1 = 13

Ordered.
A S T B/A H

Parsed as RevBinary (0=1, 1=0).
B = 2
T = 5
H = 1
A = 7
S = 6
A = 2
Ordered.
H A/B T S A

This one is annoying, I'm wanting to move onto the ones that look more like actual cryptographic solutions.

Braile was a mentioned idea from an article, as describing the problem, so I will move into that.

Normal: A T H   A S A
Braile: C B F   A E D

Braile is A B C D E F, which could be a guide.
Rearrange using Braile A-F as the key makes:
A T A A S H = Wikipedia
https://en.wikipedia.org/wiki/Abdirizak_Ibrahim_Mohamed_Attash ??
Bingo!
Oops no.

-

Normal: B T H A S A
Braile: C B F A E D
-------------------
Recons: A T B A S H

Great, we now have ATBASH which is something I am to Google immediately. https://en.wikipedia.org/wiki/Atbash
SOLVED.

-----------


"ELIZABETH II - AUSTRALIA - 2022 - 50 CENTS"
"1947-2022 - 75 - REVEAL AND PROTECT - AUSTRALIAN SIGNALS DIRECTORATE"

# Ok, problem 2.
What I believe is to be done here, is to take in the raw string which I believe is 3-bit encoded. The raw text is:

Full string:
.DVZIVZFWZXRLFHRMXLMXVKGZMWNVGRXFOLFHRMVCVXFGRLM.URMWXOZIRGBRM7DRWGSC5WVKGS

(Interpretation done using `prob_2_safesplit.py` to parse out unique parts)

Encoding A:
DRFHRMVKGNVRXFFHRVXGR.URWOIRDWCWG = 33 length. (bold)

Encoding C/B:
VZIVFWZXXMXWLCFMZGM7G5KS = 24 length. (normal)

Encoding B:
.ZLLZMGOMVLMXRBRSV = 18 length. (shaded)

Total length of all letters is 33+18+24 = 75.

Atbash is literally just a reversal of the alphabet to directly inverse the values.

Through ABCDEFGHIJKLMNOPQRSTUVWXYZ

".WEAREAUDACIOUSINCONCEPTANDMETICULOUSINEXECUTION.FINDCLARITYIN7WIDTHX5DEPTH"

WE ARE AUDACIOUS IN CONCEPT AND METICULOUS IN EXECUTION
FIND CLARITY IN 7 WIDTH X 5 DEPTH

-----------

# Ok, Problem 3.

"1947-2022 - 75 - REVEAL AND PROTECT - AUSTRALIAN SIGNALS DIRECTORATE"

From Problem 2, we have a 7x5 matrix. This equals 35, but the full string is 70 in length which would be 7x10. I'll attempt to break it down into two 7x5 chunks.

7 5 = 75 years.

Full string:
BGOAMVOEIATSIRLNGTTNEOGRERGXNTEAIFCECAIEOALEKFNR5LWEFCHDEEAEEE7NMDRXX5

BGOAMVOEIATSIRLNGTTNEOGRERGXNTEAIFC
ECAIEOALEKFNR5LWEFCHDEEAEEE7NMDRXX5

Breaking it down into x7 matrixes:
BGOAMVO
EIATSIR
LNGTTNE
OGRERGX
NTEAIFC

Transcribed into:

Belonging to a great team striving for excellence
we make a difference xor hex a5d75
xa5d75

ECAIEOA
LEKFNR5
LWEFCHD
EEAEEE7
NMDRXX5

Breaking it down into x5 matrixes:
BGOAM
VOEIA
TSIRL
NGTTN
EOGRE
RGXNT
EAIFC

ECAIE
OALEK
FNR5L
WEFCH
DEEAE
EE7NM
DRXX5

Encoding A:
BOEAIRLTOGXNTFECAOEKRWEEAEMDX = 29 length.

Encoding B:
GOAMVITSNGTNEGREREAICIEALFN5LFCHDEEE7NRX5 = 41 length.

Total length of all letters is 29+41 = 70.

-----------

# Problem 4:

Belonging to a great team striving for excellence
we make a difference xor hex a5d75

"1947-2022 - 75 - REVEAL AND PROTECT - AUSTRALIAN SIGNALS DIRECTORATE"

I googled "xa5d75" and this link was the first to come up... https://www.yh168.xyz/ ... and I don't think this is the solution.

I presume I need to xor/hex something, but I'm not completely over how these logic gates work. Hexadecimal means I am to pair these into two's, so I'll do that over in `prob_4_hex.py`. From there, it's the bonus challenge!

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

Hexadecimal.

Message:

For 75 years the Australian Signals Directorate has brought together people with the skills, adaptability and imagination to operate in the slim area between the difficult and the impossible.

See `prob_4_xor_hex.py` for how it was calculated.

-----------

There are two problems, of the three there could be:
- Outer ring shadings.
- Inner ring shadings.
- Shapes on bottom.
# Ok, bonus level...

I believe it has something to do with the differing encodings (bold, semi-shading, normal) with some of the text.

## OUTER RING:
.DVZIVZFWZXRLFHRMXLMXVKGZMWNVGRXFOLFHRMVCVXFGRLM.URMWXOZIRGBRM7DRWGSC5WVKGS

## Broken down into:
.ZLLZMGOMVLMXRBRSV = 18 length. (shaded)
DRFHRMVKGNVRXFFHRVXGR.URWOIRDWCWG = 33 length. (bold)
VZIVFWZXXMXWLCFMZGM7G5KS = 24 length. (normal)

## With their output being:
".WEAREAUDACIOUSINCONCEPTANDMETICULOUSINEXECUTION.FINDCLARITYIN7WIDTHX5DEPTH"

---

## INNER RING:
BGOAMVOEIATSIRLNGTTNEOGRERGXNTEAIFCECAIEOALEKFNR5LWEFCHDEEAEEE7NMDRXX5

## Broken down into:
B OE A IRL T O GXNT F ECA O EK R WE EA E MD X = 29 length. (normal)
GOAMV I TS NGT NE GRER EAI C IE AL FN 5L FCHDE EE 7N RX 5 = 41 length. (bold)

BOEAIRLTOGXNTFECAOEKRWEEAEMDX = 29 length. (normal)
GOAMVITSNGTNEGREREAICIEALFN5LFCHDEEE7NRX5 = 41 length. (bold)

# Normals together.
VZIVFWZXXMXWLCFMZGM7G5KS
BOEAIRLTOGXNTFECAOEKRWEEAEMDX

# Bolds together.
DRFHRMVKGNVRXFFHRVXGR.URWOIRDWCWG
GOAMVITSNGTNEGREREAICIEALFN5LFCHDEEE7NRX5

# Extra shaded.
.ZLLZMGOMVLMXRBRSV

## With their output being:
"Belonging to a great team striving for excellence
we make a difference xor hex a5d75"

As well, as have some odd shapes under Side A:

CIRCLE
SQUARE
GRID: CIRCLE, SQUARE, CIRCLE, CIRCLE
SQUARE
CIRCLE
GRID: SQUARE, SQUARE, SQUARE, CIRCLE

With 6 total "groups" or "items", but if broken down:

CIRCLE
SQUARE
CIRCLE
SQUARE
CIRCLE
CIRCLE
SQUARE
CIRCLE
SQUARE
SQUARE
SQUARE
CIRCLE

Which is a total of 12 "things", which is binary for (both ways):

101011010001 = 2769
010100101110 = 1326

Sub = 1443.

--------

I think that the hex being added  

.DVZIVZFWZXRLFHRMXLMXVKGZMWNVGRXFOLFHRMVCVXFGRLM.URMWXOZIRGBRM7DRWGSC5 WVKGS
BGOAMVOEIATSIRLNGTTNEOGRERGXNTEAIFCECAIEOALEKFNR5LWEFCHDEEAEEE7NMDRXX5 A5D75
