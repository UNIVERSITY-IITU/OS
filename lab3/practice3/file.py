def _convert(element, unit) -> float:
    if unit == "micro":
        return element * 1000
    if unit == "mili":
        return element * 1000000
    return element
def calc3(t1,t2,t3,h1,h2):
    return (h1 * t1) + (1-h1) * h2 * (t1+t2) + (1-h1) * (1-h2) * (t1+t2+t3)

def calc2(t1,t2,h):
    return t1 + (1-h)*t2
    
# 0.01
# 0.1
# 10




choose = input("level 1/2 : ")
unit = input("unit : ")
if choose == "1":
    t1 = float(input("T1 : "))
    t2 = float(input("T2 : "))
    t3 = float(input("T3 : "))
    h1 = float(input("H1 : "))
    h2 = float(input("H2 : "))
    res = calc3(
    _convert(t1, unit),
    _convert(t2, unit),
    _convert(t3, unit),
    h1,h2
    )
    print(res)

elif choose == "2": 
    t1 = float(input("T1 : "))
    t2 = float(input("T2 : "))
    h = float(input("H : "))
    res = calc2(
        _convert(t1, unit),
        _convert(t2, unit),
        h
    )
    print(res, ' {} second'.format("nano"))


a = [
    input(" 1 "),
    input(" 2 "),
    input(" 3 ")
]