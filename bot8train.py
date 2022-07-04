

def main(vhod):
    vhod = vhod.replace(" ", "")
    ans = {}
    while (vhod.find(".end;") != -1):
        key = vhod.find("@") + 2
        key1 = vhod.find(".end") - 1
        keyfin = vhod[key:key1]
        vhod1 = vhod[vhod.find("{"):vhod.find("}") + 1]
        vhod1 = vhod1.replace("{", ",")
        itog = []
        while (vhod1.find(",") != -1):
            val = vhod1.find(",") + 1
            val1 = vhod1.find(",", 2)
            valfin = vhod1[val:val1]
            itog.append(valfin)
            vhod1 = vhod1[val1:]
        ans[keyfin] = itog
        vhod = vhod[key1+4:]
    return ans

print(main("|| .begin data {esar_755 ,dima , besore_527 }=: @\"riis\" .end;"
           " .begin data {zaleat_662 , soat , leorra_123} =:@\"aare\".end; ||"))

print(main("|| .begin data { cemadi_692,orbe , reonti_428 } =: @\"berier\" .end;"
           " .begin data { bebi_443 , rion_794,matima_166 ,gela_378 } =:@\"onanle\""
           " .end; .begin data { rezave , quso_771,anvece } =: @\"arlequ\".end;"
           " .begin data { tiso , zain , tele_227 }=: @\"raer\" .end;||"))




# def main(vhod):
#     vhod.replace(" ", "")
#     ans = {}
#     while(vhod.find("") != -1):
#         key = vhod.find()
#         key1 =
#         keyfin = vhod[:]
#         vhod1 = vhod[:]
#         vhod1.replace()
#         itog = []
#         while(vhod1.find("") != -1):
#             val = vhod1.find()
#             val1 =
#             valfin = vhod1[:]
#             itog.append(valfin)
#             vhod1 = vhod1[:]
#         ans[keyfin] = itog
#         vhod = vhod[:]
#     return ans

















