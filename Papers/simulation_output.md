---
layout: default
title: 'simulation output'
---

<h1>simulation_output</h1>
<p>Discrete Tick Model Simulation</p>
<p>------------------------------</p>
<p>Fundamental Tick: 6.00e-13 seconds (0.6 ps)</p>
<p>
  Event 1 occurs over 3 full tick(s) (1.80e-12 s total, with each tick being 0.6
  ps).
</p>
<p>
  Event 2 is incomplete: it covers only 0.50 ticks, which means it does not sum
  to a whole tick. Partial ticks (e.g., 0.3 ps) must be aggregated (x2) to form
  a full 0.6 ps tick.
</p>
<p>Aggregated two 0.3 ps intervals: 6.00e-13 s, which equals 1 full tick(s).</p>
<p>
  Event 3 is incomplete:it covers 0.8 tick, which means it does not sum to a
  whole tick. Partial ticks (e.g., 0.3 ps) must be aggregated (x2) to form a
  full 0.6 ps tick.
</p>
<p>Note:</p>
<p>
  - All events must add up to whole, complete ticks (multiples of 0.6 ps) for
  full physical contribution.
</p>
<p>
  - Partial ticks (like 0.3 ps) count only as a fraction and must be aggregated
  (x2, x4, etc.) to form a full tick.
</p>
