def pays():
    pays_input = input("Veuillez indiquer votre pays d'origine :")
    if pays_input == "France":
        print ("Les frais de port se montent à CHF 4.90")
    elif pays_input == "Allemagne":
        print ("Les frais de port se montent à CHF 5.90")
    elif pays_input == "Espagne":
        print ("Les frais de port se montent à CHF 3.90")
    elif pays_input == "Portugal":
        print ("Les frais de port se montent à CHF 5.90")
    else :
        print ("Les commandes ne sont pas disponibles depuis ce pays")

def coupon():
    coupon_input = input("Veuillez saisir votre numéro de coupon : ")
    coupon = "0000"
    if coupon_input == coupon:
        input("Vous bénéficiez de 20% pourcent sur votre commande")
        input("Vous bénéficiez également de la gratuité des frais de port")
    else:
        print ("Pas de rabais, coupon non valide")

pays()
coupon()
