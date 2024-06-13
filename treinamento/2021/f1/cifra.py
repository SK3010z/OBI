P = str(input())
cifra = ""
alfabeto = "abcdefghijklmnopqrstuvxz"
vogais = "aeiou"
Ivogais = [0,4,8,14,20,100]
for letra in P:
    sigla = ""
    sigla += letra
    if letra not in vogais:
        Iconsoante = alfabeto.index(letra)
        for i,ivogal in enumerate(Ivogais):
            anterior = ivogal
            proxima = Ivogais[i + 1]
            if Iconsoante < proxima:
                break
        if (proxima - Iconsoante < Iconsoante - anterior):
            proxima_vogal = str(alfabeto[proxima])
        else:
            proxima_vogal = str(alfabeto[anterior])


        proxima_letra = str(alfabeto[Iconsoante + 1])
        if proxima_letra == proxima_vogal:
            proxima_letra = str(alfabeto[Iconsoante + 2])
        sigla += proxima_vogal
        sigla += proxima_letra
    cifra += sigla


print(cifra)