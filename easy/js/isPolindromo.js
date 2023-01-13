//  Link exercício:
//    https://leetcode.com/problems/palindrome-number/

//  Obj:
//    Verificar se um número é polindromo (número que dá o mesmo valor se for lido de tras pra frente e frente pra tras)

//  Críterios:
//    return true or false

/**
* @param {number} x
* @return {boolean}
*/

x = 10
var isPalindrome = function(x) {
    let front = x.toString()
    let reverse = front.split('')
    reverse.reverse()
    let compara = reverse.join('')

    if (front == compara){
        return true
    } else {
        return false
    }
    
};

isPalindrome(x)