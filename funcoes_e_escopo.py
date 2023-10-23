def funcao_externa(): 
    a = 10
    b = 20   #variavel da namespace local da função externa
    print(f"O valor 'a' terá o resultado de 10, pois ela está dentro da funcao_externa. Resultado: {a}")
    print(f"O valor 'b' terá o resultado de 20, pois está dentro da função externa. Resultado: {b}")
    def funcao_interna():
        a = 100
        b = 200
        c = 300   #variavel da namespace local da função externa
        print(f"O valor 'a' terá o resultado de 100, pois ela está dentro da funcao_interna . Resultado: {a}")
        print(f"O valor 'b' terá o resultado de 200, pois ela está dentro da funcao_interna . Resultado: {b}")
        print(f"O valor 'c' terá o resultado de 300, pois ela está dentro da funcao_interna . Resultado: {c}")
    
    funcao_interna() 
    print(f"O valor 'a' desta função não será 100, pois esta função está dentro da funcao_externa. resultado{a}")
    
a = 500  #variavel escopo global
print(f"Imprimindo 'a' no escopo global o resultado será de 500 não 10. Resultado: {a}")
funcao_externa() #função dentro do escolpo global
print(f"Imprimindo o 'a' de novo mesmo sendo funcao_externa, o valor será de 500, pois está dentro do escopo global. Resultado: {a} ")