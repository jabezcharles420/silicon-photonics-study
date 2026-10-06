# Week 2 · Day 1 — Monday 28 Sep 2026

*Simple-English study version of Chrostowski & Hochberg §4.1.1–4.1.3 (directional couplers: mode-solver modelling, phase, and experimental data)*

[:material-file-pdf-box: Download this day as PDF](day-01-mon-28-sep-2026.pdf){ .md-button }

---

## Before you start: the big picture

A photonic chip moves light around in tiny "wires" made of glass-like material, called **waveguides**. Very often you need to take some of the light in one wire and move it into another wire. For example, you may want to split light 50/50, or tap off 10% of it to measure it. The simplest device that does this is the **directional coupler**: two waveguides run side by side, very close together, for a short distance. While they are close, light slowly "leaks" from one waveguide into the other.

An everyday analogy: hang two identical pendulums from the same slightly flexible bar. Start one swinging and leave the other still. Slowly, the swinging moves into the second pendulum, until the first is almost still. Then the motion moves back again. The energy sloshes back and forth. A directional coupler does exactly this with light. How far the light must travel for all of it to move across is called the **cross-over length**. By choosing the gap between the waveguides and the length of the side-by-side section, you choose how much light ends up in each output.

These sections answer three practical questions. (1) How do we *calculate* the coupling for a given gap, length and wavelength (§4.1.1)? (2) What is the *phase* (timing) of the light that comes out of each output, which matters when couplers are used inside rings and interferometers (§4.1.2)? (3) Do real fabricated devices behave like the calculations, and what extra effect do the curved entry and exit sections add (§4.1.3)?

## Background you need

### Light as a wave

Light is a wave of electric and magnetic fields. At any point, the **electric field** $E$ goes up and down (positive, negative, positive…) very fast. The distance between two crests along the direction of travel is the **wavelength**, written $\lambda$ (lambda). This packet uses $\lambda = 1550$ nm $= 1.55$ µm, the standard wavelength for fibre-optic communication. It is infrared, so invisible to the eye. (1 µm = one millionth of a metre; 1 nm = one thousandth of a µm.)

What a detector measures is not the field itself but the **intensity** or **power**, which is proportional to the field squared, $|E|^2$. So a field of $+1$ and a field of $-1$ carry the same power. This fact is central to today's reading.

### Refractive index and effective index

Light travels slower in materials than in vacuum. The **refractive index** $n$ says how much slower: speed $= c/n$, where $c$ is the speed of light in vacuum. Silicon has $n \approx 3.48$ at 1550 nm; silicon dioxide (glass, used as cladding around the silicon) has $n \approx 1.44$.

Inside a waveguide, the light is partly in the silicon and partly in the surrounding glass. So it travels at a speed "in between". We describe that with the **effective index** $n_{eff}$: the light pattern behaves as if it were moving through a uniform material of index $n_{eff}$. In today's coupler, $n_{eff}$ is around 2.5–2.6.

### Phase and propagation constant

As a wave travels a distance $L$, its field goes through many up-and-down cycles. Where it is in its cycle is its **phase**, measured as an angle (a full cycle is $360°$ or $2\pi$ radians). The phase gained per unit length is the **propagation constant**:

$$\beta = \frac{2\pi n_{eff}}{\lambda}.$$

Here $2\pi/\lambda$ is "radians per metre in vacuum", and $n_{eff}$ scales it up because the wave is slower (and so more compressed) in the material. After a distance $L$, the phase is $\beta L$.

### Complex numbers as arrows (phasors)

Physicists write a wave with phase $\phi$ as $e^{i\phi}$. You can picture $e^{i\phi}$ as an **arrow of length 1** that points at angle $\phi$ from the horizontal axis. This picture is called a **phasor**.

- Multiplying by $e^{i\phi}$ rotates the arrow by $\phi$.
- $e^{i\pi} = -1$: rotating by $180°$ flips the arrow to point backwards.
- $e^{-i\pi/2} = -i$: rotating by $-90°$ (a quarter turn clockwise).
- Adding two waves means adding their arrows tip-to-tail, like adding forces.

The length of the final arrow is the **amplitude**; its angle is the phase. The symbol $\angle E$ means "the angle of the arrow $E$".

### Interference

When two waves meet, their fields add. If they are in step (arrows pointing the same way), they reinforce: **constructive interference**. If they are exactly opposite (arrows pointing opposite ways), they cancel: **destructive interference**. In between, you get something partial. A directional coupler is really an interference device.

### Waveguide modes

A **mode** is a field pattern that keeps its shape as it travels down a waveguide. Only the overall phase changes, at the rate $\beta$. Think of a guitar string: it can only vibrate in certain fixed shapes. A waveguide can carry light only in certain fixed cross-section shapes. The simplest one, the **fundamental mode**, looks like a single hump of field centred in the silicon, with tails that reach a little way into the surrounding glass. Those tails are called the **evanescent field**. They fall off roughly exponentially with distance from the silicon.

