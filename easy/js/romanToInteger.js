//  Link exercício:
//    https://leetcode.com/problems/roman-to-integer/

//  Obj:
//    Converter número romano em número inteiro

/**
 * @param {string} s
 * @return {number}
 */

var romanToInt = function(s) {
    const integer = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000
    }

    // transforma em array
    let romans = s.split('')
    let convertido = []
    let newConvetido = []
    let soma = 0
    let pass = 0

    // converti para números inteiros
    romans.map((roman) => { convertido.push(integer[roman])})

    // subtrai
    convertido.filter((e, i, a) => {
        if (a[i] < a[i+1]){
            newConvetido.push(a[i+1] - a[i])
        } else if (a[i] > a[i-1]){
            pass++
        } else {
            newConvetido.push(e)
        }
    })

    soma = newConvetido.reduce(function(soma, i) {
        return soma + i;
    }) 
    return soma
};

// para testar o códifo na IDE 
s = "MCMXCIV"
console.log(romanToInt(s))
