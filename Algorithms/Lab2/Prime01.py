def prime(n,k):
    p=1
    while(p<k):
        p*=n
    return p/n

def run():
    x=int(input("Numarul: "))
    lim=int(input("Limita: "))
    print(prime(x,lim))
    run()
 
def main():
    run()

if __name__ == "__main__":
    main()
