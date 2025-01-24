
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
        #calcul du taux de retention global
        #nombre d'utilisateurs uniques
    retained = data[data['is_retained']==True]['user_id'].nunique()
    print("le nombre de personnes restés abonnés est :",retained )

        #nombre d'utilisateurs uniques ayants souscrit au service
    n_souscripteurs = data[data['converted']==True]['user_id'].nunique()
    print("\n")
    print("le nombre d'utilisateurs uniques ayant souscrit au forfait est :",n_souscripteurs)

    #Taux de retention global
    taux_reten_global = retained/n_souscripteurs
    print("\n")
    taux = taux_reten_global*100
    
    print("le taux de conversion global est egal à :",round(taux,2),"%")

    return taux



#Taux de retention par canal

def Taux_retention_par_variable(data,variable):
        #calcul du taux de retention par canal
        #nombre d'utilisateurs uniques
    retained = data[data['is_retained']==True].groupby(variable)['user_id'].nunique()
   # print("le nombre de personnes restés abonnés par ",variable," est :")
   # print(retained)

        #nombre d'utilisateurs uniques ayants souscrit au service par canal
    n_souscripteurs = data[data['converted']==True].groupby(variable)['user_id'].nunique()
    print("\n")
   # print("le nombre d'utilisateurs uniques ayant souscrit au forfait par",variable," est :")
    #print(n_souscripteurs)

    #Taux de retention par canal
    taux_reten_canal = retained/n_souscripteurs
    print("\n")
    taux = taux_reten_canal*100
    taux.sort_values(ascending=False)
    
    #print("le taux de conversion global est egal à :",round(taux,2),"%")

    return taux


#taux de conversion par canal


def Taux_conversion_par_variable(data,variable):
        #calcul du taux de retention par canal
        #nombre d'utilisateurs uniques
    n_users = data.groupby(variable)['user_id'].nunique()
   # print("le nombre de personnes restés abonnés par ",variable," est :")
  #  print(n_users)

        #nombre d'utilisateurs uniques ayants souscrit au service par canal
    n_souscripteurs = data[data['converted']==True].groupby(variable)['user_id'].nunique()
    print("\n")
   # print("le nombre d'utilisateurs uniques ayant souscrit au forfait par",variable,"  est :")
   # print(n_souscripteurs)

    #Taux de retention par canal
    taux_reten_canal = n_souscripteurs/n_users
    print("\n")
    taux = taux_reten_canal*100
    taux.sort_values(ascending=False)
    
    #print("le taux de conversion global est egal à :",round(taux,2),"%")

    return taux