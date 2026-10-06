# Week 1 · Day 3 — Wednesday 23 Sep 2026

*Simple-English study version of Chrostowski & Hochberg §3.2.5–3.2.6 (Effective Index Method) and §3.3 (Bent waveguides)*

[:material-file-pdf-box: Download this day as PDF](day-03-wed-23-sep-2026.pdf){ .md-button }

## Before you start: the big picture

A photonic chip moves light around in tiny "wires" made of silicon. These wires are called **waveguides**. To design a chip, you need to answer two practical questions about them. First: how does light sit inside the wire, and how fast does it travel? Second: what happens when you bend the wire to route light around the chip?

This packet answers both. The first part (§3.2.5–3.2.6) teaches a quick trick, the **Effective Index Method**, that turns a hard 2D problem into two easy 1D problems. It is not perfectly accurate, but it is fast and it builds intuition. The second part (§3.3) looks at **bends**: how much light is lost when the wire curves, where that loss comes from, and how small you can make a bend before the loss gets too big.

An everyday analogy: think of a waveguide as a water slide with walls, and light as water rushing down it. On a straight slide the water stays in the middle. On a curve the water sloshes toward the outer wall. If the curve is too sharp, some water splashes over the edge (radiation loss). And even if no water escapes, the sudden change from "straight" to "curved" makes the water splash around (mode mismatch loss). Engineers want curves that are tight (to save space) but gentle enough to keep the water in.

## Background you need

**Light as a wave.** Light is a wave of electric and magnetic fields that wiggle as the wave moves. The **electric field** ($E$) is the part we usually plot. Its strength at each point tells us how much light is there. The **intensity** (brightness, or power per area) is proportional to $|E|^2$, the field squared.

**Wavelength.** The distance between two crests of the wave. Silicon photonics usually uses light with a wavelength of about 1.55 µm (micrometres; 1 µm = 1000 nm = one-millionth of a metre). That is infrared light, invisible to the eye.

**Refractive index ($n$).** A number that tells you how much a material slows light down. Light in a material with index $n$ travels at $c/n$, where $c$ is the speed of light in vacuum. Air has $n \approx 1.0$, silicon dioxide (glass, "oxide") has $n \approx 1.45$, silicon has $n \approx 3.5$. A big index means light is slowed a lot.

**Why light stays in a waveguide.** Light tends to stay in the region of higher index. If a strip of silicon ($n \approx 3.5$) is surrounded by oxide or air (lower $n$), light bouncing at a shallow angle off the boundary is reflected back completely. This is called **total internal reflection**. So the silicon acts like a pipe for light.

**Mode.** Light inside a waveguide cannot take any shape it likes. Only certain stable patterns of field fit inside, like only certain notes fit on a guitar string. Each such pattern is a **mode**. The simplest one, with a single bright hump, is the **fundamental mode**. Patterns with more humps are **higher-order modes**. A mode keeps its shape as it travels down a straight waveguide.

**Evanescent field.** Part of a mode's field leaks a little outside the core. It does not travel away; it just fades quickly (exponentially) with distance. This "tail" is the **evanescent field**.

**Effective index ($n_{eff}$).** A mode is partly in silicon and partly in the lower-index surroundings. So it "feels" an average index somewhere between the two. This average is the **effective index**. It sets how fast the mode's wave crests move: speed $= c/n_{eff}$. A higher $n_{eff}$ means the light is more tightly held in the silicon.

**Group index ($n_g$).** A pulse of light (a packet carrying information) travels at a slightly different speed from the wave crests. That pulse speed is $c/n_g$, where $n_g$ is the **group index**. It matters for resonators (see FSR below).

**Polarization: TE and TM.** The electric field points in some direction across the waveguide. For a flat chip: if $E$ points mostly sideways (parallel to the chip surface), the mode is called **TE** (transverse electric). If $E$ points mostly up and down, it is **TM** (transverse magnetic). In a real 2D waveguide modes are not purely one or the other, so we say **TE-like** and **TM-like**.

**Waveguide shapes.** Standard silicon waveguides are 500 nm wide and 220 nm tall.

- A **strip waveguide** is a simple rectangle of silicon sitting on oxide.
- A **rib waveguide** is a rectangle that sits on top of a thinner sheet ("slab") of silicon, here 90 nm thick. The slab lets you make electrical contacts, which is useful for modulators.
- A **slab waveguide** is an infinitely wide flat sheet. It only confines light in one direction (up/down). It is a 1D problem and easy to solve.

```
   Strip                     Rib
   +-----+  220 nm           +-----+   220 nm
   | Si  |              _____|     |_____ 90 nm slab
 ==+=====+== oxide      =====================  oxide
   500 nm                    500 nm
```

**Separation of variables.** A math trick for equations in several variables. You guess that the answer is a product of pieces, each depending on only one variable, e.g. $f(z,y) = g(z)\cdot h(y)$. Then the hard 2D problem splits into two easy 1D problems. It is exact only when the problem really has that structure; otherwise it is an approximation.

