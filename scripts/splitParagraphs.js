document.addEventListener("DOMContentLoaded", function() {
  // Target all paragraphs within your main container—adjust the selector to match your layout structure
  const paragraphs = document.querySelectorAll(".container p");
  paragraphs.forEach(function(p) {
    // Replace every period followed by a space with a period and two <br> tags, creating a visual paragraph break
    p.innerHTML = p.innerHTML.replace(/\. /g, ".<br><br>");
  });
});


