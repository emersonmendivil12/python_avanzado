#crear una funcion que resiva 5 numeros enteros y que retorne solo una lista de numeros pares tener en cuenta las anotaciones 
def num_pares(a:int,b:int,c:int,d:int,e:int)->list[int]:
    numeros:list[int]=[a,b,c,d,e]
    numeros_pares:list[int]=[]
    for i in numeros:
        if i%2==0:
            numeros_pares.append(i)
    return numeros_pares
# print(num_pares(4,2,6,8,5))
