def main(vhod):
    #vhod = vhod.replace(" ", "")
    ans = {}
    while(vhod.find(".") != -1):
        vhod = vhod[(vhod.find("@") + 2):]

        #key = vhod.find("@") + 2
        key1 = vhod.find("\"")
        keyfin = vhod[:key1]
        vhod1 = vhod[(vhod.find("\"") + 3):(vhod.find("]") + 1)]
        vhod1 = vhod1[:(vhod1.find("]"))]
        vhod1 = vhod1.replace("]", " ")
        itog = []
        while(vhod1.find(" ") != -1):
            #val = vhod1.find("#")+1
            val1 = vhod1.find(" ")
            valfin = vhod1[:val1]
            itog.append(valfin)
            vhod1 = vhod1[val1 + 1:]
        ans[keyfin] = itog
        vhod = vhod[vhod.find("]]") + 2:]
    return ans


print(main("[[ [[option @\"xexeon_344\" [bien oninra_321 ]. ]][[option @\"zaised\" [bisoon_631 xeat ridia reabi ]. ]] "
           "[[option @\"rixe_674\"[ risoti_946 beesin_100 soge_303 ].]] ]]"))
print(main("[[ [[ option @\"enarbe_650\" [xeen esla_795 ].]] [[option @\"sous\" [arcean_559 rais_511]. ]] ]]"))
