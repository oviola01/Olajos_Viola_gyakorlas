szam = 21
oszto = 2
prim_e = True
while oszto < szam ** 0.5 and prim_e == True:
    if szam % oszto == 0:
         prim_e = False
    oszto += 1
    print(prim_e)
    print(oszto)
print(prim_e)