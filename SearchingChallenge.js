function SearchingChallenge(num) { 

  let sum = 0;
  for (let i = 0; i<num; i++){
    if(i%3 === 0 || i%5 === 0){
      sum += i
    }
  };

  return sum
}
   
// keep this function call here 
console.log(SearchingChallenge(readline()));
