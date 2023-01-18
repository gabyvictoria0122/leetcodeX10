#  Link exercício:
#    https://leetcode.com/problems/two-sum/

#  Obj:
#    Retornar indice dos valores que somados dão o valor de tal número

#  Críterios:
#   Não pode usar o mesmo elemento duas vezes
#   Pode ter apenas uma solução
#   Resposta em qualquer ordem

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(nums, target):
        for indice1 in range(len(nums)):
            for indice2 in range(len(nums)):
                if indice1 == indice2:
                    break
                soma = nums[indice1] + nums[indice2]
                if soma == target:
                    result = [indice1, indice2]
                    break
        return result

# para testar o código na IDE 
nums = [2,7,11,15] 
target = 9
resposta_esperada = [1, 0]

print(Solution.twoSum(nums, target), resposta_esperada)