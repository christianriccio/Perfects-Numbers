def perfect(n):
  for i in range(2, n+1): #oltre la metà più uno non ci sono divisori
    somma = 0
    for j in range(1, i//2+1): 
      if i%j ==0:
        somma +=j  #aggiungo a somma il divisore trovato
        #print(i, j, somma)
    if somma == i:
      print(i, end = ' ')
perfect(10000)
