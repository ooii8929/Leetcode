let haystackArray = ["leetcode", "sadbutsad","abc"]
let needleArray = ["leeto","sad","c"]

let switcher = 2

let haystack = haystackArray[switcher]
let needle = needleArray[switcher]

function returnMatchingIndex(haystack, needle){

    if(needle.length > haystack.length) return -1

    let needleHash = 0
    for (let i = 0; i < needle.length; i++) {

        needleHash += needle[i].charCodeAt(0) * Math.pow(10, needle.length - i - 1)
        
    }

    let hayHash = 0

    for (let i = 0; i < needle.length; i++) {

        hayHash += haystack[i].charCodeAt(0) * Math.pow(10, needle.length - i - 1)
        
    }

    if(hayHash == needleHash){
        return 0
    }

    for (let j = 1; j < haystack.length - needle.length + 1; j++) {

        console.log("index",haystack[j]);

        console.log("ss",haystack[j+needle.length-1].charCodeAt(0));

        hayHash = (hayHash - haystack[j-1].charCodeAt(0) * Math.pow(10, needle.length-1)) * 10 + haystack[j+needle.length-1].charCodeAt(0)

        if(hayHash == needleHash){
            return j
        }
        
    }

    return -1
    

    console.log("needleHash",needleHash,",hayHash",hayHash);


    

}

console.log(returnMatchingIndex(haystack, needle))
