
def hanoi(n):
    tour1= ""
    for i in range(1,n):
        tour1+= str(i)

    tour2 = ""
    tour3 = ""
    while(tour1 != ""):
        if (tour1 == "1"):
            print("Déplacer du pilier 1 vers 3")
            tour3=tour1[0]
            tour1 = ""
        else:
            if(tour2[0] > tour1[0]):
                print("Déplacer du pilier 1 vers 2")
            elif(tour3[0] > tour1[0]):
                print("Déplacer du pilier 1 vers 3")
    output = tour1