A **mode solver** (also called an **eigenmode solver**) is a program that takes the cross-section (shapes and materials) and finds the allowed mode shapes and their $n_{eff}$ values. It divides the cross-section into a grid of small cells, the **mesh**. A smaller mesh (here 20 nm) gives more accurate results but takes longer.

### The waveguide geometry in this packet

The waveguides are **rib** (or ridge) waveguides: a silicon strip 500 nm wide and 220 nm tall, sitting on a thin leftover layer of silicon 90 nm thick called the **slab**. The two strips are separated by a **gap** $g$ (usually 200 nm here).

```
   cross-section (not to scale)
        wg A         gap g        wg B
      +-------+   <------->   +-------+
      |       |               |       |   220 nm tall
 _____|       |_______________|       |_____
 ___________________________________________   90 nm slab
      <-500nm->               <-500nm->
```

### Supermodes: why two waveguides give two modes

When two identical waveguides are close together, the system as a whole has its own modes, called **supermodes**. The two lowest ones are:

- the **symmetric** (even) mode: the field has the same sign in both waveguides (hump up, hump up);
- the **antisymmetric** (odd) mode: the field has opposite signs (hump up, hump down). It must pass through zero in the middle of the gap.

These two have slightly different effective indices, $n_1$ (symmetric, larger) and $n_2$ (antisymmetric, smaller). Their difference is $\Delta n = n_1 - n_2$.

### How the coupler works, using supermodes

Light launched into waveguide A alone can be written as a sum of the two supermodes: (up, up) + (up, down) = (big, nothing). The two add in A and cancel in B. But the two supermodes travel at slightly different speeds. As they travel, one slowly gets ahead in phase. After a certain distance, the antisymmetric one is half a cycle ($\pi$) behind the symmetric one, so it has effectively flipped sign: (up, up) + (down, up) = (nothing, big). Now all the light is in waveguide B. That distance is the cross-over length $L_x$.

The phase difference grows as $(\beta_1 - \beta_2) L = \frac{2\pi \Delta n}{\lambda} L$. Setting this equal to $\pi$ gives:

$$L_x = \frac{\lambda}{2\Delta n}.$$

This is Equation (4.5) from the earlier part of the chapter. A small index difference means a long cross-over length.

### Coupling coefficients $t$ and $\kappa$, and conservation of power

The book (Eqs. 4.1–4.4, earlier in the chapter) describes a coupler with two numbers:

- $t$, the **through** (or "straight-through") coefficient: the fraction of the input *field* that stays in the original waveguide;
- $\kappa$ (kappa), the **cross** coefficient: the fraction of the input *field* that crosses into the other waveguide.

The *power* fractions are $t^2$ and $\kappa^2$. If no light is lost, $t^2 + \kappa^2 = 1$. For an ideal coupler of length $z$:

$$\kappa^2 = \sin^2\left(\frac{\pi}{2}\cdot\frac{z}{L_x}\right), \qquad t^2 = \cos^2\left(\frac{\pi}{2}\cdot\frac{z}{L_x}\right).$$

Since $\sin^2 + \cos^2 = 1$, power is conserved automatically. At $z = L_x$ the sine is 1: full cross-over.

### Exponentials and log plots

The evanescent tail of a mode decays roughly like $e^{-x/d}$ with distance $x$. A quantity that changes like $e^{-Ag}$ drops by the same *factor* for each equal step in $g$. On a plot with a **logarithmic** vertical axis (each grid line 10× the previous), an exponential appears as a straight line. That is why the book shows several plots on both linear and log scales.

> **Key takeaways:**
>
> - Power $\propto |E|^2$, so a field and its negative carry the same power, but they interfere differently.
> - Two coupled waveguides have two supermodes (symmetric and antisymmetric) with slightly different $n_{eff}$.
> - Their "beating" moves light back and forth; full transfer happens after $L_x = \lambda/(2\Delta n)$.
> - $t$ and $\kappa$ are field fractions; $t^2 + \kappa^2 = 1$ for a lossless coupler.

## 4.1.1 Waveguide mode solver approach

> **In one sentence:** We use a computer mode solver to find the two supermodes of the coupler, and from their effective indices we work out how the coupling depends on gap, length and wavelength.

The procedure in the book has three steps, each done by a script (Listings 4.5 and 4.6):

1. **Draw the geometry** (Listing 4.5): two 500 × 220 nm silicon ridges on a 90 nm slab, separated by the gap $g$, surrounded by oxide.
2. **Solve for the modes** (Listing 4.6): ask the solver for the two lowest modes at $\lambda = 1550$ nm. Out come the field shapes and the two effective indices.
3. **Use the indices**: compute $\Delta n$, then $L_x = \lambda/(2\Delta n)$, then $\kappa$ for any length.

**Figure 4.2 — The two fundamental supermodes of a directional coupler** ($\lambda = 1550$ nm, gap 200 nm, 500 × 220 nm waveguides on a 90 nm slab). There are four colour maps of the cross-section. The horizontal axis is sideways position (−2 to 2 µm); the vertical axis is height (about −0.2 to 0.6 µm). Black lines outline the two ridges, centred near −0.5 µm and +0.5 µm, and the thin slab joining them.

