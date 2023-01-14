#  Link exercício:
#    https://leetcode.com/problems/trapping-rain-water/

#  Obj:
#    Saber quanto de agua cada buraco vai armazenar

#  Críterios:
#   

class Solution:
    def trap(heights):
        agua = 0
        maior_indice = []
        # só quero passar pelos valores grandes

        def maior(x,y, arr ):
            if arr[x] < arr[y]:
                return True
            elif arr[x] == arr[y]:
                return True
            else:
                return False
                    
            # else:
            #     print("x é maior do que todos")

        y = 0
        for x in range(len(height)):
            if x == 0 and height[x] == 0:
                continue
    
            if agua != 0:
                x = y
            if x == len(height)-1:
                return agua
                break
            for y in range(len(height)):
                if x < y:
                    if maior(x, y, height):
                        if ( y - x ) > 0:
                            caminha = height[x+1 : y]
                            for c in caminha:
                                agua += height[x] - c
                            x = y
                    elif y == len(height)-1:
                        i = x
                        y = i+1
                    else:
                        pass
                            # vou para o prox maior  
                


            #     if tem prox maior ou igual?:
            #     # Sim: 
            #     else:
            #         #  proximo indice
            #         continue
            # if i, tem prox maior ou igual?:
            #     # sim
            # else: 
            #     continue
height = [0,1,0,2,1,0,1,3,2,1,2,1]
inicia = Solution
inicia.trap(height)