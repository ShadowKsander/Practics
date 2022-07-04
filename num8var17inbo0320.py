def main(vhod):
    vhod = vhod.replace(" ", "")
    ans = {}
    while(vhod.find(";") != -1):
        key = vhod.find("==>")+3
        key1 = vhod.find(";")
        keyfin = vhod[key:key1]
        vhod1 = vhod[(vhod.find("{")+1):(vhod.find("}")+1)]
        vhod1 = vhod1.replace("}", ".")
        itog = []
        while(vhod1.find(".") != -1):
            val = vhod1.find("#")+1
            val1 = vhod1.find(".")
            valfin = vhod1[val:val1]
            itog.append(int(valfin))
            vhod1 = vhod1[val1+1:]
        ans[keyfin] = itog
        vhod = vhod[vhod.find("),")+2:]
    return ans


print(main("( decl { #3128 . #-960 . #6458} ==> zaesbi; ),( decl {#-3885 .#2245 .#-8598 . #7167 } ==> orgeed_907; ),"
           "( decl { #1758 .#2389 } ==>telaer_9; ),( decl { #-3519 . #9087 .#-2137 . #-2807 } ==>reen_311;),"))
