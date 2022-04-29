def contatore(list_a):
    list_b = []
    list_c=[len(p) for p in list_a]
    for parola in list_a:
        list_b.append(len(parola))
    print(list_b)
    print(list_c)

lista = ['Milano', 'Roma', 'Cagliari', 'Croazia', 'Giappone']
print(lista)
contatore(lista)
