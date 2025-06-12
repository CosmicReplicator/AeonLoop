<script>
document.addEventListener("DOMContentLoaded", () => {

  /* Helper: does a string contain any TeX delimiters? */
  const hasMath = s =>
    /[$]{1,2}|\\\(|\\\)|\\

\[|\\\]

|\\begin\{|\\end\{/.test(s);

  /* Iterate over <p> inside .container (adjust selector as needed) */
  document.querySelectorAll('.container p').forEach(p => {

    /* Skip paragraphs that already carry math delimiters */
    if (hasMath(p.textContent)) return;

    /* Walk the childNodes and add <br> after “. ” in pure text nodes */
    p.childNodes.forEach(node => {
      if (node.nodeType === Node.TEXT_NODE) {
        const html = node.textContent.replace(/\. (\S)/g, '.<br>$1');
        /* Replace only if something changed */
        if (html !== node.textContent) {
          /* Insert the new HTML right before the text node */
          const frag = document.createRange().createContextualFragment(html);
          node.replaceWith(frag);
        }
      }
    });
  });

  /* ONE MathJax typeset after we’re done */
  if (window.MathJax?.typesetPromise) {
    MathJax.typesetPromise().catch(err =>
      console.error('MathJax typeset failed:', err)
    );
  }
});
</script>

