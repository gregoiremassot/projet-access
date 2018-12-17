import pandas as pd
from random import randint

Client = pd.read_csv("Client.txt", encoding="latin1", header=0, sep=";")
Livreur = pd.read_csv("Livreur.txt", encoding="latin1", sep=";")
Plat = pd.read_csv("Plat.txt", encoding="latin1", sep=";")
Restaurant = pd.read_csv("Restaurant.txt", encoding="latin1", header=0, sep=";")

# On crée la table "portions"
portions = pd.DataFrame(columns=['ID_Plat', 'quantite', 'ID_Commande'])
commandes = pd.DataFrame(columns=['ID_Commande', 'ID_Client', 'date', 'ID_Livreur'])

Plat_Restaurant = pd.merge(Restaurant, Plat, on=['ID_Restaurant'])
Plat_Restaurant_Client = pd.merge(Plat_Restaurant, Client, on=['Ville'])
Client_Livreur = pd.merge(Livreur, Client, on=['Ville'])

nb_lignes = Plat_Restaurant_Client.shape[0]
nbCommandes = 50

# On boucle pour créer nbCommandes
j = 1
for i in range(1,nbCommandes+1):
    ID_Portion = 0
    num_ligne = randint(1,nb_lignes)
    ligne = Plat_Restaurant_Client.loc[[num_ligne]]
    ID_Restaurant = Plat_Restaurant_Client.at[num_ligne,'ID_Restaurant']
    ID_Client = Plat_Restaurant_Client.at[num_ligne, 'ID_Client']
    ID_Commande = i

    choix_plats = Plat[Plat['ID_Restaurant'] == ID_Restaurant]
    choix_plats = choix_plats.reset_index()
    nb_choix = choix_plats.shape[0]

    #print(choix_plats)
    nb_portions_commandes = 0
    max_nb_portions_commandes = randint(1, 5)

    while nb_portions_commandes < max_nb_portions_commandes:
        nb_portions = randint(1,3)
        plat_choisi = randint(0, nb_choix - 1)
        ID_Plat = choix_plats.at[plat_choisi, 'ID_Plat']
        nb_portions_commandes += nb_portions
        portions.loc[j] = [ID_Plat, nb_portions, ID_Commande]
        j += 1

    date_commande = str(randint(1,27)) + str(randint(1,12)) + "2018"
    Livreurs_a_proximite = Client_Livreur[Client_Livreur['ID_Client'] == ID_Client]
    Livreurs_a_proximite = Livreurs_a_proximite.reset_index()
    #print(Livreurs_a_proximite)
    livreur_commande =  randint(0, Livreurs_a_proximite.shape[0]-1)
    ID_Livreur = Livreurs_a_proximite.at[livreur_commande, 'ID_livreur']
    commandes.loc[i] = [ID_Commande,ID_Client, date_commande, ID_Livreur]

portions.to_csv("portions.csv", index=False)
commandes.to_csv("commandes.csv", index=False)