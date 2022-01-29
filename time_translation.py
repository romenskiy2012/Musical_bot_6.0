
def timeL(my_st):
    SAS = my_st.split(":")
    SAS.reverse()
    print(SAS)
    f = 0
    L = 0
    Q = (1, 60, 3600)
    for SUS in SAS:
        f = f + int(SUS) * Q[L]
        L = L + 1
    print(f"SAS - {f}")
    return f