- **(a) Symmetric mode, real part of $E_y$** (the sideways field component). Both waveguides show a field of the same sign.
- **(b) Antisymmetric mode, real part of $E_y$.** One waveguide is positive, the other negative. The field crosses zero in the middle of the gap.
- **(c) Symmetric mode, intensity $|E|^2$**, and **(d) antisymmetric mode, intensity $|E|^2$.** Both show bright spots in the two silicon ridges. They look almost the same.

*Lesson:* if you only looked at power (c, d) you could not tell the two modes apart. The difference is in the *sign* of the field (a, b). That sign difference is what makes interference, and so coupling, possible. The zero in the gap (b) is the signature of the antisymmetric mode.

**Figure 4.3 — Light moving from one waveguide to the other.** This is a top-down map of intensity along a coupler, 40 µm long. The two supermodes from the solver are propagated forward using the **eigenmode expansion method**: write the input as a sum of modes, let each mode advance by its own phase $\beta L$, and add them back up at each position.

- From 0 to about 12 µm, the light is almost all in the lower waveguide.
- Around 20 µm, it is shared about equally between the two.
- From about 25 to 40 µm, it is almost all in the upper waveguide.

*Lesson:* this is the "pendulum" transfer in action. The light swaps waveguides over a distance of order 15–20 µm, as predicted by the supermode picture.

```
 intensity along the coupler (sketch)
 upper wg:  .........::::::######################
 lower wg:  ##############::::::.................
            0        10       20       30      40 µm
```

### Coupler-gap dependence

> **In one sentence:** The closer the waveguides, the stronger the coupling, and this strength falls off exponentially as the gap grows.

The book repeats the mode calculation for many gaps (Listing 4.7). In words, the script loops over gap values, re-draws the geometry for each, solves the two modes, and stores $L_x$. The result: the **coupling coefficient** $C$ (how strongly the waveguides talk to each other, per unit length) behaves as

$$C = B\cdot e^{-A\cdot g}. \qquad (4.6)$$

- $g$ is the gap.
- $A$ sets how fast the coupling dies off with gap. It is related to how fast the evanescent tail of each mode decays in the gap.
- $B$ is the coupling you would extrapolate to zero gap.
- Both depend on the geometry, the wavelength, and the materials.

*Why exponential?* The coupling comes from the overlap of one waveguide's evanescent tail with the other waveguide. That tail decays exponentially, so the overlap does too. Each extra bit of gap cuts the coupling by the same factor.

Since $L_x$ is inversely related to coupling strength, $L_x$ *grows* exponentially with gap.

**Figure 4.4 — Cross-over length $L_x$ versus gap** ($\lambda = 1550$ nm, 500 × 220 nm waveguides, 90 nm slab, 20 nm mesh). Two panels show the same data:

- **(a) Linear scale.** The curve is almost flat near zero for small gaps, then shoots up at large gaps.
- **(b) Log scale.** The points lie on a nearly straight line, which confirms the exponential law.

Approximate readings:

| Gap (nm) | $L_x$ (µm) |
|---|---|
| 50 | ≈ 5 |
| 200 | ≈ 20 (fit: 15.1) |
| 400 | ≈ 50 |
| 600 | ≈ 150 |
| 800 | ≈ 550 |
| 900 | ≈ 1000 |
| 1000 | ≈ 1800 |

Read the table as "for this gap, how long must the coupler be to move all the light across". (Values are read off a graph, so they are rough.) *Lesson:* going from a 200 nm gap to a 1000 nm gap makes the needed length about 100 times longer. Coupling is *very* sensitive to the gap. A few nanometres of fabrication error in the gap changes the coupler noticeably.

**A curve fit for $L_x$.** Because the log plot is a straight line, a simple formula fits it well (for this exact geometry: 500 × 220 nm, 90 nm slab):

$$L_x = 10^{(0.0026084\cdot g[\text{nm}] + 0.657094)}\ [\mu\text{m}]. \qquad (4.7)$$

- Put the gap in nanometres; the answer comes out in micrometres.
- $0.0026084$ is the slope of the straight line on the log plot: each extra nanometre of gap multiplies $L_x$ by $10^{0.0026} \approx 1.006$. So every ~115 nm of extra gap doubles $L_x$, and every ~383 nm multiplies it by 10.
- $0.657094$ is the intercept: at zero gap the fit would give $10^{0.657} \approx 4.5$ µm.

*Worked example:* $g = 200$ nm gives exponent $0.0026084 \times 200 + 0.657094 = 1.1788$, so $L_x = 10^{1.1788} \approx 15.1$ µm. This matches the book's value.

**From $L_x$ to $\kappa$.** With $L_x$ known, the field cross-coupling for any coupler length is

$$\kappa = \left(\frac{P_{Coupled}}{P_0}\right)^{1/2} = \sin\left(\frac{\pi\Delta n}{\lambda}\cdot L\right) = \sin\left(\frac{\pi}{2}\cdot\frac{z}{L_x}\right). \qquad (4.8)$$

