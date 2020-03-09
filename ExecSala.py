"""Verifica se a media é maior que 6"""
nota1=7.8
nota2=4.5
nota3=6
nota4=5.5
media=(nota1+nota2+nota3+nota4)/4

print ('Sua media é maior que 6 ?')

if media>=6:
    print('Sim')
if media<6:
    print('Não')

print ('Sua média é = ' + str(media))

print ('Voce irá para recuperação ?')
result=media>=5 and media <6
if result == True :
        print('sim')
else:
    print('Não')


