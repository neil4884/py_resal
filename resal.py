import math


def resal(dzdt1: float, D: float,
          Lambda: float, PropDensity: float,
          Covolume: float, Gamma: float, Force: float,
          n1: float, Beta: float, Alpha: float,
          W: float, C: float, Pstart: float, fixResist: float,
          varResist: float, Vol0: float, Vol1: float,
          Bore: float, LBarrel: float, AreaLeakFrac: float,
          DeltaT: float, DeltaTPrint: float,
          F: float = 1, z1: float = 0, T: float = 0,
          Tprint: float = 0, LinePrint = 1,
          X: float = 0, V: float = 0, N: float = 10**(-5), P: float = 101324.6
          ):

    P0 = 101324.6
    R = 8.31696
    F0 = 0
    nR = n1 * R
    Cv = R * n1 / (Gamma - 1)
    Area = 0.25 * math.pi * Bore ** 2
    LEquiv = (Vol0 + Vol1) / Area
    AreaLeak = AreaLeakFrac * Area

    while (X <= LBarrel):
        if X == 0 and P <= Pstart:
            Volume = Vol0
        if X == 0 and P > Pstart:
            Volume = Vol0 + Vol1
        if X > 0:
            Volume = Vol0 + Vol1 + Area * X

    return


def dFdt(dD: float, dB: float, dA: float, dP: float, dF, dF0) -> float:
    if dP < 0:
        dP = 0
    out = -(dB / dD * dP ** dA)
    if dF <= 0:
        out = 0
    return out
