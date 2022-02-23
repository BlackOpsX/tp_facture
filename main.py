import copy
#TODO

#L'objectif de ce mini TP consite en la génération d'une facture.

produit = {
    "nom" : "<empty>",
    "prix" : 0,
    "quantité" : 0
}

myProductList = []
lineCount = 0
choix = ""

while choix != "non":
    nom=input("Entrer le nom du produit___")
    prix=int(input("Entrer le prix du produit___"))
    quantité=int(input("Entrer la quantité du produit___"))
    choix=input("Taper Entrer pour continuer ou 'non' pour arrêter___")

    print(f'nom: {nom}, prix: {prix}, quantité: {quantité}')
    
    produit["nom"]=nom
    produit["prix"]=prix
    produit["quantité"]=quantité
    currentProduit = copy.deepcopy(produit)
    myProductList.append(currentProduit)
    lineCount += 1 
    # total = prix*quantité
    # print("le total est : {}".format(total))

print(myProductList)
total=0
for produit in myProductList:
    total = total + produit["prix"]*produit["quantité"]
print ("le total est : {}".format(total))