**Decibels (dB).** A log scale for ratios of power. A power ratio $P_{out}/P_{in}$ in dB is

$$\text{loss (dB)} = -10\log_{10}\left(\frac{P_{out}}{P_{in}}\right)$$

Rules of thumb: 3 dB loss means half the power is lost. 10 dB means only 10% remains. 0.1 dB means about 2.3% lost. 0.01 dB means about 0.23% lost. Losses in dB simply add up along a path. "dB/cm" is the loss per centimetre of waveguide. For field plots "in dB", the plot shows $10\log_{10}$ of the intensity relative to the peak, so 0 dB is the peak and −30 dB is one-thousandth of it. Log plots let you see faint tails that are invisible on a linear plot.

**Simulation tools named in this packet.**

- **FDTD** (finite-difference time-domain): chop space into a fine 3D grid of little cells and step Maxwell's equations (the laws of light) forward in time. Very general and accurate, but slow, especially in 3D. **Mesh accuracy** is a setting (Lumerical uses levels like 3 or 4) for how fine the grid is; higher means finer, more accurate, slower.
- **2.5D FDTD**: run a cheaper 2D FDTD, but use effective indices (from the Effective Index Method) so the 2D model mimics the real 3D chip.
- **Eigenmode solver** (mode solver): a program that finds the allowed modes of a waveguide cross-section and their effective indices. It does not simulate light moving; it just finds the stable patterns.
- **Finite element method (FEM)**: another accurate numerical way to solve for modes in 2D; the book uses it as the "exact" reference.
- **Fully vectorial**: a solution that keeps all three directions of the field and how they couple, rather than simplifying.

**Resonators and FSR.** A **ring resonator** is a waveguide bent into a loop (a **racetrack** is a loop with straight sections). Light of certain wavelengths fits a whole number of times around the loop and builds up. Those wavelengths are spaced apart by the **free spectral range (FSR)**, which depends on the group index: $\text{FSR} \approx \lambda^2/(n_g L)$, where $L$ is the loop length. So an error in $n_g$ gives the same percent error in FSR.

**Mode overlap.** If light in mode A enters a section of waveguide whose mode is B, how much power goes into B? You measure how similar the two field shapes are by multiplying them and integrating over the cross-section (the **overlap integral**). Identical shapes: 100% coupling. Different shapes: some power is lost or goes into other modes.

**Grating coupler.** A patterned structure on the chip that couples light between an optical fibre (above the chip) and the waveguide. It is how light gets on and off the chip for testing.

**Foundry.** A factory that makes chips for many customers. IME (Singapore), imec (Belgium) and IBM are named here; **OpSIS** was a service that gave researchers access to the IME foundry.

> **Key takeaways:**
>
> - Light is guided in high-index silicon; the stable field patterns are called modes.
> - A mode's effective index $n_{eff}$ is the "average" index it feels; group index $n_g$ sets pulse speed and resonator spacing.
> - dB is a log scale for losses: 3 dB is half the power, small dB values add up.
> - FDTD is accurate but slow; mode solvers find stable patterns quickly.

## 3.2.5 Effective Index Method

> **In one sentence:** The Effective Index Method finds the mode of a 2D waveguide cross-section by solving two quick 1D slab problems in a row, giving a fast and usually decent approximation.

### Why use it

A real waveguide is a rectangle. Its cross-section is 2D (width and height), so finding its mode is a 2D problem. A fully vectorial 2D solver (Section 3.2.7 of the book) is more accurate. But the **Effective Index Method (EIM)** has three big advantages:

- It gives insight: you see *why* the waveguide behaves as it does.
- It is very fast and easy to code.
- Its output can feed other tools. The book later uses it to design modulators (Section 6.2.2) and to make 2.5D FDTD simulations (Section 2.2.3).

### How it works: two 1D steps

Think of the rectangle of silicon. Instead of solving it all at once:

**Step 1 (vertical cut).** Pretend the waveguide is infinitely wide. Then it is just a flat slab: air on top, 220 nm of silicon, oxide below. Solve this 1D problem (in the vertical direction $z$) for its mode. You get a slab effective index. For the TE slab mode the book finds $n_{eff} = 2.845$ (from Listing 3.6, earlier in the book). This number is between oxide (1.45) and silicon (3.5), and fairly close to silicon, so the light is well held in the 220 nm layer.

