function StringChallenge(str) { 
  let newStr = '';
  for (char in str){
    if (isAlphaNumeric(str[char])){
      newStr += str[char].toLowerCase()
    }
  }
  let reversedStr = newStr.split("").reverse().join("");
  if (reversedStr === newStr){
    return 'true'
  } else {
    return 'false'
  }
};

function isAlphaNumeric(str){
  for (let i = 0; i < str.length; i++){
    code = str.charCodeAt(i);
    if (!(code > 47 && code <58) &&
        !(code > 64 && code <91) &&
        !(code > 96 && code < 123)){
          return false;
        }
    return true;
  };
};

// keep this function call here 
console.log(StringChallenge(readline()));
