velha="1|2|3\n------\n4|5|6\n------\n7|8|9"

print (velha)

while True:
 print('* Player 1 joga: *')
 c=int(input('Posição:'))
 velha=velha.replace(str(c),'X')
 
 #Linha 1
 if velha[0]==velha[2]==velha[4]:
  if velha[0]=='X': 
   print(velha)
   print('Player 1 Ganhou')
   break
 #Coluna 1
 if velha[0]==velha[13]==velha[26]:
  if velha[0]=='X': 
   print(velha)
   print('Player 1 Ganhou')
   break
 #Linha 2
 if velha[13]==velha[15]==velha[17]:
  if velha[13]=='X': 
   print(velha)
   print('Player 1 Ganhou')
   break
#coluna 2
 if velha[2]==velha[15]==velha[28]:
  if velha[2]=='X': 
   print(velha)
   print('Player 1 Ganhou')
   break
#Linha 3
 if velha[26]==velha[28]==velha[30]:
  if velha[26]=='X': 
   print(velha)
   print('Player 1 Ganhou')
   break
#Coluna 3
 if velha[4]==velha[17]==velha[30]:
  if velha[4]=='X': 
   print(velha)
   print('Player 1 Ganhou')
   break
#Diagonal 1
 if velha[0]==velha[15]==velha[30]:
  if velha[0]=='X': 
   print(velha)
   print('Player 1 Ganhou')
   break
#Diagonal 2
 if velha[4]==velha[15]==velha[26]:
  if velha[4]=='X': 
   print(velha)
   print('Player 1 Ganhou')
   break
 print(velha) 
#Empate   
 if velha[0]!='1' and velha[2]!='2' and velha[4]!='3' and velha[13]!='4' and velha[15]!='5' and velha[17]!='6' and velha[26]!='7' and velha[28]!='8' and velha[30]!='9':
   print(velha)
   print('Empate')
   break  
 print('* Player 2 joga: *')
 c=int(input('Posição:'))
 velha=velha.replace(str(c),'O')
 #Linha 1
 if velha[0]==velha[2]==velha[4]:
  if velha[0]=='O':
   print(velha)
   print('Jogador 2 Ganhou')
   break
 #Coluna 1
 if velha[0]==velha[13]==velha[26]:
  if velha[0]=='O':
   print(velha)
   print('Jogador 2 Ganhou')
   break
 #Linha 2
 if velha[13]==velha[15]==velha[17]:
  if velha[13]=='O':
   print(velha)
   print('Jogador 2 Ganhou')
   break
#coluna 2
 if velha[2]==velha[15]==velha[28]:
  if velha[2]=='O':
   print(velha)
   print('Jogador 2 Ganhou')
   break
#Linha 3
 if velha[26]==velha[28]==velha[30]:
  if velha[26]=='O':
   print(velha)
   print('Jogador 2 Ganhou')
   break
#Coluna 3
 if velha[4]==velha[17]==velha[30]:
  if velha[4]=='O':
   print(velha)
   print('Jogador 2 Ganhou')
   break
#Diagonal 1
 if velha[0]==velha[15]==velha[30]:
  if velha[0]=='O':
   print(velha)
   print('Jogador 2 Ganhou')
   break
#Diagonal 2
 if velha[4]==velha[15]==velha[26]:
  if velha[4]=='O':
   print(velha)
   print('Jogador 2 Ganhou')
   break
   
 print(velha)