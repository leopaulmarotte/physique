#%%

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
    return dico



def Euler(q, gamma) : 
    P = 1000000
    t=[1880 + i for i in range(141)]
    l=names(1880, 2020)['Diane']
    y = [l[0][1]]
    K = int(P*(q)/(q + gamma))
    q = alpha + beta
    print(y)
    def f(x):
        return q*x*(1-(x/K))
    for i in range(1, len(t)):
        y.append(y[i-1] + f(y[i-1]))
    print(y)
    
    plt.plot(t,y) 
    plt.show()



#%%