- $P_0$ is the input power; $P_{Coupled}$ is the power that crossed over. Their ratio is $\kappa^2$; the square root gives the field fraction $\kappa$.
- The middle form uses $\Delta n$ directly. The last form substitutes $L_x = \lambda/(2\Delta n)$. They are the same thing. ($L$ and $z$ both mean the coupler length here.)
- The shape is a sine because of the supermode beating: the cross-over field grows as the two supermodes drift out of step.

*Worked example:* a coupler with $g = 200$ nm ($L_x = 15.1$ µm) and length 5 µm has $\kappa = \sin(\frac{\pi}{2}\cdot\frac{5}{15.1}) = \sin(0.52) \approx 0.50$. So $\kappa^2 \approx 0.25$: about a quarter of the power crosses over.

**Figure 4.5 — $\kappa$ versus gap for 5 µm and 15 µm long couplers** ($\lambda = 1550$ nm, same waveguides). Points come from the mode solver; solid lines come from the fit, Eq. (4.7). Two panels: (a) linear and (b) log vertical axis.

- **5 µm coupler (circles):** $\kappa$ falls steadily as the gap grows. About 0.96 at 50 nm, 0.8 at ~90 nm, 0.6 at ~150 nm, 0.1 at ~500 nm, and about 0.004 at 1000 nm.
- **15 µm coupler (squares):** $\kappa$ starts near zero at small gaps, rises to a peak near 1 at about 200 nm, then falls: ~0.6 at 320 nm, ~0.2 at 550 nm, ~0.02 at 1000 nm. For gaps above ~150 nm it is always higher than the 5 µm curve.

The fit is most accurate for larger gaps. For small gaps the real coupling departs a little from the pure exponential, because the simple "overlapping tails" picture is less accurate when the waveguides are very close.

*Why does the 15 µm coupler have almost zero coupling at a 100 nm gap?* At $g = 100$ nm, the fit gives $L_x \approx 8$ µm. A 15 µm coupler is then nearly $2L_x$ long. The light crosses over (at 8 µm) and then comes almost all the way back (at ~16 µm). So at the output, nearly all the power is back in the input waveguide. *Lesson:* "closer gap" does not always mean "more coupling at the output". Because the transfer is periodic, a long coupler with a small gap can overshoot and come back.

### Coupler-length dependence

> **In one sentence:** For a fixed gap, the power sloshes back and forth between the two outputs as a sine-squared function of length.

Using Eq. (4.8) with a fixed gap, you can plot coupling against length.

**Figure 4.6 — Power coupling versus length of an ideal coupler** (only straight parallel waveguides, no bends; $g = 200$ nm, $\lambda = 1550$ nm).

- The **cross port** ($\kappa^2$, solid line) starts at 0, reaches 0.5 at about 7.5 µm, reaches 1.0 at about 15 µm, and drops back to 0.5 at ~22.5 µm and ~0.32 at 25 µm.
- The **through port** ($t^2$, dashed line) is its mirror image: starts at 1, is 0 at 15 µm, and is ~0.68 at 25 µm.
- The two curves always add to 1, and they cross at 0.5 at the same lengths.

*Lesson:* a 50/50 splitter at this gap needs about 7.5 µm (half of $L_x$); full transfer needs about 15 µm.

**Designing for a target.** To make, say, a 10% coupler, pick a gap and solve Eq. (4.8) for length. The book's example is $g = 200$ nm, $L = 3$ µm. Check: $\kappa = \sin(\frac{\pi}{2}\cdot\frac{3}{15.1}) = \sin(0.312) \approx 0.307$, so $\kappa^2 \approx 0.094$, about 10% of the power. (Here "10%" means power, $\kappa^2$.) Many (gap, length) pairs give the same coupling; you choose one that is easy to fabricate and not too sensitive.

### Wavelength dependence

> **In one sentence:** Longer wavelengths spread further out of the waveguides, so they couple more strongly and cross over in a shorter distance.

The book repeats the mode calculation for many wavelengths (Listing 4.8): loop over $\lambda$, solve the two supermodes at each, store $n_{eff}$ of both, then compute $L_x = \lambda/(2\Delta n)$ using Eq. (4.5).

**Figure 4.7 — Wavelength dependence of the coupler** ($g = 200$ nm, 20 nm mesh).

- **(a) $n_{eff}$ of the two modes from 1.50 to 1.60 µm.** Both fall in nearly straight lines as wavelength rises. The symmetric mode goes from about 2.63 to 2.553; the antisymmetric from about 2.589 to 2.495. The symmetric mode is always higher, by roughly 0.04–0.06.
- **(b) Cross-over length.** It falls from about 17.7 µm at 1.50 µm, through about 15.5 µm at 1.55 µm, to about 13.85 µm at 1.60 µm.

| $\lambda$ (µm) | $n_{eff}$ symmetric | $n_{eff}$ antisymmetric | $L_x$ (µm) |
|---|---|---|---|
| 1.50 | ≈ 2.630 | ≈ 2.589 | ≈ 17.7 |
| 1.55 | ≈ 2.590 | ≈ 2.543 | ≈ 15.5 |
| 1.60 | ≈ 2.553 | ≈ 2.495 | ≈ 13.85 |

