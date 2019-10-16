def main():
    i=0
    numar=int(input("dati cifrele"))
    while(numar):
        cif[i]=numar%10
        i+=1
        numar//=10
    for x in range(0,i):
        print(cif[x]," ")

