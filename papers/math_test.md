---
layout: default
title: "Math Rendering Test Paper"
---

# Math Rendering Test Paper

This document is designed to test the rendering of many different math styles. Below are sections that each illustrate a specific approach or syntax. Use these to diagnose which math expressions render as expected and which don’t.

---

## 1. Inline Math Examples

Here are some inline math examples:

- Using inline delimiters with backslashes:
  - \( a + b = c \)
  - \( \frac{a}{b} \)
  - \( \alpha, \beta, \gamma \)

- Alternatively, some environments support single-dollar inline math (though this can sometimes conflict with regular text):
  - $a - b = c$

Observe the spacing and positioning relative to the text.

---

## 2. Display Math with `$$ ... $$`

Display math is usually best when set off on its own line. For example:

$$
a + b = c
$$

Using display mode with a larger integral:

$$
\displaystyle \int_0^1 x^2 \, dx = \frac{1}{3}
$$

And a summation:

$$
\displaystyle \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}
$$

---

## 3. Display Math with `

\[ ... \]

`

Some authors prefer using the LaTeX display-style delimiters `

\[ ... \]

`:



\[
\sqrt{2} \times \sqrt{2} = 2
\]





\[
\frac{d}{dx} \, (x^2) = 2x
\]



Check that these render in a similar style to the previous section.

---

## 4. Boxed Equations

To highlight an entire equation, you can use the `\boxed{...}` command (provided by amsmath):

For example, box a famous equation:
  
$$
\boxed{E = mc^2}
$$

Or box a more complex inequality:

$$
\boxed{\displaystyle \left|\frac{\dot{G}}{G}\right| < 10^{-14}\,\text{yr}^{-1}}
$$

Compare these boxed outputs with the non-boxed versions.

---

## 5. Delimiter Testing with `\left` and `\right`

Proper use of variable-sized delimiters is critical. Correct usage:

$$
\left( \frac{a}{b} \right)
$$

**Note:** If one omits a matching delimiter, for example:

```latex
```

$$\left( \frac{a}{b}$$

# Minimal Math Test

Inline math with dollars: $a + b = c$.

Inline math with LaTeX delimiter: \( \frac{a}{b} \).

Display math with dollars:

$$
\int_0^1 x^2 \, dx = \frac{1}{3}
$$

Display math with LaTeX delimiter: