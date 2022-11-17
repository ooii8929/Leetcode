let haystackArray = ["leetcode", "sadbutsad","abc"]
let needleArray = ["leeto","sad","c"]

let switcher = 0

let haystack = haystackArray[switcher]
let needle = needleArray[switcher]

function returnMatchingIndex(haystack, needle){

    for (let i = 0; i < haystack.length; i++) {
        
        if(needle[0] == haystack[i]){

            if(needle.length == 1) return i

            let tmpIndex = i + 1
            for (let j = 1; j < needle.length; j++) {

                if(needle[j] !== haystack[tmpIndex]) break

                if(j == needle.length-1) return i
                
                tmpIndex++
                
            }

        }
        
    }

    return -1
}

console.log(returnMatchingIndex(haystack, needle))
