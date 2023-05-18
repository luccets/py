def situacao(estado) :
    if estado.lower() == "solteiro":
        print ("É casada cmg sim!!")
    else :
        print("sim, cmg")

print ("Digite seu estado civil")
ecivil = input()
situacao(ecivil)