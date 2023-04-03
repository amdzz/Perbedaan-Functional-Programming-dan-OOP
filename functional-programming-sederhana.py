def kuadrat(List): #fungsi untuk mengkuadratkan item dari list
    newList = []
    for i in List:
        newList.append(i**2)

    return newList

listSebelum = [1,2,3,4,5] #list awal yang akan dikuadratkan
listSesudah = kuadrat(listSebelum) 

print("List Sebelumnya:", listSebelum)
print("List Sesudah:", listSesudah)
