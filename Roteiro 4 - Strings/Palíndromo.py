# n = int(input())
# for x in range(0, n):
#     string = str(input()).strip().lower()
#     string = string.split()
#     string_junta = ''.join(string)
#     string_reverse = string_junta[::-1]
#
#     if string_junta == string_reverse:
#         print("SIM")
#     else:
#         print("NAO")
n = int(input())
for x in range(0, n):
    string = str(input()).lower().replace(' ', '')
    if string == string[::-1]:
        print('SIM')
    else:
        print('NAO')