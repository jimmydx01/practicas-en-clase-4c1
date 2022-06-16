class Sintaxis:
    def usoIf(self,numero):
        if numero % 2==0:
            print("el numero {} es Par".format(numero))
        else:
            print("el numero {} es Impar".format(numero))
    def usoFor(self,dato):
        for ele in dato:
            print(ele,end="")
        print()
            
        inicio=len(dato)-1
        for pos in range(inicio,-1,-1):
            print(pos,dato [pos],end=" ")  
        print() 
        for pos,ele in enumerate(dato):
            print("[{}]={}".format (pos,ele))
            
                
sintaxis=Sintaxis()
sintaxis.usoFor("Hola")

sintaxis.usoFor((10,"hola",True,50.50))
sintaxis.usoFor(["Dan",20,50,70  ])

# lista=[2,5,7,10] 
# for num in lista:
#     sintaxis.usoIf(num)           
            
            