(Graph readings; small inconsistencies are reading error.) Read each row as: at this colour of light, here are the two supermode indices and the resulting cross-over length.

*Why does this happen?* A longer wavelength is "bigger" compared with the waveguide. It is less tightly held by the silicon, so $n_{eff}$ drops and the evanescent tails reach further. Bigger tails mean more overlap with the neighbour, so a larger $\Delta n$ and a shorter $L_x$. That is about a 20% change in $L_x$ over a 100 nm band: a coupler designed for one wavelength gives a different split at another.

**Figure 4.8 — $\kappa$ versus wavelength for 1, 2 and 5 µm long couplers** ($g = 200$ nm, mode solver).

| Length | $\kappa$ at 1.50 µm | $\kappa$ at 1.55 µm | $\kappa$ at 1.60 µm |
|---|---|---|---|
| 1 µm | ≈ 0.090 | ≈ 0.105 | ≈ 0.117 |
| 2 µm | ≈ 0.175 | ≈ 0.202 | ≈ 0.228 |
| 5 µm | ≈ 0.267 | ≈ 0.30 | ≈ 0.338 |

All three rise in nearly straight lines with wavelength. Longer couplers have larger $\kappa$ (as expected for lengths well below $L_x$). *Lesson:* coupling is wavelength-dependent. The 5 µm coupler changes from 0.267 to 0.338 field coupling over 100 nm, i.e. power coupling from about 7% to 11%. Designers of broadband circuits must plan for this.

> **Key takeaways:**
>
> - A mode solver gives the two supermode indices; $L_x = \lambda/(2\Delta n)$ follows directly.
> - Coupling falls (and $L_x$ rises) exponentially with gap: $L_x \approx 15.1$ µm at 200 nm, roughly 1800 µm at 1000 nm.
> - $\kappa = \sin(\frac{\pi}{2} z/L_x)$; the transfer is periodic, so too-long couplers overshoot.
> - Longer wavelengths couple more strongly: $L_x$ drops from ~17.7 to ~13.85 µm between 1.50 and 1.60 µm.
> - A 10% power coupler can be made with $g = 200$ nm and $L = 3$ µm.

## 4.1.2 Phase

> **In one sentence:** The light that crosses over to the other waveguide is always a quarter-cycle (90°) out of step with the light that stays, and circuit models must include this.

So far we only asked *how much* light goes to each output: the sizes $|t|$ and $|\kappa|$. But light is a wave, so each output also has a **phase**. When couplers are combined into rings or interferometers, outputs interfere with other light, so the phase matters as much as the power.

### Building the outputs from the two supermodes

**Figure 4.9 — The two eigenmodes and the phase picture.** The figure has three parts.

