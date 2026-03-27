def tiersort(tab, start, end, step):
    length = len(tab)
    if (start == 0 and end == length):
        step+=1
        tiersort(tab,0,int(2*length/3), step)
    else:
        if step == 3:
            return
        else :
            step+=1
            sort(tab, start, end)
            tiersort(tab,int(length/3),length, step)

def sort(tab , start, end):
    subtab = tab[start:end]
    if(start > 0):
        other = tab[0:start]
        subtab.sort()
        tab = other + subtab
    else:
        other = tab[end:len(tab)]
        subtab.sort()
        tab = subtab + other
    print("Tab ", tab)

tab= [2,15,6,12,9]
print("Debut", tab)
print(tiersort(tab,0,len(tab), 0))
