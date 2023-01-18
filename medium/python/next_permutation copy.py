
    
            # está no meio
# ********
            else:
                # vejo se dá pra gerar a prox menor permutação com os do final
                if len(lista_nums) >= 3:
                    # pega os ultimos elementos
                    array = lista_nums[index:len(lista_nums)]
                    def proxMaior(prox):
                        if prox > lista_nums[index-1]:
                            menor = 0
                            if  lista_nums[index-1] < prox < menor:
                                menor = prox
                                
                                return menor
                    
                    for x in array:
                        proxMaior(x)

                # saber os que estão ao redor
                # qual é o 2maior?
                    # comparar os anteriores
                    #  saber se tem o prox maior do que oq está a esquerda 
                    
                    x = map(proxMaior, array)
                    index_x = lista_nums.index(x)
                    lista_nums[index_x] = lista_nums[index-1]
                    lista_nums[index-1] = x
                    


                # else:
                direita = lista_nums[index+1]
                esquerda = lista_nums[index-1]
                if direita <= esquerda:
                # o da esquerda é o 2maior? 1maior uma casa a frente  
                    lista_nums[index] = lista_nums[index+1] 
                    lista_nums[index+1] = lista_nums[index-1]
                    lista_nums[index-1] = maior
                else:
                # O da direita é o 2maior> troca de lugar com o da direita
                    for i in range(1, 10):
                        prox = all(lista_nums.index(esquerda+1))
                        if prox:
                            brak
                        
                    lista_nums[index-1] = direita
                    lista_nums[index] = esquerda
                    lista_nums[index+1] = maior
                    if len(lista_nums) > 3: 
                        arr = lista_nums[index: len(lista_nums)]
                        del(lista_nums[index: len(lista_nums)])
                        arr.sort()
                        for a in arr:
                            lista_nums.append(a)