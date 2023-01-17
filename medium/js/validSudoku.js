//  Link exercício:
//    https://leetcode.com/problems/valid-sudoku/

//  Obj:
//    

//  Críterios:
//   

/**
 * @param {character[][]} board
 * @return {boolean}
*/

var isValidSudoku = function(board) {
    function hasDuplicate(arr){
        // transforma em numero
        let number = arr.map((Number))
        // filtra os NaN
        let newArray = number.filter(function (value) {
        return !Number.isNaN(value);})
        // se for diferente tem duplicado
        return new Set(newArray).size != newArray.length
    }

    let repetiL = 0
    let inicial = [0,3,6]
    let final = [2,5,8]
    while(repetiL <= 2 ){
        let repetiC = 0
        let linha3 = board.slice(inicial[repetiL], (final[repetiL]+1))

        // conferir duplicação no 3X3
        while(repetiC <= 2){
            let coluna3 = []
            let quant = 0
            while (quant < linha3.length) {
                coluna3.push(...linha3[quant].slice(inicial[repetiC], (final[repetiC]+1)))
                quant++
                if (coluna3.length == 9){
                    if ( hasDuplicate(coluna3)){
                        return false
                    }
                }
            }
            repetiC++
        }
        repetiL ++
    }

    for (c in board) {    
        let arrayColumn = []
        for (l in board){
            arrayColumn.push(board[l][c])
            // confere duplicação na coluna
            if ( hasDuplicate(arrayColumn)){
                return false
            } else if (hasDuplicate(board[l])){
                // confere duplicação na linha
                return false
            }
        }
    }
    return true
};

// Para rodar na IDE
board4 =
[
[".",".",".",".",".",".","5",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
["9","3",".",".","2",".","4",".","."],
[".",".","7",".",".",".","3",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".","3","4",".",".",".","."],
[".",".",".",".",".","3",".",".","."],
[".",".",".",".",".","5","2",".","."]]
console.log(isValidSudoku(board4))