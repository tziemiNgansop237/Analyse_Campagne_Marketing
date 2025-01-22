
##foncttion pour le calcul du taux de conversion

def Taux_conversion(data):
        #calcul du taux de convertion global
        #nombre d'utilisateurs uniques
    n_unique_users = data["user_id"].nunique()
    print("le nombre d'utilisateurs uniques est :",n_unique_users )

        #nombre d'utilisateurs uniques ayants souscrit au service
    n_souscripteurs = data[data['converted']==True]['user_id'].nunique()
    print("\n")
    print("le nombre d'utilisateurs uniques ayant souscrit au forfait est :",n_souscripteurs)

    #Taux de convertion global
    taux_conv_global = n_souscripteurs/n_unique_users
    print("\n")
    taux = taux_conv_global*100

    print("le taux de conversion global est egal à :",round(taux,2),"%")

    return taux

def Taux_retention(data):
        #calcul du taux de convertion global
        #nombre d'utilisateurs uniques
    retained = data[data['is_retained']==True]['user_id'].nunique()
    print("le nombre de personnes restés abonnés est :",retained )

        #nombre d'utilisateurs uniques ayants souscrit au service
    n_souscripteurs = data[data['converted']==True]['user_id'].nunique()
    print("\n")
    print("le nombre d'utilisateurs uniques ayant souscrit au forfait est :",n_souscripteurs)

    #Taux de convertion global
    taux_reten_global = retained/n_souscripteurs
    print("\n")
    taux = taux_reten_global*100
    
    print("le taux de conversion global est egal à :",round(taux,2),"%")

    return taux

