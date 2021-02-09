"""
Power set - Given a string, generate all subsets of it

i/p: "abc", o/p: "", "a", "b", "c", "ab", "ac", "abc"
i/p: "ab", o/p: "", "a", "b", "ab"

In general, if there are n characters in input string, there will
be 2^n subsets.

Idea:
Since there will be 2^n subsets
- Generate a counter from 0 to 2^n
- Use binary representation of the counter.
- Assign characters to iindividual bits.
- Iterate on bits of the counter and for the bits that are set add
corresponding characters to the result.

Logic: Input 1
We add "a" id rightmost first bit is set, "b" for second and "c" for third.

counter | Counter (binary)  | subset
    0   |       000         |   ""
    1   |       001         |   "a"
    2   |       010         |   "b"
    3   |       011         |   "ab"
    4   |       100         |   "c"
    5   |       101         |   "ac"
    6   |       110         |   "bc"
    7   |       111         |   "abc"

Time complexity: Theta(2^n * n)
"""


def powerSet(str):
    res = []
    n = len(str)
    powSize = pow(2, n)
    for i in range(powSize):  # run loop for counter
        tmp = []
        for j in range(n):  # traverse through string
            # for every character, check if corresponding bit is set
            # in counter
            if i & (1 << j) != 0:
                tmp.append(str[j])  #
        res.append("".join(tmp))
    return res


def test_powerSet():
    assert (powerSet("abc")) == ["", "a", "b", "ab", "c", "ac", "bc", "abc"]
    assert (powerSet("ab")) == ["", "a", "b", "ab"]
