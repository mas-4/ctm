def maxBoth(S: list) -> complex:
    real = max(S, key=lambda s: s.real)
    imag = max(S, key=lambda s: s.imag)
    return real.real + imag.imag * 1j
