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


