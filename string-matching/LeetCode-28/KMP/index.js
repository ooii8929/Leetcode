let haystackArray = ["leetcode", "sadbutsad","abc","afaabf","aabaaabaaac"]
let needleArray = ["leeto","sad","c","ab","aabaaac"]

let switcher = 0

let haystack = haystackArray[switcher]
let needle = needleArray[switcher]

function returnMatchingIndex(haystack, needle){

    let LPS = getLPS(needle)

    console.log("LPS",LPS);

    let needleIndex = 0

    let haystackIndex = 0
    
    while(haystackIndex < haystack.length){

        console.log("Now",haystack[haystackIndex] , "," , needle[needleIndex]);

        if(haystack[haystackIndex] == needle[needleIndex]){
            haystackIndex++
            needleIndex++
        }else{
            if(needleIndex == 0){
                haystackIndex++
            }else{
                needleIndex = LPS[needleIndex - 1]
            }
        }

        console.log("needleIndex",needleIndex);

        if(needleIndex >= needle.length){
            return haystackIndex - needle.length
        }

    }

    return -1

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






//      now
//   j
// aabaaac

// if now == 0
//     push(0)


// if li[now] == li[j]
//     push(j+1)
//     j++

// if li[now] != li[j]
//     push(0)
//     j = 0

//                i 
// haystack = afaabf

//                   needleIndex
// LPS = [ 0, 0, 0, 0, 1, 2 ]
//                   a  b  c  a  b
// while 
//     if haystack[i] == LPS[needleIndex+1]
//         i++
//         needleIndex++
//     else
//         if(needleIndex == 0){
//             i++
//         }else{
//             needleIndex = LPS[needleIndex]
//         }
        

