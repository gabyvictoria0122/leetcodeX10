//  Link exercício:
//    https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

let traversal = "1-2--3--4-5--6--7"
var recoverFromPreorder = function(traversal) {
    // array com traço e como string
    let arrayString = traversal.split('')
    // array só com os números
    let arrayNumber = []
    arrayString.map(function(number){
        if(!isNaN(number)){
            arrayNumber.push(number)
        }
    } )
    // console.log(traversal)
    let conta = 0
    let arrayFinal = []
    let quantidadeT = 0
    let indice = 0
    let e = 
    // armazena o primeiro
    arrayFinal.push(traversal[0])
    while (indice <= arrayNumber.length){
        if (arrayFinal.length < arrayNumber.length){
            quantidadeT++
            e++
            loop(traversal, arrayFinal, quantidadeT, conta, e)
        }else {
            break
        }
    }
};
function loop (traversal, arrayFinal, quantidadeT, conta, e){
    let ramo = 0
    // number inicial
    for (i of traversal) {
        // pass o primeiro
        let indice = traversal.indexOf(i) 
        if ( indice == 0) {
            continue
        } else if ( !isNaN(i)){
            if (conta == 2**e){
                conta = 0
                break
            }
            if (ramo == quantidadeT){
                arrayFinal.push(i)
                conta++
            }
            ramo = 0
            continue
        } else {
            ramo++
        }
    }
}

recoverFromPreorder(traversal)