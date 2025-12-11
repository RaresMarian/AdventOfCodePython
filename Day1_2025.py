with open("./input_day1.txt", "r") as file:
    contenuto = file.readlines()


somma=50
password=0
for x in contenuto:         
    if(x[0]=="R"):
        numero=int(x[1:])
        somma= (somma+numero)%100
        
    else :
        numero=int(x[1:])
        somma= (somma-numero)%100

    if(somma==0):
        password+=1


       

print(password)
            
      
    

