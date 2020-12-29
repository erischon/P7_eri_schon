const button = document.querySelector('.btn')

button.addEventListener('click', () => myFunction())

function myFunction() {
    var x = document.getElementById("answerElement");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }
  