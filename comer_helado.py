
apetece_helado_input = input("¿Te apetece un helado? (Si/No) :").upper()
tiene_dinero_input = input("¿Tiene dinero para un helado? (Si/No) :").upper()
esta_la_heladeria_abierta_input = input("¿Esta la heladeria abierta? (Si/No) :").upper()
esta_su_tia_input = input("¿Estas con tu tia? (Si/No) :").upper()

apetece_helado = apetece_helado_input == "Si"
puede_permitirselo = tiene_dinero_input == "Si" or esta_su_tia_input == "Si"
esta_la_heladeria_abierta = esta_la_heladeria_abierta_input == "Si"




if apetece_helado and puede_permitirselo and esta_la_heladeria_abierta:
    print("Pues comete un helado")
else:
    print("Pues nada")