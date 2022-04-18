import random
NUMACCNTS = 10
NUMTRANS = 20
def main():
    f1 = open("accounts.dat","w")
    for i in range(NUMACCNTS):
        f1.write("{:04d} {:013.2f}\n".format(i+1,(100*random.random())**2))
    f1.close()

    f2 = open("transactions.dat","w")
    for i in range(NUMTRANS):
        accnt1 = random.randint(1,NUMACCNTS)
        accnt2 = accnt1
        while(accnt2 == accnt1):
            accnt2 = random.randint(1,NUMACCNTS)
        f2.write("{:04d} {:04d} {:013.2f}\n".format(accnt1,accnt2,1000*random.random()))
    f2.close()
if __name__=="__main__":
    main()
