tipo = input()

if tipo == "PV":
    sexo = input().upper()
    idade = int(input())
    tempo_contr = int(input())

    if sexo == "M" and idade >= 65 and tempo_contr >= 20:
        print("Trabalhador Privado pode se aposentar.")
    elif sexo == "F" and idade >= 62 and tempo_contr >= 20:
        print("Trabalhador Privado pode se aposentar.")
    else:
        print("Trabalhador Privado NAO pode se aposentar!")

elif tipo == "TR":
    sexo = input().upper()
    idade = int(input())
    tempo_contr = int(input())

    if idade >= 60 and tempo_contr >= 20:
        print("Trabalhador Rural pode se aposentar.")
    else:
        print("Trabalhador Rural NAO pode se aposentar!")

elif tipo == "SP":
    sexo = input().upper()
    idade = int(input())
    tempo_contr = int(input())
    serv_pub = int(input())
    cargo = int(input())

    if sexo == "M":
        if idade >= 65 and tempo_contr >= 25 and serv_pub >= 10 and cargo >= 5:
            print("Servidor publico pode se aposentar.")

        else:
            print("Servidor publico NAO pode se aposentar.")

    elif sexo == "F":
        if idade >= 62 and tempo_contr >= 25 and serv_pub >= 10 and cargo >= 5:
            print("Servidora publica pode se aposentar.")

        else:
            print("Servidor publico NAO pode se aposentar.")

elif tipo == "PR":
    sexo = input().upper()
    idade = int(input())
    tempo_contr = int(input())

    if idade >= 60 and tempo_contr >= 30:
        print("Professor pode se aposentar.")

    else:
        print("Professor NAO pode se aposentar!")

elif tipo == "PC":
    sexo = input().upper()
    idade = int(input())
    tempo_contr = int(input())
    tempo_serv = int(input())

    if sexo == "M":
        if idade >= 55 and tempo_contr >= 30 and tempo_serv >= 20:
            print("Policial pode se aposentar.")

        else:
            print("Policial NAO pode se aposentar!")

    elif sexo == "F":
        if idade >= 55 and tempo_contr >= 25 and tempo_serv >= 15:
            print("Policial pode se aposentar.")

        else:
            print("Policial NAO pode se aposentar!")

else:
    print("Categoria de trabalhador invalida.")
