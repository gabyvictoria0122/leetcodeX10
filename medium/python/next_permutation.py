#  Link exercício:
#    https://leetcode.com/problems/next-permutation/

#  Obj:
#    Achar a proxima permutação

#  Críterios:
#   
nums = [2,2,7,5,4,3,2,2,1]
class Solution:
    def nextPermutation(self, nums) -> None:        
        """
        Do not return anything, modify nums in-place instead.
        """
# Acha o maior e pega o indice dele
        maior = max(nums)
        index = nums.index(maior)

# Verifico se todos os elementos são iguais
        for i in range(len(nums)):
            igual = all(num == nums[i] for num in nums)
        if igual:
            return nums
        else:
# Se os elementos forem diferente:
    # verifico se está no final
            if index == (len(nums)-1):
        # vai pra frente
                nums[index] = nums[index-1]
                nums[index-1] = maior
            # verifico se está no começo:
            elif index == 0: 
                # vejo se dá pra gerar a prox menor permutação com os do final (len == 3, acho que vai ter que fazer outra mais geral) 
                if nums[index+2] > nums[index+1]:
                    segundo_maior = nums[index+2]
                    nums[index+2] = nums[index+1] 
                    nums[index+1] = segundo_maior
                else:
                    # deixa os elementos em ordem crescente
                    nums.sort()
            # está no meio
            else:
                # vejo se dá pra gerar a prox menor permutação com os do final
                if len(nums) > 3:
                    # pega os ultimos elementos
                    array = nums[index:len(nums)]
                    def proxMaior(prox):
                        if prox > nums[index-1]:
                            if  nums[index-1] < prox < menor:
                                menor = prox
                                
                                return menor
                    
                    for x in array:
                        proxMaior(x)

                # saber os que estão ao redor
                # qual é o 2maior?
                    # comparar os anteriores
                    #  saber se tem o prox maior do que oq está a esquerda 
                    
                    x = map(proxMaior, array)
                    index_x = nums.index(x)
                    nums[index_x] = nums[index-1]
                    nums[index-1] = x
                    


                # else:
                direita = nums[index+1]
                esquerda = nums[index-1]
                if direita <= esquerda:
                # o da esquerda é o 2maior? 1maior uma casa a frente  
                    nums[index] = nums[index+1] 
                    nums[index+1] = nums[index-1]
                    nums[index-1] = maior
                else:
                # O da direita é o 2maior> troca de lugar com o da direita
                    for i in range(1, 10):
                        prox = all(nums.index(esquerda+1))
                        if prox:
                            brak
                        
                    nums[index-1] = direita
                    nums[index] = esquerda
                    nums[index+1] = maior
                    if len(nums) > 3: 
                        arr = nums[index: len(nums)]
                        del(nums[index: len(nums)])
                        arr.sort()
                        for a in arr:
                            nums.append(a)

inicia = Solution()
inicia.nextPermutation(nums)