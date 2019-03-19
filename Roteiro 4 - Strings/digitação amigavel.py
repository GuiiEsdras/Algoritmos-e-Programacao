while True:
    flex_num = str(input()).upper()
    if flex_num == "FIM":
        break
    flex_num = flex_num.replace("O", "0")
    flex_num = flex_num.replace("L", "1")
    if not flex_num.isdigit():
        print("ERRO")
    else:
        print(int(flex_num))