- **Left, "Mode 1"** (symmetric): a plot of field $E$ against sideways position $x$. There is a positive hump over "wg A" and a positive hump over "wg B".
- **Middle, "Mode 2"** (antisymmetric): a positive hump over wg A and a *negative* hump over wg B, crossing zero between them.
- **Right, an arrow (phasor) diagram.** Blue arrows are the mode contributions: "Mode 1" points horizontally; "Mode 2" points up-right; "Mode 2b" (Mode 2's part in waveguide B) is drawn dashed, pointing exactly the opposite way to Mode 2. Red arrows are the sums: "wg A" = Mode 1 + Mode 2 (pointing up-right, between them), and "wg B" = Mode 1b + Mode 2b (pointing down-right). A small right-angle mark highlights a 90° angle.

*Lesson:* the field in each waveguide is the arrow-sum of the two supermodes' contributions there. In wg B, Mode 2 enters with a flipped sign. That flip makes the two sums end up at right angles to each other.

```
 arrow picture (sketch)
            Mode 2
             /
            /  wg A = Mode1 + Mode2
           / _/
          /_/
   ------+-------> Mode 1
         /\_
        /   \_  wg B = Mode1 + (-Mode2)
       /      \
   Mode 2b (= -Mode 2)
```

Light launched into wg A is half symmetric mode plus half antisymmetric mode. After a length $L$, mode 1 has gained phase $\beta_1 L$ and mode 2 has gained $\beta_2 L$. Adding their contributions in each waveguide:

$$E_{wg A} = \frac{1}{\sqrt{2}}\left(e^{i\beta_{1}L}+e^{i\beta_{2}L}\right) \qquad (4.9a)$$

$$E_{wg B} = \frac{1}{\sqrt{2}}\left(e^{i\beta_{1}L}+e^{i\beta_{2}L-i\pi}\right). \qquad (4.9b)$$

- $\beta_1, \beta_2$: propagation constants of the symmetric and antisymmetric modes.
- $e^{i\beta L}$: an arrow rotated by the phase the mode has gained over length $L$.
- The extra $-i\pi$ in (4.9b): multiplying by $e^{-i\pi} = -1$. This is the sign flip of Mode 2 in wg B (its negative lobe).
- $\frac{1}{\sqrt{2}}$: a scaling factor for splitting the input between the two modes. It does not affect the phase, which is what we care about here.

**What it says.** In wg A, the two arrows are *added*. In wg B, one is *subtracted*. At $L = 0$ the arrows point the same way, so wg A gets everything and wg B gets zero. As $L$ grows, the arrows drift apart (because $\beta_1 \neq \beta_2$). Their sum shrinks and their difference grows: light moves from A to B.

### The phase of each output

A neat trick: factor out the *average* phase. Let $\bar\beta = \frac{\beta_1+\beta_2}{2}$ (the average) and $\Delta\beta = \beta_1 - \beta_2$. Then

$$e^{i\beta_1 L} + e^{i\beta_2 L} = e^{i\bar\beta L}\cdot 2\cos\left(\frac{\Delta\beta L}{2}\right),$$

$$e^{i\beta_1 L} - e^{i\beta_2 L} = e^{i\bar\beta L}\cdot 2i\sin\left(\frac{\Delta\beta L}{2}\right).$$

The first is a real number times the average-phase arrow. The second has an extra factor $i$, which is a 90° rotation. This gives the book's results:

$$\angle E_{wg A} = \frac{\beta_{1}+\beta_{2}}{2}L \qquad (4.10a)$$

$$\angle E_{wg B} = \frac{\beta_{1}+\beta_{2}}{2}L-\frac{\pi}{2} \qquad (4.10b)$$

$$\angle E_{wg B}-\angle E_{wg A} = -\frac{\pi}{2}. \qquad (4.10c)$$

In words:

- The light staying in wg A has simply picked up the *average* phase of the two modes, as if it travelled in one waveguide with the average index.
- The light in wg B has the same average phase, plus a quarter-turn shift.
- So the crossed light and the through light are always **90° apart** (in **quadrature**), whatever the length.

A note on the sign: whether the shift is written as $-\pi/2$ or $+\pi/2$ depends on bookkeeping choices (how the wave's time dependence is written, and which waveguide's lobe is taken as negative). The book uses $-\pi/2$. The physical, convention-free fact is the 90° difference between the two outputs. Also note: the cos/sin factors above are the familiar $t$ and $\kappa$ magnitudes, $\cos(\frac{\pi}{2}\frac{L}{L_x})$ and $\sin(\frac{\pi}{2}\frac{L}{L_x})$, since $\Delta\beta L/2 = \pi\Delta n L/\lambda$.

*Why must it be 90°?* Think of energy conservation. If the crossed light came out exactly in step with the through light, combining couplers could create or destroy energy in impossible ways. A 90° shift is what keeps $|t|^2 + |\kappa|^2 = 1$ true for every input combination. This is a general property of any lossless, symmetric 2×2 coupler.

### Putting the phase into $t$ and $\kappa$

The book now writes the coefficients with their phases:

$$t = |t|^{2}\cdot e^{i\frac{\beta_{1}+\beta_{2}}{2}L} \qquad (4.11a)$$

$$\kappa = |\kappa|^{2}\cdot e^{i\frac{\beta_{1}+\beta_{2}}{2}L-i\frac{\pi}{2}}. \qquad (4.11b)$$

Each is "size × phase arrow". The phase arrow is the average propagation phase, with the extra $-\pi/2$ on the cross term.

A caution when reading: $t$ and $\kappa$ are *field* coefficients, so the size in front should be the field magnitude, $|t|$ and $|\kappa|$ (whose squares are the power fractions). The book prints $|t|^2$ and $|\kappa|^2$ here and in (4.12); treat the prefactor as "the magnitude of the coefficient". The phase part, which is the point of the section, is unaffected.

### Two ways to handle phase in circuit models

In **photonic circuit modelling**, each device is represented by a **compact model**: a small mathematical description (often a matrix of $t$'s and $\kappa$'s) instead of a full field simulation. There are two options:

1. **Keep the propagation phase inside the coupler model**, as in (4.11).
2. **Move it out.** Assume the coupler's average propagation constant equals that of a single plain waveguide. Then the phase $\bar\beta L$ can be counted as part of the ordinary waveguide length in the circuit (this is what the book does for the ring resonator model in §4.4.1). The coupler itself keeps only the 90° shift:

$$t = |t|^{2} \qquad (4.12a)$$

$$\kappa = |\kappa|^{2}\cdot e^{-i\frac{\pi}{2}} = -i|\kappa|^{2}. \qquad (4.12b)$$

The through coefficient is a plain positive number. The cross coefficient is multiplied by $-i$: a quarter-turn. (Same caution about $|\cdot|^2$ versus $|\cdot|$ as above.) This is the form most often used in ring and interferometer formulas: "through gets $t$, cross gets $-i\kappa$".

> **Key takeaways:**
>
> - The output in each waveguide is an arrow-sum of the two supermodes; Mode 2 enters wg B with a minus sign.
> - Both outputs carry the average propagation phase $\frac{\beta_1+\beta_2}{2}L$.
> - The crossed light is shifted by a quarter cycle ($\pi/2$, 90°) relative to the through light, at every length.
> - Circuit models often move the average phase into the waveguide and keep only $t$ and $-i\kappa$ in the coupler.

## 4.1.3 Experimental data

> **In one sentence:** By measuring many real couplers of different lengths and fitting a sine-squared curve, we extract the real cross-over length and the extra coupling contributed by the curved bends.

### What the experiment does

Real couplers are not just two straight parallel waveguides. The waveguides must curve in towards each other and curve away again. Those **bends** are also fairly close together, so some coupling happens there too. That extra coupling is hard to calculate, so we measure it.

The method:

- Use a basic coupler design (Figure 4.1a of the book, earlier in the chapter, which shows a 1 µm long coupler with its bends).
- Make many copies, changing only the straight coupler length: from 0 to 25 µm in steps of 0.5 µm.
- Measure the power coming out of the through port and the cross port of each.
- An **automated probe station** (a machine that moves an optical fibre from device to device; see §12.2) measured 100 devices on each of two separate **die** (individual chips cut from the same silicon wafer). Each measurement was done twice to check it was **repeatable**.
- Light goes in and out through **grating couplers**: small patterned structures that redirect light between a fibre above the chip and the waveguide. Their efficiency depends on wavelength and fibre angle. The fibre angle was adjusted so the grating response is centred on 1550 nm.
- Spectra were measured from 1500 to 1570 nm. Each power trace was **integrated** (summed) over that range, then **normalized** to the maximum power, so values run from 0 to 1.

### The fit

The data are fitted with:

$$\kappa^{2} = \sin^{2}\left(\frac{\pi}{2L_{x}}\cdot\left[L+z_{bend}\right]\right) \qquad (4.13a)$$

$$t^{2} = \cos^{2}\left(\frac{\pi}{2L_{x}}\cdot\left[L+z_{bend}\right]\right). \qquad (4.13b)$$

- $L$: the drawn straight coupler length (what was varied).
- $L_x$: the cross-over length (unknown, to be fitted).
- $z_{bend}$: the **effective extra length** due to the bends (unknown, to be fitted). The bends add some coupling; we pretend this is the same as having $z_{bend}$ more micrometres of straight coupler.
- These are just the ideal-coupler formulas with $L$ replaced by $L + z_{bend}$.

Two free numbers, $L_x$ and $z_{bend}$, are adjusted until the curves best match the measured points.

**Figure 4.10 — Measured coupler behaviour, with fits** (devices made by the OpSIS-IME foundry service). Two panels, (a) Die #1 and (b) Die #2. Horizontal axis: coupler length 0–25 µm. Vertical axis: normalized power.

- **Cross port** ($\kappa^2$, circles = measurements, line = fit): starts low (~0.1 or ~0.08 at 1 µm, not zero), peaks near 1.0 around 13–16 µm, and falls again (~0.2 on Die #1, ~0.35 on Die #2 at 25 µm).
- **Through port** ($t^2$, squares and line): the mirror image, starting near 0.95, dipping to a few percent (~0.02–0.05) near the peak of the cross port, and recovering (~0.85 and ~0.7 at 25 µm).
- Fit results: Die #1 has $L_x = 16.2$ µm and $z_{bend} = 2.8$ µm. Die #2 has $L_x = 16.8$ µm and $z_{bend} = 2.3$ µm.

*Lesson:* the real devices show the clean sine-squared sloshing that theory predicts. Note that even at zero straight length the cross port is not zero: the bends already couple some light. That is exactly what $z_{bend}$ captures. The through port never quite reaches 0 because real devices are imperfect.

### What we learn

| Quantity | Die #1 | Die #2 | Simulation |
|---|---|---|---|
| $L_x$ (µm) | 16.2 | 16.8 | 15.5 (Fig. 4.7b) |
| $z_{bend}$ (µm) | 2.8 | 2.3 | — |

Read the table as: measured values on two chips, compared with the mode-solver prediction.

- The measured cross-over length is 16.2–16.8 µm, within about 5–8% of the simulated 15.5 µm. Good agreement, given fabrication variations (slightly different gap or waveguide width change $L_x$, as §4.1.1 showed).
- The bends add the equivalent of 2.3–2.8 µm of straight coupler. That is a large fraction of a short coupler. For example, for a 3 µm design, ignoring the bends would badly under-estimate the coupling.
- The two die differ slightly, which shows the size of chip-to-chip variation across a wafer.

> **Key takeaways:**
>
> - Measure many couplers of different lengths, then fit $\sin^2$ and $\cos^2$ curves with $L \to L + z_{bend}$.
> - Measured $L_x = 16.2$–$16.8$ µm agrees well with the simulated 15.5 µm.
> - The bends act like an extra 2.3–2.8 µm of coupler, which matters a lot for short couplers.
> - Small differences between die reflect normal fabrication variation.

## Glossary

| Term | Plain meaning |
|---|---|
| Amplitude | The size of a wave's field (the length of its phasor arrow). |
| Antisymmetric (odd) mode | Supermode whose field has opposite signs in the two waveguides, with a zero in the gap. |
| Automated probe station | Machine that moves fibres from device to device on a chip to measure many devices automatically. |
| Bend | Curved waveguide section that brings the two waveguides together or takes them apart. |
| Compact model | A small mathematical description of a device (e.g. its $t$ and $\kappa$) used in circuit simulation. |
| Constructive / destructive interference | Waves adding in step (stronger) / out of step (cancelling). |
| Coupling coefficient $C$ | How strongly two waveguides exchange light per unit length; falls exponentially with gap. |
| Cross port | The output on the *other* waveguide from the input. |
| Cross-over length $L_x$ | Length needed for all the light to move from one waveguide to the other; $L_x = \lambda/(2\Delta n)$. |
| Die | One chip cut from a wafer. |
| Directional coupler | Two waveguides running close side by side so light transfers between them. |
| Effective index $n_{eff}$ | The refractive index the guided light "feels" overall; sets its speed. |
| Eigenmode (mode) | A field pattern that travels down a waveguide without changing shape. |
| Eigenmode expansion | Simulation method: write the light as a sum of modes, advance each by its own phase, re-add. |
| Electric field $E$ | The oscillating quantity in a light wave; can be positive or negative. |
| Evanescent field | The tail of a mode that extends outside the waveguide core, decaying exponentially. |
| Gap $g$ | Distance between the two waveguides in the coupler. |
| Grating coupler | Patterned structure that couples light between an optical fibre and an on-chip waveguide. |
| Intensity $\vert E\vert^2$ | Power density of light; proportional to field squared. |
| $\kappa$ (kappa) | Field cross-coupling coefficient; $\kappa^2$ is the fraction of power that crosses over. |
| Mesh | The grid of small cells a mode solver uses; finer mesh is more accurate. |
| Mode solver | Program that computes the modes and effective indices of a waveguide cross-section. |
| Normalize | Divide by a reference (here the maximum) so values run from 0 to 1. |
| Phase | Where a wave is in its cycle, as an angle. |
| Phasor | Picture of a wave as an arrow whose length is the amplitude and angle is the phase. |
| Propagation constant $\beta$ | Phase gained per unit length; $\beta = 2\pi n_{eff}/\lambda$. |
| Quadrature | Being 90° apart in phase. |
| Refractive index $n$ | How much slower light travels in a material than in vacuum. |
| Rib / ridge waveguide | A silicon strip sitting on a thinner silicon slab. |
| Slab | The thin (here 90 nm) silicon layer left under and between the ridges. |
| Supermode | A mode of the two-waveguide system as a whole. |
| Symmetric (even) mode | Supermode with the same field sign in both waveguides. |
| $t$ | Field through coefficient; $t^2$ is the fraction of power that stays in the input waveguide. |
| Through port | The output on the same waveguide as the input. |
| Wavelength $\lambda$ | Distance between wave crests; here about 1550 nm. |
| $z_{bend}$ | Extra effective coupler length contributed by the bends. |

## Check yourself

1. Why can't you tell the symmetric and antisymmetric supermodes apart by looking only at their intensity plots?

   *Answer:* Intensity is $|E|^2$, which ignores sign. The two modes differ only in the sign of the field in one waveguide, which shows up in Real($E_y$) but not in $|E|^2$.

2. Using Eq. (4.7), what is $L_x$ for a 200 nm gap, and roughly how much longer is it for a 300 nm gap?

   *Answer:* 15.1 µm at 200 nm. Adding 100 nm multiplies $L_x$ by $10^{0.26} \approx 1.82$, giving about 27.5 µm.

3. Why does coupling fall off exponentially with gap?

   *Answer:* It comes from the overlap of each waveguide's evanescent tail with the neighbour, and those tails decay exponentially with distance.

4. A 15 µm coupler with a 100 nm gap couples almost no light to the cross port. Why?

   *Answer:* At 100 nm, $L_x \approx 8$ µm. 15 µm is close to $2L_x$, so the light crosses over and then nearly all comes back to the input waveguide.

5. What length gives a 50/50 power split at $g = 200$ nm (ideal coupler, no bends)?

   *Answer:* About $L_x/2 \approx 7.5$ µm, where $\sin^2(\pi/4) = 0.5$.

6. Does $L_x$ get longer or shorter at longer wavelengths, and why?

   *Answer:* Shorter (about 17.7 µm at 1.50 µm to 13.85 µm at 1.60 µm). Longer wavelengths are less tightly confined, so their tails overlap more, $\Delta n$ grows and $L_x = \lambda/(2\Delta n)$ falls.

7. What is the phase difference between the through and cross outputs, and where does it come from?

   *Answer:* 90° ($\pi/2$; the book writes $-\pi/2$). It comes from the antisymmetric mode entering the second waveguide with a minus sign, which turns the sum of two arrows into a difference, giving an extra factor $i$.

8. In the simplified circuit model (4.12), what are the through and cross coefficients?

   *Answer:* Through is a real positive magnitude; cross is the magnitude times $-i$ (a quarter-turn). The average propagation phase is counted in the ordinary waveguide instead.

9. What does $z_{bend}$ represent, and what values were measured?

   *Answer:* The extra coupling from the curved sections, expressed as an equivalent extra length of straight coupler. It was 2.8 µm (Die #1) and 2.3 µm (Die #2).

10. How well did simulation match experiment for $L_x$?

    *Answer:* Simulated 15.5 µm vs measured 16.2–16.8 µm, about 5–8% apart, which is good given fabrication variation.
