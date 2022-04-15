def contatore(list_a):
    list_b = []
    for parola in list_a:
        list_b.append(len(parola))
    print(list_b)


lista = ['Milano', 'Roma', 'Cagliari', 'Croazia', 'Giappone']
print(lista)
contatore(lista)
