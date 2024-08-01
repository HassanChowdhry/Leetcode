// https://leetcode.com/problems/first-unique-character-in-a-string

/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
     var mainq=[];
    var res;
    var q=new Map();
    for(var i=0;i<s.length;i++){
        if(q.has(s[i])){
            q.set(s[i],"r");
            if((mainq.length>0)&&(mainq[mainq.length-1]===s[i])){
                mainq.pop();
            }
        }
        else{
            q.set(s[i],i);
            mainq.unshift(s[i]);
        }
    }
    
    while(mainq.length>0){
         res=mainq.pop();
        if(q.get(res)!=='r'){
            return q.get(res);
        }
    }
    
    return -1;
};