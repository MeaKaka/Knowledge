/**
 * Created by HXH on 2018/3/15.
 */

/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function(board) {
    //遍历数组得到所有的O的位置,及一定自由的0
    var array=[];
    var z=0;
    var free=[];
    var m=0;
    for(var i=0;i<board.length;i=i+board.length){
        for(var j=0;j<board[0].length;j=j+board[0].length){
            if(board[i][j]=='O'){
                // array[z]=[i,j];
                // z++;
                // if(i==0||i==(board.length-1)||j==0||j==(board[0].length-1)){
                    free[m]=[i,j];
                    m=m+1;
                // }
            }
        }
    }
    //通过已经存在在free数组中的元素去判断array数组中的元素是否也是自由的
    for(i=0;i<free.length;i++){
        if(board[free[i][0]+1][free[i][1]]=='O'){
            free.push(free[i][0]+1,free[i][1]);
        }
        if(board[free[i][0]-1][free[i][1]]=='O'){
            free.push(free[i][0]+1,free[i][1]);
        }
        if(board[free[i][0]][free[i][1]+1]=='O'){
            free.push(free[i][0]+1,free[i][1]);
        }
        if(board[free[i][0]][free[i][1]-1]=='O'){
            free.push(free[i][0]+1,free[i][1]);
        }
    }
    for(i=0;i<board.length;i=i+board.length){
        for(j=0;j<board[0].length;j=j+board[0].length){
            if(free.indexOf([i,j])!=-1){
                board[i][j]='O';
            }
            else{
                board[i][j]='X';
            }
        }
    }
};