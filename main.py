def sonni_raqamlari_teskari_bilan_koypaytir(sonlar):
    yangi_sonlar = []
    for son in sonlar:
        raqamlar = [int(x) for x in str(son)]
        teskari = int(''.join(map(str, raqamlar[::-1])))
        yangi_son = son * teskari
        yangi_sonlar.append(yangi_son)
    return yangi_sonlar

sonlar = [12, 34, 56, 78, 90]
print(sonni_raqamlari_teskari_bilan_koypaytir(sonlar))
