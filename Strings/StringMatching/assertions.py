from random import randint

from KMP.KMP import KMP
from RabinKarp.rabinKarp import RabinKarp
from ZAlgorithm.ZAlgorithm import ZAlgorithm


def occurrences(text: str, pattern: str) -> list[int]:
    if not pattern:
        return [0]

    res, start = [], -1
    while True:
        start = text.find(pattern, start + 1)
        if start != -1:
            res.append(start)
        else:
            return res


for cl in KMP, RabinKarp, ZAlgorithm:
    for i in range(100):
        text = "".join("".join(ch * randint(0, 20) for ch in "abc") for _ in range(randint(0, 10)))
        pattern = "".join(ch * randint(0, 10) for ch in "abc")

        expected = occurrences(text, pattern)
        result = cl.findMatches(text, pattern)

        try:
            assert (
                result == expected
            ), f"class={cl.__name__}\n{text}\npattern={pattern}\nexpected={expected}\nresult={result}"
        except AssertionError as error:
            print(error, end="\n\n")
