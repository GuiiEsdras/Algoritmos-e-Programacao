CrimeDoDelator = input()
Crimes = ["roubo", "tráfico", "homicídio"]
if (CrimeDoDelator not in Crimes):
  print("Crime inválido.")

else:
  if (CrimeDoDelator == "roubo" or CrimeDoDelator == "tráfico"):
    ValorDoCrimeDelator = float(input())
    CrimeDelatado = input()
  else:
    CrimeDelatado = input()

  if CrimeDelatado not in Crimes:
    print("Crime inválido.")

  else:
    if (CrimeDelatado == "roubo" or CrimeDelatado == "tráfico"):
      ValorDoCrimeDelatado = float(input())

    if CrimeDelatado == "roubo" or CrimeDelatado == "tráfico" or CrimeDelatado == "homicídio":

      if (CrimeDoDelator == "roubo" or CrimeDoDelator == "tráfico") and (CrimeDelatado == "homicídio"):
        print("Delação concedida.")
      elif (CrimeDoDelator == "roubo" and CrimeDelatado == "roubo") and ValorDoCrimeDelatado > (5* ValorDoCrimeDelator):
        print("Delação concedida.")
      elif (CrimeDoDelator == "roubo" and CrimeDelatado == "tráfico") and ValorDoCrimeDelatado > (3* ValorDoCrimeDelator):
        print("Delação concedida.")
      elif (CrimeDoDelator == "tráfico" and CrimeDelatado == "tráfico") and ValorDoCrimeDelatado > (5* ValorDoCrimeDelator):
        print("Delação concedida.")
      elif (CrimeDoDelator == "homicídio" and CrimeDelatado == "homicídio"):
        print("Delação concedida.")
      else:
        print("Delação rejeitada.")