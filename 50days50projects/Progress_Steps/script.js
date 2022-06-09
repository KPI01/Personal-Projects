/*Declaring variables*/
const progress = document.getElementById("progress");
const prev = document.getElementById("prev");
const next = document.getElementById("next");
const circles = document.querySelectorAll(".circle");

/*Variable for counting active circles*/
let currentActive = 0;

/*Event Listener on click 'prev' Button*/
prev.addEventListener("click", () => {
  currentActive--;

  if (currentActive < 0) {
    currentActive = 0;
  }

  update();

  btnCheck();
});

/*Event Listener on click 'next' button*/
next.addEventListener("click", () => {
  currentActive++;

  if (currentActive > circles.length) {
    currentActive = circles.length;
  }

  update();

  btnCheck();
});

/*function for changing actives circles*/
function update() {
  circles.forEach((circle, idx) => {
    if (idx < currentActive) {
      circle.classList.add("active");
    } else {
      circle.classList.remove("active");
    }
  });

  const actives = document.querySelectorAll(".active");

  progress.style.width =
    ((actives.length - 1) / (circles.length - 1)) * 100 + "%";

  if (currentActive === 0) {
    prev.disabled = true;
  } else if (currentActive === circles.length) {
    next.disabled = true;
  } else {
    next.disabled = false;
    prev.disabled = false;
  }
}

function btnCheck() {
  if (currentActive === 0) {
    prev.innerHTML = "-";
  } else if (currentActive === circles.length) {
    next.innerHTML = "-"
  } else {
    prev.innerText = "Prev";
    next.innerHTML = "Next"
  }
}
