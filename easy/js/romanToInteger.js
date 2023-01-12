//  Link exercício:
//    https://leetcode.com/problems/roman-to-integer/

//  Obj:
//    Converter número romano em número inteiro

//  Críterios:
//    Symbol       Value
//    I             1
//    V             5
//    X             10
//    L             50
//    C             100
//    D             500
//    M             1000


/**
 * @param {string} s
 * @return {number}
 */

 s = "MCMXCIV"

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

    // converti pra números inteiros
    romans.map((roman) => { convertido.push(integer[roman])})

    let subtrai = convertido.filter((e, i, a) => {
        if (a[i] < a[i+1]){
            // subtrai
            // subtracao.push(a[i+1] - a[i])
            newConvetido.push(a[i+1] - a[i])
            //  armazena elementos que subtraiu
            // tira.push(i, (i-1))
        } else if (a[i] > a[i-1]){
            pass++
        } else {
            newConvetido.push(e)
        }
    })

    soma = newConvetido.reduce(function(soma, i) {
        return soma + i;
    }) 
    console.log(soma) 
    return soma
};

romanToInt(s)