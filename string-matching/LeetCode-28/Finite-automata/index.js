let haystackArray = ["leetcode", "sadbutsad","abc","afaabf","aabaaabaaac"]
let needleArray = ["leeto","sad","c","ab","aabaaac"]

let switcher = 4

let haystack = haystackArray[switcher]
let needle = needleArray[switcher]

function returnMatchingIndex(haystack, needle){

    let LPS = getLPS(needle)

    console.log("LPS",LPS);

    const sigma = new Set()

    for (let i = 0; i < haystack.length; i++) {
        sigma.add(haystack[i])
    }


    // mySet = {a,b,c}

    let M = needle.length;
    let N = haystack.length;

    let TF = new Array(M + 1);


    // 建立空白 TF
    for(let i=0;i<M+1;i++){
        
        TF[i] = new Array(sigma);

        for(let j=0;j<sigma.size;j++){
            TF[i][j]=0;
        }
    }

    let sigmaArr = [...sigma]; 

    

    // TF 第一列
    for (let i = 0; i < sigmaArr.length; i++) {

        if(needle[0] == sigmaArr[i]){
            TF[0][i] = 1
        }
        
    }

    console.log({TF});

    let state = 1



    // 輪詢全部狀態
    for (let i = 1; i < TF.length; i++) {
  
        // 輪詢全部 inputs
        for (let k = 0; k < sigmaArr.length; k++) {

            console.log("test",needle[i],",", sigmaArr[k]);

            console.log("state",state);    

            // 如果當前 pattern(needle) 的值等於input，則前往下一位
            if(needle[i] == sigmaArr[k] && needle[i] != undefined){
                state++
                TF[i][k] = state
            // 如果不等於input，則計算當前LPS
            }else{
                console.log("getLPSnumber(needle.slice(0,i-1),sigmaArr[k])",needle.slice(0,i),",",sigmaArr[k]);
                TF[i][k] = getLPSnumber(needle.slice(0,i),sigmaArr[k])
            }
            
        }
        
    }

    let currentState = 0

    let ans = []

    for (let i = 0; i < haystack.length; i++) {



        const isSame = (element) => element == haystack[i];

        console.log("sigmaArr.findIndex(isSame)",sigmaArr);

        currentState = TF[currentState][sigmaArr.findIndex(isSame)]

        console.log({currentState});

        if(currentState == needle.length){
            ans.push(i - needle.length + 1)
            return i - needle.length + 1
        }
        
    }
    return -1
    

    

}







function getLPSnumber(pattern,char){

    let LPS = [0]
    let LPSCounts = 0
    let needleIndex = 1
    let needle = pattern+char

    // LPS[0] always is 0
    while(needleIndex < needle.length){

        if(needle[needleIndex] == needle[LPSCounts]){
            needleIndex++
            LPSCounts++
            LPS.push(LPSCounts)

        }else if(LPSCounts > 0){
            LPSCounts = LPS[LPSCounts - 1]
        }else if(LPSCounts == 0){
            needleIndex++
            LPS.push(LPSCounts)
        }
        
    }

    return LPS[LPS.length-1]

}


function getLPS(needle){

    let LPS = [0]
    let LPSCounts = 0
    let needleIndex = 1

    // LPS[0] always is 0
    while(needleIndex < needle.length){
        if(needle[needleIndex] == needle[LPSCounts]){
            needleIndex++
            LPSCounts++
            LPS.push(LPSCounts)
        }else if(LPSCounts > 0){
            LPSCounts = LPS[LPSCounts - 1]
        }else if(LPSCounts == 0){
            needleIndex++
            LPS.push(LPSCounts)
        }

    }

    return LPS

}


console.log(returnMatchingIndex(haystack, needle))
