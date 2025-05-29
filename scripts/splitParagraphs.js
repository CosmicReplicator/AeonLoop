<script>
document.addEventListener("DOMContentLoaded", function() {
  // Target all paragraphs within your container—adjust the selector as needed.
  const paragraphs = document.querySelectorAll(".container p");
  paragraphs.forEach(function(p) {
    // Replace every period followed by a space with a period and two <br> tags.
    p.innerHTML = p.innerHTML.replace(/\. /g, ".<br><br>");
  });

  // Check if MathJax is loaded, then re-typeset the page.
  if (window.MathJax) {
    MathJax.typesetPromise().catch(function(err) {
      console.error("MathJax typeset failed: ", err);
    });
  }
});
</script>
