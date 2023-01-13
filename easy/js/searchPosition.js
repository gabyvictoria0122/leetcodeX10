//  Link exercício:
//    https://leetcode.com/problems/search-insert-position/

//  Obj:
//    Achar a posição de um determinado elemento
//    Se não tiver, indicar em que posição estaria (ordem crescente).

//  Críterios:
//   

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
nums = [1,3,5,6]
target = 7
var searchInsert = function(nums, target) {
    let tamanho = nums.length
    let find = nums.indexOf(target)
    if (find != -1){
        return find
    } else if ( target > nums[tamanho-1]) {
        return tamanho

    } else {
        for ( i in nums ){
            if ( nums[i] > target ){
            return i

            }
        }

    }
};