**Step 2 (horizontal cut).** Now look sideways. Inside the 500 nm width, the light "sees" a material of index 2.845 (the slab's effective index from step 1). Outside the width there is no silicon, so it sees the cladding index. This is again a 1D slab problem, now in the horizontal direction $y$. Solve it. The effective index of this mode is the answer for the whole 2D waveguide.

```
 Step 1: vertical slab          Step 2: horizontal slab
   air     n=1.0                  |        |
   Si      n=3.5   -> n=2.845     | 2.845  |  cladding
   oxide   n=1.45                 |<-500nm>|
```

The book does this in Listing 3.10 (a Lumerical script). In plain steps the script:

1. Takes the slab TE effective index (2.845) as input.
2. Builds a 1D horizontal structure: a 500 nm-wide "core" of index 2.845 with cladding on both sides.
3. Solves for the mode of that structure.
4. Outputs the effective index and the 1D field profile.

**Result:** the strip waveguide's TE-like mode has $n_{eff} = 2.489$. It is lower than 2.845 because now the light is also squeezed sideways and more of it leaks into the low-index sides.

### Why the polarization switches between the steps

This is a subtle point. For the **TE-like** mode, the main electric field points sideways (horizontal, in the chip plane).

- In step 1 (vertical cut), sideways $E$ is parallel to the silicon/oxide interfaces. That is a **TE** slab mode.
- In step 2 (horizontal cut), the interfaces are now the left and right walls. Sideways $E$ points *across* those walls, i.e. perpendicular to them. Relative to this new cut, that is a **TM** mode.

So for a TE-like mode you do: TE in step 1, then TM in step 2. The field direction did not change; only the frame of reference (which walls you are looking at) did. For **TM-like** modes you do the reverse: TM first, then TE.

### Building the 2D picture

Each step gives a 1D field shape: $E(z)$ from step 1 (the book's Figure 3.6a) and $E(y)$ from step 2 (Figure 3.11a). The method assumes the 2D field is just their product:

$$E(z,y) = E(z)\cdot E(y)$$

- $E(z,y)$: the electric field at height $z$ and sideways position $y$.
- $E(z)$: the vertical shape, from the slab solution.
- $E(y)$: the horizontal shape, from the second step.

What it says: the vertical shape is the same at every sideways position, just scaled up or down. That is the "separation of variables" guess. It is only approximately true: near the corners of the rectangle the real field does not split this neatly. That is where the method makes its errors.

**Figure 3.11 — The fundamental TE mode found with the EIM ($n_{eff} = 2.489$).** Two panels show the horizontal field $E(y)$ across the waveguide, from −1 to +1 µm.

- (a) Linear scale. The field peaks at 1.0 at the centre ($y = 0$). Moving out, it dips to about 0.35 near $y \approx \pm 0.15$ µm, then rises to side peaks of about 0.63 near $y \approx \pm 0.25$ µm, which is right at the waveguide walls (the core is 500 nm wide, so its edges are at ±0.25 µm). Beyond the walls it fades to almost zero by about ±0.6 µm.
- (b) The same curve in dB. The peak is 0 dB, the side peaks are about −3 to −4 dB, the dips about −9 to −10 dB, and the field falls to −50 dB by ±1 µm.

Lesson: the light is mostly within the 500 nm core, with a short evanescent tail outside. The bumps at the walls come from step 2 being a TM problem: the field component pointing across a wall must jump in size at the wall (it is larger on the low-index side), so the profile gets a spike at each edge. The log plot lets you see how fast the tail decays, which matters for how close you can put other things to the waveguide.

**Figure 3.12 — EIM 2D field vs. the "exact" 2D calculation, for the strip waveguide.**

- (a) The 2D field built by multiplying $E(z)\cdot E(y)$. It is a colour map with a bright (red, above 0.8) centre at about $y = 0$, $z \approx 0.12$ µm, i.e. the middle of the silicon, fading outward through yellow, green and blue (below 0.1). The spot is a bit taller than you might guess and has small sideways "ears" at around $z \approx 0.15$–$0.25$ µm, $y \approx \pm 0.25$ µm (the wall bumps from Figure 3.11).
- (b) The difference between the EIM field and the fully vectorial finite-element field (Section 3.2.7). The colour scale runs from −0.05 to +0.15. The centre is close to zero error. The errors are in four lobes near the corners of the waveguide (around $y \approx \pm 0.25$ µm, $z \approx \pm 0.2$ µm), where the EIM overestimates the field by up to about 0.15, with small negative patches next to them.

Lesson: the EIM gets the core of the mode right and goes wrong at the corners, exactly where the "separable" guess is weakest.

**How big is the error in numbers?** For this strip waveguide:

- error in effective index: $\Delta n_{eff} \sim 1.2\%$
- error in group index: $\Delta n_g \sim 2.7\%$

Both are small. For example, 1.2% of 2.489 is about 0.03.

### Why that is good enough

You can pair the EIM with 2D FDTD (the 2.5D FDTD approach) and expect only a few percent error in the group index. Since the FSR of a ring resonator is inversely proportional to $n_g$, that gives a few percent error in FSR. In return the simulation is dramatically faster than full 3D FDTD. When you must run many simulations to optimize a design, that trade is often worth it.

> **Key takeaways:**
>
> - The EIM solves a 2D waveguide as two 1D slab problems: first vertical, then horizontal using the slab's effective index as the core index.
> - For TE-like modes: TE slab first, then TM; for TM-like modes the reverse.
> - Example: slab $n_{eff} = 2.845$ leads to strip waveguide $n_{eff} = 2.489$.
> - It assumes $E(z,y) = E(z)\cdot E(y)$; errors show up at the corners, about 1.2% in $n_{eff}$ and 2.7% in $n_g$.
> - Fast and good enough for many design loops, e.g. 2.5D FDTD of resonators.

## 3.2.6 Effective Index Method – analytic

> **In one sentence:** The same two-step method can be done with exact pen-and-paper (analytic) 1D slab solutions in MATLAB, here applied to a rib waveguide.

Earlier in the book (MATLAB code 3.3) a 1D slab can be solved analytically: there is a formula-based solution, no numerical grid needed. MATLAB code 3.11 uses that analytic slab solver twice, following the EIM, to build the 2D field of a **rib waveguide**. The book later uses this to model **pn-junction modulators** (Section 6.2.2), devices that change the light by moving electrical charges in a rib waveguide.

What the code does, step by step:

1. Defines the stack: air, silicon, oxide (a silicon-on-insulator, or **SOI**, wafer).
2. Step 1, vertical: solves the slab mode for the 220 nm-thick region (the rib) and finds its effective index. Repeats for the 90 nm-thick region (the slab on each side). The thinner region holds light less well, so it gets a lower effective index.
3. Step 2, horizontal: builds a 1D sideways profile whose "index" is the rib's effective index in the middle and the thin slab's effective index on each side. Solves it for the TE-like modes.
4. Multiplies the vertical and horizontal fields to get the 2D field profile.

Inputs: thicknesses, width, material indices, wavelength. Outputs: effective indices, 1D profiles, and the 2D field.

Note the difference from the strip: in a rib, the sides are not air or oxide but a thinner silicon slab. So the sideways index contrast is much smaller. The light is held less tightly sideways.

**Figure 3.13 — Analytic EIM for a rib waveguide, in three panels.**

- Top right, "Material Index": a vertical cut. The dashed step line is the material index: about 1.0 (air) above, about 3.5 (silicon) in the 220 nm layer (from about $z = -0.1$ to $+0.1$ µm), about 1.45 (oxide) below. The solid curve is the vertical TE field $E(z)$ found in step 1. It is concentrated in the silicon layer. The same procedure is repeated for the 90 nm slab regions.
- Bottom, horizontal cut. The green curve (right axis) is the slab effective index versus sideways position $y$: about 2.55 inside the 500 nm rib ($|y| < 0.25$ µm) and dropping to about 2.3 in the thin-slab regions outside. Dashed lines mark the rib edges. The blue curve (left axis) is the horizontal field of the TE-like mode, found as a TM problem in step 2. It peaks at the centre and fades away by about ±0.5 µm and beyond. The caption says two guided TE-like modes exist in this horizontal problem; the fundamental one is the one with a single central hump.
- Top left, "2D Field Profile": the product of the two, drawn as colour contours (red centre, fading to blue) on top of a white outline of the rib (about 500 nm wide, about 220 nm tall) and lines marking the slab layer.

Lesson: the figure is a visual recipe for the EIM. Vertical solve gives effective indices; those become a sideways index profile; the sideways solve gives the final mode. Because the step from 2.55 to 2.3 is small, the mode spreads further sideways than in a strip waveguide.

> **Key takeaways:**
>
> - The EIM can use exact analytic slab solutions instead of numerical ones.
> - In a rib waveguide, the 220 nm rib and the 90 nm side slab each get their own effective index (about 2.55 and 2.3 here).
> - The small sideways index step means weaker sideways confinement than a strip.
> - This model is the basis for pn-junction modulator design later in the book.

## 3.3 Bent waveguides

> **In one sentence:** Bending a waveguide loses some light, mostly because the bent mode has a different shape from the straight one, and the loss drops fast as the bend radius grows.

### Why bends matter

On a chip you must turn corners to route light from one device to another. Ring and racetrack resonators are bends by design. Every bend costs some light, so we need to know how much. The section does three things:

1. Simulates bend loss with 3D FDTD.
2. Uses an eigenmode solver to split the loss into its causes (radiation vs. mode mismatch).
3. Compares with measurements from real chips.

The **bend radius** $R$ is the radius of the curve, measured to the *centre* of the waveguide. Smaller $R$ means a tighter turn.

### Three ways a bend loses light

**(1) Scattering loss and substrate leakage.** **Scattering loss** comes from rough sidewalls that knock light out of the waveguide. **Substrate leakage** is light tunnelling down through the oxide into the silicon wafer underneath. Both grow with length. A bend is short, so these are small for bends with radii below about 10 µm.

**(2) Radiation loss.** On a curve, the part of the mode on the outer side would have to travel faster to keep up with the inner part (it has a longer path). Far enough out, it would need to go faster than light can in the cladding, so it cannot keep up and flies off as radiation. Think of the outer skater on a spinning line of skaters who cannot hold on. In tightly confined waveguides (TE modes in strip waveguides) this is small. It does matter in rib waveguides for $R < 5$ µm (the light is held less tightly sideways) and for TM-polarized modes.

**(3) Mode mismatch loss.** The biggest loss. A mode in a bend has a different shape from a mode in a straight guide (it shifts outward, see Figure 3.27). Where a straight piece suddenly joins a bend of fixed radius, the incoming shape does not match the shape the bend wants. The part that does not overlap is scattered away or goes into higher-order modes. This happens at both the start and the end of the bend.

Ways to reduce mode mismatch:

- (a) **Lateral offset:** shift the straight waveguide sideways a little relative to the bend, so that its mode lines up better with the shifted bent mode.
- (b) **Gradually changing curvature:** instead of jumping from straight (curvature 0) to curved, change the curvature smoothly. The book's example: a 90° bend with an effective radius of 20 µm in which the curvature rises from 0 to $1/15\ \mu\text{m}^{-1}$ (i.e. a tightest radius of 15 µm) and then back to 0. **Curvature** is just $1/R$: zero for a straight line, larger for tighter turns. A bonus: such a bend does not excite higher-order modes. (Book Figures 10.6–10.8 give more detail.)

```
  Abrupt bend:  straight ----+  (curvature jumps 0 -> 1/R)
                              \
  Smooth bend:  straight ------~-.  (curvature ramps 0 -> max -> 0)
                                  \
```

### Reported numbers from other labs

All for 500 × 220 nm strip waveguides, per 90° bend:

| Lab | Radius | Loss per 90° bend |
|---|---|---|
| IBM | 1 µm | ≈ 0.09 dB |
| IBM | 2 µm | ≈ 0.02 dB |
| imec (Belgium) | 1 µm | 0.1 dB |
| imec (Belgium) | 5 µm | 0.01 dB |

Read it as: each row is one measured bend size. Going from 1 µm to a few µm cuts the loss roughly tenfold. 0.1 dB is about 2% of the power, so even a 1 µm bend is quite good. imec concluded that at about $R = 10$ µm the bend loss drops to the same level as the ordinary loss of the straight waveguide. Beyond that, making the bend bigger does not help.

### The experiments in this book

The book's own data come from chips made at IME (Singapore) through the OpSIS foundry service.

- Test structures each contain two bends, with radii from 0.5 µm to 50 µm.
- Both strip and rib waveguides were tested.
- Light goes in and out through fibre grating couplers.
- Results: Figure 3.24 (strip), Figure 3.25 (rib).
- Measurement uncertainty is about 0.2 dB. So when the real bend loss is much smaller than 0.2 dB (large bends), the data cannot resolve it reliably.

> **Key takeaways:**
>
> - Bends lose light by scattering/substrate leakage (small), radiation (matters for rib and TM, small $R$), and mode mismatch (the biggest).
> - Mode mismatch can be reduced by offsetting the straight guide or by changing curvature smoothly.
> - For 500 × 220 nm strips, a 1 µm bend loses about 0.1 dB; at about 10 µm the bend loss equals the straight-guide loss.
> - Measurements have about 0.2 dB uncertainty, so very small losses cannot be seen.

## 3.3.1 3D FDTD bend simulations

> **In one sentence:** A full 3D FDTD simulation of a 90° bend, run for many radii, predicts bend loss that matches experiments well where the loss is large.

### What the scripts do

Listings 3.16 and 3.17 (Lumerical scripts) set up one bend simulation:

1. Draw the input straight waveguide, the bent section, and the output straight waveguide.
2. Define the simulation box and settings (mesh, time, boundaries).
3. Put an optical **mode source** in the input waveguide: it launches the fundamental mode.
4. Add **power monitors** to measure how much power arrives.
5. Add a **mode expansion monitor**: it measures how much power is in the fundamental mode only.
6. Optionally record a movie of the light moving.

Listing 3.18 runs this for many radii, with mesh accuracy 3 and 4, and computes the **transmission** = output power / input power, then plots loss vs. radius.

### Two ways to count "transmitted" light

**(1) Total transmission.** All power in the output waveguide, whatever mode it is in. This includes light in higher-order modes and light that is not properly guided. That light will be lost later, so this measure *underestimates* the real loss. Labeled "3D FDTD, Total" in the figures.

**(2) Fundamental mode transmission.** Only the power in the fundamental mode at the output. Reason: higher-order modes will leak away as they travel, or be blocked by mode-selective parts (grating couplers, directional couplers). It is computed by a mode overlap between the FDTD field and the waveguide's mode shape. Labeled "3D FDTD, Fundamental". This is the more honest number.

**Figure 3.24 — Bend loss vs. radius for 500 × 220 nm strip waveguides (simulation and OpSIS-IME experiment).**

- (a) Linear axes, radius 0–50 µm, loss 0–2.5 dB. The 3D FDTD curve starts at about 2.35 dB near $R \approx 0.5$ µm, falls to about 0.48 dB at $R = 1$ µm, and is near zero beyond 5 µm. Experimental points (crosses) cluster at small radii with values from about 0 to 1.4 dB (about 1.0–1.4 dB at 0.5 µm), and are near zero at large radii. A dashed line for 3 dB/cm propagation loss lies at essentially zero on this scale.
- (b) Log axes (radius about 0.3 to 50 µm; loss about 0.002 to 3 dB). Now you can see small numbers. The "Fundamental, Mesh 4" curve falls steadily from about 2 dB at small $R$ to a minimum of about 0.0015 dB around 15–20 µm, then turns slightly up. "Total, Mesh 4" is lower still (down to about 0.0002 dB), as expected since it counts all light. "Fundamental, Mesh 3" (coarser grid) departs from Mesh 4 above about 10 µm, giving higher values (about 0.003 dB at 25 µm). This shows the coarse mesh is not accurate enough for tiny losses. The dashed 3 dB/cm line slopes upward: a bigger bend is longer, so it picks up more ordinary propagation loss (about 0.001 dB at 3 µm, 0.01 dB at 30 µm). Experimental points are 0.8–2 dB below 2 µm, and scatter between 0.01 and 0.15 dB above 10 µm, generally above the simulation (that is the noise floor).

Lesson: strip bend loss falls very quickly with radius and is negligible past about 5–10 µm. Simulation matches experiment where losses are big; at large radii the experiment's noise hides the true value.

**Figure 3.25 — Bend loss vs. radius for 500 × 220 nm rib waveguides with a 90 nm slab.**

- (a) Linear axes, loss 0–12 dB. Rib losses are much higher at small radius: about 11.5 dB at 0.5 µm (FDTD) falling to near 0 by 10 µm. Experiment follows the FDTD curve closely.
- (b) Log axes. Fundamental-mode curves for mesh 3 and 4 almost coincide (here the coarse mesh is good enough). Total is a little below Fundamental for $R > 2$ µm. The 2 dB/cm propagation line slopes up. Experimental points scatter for $R > 5$ µm, with a few outliers above the simulations.

Approximate readings:

| Radius | FDTD loss | Experiment |
|---|---|---|
| 0.5 µm | ≈ 11.5 dB | ≈ 9.5–10 dB |
| 1 µm | ≈ 8 dB | ≈ 6–7 dB |
| 2 µm | ≈ 3 dB | ≈ 2–3 dB |
| 5 µm | ≈ 0.2 dB | ≈ 0.2 dB |
| 10 µm | ≈ 0.05 dB | ≈ 0.05 dB |
| 30 µm | ≈ 0.02 dB | — |

Read it as: rib bends need much larger radii than strip bends for the same loss. 8 dB at 1 µm means only about 16% of the light survives; a strip at 1 µm keeps about 90%. The reason: the rib holds light weakly sideways, so it radiates in tight bends.

### Comparing with experiment, and finding the best radius

**Strip waveguides (Figure 3.24).** Excellent agreement for small radii (0.5–1 µm), where losses are large. For larger radii the experimental uncertainty is bigger than the predicted loss. A line for 3 dB/cm straight-guide scattering loss is added. Bend loss falls with radius; propagation loss rises with radius (longer path). Where the two cross is the sweet spot: the simulations predict the lowest total loss for a conventional 90° strip bend at about **$R = 10$ µm**.

**Rib waveguides (Figure 3.25).** Good agreement up to about 4 µm. Beyond that, experimental uncertainty again dominates. Using a 2 dB/cm propagation-loss line, the best conventional 90° rib bend is at about **$R = 25$ µm**.

**A caveat.** The dB/cm values used are for *straight* waveguides. Bent waveguides are known to have higher propagation loss (the mode is pushed against the outer, rough sidewall). If the true propagation loss in the bend is higher, the rising line moves up and crosses the falling curve earlier. So the real best radius is probably smaller than 10 µm and 25 µm.

### Seeing where the light escapes

To see where energy is lost, you can make a movie, or record the **time-integrated field intensity** at every point:

$$|E|^{2} = |E_{x}|^{2} + |E_{y}|^{2} + |E_{z}|^{2} \qquad (3.10)$$

- $E_x, E_y, E_z$: the three components of the electric field (along $x$, $y$, $z$).
- $|E|^2$: the total intensity, the sum of the squares of the parts. It is just Pythagoras: the squared length of the field arrow.
- "Time-integrated" means this is added up over the whole simulation time, so you see where light has been on average, not a single snapshot.

Listing 3.19 adds a power monitor across the waveguide to record this. The result for a 1 µm strip bend is Figure 3.26 (described in the next section).

> **Key takeaways:**
>
> - 3D FDTD sweeps of bend radius give loss curves; "Fundamental" (power in the main mode) is the honest loss, "Total" underestimates it.
> - Strip bends: about 2.35 dB at 0.5 µm, 0.48 dB at 1 µm, negligible beyond about 5 µm. Rib bends are far lossier: about 8 dB at 1 µm, 0.2 dB at 5 µm.
> - Simulation agrees with experiment where losses are large; experimental noise (about 0.2 dB) hides small losses.
> - Best conventional 90° bend radius: about 10 µm (strip) and 25 µm (rib), probably smaller in reality since bent guides have higher propagation loss.
> - A finer mesh (4) is needed to trust very small loss values for strips.

## 3.3.2 Eigenmode bend simulations

> **In one sentence:** A mode solver shows that the bent mode is shifted outward compared to the straight mode, and the overlap between them explains most of the bend loss.

### The idea

Another tool is the **waveguide mode eigensolver** (Section 2.1 of the book). It can find the mode of a *bent* waveguide cross-section, not just a straight one. Comparing straight and bent modes lets us separate the two main losses: mode mismatch (shape difference) and radiation (light leaking out of the bend itself).

**Figure 3.26 — Time-integrated field in a 90° bend of radius 1 µm (FDTD, mesh accuracy 3).** A top-down colour map (log scale) of a strip waveguide. Light enters along a straight section from the left (centred at $y = 0$, about 0.5 µm wide), curves upward through a quarter circle, and exits upward along a straight section near $x \approx 1$ µm. Bright colours trace the waveguide; the field shows two bright stripes along the guide with a dimmer region between. A faint glow (evanescent field) surrounds the core out to about 0.2–0.3 µm. At the outer corner of the bend (around $x = 1.5$, $y = 1.5$ µm) there is a visible bulge or ripple of field leaving the guide.

Lesson: in a tight 1 µm bend you can literally see light escaping at the outer side of the curve.

**Figure 3.27 — Mode of a straight 500 × 220 nm strip (left) vs. the same strip bent at $R = 2$ µm (right).** Four cross-section colour maps (sideways $y$ vs. height $z$):

- (a) Straight, linear scale: a symmetric bright spot centred at $y = 0$, $z \approx 0.11$ µm (the middle of the 220 nm silicon), confined to the 500 nm width.
- (b) Bent, linear scale: the spot is pushed toward the outer edge (positive $y$), centre at about $y \approx +0.05$ µm. The tail on the outer side is longer than on the inner side.
- (c), (d) The same in dB (from −40 to −5 dB). The log scale makes the lopsided tail of the bent mode very clear.

Lesson: bending pushes the mode outward. That shape change is exactly what causes mode mismatch loss.

```
  straight mode        bent mode (outer side ->)
     .-""-.                 .-""-.
    (  ##  )               (   ##  )~~
     '-..-'                 '-..-'
```

### What Script 3.20 does

1. **First part:** computes the mode of the straight waveguide and of bent waveguides of various radii (giving Figure 3.27).
2. **Second part:** computes **mode overlap integrals** between the straight mode and each bent mode. This tells how much power passes from the straight section into the bend's mode at the junction. (More detail in the book's reference [35].)
3. It also gives the bent mode's own loss as it travels around the curve (the radiation loss).
4. Bent modes with $R < 3$ µm are numerically hard to compute, so results are given only for $R \ge 3$ µm.

**Figure 3.28 — Mode-solver loss predictions vs. radius: (a) strip, (b) rib.** (No detailed rendering is in the source; this is from the text.) The plots break the bend loss into mode-mismatch and radiation parts:

- **Strip (a):** radiation loss is negligible. Essentially all the loss is mode mismatch. However, these predicted losses are *higher* than both the experiments and the FDTD results.
- **Rib (b):** mode mismatch still dominates, but radiation loss contributes significantly for $R < 4$ µm (consistent with weak sideways confinement). Agreement among FDTD, experiment, and mode calculations is better for rib than for strip.

### Summary of the section

Both 3D FDTD and the eigenmode solver are well suited to evaluating bend loss, and the simulations agree well with experiments. FDTD gives the full picture directly; the mode solver is quicker and tells you *why* (mismatch vs. radiation).

> **Key takeaways:**
>
> - A bent mode is pushed toward the outside of the curve; the straight-to-bent shape difference is mode mismatch.
> - Overlap integrals between straight and bent modes give the mismatch loss at each junction.
> - Strip bends: loss is almost all mode mismatch; radiation is negligible (mode solver overestimates the total somewhat).
> - Rib bends: mismatch dominates, but radiation matters for $R < 4$ µm.
> - Mode solvers struggle below $R = 3$ µm; FDTD handles any radius.

## Glossary

| Term | Plain meaning |
|---|---|
| 2.5D FDTD | A 2D FDTD simulation that uses effective indices to imitate a 3D chip; much faster than 3D. |
| Bend radius | Radius of a waveguide curve, measured to the centre of the waveguide. |
| Cladding | The lower-index material (air, oxide) around the silicon core. |
| Core | The high-index part of a waveguide (silicon) where light is held. |
| Curvature | $1/R$; zero for straight, large for tight bends. |
| dB (decibel) | Log scale for power ratios; 3 dB = half, 10 dB = one tenth. |
| dB/cm | Loss per centimetre of waveguide length. |
| Directional coupler | Two waveguides side by side that swap light; mode-selective. |
| Effective index ($n_{eff}$) | The average index a mode feels; sets the speed of its wave crests. |
| Effective Index Method (EIM) | Approximating a 2D waveguide mode by two 1D slab solutions in sequence. |
| Eigenmode solver | Program that finds the allowed modes of a waveguide cross-section. |
| Electric field ($E$) | The wiggling electric part of light; intensity is the field squared. |
| Evanescent field | The part of a mode that leaks just outside the core and fades fast. |
| FDTD | Finite-difference time-domain: grid-based simulation of light in time. |
| Finite element method | Accurate numerical method used here as the "exact" 2D mode reference. |
| Foundry | A factory that makes chips for outside customers (IME, imec, IBM). |
| Free spectral range (FSR) | Wavelength spacing between resonances of a ring; $\propto 1/n_g$. |
| Fully vectorial | A solution keeping all field directions and their coupling. |
| Fundamental mode | The simplest mode, with one main hump of field. |
| Grating coupler | Patterned structure coupling light between a fibre and the chip. |
| Group index ($n_g$) | Sets the speed of a light pulse; $c/n_g$. |
| Higher-order mode | A mode with more humps/nodes than the fundamental. |
| Mesh accuracy | Simulation setting for how fine the grid is (3 coarser, 4 finer). |
| Mode | A stable field pattern that travels along a waveguide without changing shape. |
| Mode expansion monitor | FDTD tool that measures power in a specific mode. |
| Mode mismatch loss | Loss from the shape difference between straight and bent modes at a junction. |
| Mode overlap integral | Measure of how similar two field shapes are; gives coupled power. |
| Mode source | Simulation source that launches a chosen waveguide mode. |
| OpSIS | Service that gave researchers access to the IME foundry. |
| pn-junction modulator | Device that changes light by moving charges in a doped rib waveguide. |
| Polarization | The direction the electric field points. |
| Propagation loss | Ordinary loss of a straight waveguide per length (e.g. 2–3 dB/cm). |
| Radiation loss | Light flying out of a bend because the outer part cannot keep up. |
| Refractive index ($n$) | How much a material slows light; air 1.0, oxide 1.45, silicon 3.5. |
| Resonator (ring, racetrack) | A looped waveguide where certain wavelengths build up. |
| Rib waveguide | A silicon ridge on a thin silicon slab (here 220 nm on 90 nm). |
| Scattering loss | Light knocked out of the guide by rough sidewalls. |
| Separation of variables | Writing a multi-variable function as a product of one-variable pieces. |
| Slab waveguide | An infinitely wide flat layer; confines light only vertically. |
| SOI (silicon-on-insulator) | Wafer of silicon on top of oxide on top of a silicon substrate. |
| Strip waveguide | A plain rectangle of silicon (here 500 × 220 nm). |
| Substrate leakage | Light tunnelling through the oxide into the wafer below. |
| TE / TE-like | Mode whose electric field points mainly sideways (in the chip plane). |
| TM / TM-like | Mode whose electric field points mainly up/down. |
| Time-integrated intensity | Field strength squared, added up over the whole simulation time. |
| Total transmission | All output power, including unguided and higher-order light. |
| Transmission | Output power divided by input power. |
| Waveguide | A "wire" for light, made of a high-index core in low-index cladding. |

## Check yourself

1. In the EIM for a TE-like mode, which polarization do you use in each of the two steps, and why does it switch?

   *Answer:* TE in the vertical slab step, then TM in the horizontal step. The field still points sideways, but in step 2 the interfaces are the side walls, so the field is perpendicular to them, which is TM for that cut.

2. The slab effective index is 2.845 and the strip result is 2.489. Why is the second number lower?

   *Answer:* In step 2 the light is also squeezed sideways, so more of it sits in the low-index cladding, lowering the average index it feels.

3. What is the key assumption of the EIM, and where does it fail most?

   *Answer:* That the field is separable, $E(z,y) = E(z)\cdot E(y)$. It fails most at the corners of the waveguide.

4. The EIM has a 2.7% error in group index. What does that mean for a ring resonator simulated with 2.5D FDTD?

   *Answer:* The FSR scales as $1/n_g$, so it will be off by a few percent, in exchange for much faster simulation.

5. Name the three bend-loss mechanisms and say which is usually biggest.

   *Answer:* Scattering/substrate leakage, radiation, and mode mismatch. Mode mismatch is usually biggest.

6. Give two ways to reduce mode mismatch loss.

   *Answer:* Offset the straight waveguide sideways relative to the bend; or change the curvature gradually instead of abruptly.

7. Why does "Total transmission" underestimate loss?

   *Answer:* It counts light in higher-order and unguided modes that will be lost later or filtered by mode-selective components.

8. Why is there an optimum bend radius (about 10 µm strip, 25 µm rib)?

   *Answer:* Bend loss falls with radius but propagation loss rises with path length; the best radius is where they meet. Because bent guides have higher propagation loss than assumed, the true optimum is likely smaller.

9. Why are rib bends much lossier than strip bends at small radius?

   *Answer:* The rib's sideways index contrast is small (about 2.55 vs 2.3), so light is weakly held sideways and radiates in tight bends.

10. What does Figure 3.27 show about a bent mode, and why does it cause loss?

    *Answer:* The mode shifts toward the outer edge of the bend and gets a longer outer tail. Its shape no longer matches the straight mode, so power is lost at each straight-to-bend junction.
