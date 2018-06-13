var headone  = document.getElementById("one")
var headtwo  = document.getElementById("two")
var headthree  = document.getElementById("three")

// console.log("connected")

headone.addEventListener('mouseover',function(){
  headone.textContent = "Mouse currently over";
  headone.style.color = 'red';
})

headtwo.addEventListener('mouseout',function(){
  headtwo.textContent = "Hover over me!";
  headtwo.style.color = 'black';
})

headthree.addEventListener("click", function(){
  headthree.textContent = "CLICKED ON";
  headthree.style.color -"red"
})

headthree.addEventListener("dblclick", function(){
  headthree.textContent = "DoubleCLICKED ON";
  headthree.style.color ="red"
})
