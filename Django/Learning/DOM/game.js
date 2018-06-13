var restart = document.getElementById("restart")
var squares = document.querySelectorAll("td")
console.log(squares)

function clearBoard(){
  for(var i=0;i < squares.length;i++){
    squares[i].textContent = "";
  }
}

restart.addEventListener("click",clearBoard);

function changemarker(){
  if (this.textContent == ''){
      this.textContent ='X';
  }else if (this.textContent === "X"){
      this.textContent = 'O';
  } else {
    this.textContent = "";
  }
}

for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener('click',changemarker)
}
