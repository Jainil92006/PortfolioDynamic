document.getElementById("no-btn").addEventListener("click", function () {
    document.getElementById("hm").style.display = "none"; // Hides the element
});

document.getElementById("hire-btn").addEventListener("click", function () {
    document.getElementById("hm").style.display = "yes"; // Shows the element
});




const button = document.getElementById("scrollButton");
let scrollTimeout;

window.addEventListener("scroll", () => {
  // Show the button
  button.style.display = "block";

  // Clear any previous timeout
  clearTimeout(scrollTimeout);

  // Hide the button after 2 seconds of no scrolling
  scrollTimeout = setTimeout(() => {
    button.style.display = "none";
  }, 2000);
});

