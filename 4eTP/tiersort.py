def tiersort(tab, start, end, step):
    length = len(tab)
    if (start == 0 and end == len(tab)):
        tiersort(tab,0,int(2*length/3), step+1)
    subtab = tab[start:end]
    if(start > 0):
        other = tab[0:start]
        subtab.sort()
        tab = other + subtab
    else:
        other = tab[end:len(tab)]
        subtab.sort()
        tab = subtab + other
    if(start == 0 and end != length ):
        if step == 3:
            print(tab)
            return tab
        else :
            tiersort(tab,int(length/3),length, step+1)

tab= [2,5,6,12,9]
print("Debut", tab)
tiersort(tab,0,len(tab), 0)