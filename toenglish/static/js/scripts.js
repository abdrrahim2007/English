
        
// var t = document.getElementById('t');
// var p = document.getElementById('p');
// t.addEventListener('click', function() {
//     t.classList.toggle('t')
//     p.classList.toggle('p')
// })



var menu = document.getElementById('menu')
function beCurent(listItem) {
  var items = document.getElementsByClassName('list-item');
  
  for (var i = 0; i < items.length; i++) {
    if (items[i] === listItem) {
      items[i].classList.add('curent');
      menu.classList.remove('active')
    } else {
      items[i].classList.remove('curent');
      menu.classList.remove('active')
    }
  }
}


var header = document.querySelector("header");

// Function to toggle the class based on scroll position
function toggleHeaderClass() {
    // Add a class to the header when scrolled beyond 100 pixels
    if (window.pageYOffset > 100) {
        header.classList.add("scrolled");
    } else {
        // Remove the class if not scrolled beyond 100 pixels
        header.classList.remove("scrolled");
    }
}

// Listen for the scroll event and call the toggleHeaderClass function
window.addEventListener("scroll", toggleHeaderClass);

var openMenu = document.getElementById('openMenu')
var menu = document.getElementById('menu')
openMenu.addEventListener('click',function(event){
    event.stopPropagation()
    menu.classList.add('active')
})

window.addEventListener('click',function(event){
    if(menu.classList.contains('active') && !menu.contains(event.target)){
        menu.classList.remove('active')
    }
    
    
})




// // Get the timer element from the DOM
// var timerElement = document.getElementById('timer');

// // Set the duration in seconds (e.g., 8 hours = 8 * 60 * 60 seconds)
// var durationInSeconds = 8 * 60 * 60;

// // Update the timer display
// function updateTimer() {
//   var hours = Math.floor(durationInSeconds / 3600);
//   var minutes = Math.floor((durationInSeconds % 3600) / 60);
//   var seconds = durationInSeconds % 60;

//   // Format the time values to have leading zeros if necessary
//   var formattedTime = hours.toString().padStart(2, '0') + ':' +
//                       minutes.toString().padStart(2, '0') + ':' +
//                       seconds.toString().padStart(2, '0');

//   // Update the timer element with the current time
//   timerElement.textContent = formattedTime;

//   // Decrease the duration by 1 second
//   durationInSeconds--;

//   // Check if the timer has reached zero
//   if (durationInSeconds < 0) {
//     clearInterval(timerInterval); // Stop the timer
//     timerElement.textContent = 'Timer Expired';
//   }
// }

// // Update the timer immediately and then every second
// updateTimer();
// var timerInterval = setInterval(updateTimer, 1000);
