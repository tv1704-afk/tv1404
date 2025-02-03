class The_exception():
    pass

def decor(funk):
    def obertka(v0,v,t):
        s = (v**2-v0**2)/2*(v-v0)/t
        funk(v0,v,t)
        print(s,"км")
    return(obertka)

@decor
def funk(v0,v,t):
    if t > 0:
        a = (v-v0)/t
        print(a, "м/с2")
    else:
        raise The_exception()

try:
    a = funk
except The_exception as e:
    print("неправильно")


funk(v0 = int(input("начальная скорость")),v = int(input("конечная скорость")),t = int(input("время")))