#  Link exercício:
#    https://leetcode.com/problems/next-permutation/

#  Obj:
#    Achar a proxima permutação

#  Críterios:
#   
class Solution:
    def nextPermutation(self, lista_nums) -> None:        
        """
        Do not return anything, modify lista_nums in-place instead.
        """
        # ver se os elementos da lista são iguais
        for i in range(len(lista_nums)):
            igual = all(num == lista_nums[i] for num in lista_nums)
        if igual:
            pass
        else:
            info_maior = maior(lista_nums)
            index = info_maior[1]
            number = info_maior[0]
            # verifico se está no final
            if index == (len(lista_nums)-1):
                maior_no_final(index, number, lista_nums)
            # veridico se está no começo
            elif index == 0:
                maior_no_inicio(index, number, lista_nums)
                # ordena depois do que foi mudado
                
            # está no meio
            else:
                list_new = []
                maior_no_meio(index,number, lista_nums, list_new)
                # ordena
                lista_copy = sorted(lista_nums[index:])
                intervalo = lista_nums[:index]
                lista_nums.clear()
                lista_nums.extend(intervalo)
                lista_nums.extend(lista_copy)
                # lista_nums = lista_nums[:index] + lista_copy
                print(lista_nums)


def maior(lista_nums):
    maior = max(lista_nums)
    index = lista_nums.index(maior)
    return maior, index

def maior_no_inicio(index, number, lista_nums):
    if lista_nums == sorted(lista_nums, reverse=True):
        # deixa os elementos em ordem crescente
        lista_nums.sort()
    else:
        prox_maior = maior(lista_nums[1:])
        index_new = prox_maior[1]
        number_new = prox_maior[0]
        for i in range(len(lista_nums)):
            if lista_nums[i] < number_new:
                # troca uma casa a frente
                lista_nums[index_new+1] = lista_nums[index_new] 
                lista_nums[index_new] = number_new
                lista_copy = sorted(lista_nums[prox_maior[1]+1:])
                intervalo = lista_nums[:prox_maior[1]+1]
                lista_nums.clear()
                lista_nums.extend(intervalo)
                lista_nums.extend(lista_copy)
                break
                # lista_nums[prox_maior[1]+1] = lista_nums[1]
                # lista_nums[1] = prox_maior[0]
            else:
                continue
            # Permuta a direita
            # Dá pra gerar a prox menor permutação com os do final
            # maior(lista_nums[(index-1):])
            # recursividade

def maior_no_final(index, number, lista_nums):
    # vai pra frente
    lista_nums[index] = lista_nums[index-1]
    lista_nums[index-1] = number
    return lista_nums

def maior_no_meio(index, number, lista_nums, list_new):
    # onde está o segundo maior?
    prox_esquerda = lista_nums[index-1]
    prox_direita = lista_nums[index+1]
    # prox_maior_D = maior(lista_nums[index+1:len(lista_nums)])
    if prox_esquerda < prox_direita:
        # tem permutação na parte direita? 
        # nop
        if lista_nums[index+1:] == sorted(lista_nums[index+1:], reverse=True):
            diff = 1000
            prox_maior = 0
            prox_indice = 0
            # prox maior que o da esquerda? é oq tem a menor diferença
            for i, el in enumerate(lista_nums[index+1:], start=index+1):
                diferenca = el - prox_esquerda
                if  diferenca > 0 and diferenca < diff:
                    diff = diferenca
                    prox_maior = el
                    prox_indice = i
                else:
                    continue
            # troca
            lista_nums[prox_indice] = lista_nums[index-1]
            lista_nums[index-1] = prox_maior
        else:
        # sim
            # Permuta a direita.
            pass
    else:
        if lista_nums[index+1:] == sorted(lista_nums[index+1:], reverse=True):
            lista_nums[index] = lista_nums[index+1] 
            lista_nums[index+1] = lista_nums[index-1]
            lista_nums[index-1] = number
            pass
        else:
            # caso basico
            # mudar de estado
            # chamar a si mesmo 
            
            # não consegui cobrir todos os casos. queria usar recursividade
            list_recursiva = lista_nums
            if(len(lista_nums) < 5):
                pass
            else:
                inicia_novamente = Solution()
                return inicia_novamente.nextPermutation(list_recursiva[index+1:])
            pass
            # Permuta a direita
        
#para testar o código na IDE 

# lista_nums = [4,2,0,2,3,2,0]
# lista_nums = [3,1,2]
lista_nums = [2,2,3,4,2,3,1,1,2]


inicia = Solution()
print(inicia.nextPermutation(lista_nums), lista_nums)
