

const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

const question1 = () => {
  return new Promise((resolve, reject) => {
    rl.question('q1 What do you think of Node.js? ', (answer) => {
        std_name = answer;
      console.log(`Thank you for your valuable feedback: ${answer}`)
      resolve()
    })
  })
}

const question2 = () => {
  return new Promise((resolve, reject) => {
    rl.question('q2 What do you think of Node.js? ', (answer) => {
      console.log(`Thank you for your valuable feedback: ${answer}`)
      resolve()
    })
  })
}

const main = async () => {
    var std_name = "";
  await question1()
  console.log(`std_name: ${std_name}`);
  await question2()
  rl.close()
}

main()