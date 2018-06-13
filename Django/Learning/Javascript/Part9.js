firstName = prompt("Enter your First name?")
lastName = prompt("Enter your Last name?")
age = prompt("Enter your age?")
height = prompt("Enter how tall you are in centimeters?")
petname = prompt("Enter your pet name?")
flag = 1;
age = parseInt(age)
height = parseInt(height)
//Check if the first letter of first name and second name is equal or not
if (firstName[0] != lastName[0]){
  flag = 0;
}

//check if the age is between 20-30
if (!(age >= 20 && age <=30)){
  flag=0;
}

//check if the height is more then 170 centimeters.
if (height < 170){
  flag = 0;
}

//check if the pet name ends with letter 'y'
if (petname.substr(petname.length - 1) != "y"){
  flag = 0;
}

if (flag === 1){
  console.log("Welcome comrade!.You have passed the spy test")

}else{
  console.log("Sorry! Nothing to see here!");
}
