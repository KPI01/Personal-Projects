/*Declaring variables*/
const progress = document.getElementById('progress');
const prev = document.getElementById('prev');
const next = document.getElementById('next');
const circles = document.querySelectorAll('.circle');

/*Variable for counting active circle*/
let currentActive = 1;

/*EventListener for clicks on buttons*/
next.addEventListener('click', () => {
 currentActive++;

 /*Conditional in case currentActive is bigger than number of circles*/
 if (currentActive > circles.length) {
  currentActive = circles.length;
 }

 update();
})
prev.addEventListener('click', () => {
 currentActive--;

 if (currentActive < 1) {
  currentActive = 1;
 }

 update();
})

/*function for updating which circle is active*/
function update() {
 circles.forEach((circle, idx) => {
  if(idx < currentActive) {
   circle.classList.add('active');
  }else{
   circle.classList.remove('active');
  }
 })
}

/*declaring variable for active circles*/
const actives = document.querySelectorAll('.active');

/*calculate % for filled progress bar width*/
progress.style.width = (actives.length - 1) / (circles.length - 1) * 100 + '%';

/*disable or enable buttons*/
if (currentActive === 1) {
 prev.disabled = true;
} else if (currentActive === circles.length) {
  next.disabled = true;
} else {
 prev.disabled = false;
 next.disabled = false;
}