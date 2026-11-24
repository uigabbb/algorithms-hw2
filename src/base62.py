"""Base62 인코딩/디코딩."""

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = len(ALPHABET)  # 62
_INDEX = {ch: i for i, ch in enumerate(ALPHABET)}


def encode(n: int) -> str:
    """0 이상의 정수를 base62 문자열로 바꾼다."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n은 정수여야 합니다.")
    if n < 0:
        raise ValueError("n은 0 이상이어야 합니다.")
    if n == 0:
        return ALPHABET[0]

    chars = []
    while n > 0:
        n, r = divmod(n, BASE)
        chars.append(ALPHABET[r])
    return "".join(reversed(chars))


def decode(s: str) -> int:
    """base62 문자열을 정수로 바꾼다."""
    if not isinstance(s, str):
        raise TypeError("s는 문자열이어야 합니다.")
    if not s:
        raise ValueError("빈 문자열은 디코딩할 수 없습니다.")

    n = 0
    for ch in s:
        if ch not in _INDEX:
            raise ValueError(f"base62에 없는 문자입니다: {ch!r}")
        n = n * BASE + _INDEX[ch]
    return n


if __name__ == "__main__":
    for x in [0, 1, 61, 62, 12345, 2**64]:
        e = encode(x)
        print(x, "->", e, "->", decode(e))
