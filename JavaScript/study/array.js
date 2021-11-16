let num = []
const generateRandomNumber = (min, max) =>  {
    return Math.floor(Math.random() * (max - min) + min);
      };


do {
    let random = generateRandomNumber(0, 100)
    num.push(random)
    num.sort()
    console.log(`adding ${random}`)
} while (num.length < 10)



for (let pos in num) {
    console.log(`showing ${num[pos]}`)
}