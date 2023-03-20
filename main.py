import matplotlib.pyplot as plt






def names(year1, year2):
    dico = {}
    for i in range(year1, year2):
        with open('namess/yob' + str(i) + '.txt') as file:
            ligne = file.readline().split(',')
            nom = ligne[0]
            nb = int(ligne[2])
            while nb > 5:
                if nom not in dico:
                 dico[nom] = []
                dico[nom].append((i, nb))
                ligne = file.readline().split(',')
                nom = ligne[0]
                nb = int(ligne[2])
    print(dico)


def f(alpha, beta, gamma, N):
    P =
    K = P*(alpha+beta)/(alpha + beta + gamma)
    return (alpha + beta)*N*(1 - N/K)




def Euler(f,a,t0,T,n) : 
    dt=T/n
    t=[t0+i*dt for i in range(n+1)]
    y=[a]
    
    for i in range(1,n+1):
        y . append ( y [ i - 1 ] + dt * f ( y [ i - 1 ] ) )
    plt.plot(t,y) plt.show()


#def f(x,t) : #fonction f pour tester
    #return x


