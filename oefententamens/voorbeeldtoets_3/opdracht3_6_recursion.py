def pi_benadering(N):
    result = 0
    for i in range(N + 1):
        result += 4 * ((-1) ** i) / (2 * i + 1)
    return result, N


def bereken_pi_met_nauwkeurigheid(decimalen):
    nauwkeurigheid = 10 ** (-decimalen)
    vorige_benadering = 0
    huidige_benadering = 0
    N = 0

    while True:
        huidige_benadering += 4 * ((-1) ** N) / (2 * N + 1)

        if abs(huidige_benadering - vorige_benadering) < nauwkeurigheid:
            return round(huidige_benadering, decimalen), N

        vorige_benadering = huidige_benadering
        N += 1


# Benader π met 3 decimalen nauwkeurigheid
pi_met_3_decimalen, N_value = bereken_pi_met_nauwkeurigheid(4)
print(pi_met_3_decimalen, N_value)

