user_input_pays = input("Veuillez entrer votre pays : ")
user_input_montant = input("Veuillez entrer le montant :")

def pays():
    if user_input_pays == "France":
        message = "Les frais de port se montent à chf 20."
    elif user_input_pays == "Allemagne":
        message = "Les frais de port se montent à chf 25."
    else:
        message = "Les frais de port se montent à chf 50."
    print(message)

pays()

def montant():
    if user_input_montant >=100:
        message = "S'ajoutent chf 10."
    else:
        message = "S'ajoutent chf 20."
        print(message)

montant()   


