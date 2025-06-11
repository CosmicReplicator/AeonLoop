<script>
document.addEventListener("DOMContentLoaded", function() {
  // Target all paragraphs within .container (adjust the selector if needed)
  const paragraphs = document.querySelectorAll(".container p");

  paragraphs.forEach(function(p) {
    // Check if the paragraph likely contains math delimiters
    if (
      p.innerHTML.includes("$") || 
      p.innerHTML.includes("$$") || 
      p.innerHTML.includes("\\(")
    ) {
      // If math is found, skip replacement in this paragraph.
      return;
    }
    // For paragraphs without math content, replace ". " with a single <br>
    p.innerHTML = p.innerHTML.replace(/\. /g, ".<br>");
  });

  // If MathJax is loaded, re-typeset the page to render math correctly.
  if (window.MathJax) {
    MathJax.typesetPromise().catch(function(err) {
      console.error("MathJax typeset failed: ", err);
    });
  }
});
</script>
