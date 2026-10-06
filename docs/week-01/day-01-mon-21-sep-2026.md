# Week 1 · Day 1 — Monday 21 Sep 2026

*Simple-English study version of Chrostowski & Hochberg, Silicon Photonics Design: From Devices to Systems, §3.2.1–3.2.4*

[:material-file-pdf-box: Download this day as PDF](day-01-mon-21-sep-2026.pdf){ .md-button }

---

## Before you start: the big picture

A photonic chip moves information with light instead of with electric current. To do that, it needs "wires for light". These are called **waveguides**. A waveguide is a thin line of silicon, a few hundred nanometres across, that traps light and carries it from one place on the chip to another. Almost every other device on the chip (splitters, filters, modulators, detectors) is built from waveguides. So the first job of a photonic designer is to choose the size of the waveguide.

Think of a garden hose. If the hose is very narrow, water barely flows. If it is very wide, the water sloshes around in messy ways. You want a size that carries the flow cleanly. A waveguide is similar. If it is too thin, light leaks out. If it is too thick, light can travel in several different "patterns" at once, and those patterns get mixed up and spoil the signal. Designers usually want the waveguide to carry exactly one clean pattern for each polarization.

These four sections show how to find that size. First you look at a very simple version of the problem: an infinitely wide, flat sheet of silicon (a "slab"), where only the thickness matters. You solve it with a formula (the analytic method) and with a computer solver (the numerical method). Along the way the book teaches an important habit: how to check that a computer simulation is giving you a trustworthy answer (convergence tests). Finally, a sweep over thickness explains why the whole industry uses silicon that is 220 nm thick.

## Background you need

### Light is a wave

Light is a wave of electric and magnetic fields. The **electric field** ($E$) is a push that a charge would feel at a point in space. In a light wave this push wiggles back and forth very fast. The magnetic field ($H$) wiggles along with it, at right angles. For most of this packet we only care about the electric field.

The **wavelength** ($\lambda$, "lambda") is the distance from one wave crest to the next. Photonic chips for telecoms usually use **1550 nm** (1.55 µm) or **1310 nm** (1.31 µm). These are infrared, invisible to the eye. They are used because glass optical fibre loses very little light at these wavelengths, and because silicon is transparent there (it does not absorb them).

A useful number is the **free-space wavenumber**:

$$k_0 = \frac{2\pi}{\lambda}$$

It says how fast the wave's phase turns (in radians) per unit distance in vacuum. For $\lambda = 1.55\ \mu\text{m}$, $k_0 \approx 4.05$ radians per µm.

### Refractive index

Light travels slower inside a material than in vacuum. The **refractive index** $n$ says how much slower: speed in material $= c/n$, where $c$ is the speed of light in vacuum. Numbers used here (at 1550 nm):

| Material | Refractive index $n$ |
|---|---|
| Silicon (Si) | 3.473 |
| Silicon dioxide (SiO$_2$, "oxide", glass) | 1.444 |
| Air | 1.0 |

Silicon has a very high index. Oxide has a low index. This big difference ("high index contrast") is what makes silicon photonics special: it traps light very tightly, so devices can be tiny.

The index also changes a bit with wavelength. This is called **material dispersion**. If you only solve at one wavelength you can use one fixed index. If you sweep wavelength, you must let the index change too.

### Total internal reflection: how light gets trapped

When light inside a high-index material hits a boundary with a low-index material at a shallow (grazing) angle, it cannot escape. It reflects back completely. This is **total internal reflection**. A sheet of silicon surrounded by oxide works like a hall of mirrors: light bounces between the top and bottom surfaces and travels along the sheet.

The high-index middle part is the **core**. The low-index material around it is the **cladding**.

### Silicon-on-insulator (SOI) wafers

The chips start as a **silicon-on-insulator (SOI)** wafer. From bottom to top: a thick silicon **substrate** (just mechanical support), a layer of oxide (the **buried oxide**, or BOX, typically 2–3 µm thick), and then a thin top layer of silicon. The top silicon is where waveguides are made. A **foundry** (the factory that makes chips) offers fixed thicknesses, very commonly **220 nm**. Waveguides are usually covered with more oxide on top (the "coating" or upper cladding), so the silicon is surrounded by oxide on both sides.

```
      oxide cladding  (n = 1.444)
  ============================   <- top surface
      silicon core 220 nm (n = 3.473)
  ============================
      buried oxide    (n = 1.444)
  ----------------------------
      silicon substrate (support only)
```

### Waveguide shapes: slab, strip, rib

- A **slab waveguide** is a flat silicon sheet that is infinitely wide. Only its thickness matters. This is a **1D** problem: things change only in the up-down direction.
- A **strip waveguide** (also called a channel or wire) is a narrow rectangle of silicon, for example 500 nm wide and 220 nm tall. Now both width and height matter: a **2D** cross-section problem.
- A **rib waveguide** (also called a ridge) is a wide, thin silicon slab with a thicker raised ridge in the middle. Only part of the silicon is etched away. For example a 220 nm rib on a 90 nm slab.

### Modes

When light is trapped in a waveguide, it cannot take any shape it likes. Only certain stable patterns survive. Each such pattern is a **mode**. A mode keeps its shape as it travels down the waveguide; only its phase moves forward.

Analogy: a guitar string can only vibrate in certain patterns (the fundamental note, the first overtone, and so on). A waveguide is similar in the cross-section direction. The simplest pattern, with one hump, is the **fundamental mode**. Patterns with more humps and zero crossings are **higher-order modes**.

A waveguide that supports only one mode (per polarization) is called **single-mode**. Designers want this. If several modes travel together, they move at different speeds and interfere, which scrambles the signal and makes devices behave unpredictably.

### Effective index

Each mode travels along the waveguide at its own speed. We describe this speed by its **effective index**, $n_{eff}$. It is like a refractive index for the whole mode: the mode moves at speed $c/n_{eff}$.

Part of the mode's light is in the silicon (index 3.473) and part is in the oxide (index 1.444). So $n_{eff}$ is somewhere in between. It is a sort of weighted average:

- If most of the light is inside the silicon, $n_{eff}$ is close to 3.47.
- If much of the light spills into the oxide, $n_{eff}$ is closer to 1.44.

The key rule: **a mode is guided only if $n_{eff}$ is larger than the cladding index**. If $n_{eff}$ drops below 1.444, the light is no longer trapped; it leaks away into the oxide. The thickness (or wavelength) where a mode stops being guided is called its **cutoff**.

### Polarization: TE and TM

The electric field points in some direction. That direction is the **polarization**. In a flat slab there are two basic cases:

- **TE (transverse electric)**: the electric field lies flat, parallel to the silicon surface (side to side).
- **TM (transverse magnetic)**: the magnetic field lies flat, and the electric field points mostly up-down, perpendicular to the silicon surface.

TE and TM modes behave differently. In thin silicon the TE mode is held more tightly and has a higher effective index.

### Evanescent tails and exponential decay

The mode does not stop sharply at the silicon edge. A little bit of the field leaks into the cladding and fades away. This fading part is the **evanescent tail**. It falls off **exponentially**: every extra step of distance multiplies the field by the same fraction. For example, if the field halves every 70 nm, then after 700 nm it is down by a factor of $2^{10} \approx 1000$.

How tightly a mode is **confined** (held) is about how fast this tail dies away. Fast decay = tight confinement.

### Field amplitude, intensity, and decibels

The **amplitude** is the size of the field, $E$. The **intensity** (power per area) goes as the square, $|E|^2$.

Because the tails cover many powers of ten, plots often use **decibels (dB)**, a logarithmic scale. For power or intensity:

$$\text{dB} = 10 \log_{10}\left(\frac{I}{I_{max}}\right)$$

So 0 dB is the peak, −10 dB is one tenth, −20 dB is one hundredth, −60 dB is one millionth ($10^{-6}$). On a dB scale an exponential decay looks like a straight line, which makes it easy to see.

### Eigenmode solvers

To find modes, you solve Maxwell's equations (the basic laws of electricity and magnetism) for fields that keep their shape as they travel. Mathematically this is an **eigenvalue problem**: you look for special shapes (the **eigenmodes**) and their matching numbers (the **eigenvalues**, which give the effective index). A program that does this is an **eigenmode solver**. Lumerical MODE Solutions, used in the book, is a commercial example.

### Numerical simulation: mesh and boundaries

A computer cannot handle a smooth, continuous space. It chops space into small cells, a grid called the **mesh**. The field is computed only at the grid points. Smaller cells give a more accurate answer but take longer to compute.

The computer also cannot simulate infinite space. It only simulates a box of a certain size, the **simulation span**. The edges of the box are the **simulation boundaries**. If the box is too small, the boundaries cut into the mode's tails and change the answer.

A **numerical artifact** is a wrong result caused by these computer shortcuts, not by real physics. A **convergence test** checks for artifacts: you change a numerical setting (box size or mesh size) and see whether the answer stops changing. When it stops changing, the answer has **converged**.

## 3.2.1 Waveguide design

> **In one sentence:** You design a waveguide in steps: first pick the silicon thickness with a simple 1D model, then pick the width with a 2D model, then check for extra losses.

Designing a waveguide follows a fixed recipe. You go from the simplest model to more complete ones.

**Step 1 — choose the thickness (1D).** Imagine the silicon layer of the wafer as an infinite flat sheet (a slab), with oxide above and below (the wafer cross-section the book calls Figure 3.1; that figure is not in this packet). Find which modes this slab supports. You can do this with a formula (**analytic method**, Section 3.2.2) or with a computer solver (**numerical method**, Sections 3.2.3–3.2.4). You choose the thickness to meet a goal. A common goal is: the slab supports only one TE mode and one TM mode.

In practice you rarely get free choice. The foundry offers fixed options. Typical examples:

- SOI wafers with a **220 nm** silicon layer, or
- silicon that has been partly **etched** (cut down) to **90 nm**, as used for the thin slab next to a rib waveguide.

**Step 2 — choose the width (2D).** A real waveguide is not infinitely wide. Once the thickness is fixed, you find a suitable width, again often so that only one TE and one TM mode are supported. Two tools for this:

- the **effective index method (EIM)**, Section 3.2.5: a clever shortcut that turns the 2D problem into two 1D problems;
- a **fully vectorial 2D** solver, Section 3.2.7: the full, exact calculation over the rectangle-shaped cross-section. "Vectorial" means it keeps track of all three directions of the electric field, not just one.

**Step 3 — check the extras.** Even a good cross-section can lose light in other ways:

- **Bend loss**: when the waveguide curves, some light flies off the outside of the bend, like a car taking a corner too fast.
- **Substrate leakage**: the evanescent tail reaches down through the buried oxide into the silicon substrate below. Silicon has a high index, so light that reaches it can leak away.

The simulations in Sections 3.2.2 to 3.2.10 focus on the main properties of the waveguide:

- the **effective index** (how fast the mode's phase travels),
- the **mode profile** (the shape of the field in the cross-section),
- the **group index** (Section 3.2.9; how fast a pulse of light, i.e. the information, travels; not covered in today's reading).

> **Key takeaways:**
>
> - Waveguide design goes 1D (thickness) → 2D (width) → extra checks (bends, substrate leakage).
> - A common target is a single TE and a single TM mode.
> - Thickness is usually fixed by the foundry (e.g. 220 nm SOI, or 90 nm etched slab).
> - The main outputs of the simulations are the effective index, the mode profile, and the group index.

## 3.2.2 1D slab waveguide – analytic method

> **In one sentence:** A short MATLAB program solves the slab-waveguide equations exactly and finds that a 220 nm silicon slab in oxide at 1550 nm has $n_{eff} = 2.845$ for TE and $2.051$ for TM.

For a slab, the math is simple enough to solve almost by hand. Inside the silicon the field is a wave (sine and cosine shapes). Outside, in the oxide, it is a decaying exponential (the evanescent tail). At the two surfaces, the field and its slope must join up smoothly according to Maxwell's rules. Only certain values of $n_{eff}$ allow this smooth joining. Those values are the modes. The joining condition gives one equation in one unknown ($n_{eff}$), which the computer solves by searching for its roots. This is the **analytic method**: it uses the exact equations, not a grid.

The book's MATLAB function (Listing 3.2, not reproduced here) is called like this:

```
[n_te, n_tm] = wg_1D_analytic (1.55e-6, 0.22e-6, 1.444, 3.473, 1.444)
```

What goes in, in order:

- `1.55e-6` — wavelength, 1.55 µm (1550 nm), in metres;
- `0.22e-6` — slab thickness, 0.22 µm (220 nm);
- `1.444` — index of the cladding below (buried oxide);
- `3.473` — index of the core (silicon);
- `1.444` — index of the cladding above (oxide coating).

What comes out: the effective index of the TE mode and of the TM mode.

**Results:** $n_{eff} = 2.845$ (TE) and $n_{eff} = 2.051$ (TM).

What these numbers mean:

- Both are between 1.444 (oxide) and 3.473 (silicon), as they must be for a guided mode.
- The TE value, 2.845, is fairly close to silicon's 3.473. So most of the TE light sits inside the silicon. It is tightly confined.
- The TM value, 2.051, is much lower. So a large part of the TM light spills out into the oxide. It is weakly confined.

Some cautions and extras:

- This solves at **one wavelength only**. To sweep wavelength, you must include **material dispersion** (the change of silicon's and oxide's index with wavelength). Otherwise the results will be wrong away from 1550 nm.
- The **mode profiles** (shapes) can also be computed, using MATLAB Script 3.3.
- The same slab calculation is reused later for designing **fibre grating couplers** (Section 5.2). These are structures that couple light between an optical fibre and the chip.

> **Key takeaways:**
>
> - The slab problem can be solved exactly (analytically) with a short program.
> - Inputs: wavelength, thickness, and the three refractive indices. Outputs: $n_{eff}$ for TE and TM.
> - For 220 nm Si in oxide at 1550 nm: TE $n_{eff} = 2.845$ (tightly confined), TM $n_{eff} = 2.051$ (looser).
> - For wavelength sweeps, include material dispersion.

## 3.2.3 Numerical modelling of waveguides

> **In one sentence:** For shapes too complex for formulas, you draw the waveguide in a simulator and let a numerical eigenmode solver find the modes; the slab case is a good test because we already know the answer.

Real waveguides (strips, ribs) have no simple exact formula. So we use a **numerical eigenmode solver**: a program that chops the cross-section into a mesh and solves for the modes on the computer.

The workflow in the book:

1. **Draw the geometry.** Listing 3.4 is a Lumerical MODE Solutions script that builds the wafer layers and the waveguides (the structures shown in the book's Figures 3.4 and 3.5).
2. **Assign materials.** The material models (refractive indices, including how they change with wavelength) come from Listing 3.1.
3. **Solve three ways**, from simple to complete:
   - as a 1D slab (only the thickness),
   - with the effective index method (an approximation for the 2D shape),
   - with the fully vectorial 2D solver (the full cross-section).

Comparing the three tells you how good the simple approximations are.

**Figure 3.5 — Electron-microscope pictures of real strip and rib waveguides.** These are **SEM** (scanning electron microscope) images. An SEM forms a picture with a beam of electrons instead of light, so it can see things far smaller than a light microscope can. Each sample has been cut (cleaved) to show the cross-section, and is viewed at a 52° tilt.

- **(a) Strip waveguide.** A single tall rectangle of silicon sitting on the oxide. The top corners are slightly rounded and the sidewalls are fairly smooth. The scale bar is 200 nm; the image is magnified 80,000 times and is 1.90 µm wide.
- **(b) Rib waveguide.** A wide thin silicon slab with a raised ridge in the middle. The ridge's sidewalls have deliberate, regular notches (**corrugations**). These form a **Bragg grating**: a periodic pattern that reflects one narrow band of wavelengths, like a mirror that works for only one colour (covered in Section 4.5). Scale bar 200 nm; magnified 120,000 times; image 1.27 µm wide.

```
 (a) strip                 (b) rib
      ____                      ____
     |    |                 ___|    |___
     | Si |                |  Si  rib   |  <- thin Si slab
 ____|____|____        ____|____________|____
     oxide                   oxide
```

*Lesson:* real waveguides are tiny (a few hundred nanometres), not perfect rectangles (corners round off), and come in two main shapes. The strip etches all the way through the silicon; the rib etches only part way.

**Figure 3.6 — Fundamental TE mode of the 220 nm slab.** This is the shape of the first mode found by the numerical eigenmode solver. Its effective index is **2.845**, the same value the analytic method gave. That agreement is a good sign the solver is set up correctly. The x-axis is height (position across the slab, from −1 µm to +1 µm, with 0 at the centre of the silicon). A grey band marks where the silicon is (220 nm thick, so roughly −0.11 to +0.11 µm).

- **(a) Linear scale.** The field is a single smooth hump, like a bell curve, peaking at 1.0 in the centre of the silicon. It falls to nearly zero by about ±0.5 µm. Most of the light is in or very near the silicon.
- **(b) Log scale, dB.** The same curve in decibels. The peak is 0 dB. Outside the silicon, the curve falls as a straight line, down to about −100 dB at the plot edges. A straight line on a log scale means an exponential decay: the evanescent tail.

*Lesson:* the TE mode is tightly held in the silicon, but it does have tails reaching into the oxide. The linear plot shows where the light mostly is; the log plot shows how quickly the tails vanish, which matters for choosing the simulation box size.

> **Key takeaways:**
>
> - Numerical eigenmode solvers handle shapes that formulas can't.
> - Workflow: draw the geometry, assign materials, solve as 1D slab, then EIM, then full 2D.
> - Real strip and rib waveguides (Figure 3.5) are a few hundred nm in size; ribs can carry gratings on their sidewalls.
> - The numerical TE slab mode has $n_{eff} = 2.845$, matching the analytic method.

## 3.2.4 1D slab – numerical

> **In one sentence:** A 1D numerical solver finds the two slab modes (TE and TM), shows that their tails decay at different rates, and is then tested for trustworthiness (box size, mesh) and swept over thickness to explain why 220 nm silicon is the standard.

### Setting up and running the solver

We now simulate the slab of the wafer (the structure of Figure 3.1) numerically. Two steps:

1. **Configure** a 1D eigenmode solver along a line through the waveguide cross-section (Script 3.5). This sets the line's position and length, the mesh, and the wavelength.
2. **Run** the calculation and plot the mode profiles (Listing 3.6). The solver returns a list of modes, sorted from highest to lowest effective index.

At 1550 nm this 220 nm slab supports **only two modes**: the TE mode (Figure 3.6, above) and the TM mode (Figure 3.7, below). No other pattern is guided.

**Figure 3.7 — The TM mode of the slab (2nd mode in the solver's list).** "2nd mode" here just means it is second in the solver's list, because its effective index is lower than the TE mode's. It is still the fundamental (simplest) TM mode. Its effective index is **2.054**, essentially the same as the analytic 2.051. The small difference (0.003) comes from the numerical shortcuts (mesh and box size), which the convergence tests below examine. Same axes and grey silicon band as Figure 3.6.

- **(a) Linear scale.** The curve looks odd at first: it has two peaks (value 1.0), one at each edge of the silicon, and a dip in the middle (around 0.2). Outside the silicon it decays, reaching near zero at ±1 µm.
- **(b) Log scale, dB.** Peaks at 0 dB at the silicon edges, a small dip of about −5 dB in the centre, and tails that fall only to about **−45 dB** at ±1 µm. Compare this with about −100 dB for TE in Figure 3.6.

Why the dip? For TM, the electric field points across the silicon surface (up-down). Maxwell's equations say that when a field crosses a boundary this way, the field jumps in size by the ratio of the squared indices. Here that ratio is $(3.473/1.444)^2 \approx 5.8$. So the field is about 5.8 times stronger just outside the silicon than just inside. That is why the field is low inside the silicon and peaks right at its edges.

*Lesson:* the TM mode puts much more of its light in the oxide and its tails reach much farther. That matches its lower effective index.

### Why log-scale plots matter

The log-scale plots let you check that the field has decayed to almost nothing before it reaches the edge of the simulation box. If the field is still large at the boundary, the boundary distorts the mode and the answer is wrong.

### How fast do the tails decay? Equation 3.3

The figures show that the two modes decay at different rates: **TE is more strongly confined**. The general rule is:

**Higher effective index → mode more tightly confined → tails decay faster.**

The decay of the field in the cladding is approximately:

$$E \propto e^{-\frac{2\pi d}{\lambda}\sqrt{n_{eff}^{2}-n_{c}^{2}}} \qquad (3.3)$$

What each symbol means:

- $E$ — the field amplitude in the cladding;
- $\propto$ — "is proportional to";
- $d$ — the distance from the core–cladding surface into the cladding;
- $\lambda$ — the wavelength in vacuum;
- $n_{eff}$ — the effective index of the mode;
- $n_c$ — the refractive index of the cladding (1.444 for oxide).

What it says: the field falls exponentially with distance $d$. The decay rate is

$$\gamma = \frac{2\pi}{\lambda}\sqrt{n_{eff}^{2}-n_{c}^{2}} = k_0\sqrt{n_{eff}^{2}-n_{c}^{2}}$$

so $E \propto e^{-\gamma d}$. The field shrinks by a factor of $e \approx 2.72$ every $1/\gamma$ of distance (the **decay length**).

Why this shape:

- The bigger the gap between $n_{eff}$ and $n_c$, the faster the decay. A mode whose $n_{eff}$ is far above the cladding is "deep inside" the guided regime and is held tightly.
- If $n_{eff}$ falls to $n_c$, the square root becomes zero, so there is no decay at all. The field spreads out forever: the mode is no longer guided. That is exactly the cutoff condition $n_{eff} > n_c$ from the background section.
- Shorter wavelength gives faster decay (because of the $1/\lambda$), for the same indices.

**Worked example** ($\lambda = 1.55\ \mu\text{m}$, so $k_0 = 2\pi/1.55 \approx 4.05\ \mu\text{m}^{-1}$; $n_c = 1.444$, $n_c^2 \approx 2.085$):

| Mode | $n_{eff}$ | $n_{eff}^2 - n_c^2$ | $\sqrt{\cdot}$ | $\gamma$ (per µm) | Decay length $1/\gamma$ |
|---|---|---|---|---|---|
| TE | 2.845 | $8.094 - 2.085 = 6.009$ | 2.451 | 9.9 | about 100 nm |
| TM | 2.051 | $4.207 - 2.085 = 2.122$ | 1.457 | 5.9 | about 170 nm |

Read across each row: the TM tail reaches about 1.7 times farther than the TE tail. Over long distances that adds up. After 500 nm of oxide, the TE field is down by $e^{-9.9 \times 0.5} \approx e^{-5} \approx 0.007$, but the TM field is only down by $e^{-5.9 \times 0.5} \approx e^{-3} \approx 0.05$. This is why the TM tails in Figure 3.7 look so much longer.

### Convergence tests

> **In one sentence:** Before trusting a simulation, change one numerical setting at a time (box size, mesh size) and confirm that the answer stops changing.

**Convergence tests** are critical in any numerical simulation. They make sure the result is real physics and not a **numerical artifact**. Here the book tests two things: whether the box edges disturb the mode, and whether the mesh is fine enough.

A key rule: **change only one parameter at a time.** For example, when you change the box size, the mesh points inside the waveguide should stay in exactly the same places. Otherwise you can't tell whether a change in the answer came from the box size or from the mesh moving.

#### Test 1: simulation box size (span)

Script 3.7 computes the effective index for many different **simulation spans** (the height of the simulation box along the z-axis, i.e. the up-down direction). It picks mode #1 for TE and mode #2 for TM.

**Figure 3.8 — Convergence with simulation box size.**

- **(a) Effective index vs. span (linear scale).** Two curves, starting from a span of about 250 nm.
  - TE (solid line): starts too low (about 2.7) when the box is tiny, rises fast, and levels off at about **2.85** by a span of about 750 nm.
  - TM (dashed line): starts too high (about 2.3), falls, and levels off at about **2.05** by about 1000 nm.
- **(b) Error vs. span (log scale).** The error $\Delta n$ is the difference from the result at a 2000 nm span (taken as the "true" answer). Both curves fall steadily. On this log axis they are roughly straight lines, which means the error falls **exponentially** with box size.
  - TE: about $10^{-1}$ at 400 nm, $10^{-4}$ at 1000 nm, $10^{-7}$ near 2000 nm.
  - TM: falls more slowly: about $10^{-1}$ at 400 nm, $10^{-2}$ at 1000 nm, $10^{-4}$ near 2000 nm.

What the book concludes:

- **TE:** for spans larger than **1300 nm**, the effective index changes by less than **0.0001**. The slab is 220 nm thick, so this leaves $(1300 - 220)/2 \approx 540$ nm, i.e. about **550 nm of oxide above and below** the silicon. That is enough for accurate TE simulations. This number will be reused to size the much more expensive 3D **FDTD** simulations later (FDTD = finite-difference time-domain, a method that simulates the full light wave moving step by step in time).
- **Rule of thumb from Figure 3.6:** comparing this span to the TE mode profile, the **intensity** should have decayed to about $10^{-6}$ of its peak (−60 dB) at the boundary, so that the boundary does not disturb the mode.
- **TM:** its tail is longer (as you can predict from its lower effective index and Equation 3.3). So it needs a bigger box: spans of about **2000 nm** for the same precision.
- The error drops exponentially with box size; an error of $\Delta n = 10^{-6}$ is reached at a span of **1600 nm**.

*Lesson:* the box must be big enough to contain the tails. Modes with lower $n_{eff}$ (like TM) have longer tails and need bigger boxes. Exponential convergence means a modest increase in box size buys a lot of accuracy.

#### Test 2: mesh size

Next the book tests the **mesh** (grid spacing). The box is made large (2 µm) so it does not matter, and only the TE mode is studied (Script 3.8).

There are two ways to handle a material boundary that falls between grid points:

- **Staircase mesh** (the conventional method): each grid cell is filled with just one material, either all silicon or all oxide. A smooth surface becomes a jagged staircase. If the silicon edge falls in the middle of a cell, the silicon effectively gets a bit thicker or thinner than it really is.
- **Conformal mesh** (an advanced method): cells cut by a boundary are treated specially, taking into account where exactly the boundary lies inside the cell. The surface position is represented accurately even with large cells.

```
 true edge:  |      staircase:  ___|        conformal: cell knows edge
             |                 |            is 37% of the way across
```

**Figure 3.9 — Convergence with mesh size (TE mode).**

- **(a) Effective index vs. mesh size (0–50 nm).**
  - Staircase (solid): about 2.85 for very small meshes, but it jumps around more and more as the mesh grows. Between 30 and 50 nm it swings wildly, from about 2.96 (near 45 nm) down to about 2.71 (near 47 nm).
  - Conformal (dashed): almost flat at about **2.845** across the whole range.
- **(b) Error vs. mesh size (log scale).**
  - Staircase: starts at about $3 \times 10^{-3}$ and grows to between $10^{-2}$ and $10^{-1}$ for meshes of 30–50 nm.
  - Conformal: starts at about $10^{-4}$, and even at 30–50 nm stays between $10^{-3}$ and $10^{-2}$. That is 10 to 100 times smaller error than staircase.

Why does the staircase curve wiggle? As the mesh size changes, the grid points move relative to the silicon edges. Sometimes an edge lands neatly on a grid point; sometimes it falls mid-cell and gets rounded the wrong way. So the "effective thickness" of the silicon jumps up and down, and so does $n_{eff}$.

What the book concludes:

- The staircase mesh needs about **1 nm** cells or smaller to be accurate. That is usually impractical: it makes simulations very slow.
- At a typical **10 nm** mesh, the staircase error is $\delta n_{eff} = 0.05$. That is large. (For comparison, the TE and TM indices differ by about 0.8, and many devices are sensitive to changes of 0.001.)
- Fixes for staircase meshes:
  - **Mesh overrides**: add extra grid points only where they matter (in and near the waveguide), keeping the grid coarse elsewhere.
  - Place a **grid point at every material interface**, so edges are never rounded the wrong way.
- The **conformal mesh** is much better: a **20 nm** conformal mesh is about as accurate as a **1 nm** staircase mesh.
  - 10 nm conformal mesh: error about $\Delta n = 10^{-4}$.
  - 20 nm conformal mesh: error about $\Delta n = 10^{-3}$.
  - 40–50 nm conformal mesh: error typically still below $\Delta n = 10^{-2}$.
- In Lumerical, the algorithm is chosen with the **"mesh refinement"** setting.

*Lesson:* the way the computer handles material edges matters as much as the grid size. Use a conformal mesh, or else refine the mesh and align grid points with the edges.

### Parameter sweep – slab thickness

> **In one sentence:** Sweeping the silicon thickness shows that, at 1550 nm, the slab carries just one TE and one TM mode for thicknesses below about 240 nm, which is why 220 nm became the standard.

Script 3.9 repeats the slab calculation for many silicon thicknesses. For each mode it returns:

- the **effective index**, and
- the **polarization fraction**: how much of the mode is TE versus TM. This is used to label each curve as TE or TM.

A note on polarization: in a **1D slab**, every mode is either **pure TE or pure TM**. In a **2D waveguide** (a strip or rib), pure TE or TM modes do not exist; each mode is a mixture, though usually mostly one or the other. People then say "TE-like" or "quasi-TE".

**Figure 3.10 — Effective index of slab modes vs. silicon thickness** (silicon in oxide; thickness 0 to 400 nm). Each panel has:

- a horizontal **dotted line** at about 1.44, the oxide index. Only modes **above** this line are guided;
- a vertical **solid line**, labelled "Single mode cutoff (TE, TM)", marking where a third mode starts to be guided.

**(a) At 1550 nm:**

| Mode | Behaviour as thickness grows | Value at 400 nm |
|---|---|---|
| TE fundamental | starts at about 1.44 at zero thickness, rises steadily | about 3.2 |
| TM fundamental | stays near 1.44 until about 100 nm, then rises | about 3.0 |
| TE first-order (2nd TE mode) | not guided until about 250 nm, then rises sharply | about 2.25 |
| TM first-order (2nd TM mode) | not guided until about 300 nm, then rises slightly | about 1.6 |

Single-mode cutoff line: about **240–245 nm**.

**(b) At 1310 nm:**

| Mode | Behaviour as thickness grows | Value at 400 nm |
|---|---|---|
| TE fundamental | starts near 1.45, rises steadily | about 3.3 |
| TM fundamental | flat until about 80 nm, then rises | about 3.15 |
| TE first-order | not guided until about 230 nm, then rises | about 2.55 |
| TM first-order | not guided until about 280 nm, then rises | about 1.95 |

Single-mode cutoff line: about **220 nm**.

How to read the tables: go down a row to see one mode's story. Each mode is born at a cutoff thickness (where it crosses above the dotted line), and then its effective index climbs toward silicon's 3.47 as the slab gets thicker and holds more of the light.

What to learn from Figure 3.10:

- **Thicker silicon → higher effective index** for every mode. More silicon means more light inside silicon.
- **TE is always above TM** for the same order. TE is held more tightly in a thin slab.
- **Thicker silicon → more modes.** Below the cutoff line there are exactly two guided modes (one TE, one TM). Above it, a third (the first-order TE) appears.
- **At 1550 nm the slab is single-mode (one TE + one TM) below about 240 nm.** This is why **220 nm** SOI is the common choice for 1550 nm: it is as thick as possible (for tight confinement) while staying safely single-mode.
- **At 1310 nm the cutoff is lower, about 220 nm.** Shorter wavelength "fits" more easily into the same thickness, so higher modes appear sooner. Effective indices are also a little higher at 1310 nm for the same thickness.
- These charts are design tools: use them to pick a thickness for a different wavelength or polarization.

> **Key takeaways:**
>
> - The 220 nm slab at 1550 nm supports exactly two modes: TE ($n_{eff} = 2.845$) and TM ($n_{eff} \approx 2.05$).
> - Higher $n_{eff}$ means tighter confinement and faster-decaying tails, as Equation 3.3 shows: decay rate $= \frac{2\pi}{\lambda}\sqrt{n_{eff}^2 - n_c^2}$.
> - Always run convergence tests, changing one setting at a time. TE needs about 550 nm of cladding on each side (1300 nm span); TM needs about 2000 nm span.
> - Staircase meshes give large errors (0.05 at 10 nm mesh); conformal meshes are 10–100 times better (about $10^{-4}$ at 10 nm).
> - At 1550 nm the slab is single-mode below about 240 nm, which is why 220 nm SOI is the standard; at 1310 nm the cutoff is about 220 nm.

## Glossary

| Term | Plain meaning |
|---|---|
| Amplitude | The size of the field at a point (not squared). |
| Analytic method | Solving the exact equations with formulas, not with a grid. |
| Bend loss | Light lost when a waveguide curves too sharply. |
| Bragg grating | A periodic pattern that reflects a narrow band of wavelengths. |
| Buried oxide (BOX) | The glass layer under the top silicon in an SOI wafer. |
| Cladding | Low-index material around the core (here, oxide). |
| Confinement | How tightly a mode is held inside the core. |
| Conformal mesh | A meshing method that accounts for exactly where an edge cuts a grid cell. |
| Convergence test | Changing a numerical setting to check the answer no longer changes. |
| Core | The high-index part of a waveguide that carries the light (here, silicon). |
| Corrugations | Regular notches cut into a waveguide wall. |
| Cutoff | The size or wavelength at which a mode stops being guided. |
| Decay length | Distance over which an exponentially decaying field falls by a factor $e$. |
| Decibel (dB) | Log scale: $10\log_{10}$ of a power ratio; −10 dB = 1/10, −60 dB = $10^{-6}$. |
| Effective index ($n_{eff}$) | A mode's own "refractive index"; it travels at speed $c/n_{eff}$. |
| Effective index method (EIM) | Shortcut that splits a 2D waveguide problem into two 1D slab problems. |
| Eigenmode / eigenvalue | A shape that keeps its form as it travels / the number (here $n_{eff}$) that goes with it. |
| Eigenmode solver | Program that finds a waveguide's modes. |
| Electric field ($E$) | The push a charge would feel; it oscillates in a light wave. |
| Evanescent tail | The part of the mode outside the core, fading exponentially. |
| FDTD | Finite-difference time-domain: a full 3D simulation of light stepping in time. |
| Foundry | Factory that makes chips with fixed process options. |
| Fully vectorial | A solver that keeps all field directions, with no simplifying approximation. |
| Fundamental mode | The simplest mode, with the highest effective index. |
| Grating coupler | A structure that couples light between an optical fibre and the chip. |
| Group index | Sets the speed of a light pulse (the information) in a waveguide. |
| Higher-order mode | A mode with more lobes and lower effective index. |
| Intensity | Power per area; proportional to the field amplitude squared. |
| Material dispersion | The change of a material's refractive index with wavelength. |
| Mesh | The grid of points a simulator uses to represent space. |
| Mesh override | Extra-fine mesh added only in a chosen region. |
| Mode | A stable field pattern that travels along a waveguide without changing shape. |
| Mode profile | The shape of a mode's field across the waveguide. |
| Numerical artifact | A wrong result caused by simulation shortcuts, not by physics. |
| Polarization | The direction in which the electric field points. |
| Polarization fraction | How much of a mode is TE versus TM. |
| Refractive index ($n$) | How much slower light goes in a material than in vacuum. |
| Rib waveguide | A partly etched waveguide: a ridge on top of a thin silicon slab. |
| SEM | Scanning electron microscope; images tiny structures with electrons. |
| Simulation span / boundary | Size of the simulation box / its edges. |
| Single-mode | Supports only one mode (per polarization). |
| Slab waveguide | An infinitely wide flat sheet of core material; only thickness matters. |
| SOI (silicon-on-insulator) | Wafer with a thin silicon layer on top of oxide on a silicon substrate. |
| Staircase mesh | Meshing where each cell is one material, so edges become jagged steps. |
| Strip waveguide | A fully etched rectangular silicon waveguide. |
| Substrate leakage | Light escaping through the buried oxide into the silicon substrate. |
| TE (transverse electric) | Mode whose electric field lies parallel to the slab surface. |
| TM (transverse magnetic) | Mode whose electric field points mostly perpendicular to the slab surface. |
| Total internal reflection | Complete reflection of light hitting a lower-index material at a grazing angle. |
| Wavelength ($\lambda$) | Distance between wave crests; here 1550 nm or 1310 nm. |
| Wavenumber ($k_0$) | $2\pi/\lambda$; phase change per unit length in vacuum. |

## Check yourself

1. Why must a guided mode have $n_{eff}$ larger than the cladding index?

   *Answer:* In Equation 3.3 the decay rate is proportional to $\sqrt{n_{eff}^2 - n_c^2}$. If $n_{eff} \le n_c$ there is no decay, so the field does not stay near the core and the light leaks away.

2. For a 220 nm silicon slab in oxide at 1550 nm, what are the TE and TM effective indices, and which mode is more tightly confined?

   *Answer:* TE 2.845, TM 2.051 (2.054 numerically). TE is more tightly confined because its $n_{eff}$ is higher, closer to silicon's 3.473.

3. Using Equation 3.3, roughly what is the decay length of the TE mode's tail?

   *Answer:* $\gamma = (2\pi/1.55)\sqrt{2.845^2 - 1.444^2} \approx 4.05 \times 2.45 \approx 9.9\ \mu\text{m}^{-1}$, so $1/\gamma \approx 100$ nm.

4. Why does the TM mode profile have a dip in the middle of the silicon?

   *Answer:* Its electric field points across the silicon surface, and that field component jumps by $(n_{Si}/n_{ox})^2 \approx 5.8$ at the boundary. So the field is stronger just outside the silicon than inside.

5. Why does the TM mode need a larger simulation box than the TE mode?

   *Answer:* Its lower effective index means a slower-decaying, longer tail. The box must hold the tail (down to about $10^{-6}$ in intensity), so TM needs about 2000 nm span versus about 1300 nm for TE.

6. What is the "change one parameter at a time" rule in convergence tests, and why does it matter?

   *Answer:* When sweeping, e.g., box size, keep the mesh points inside the waveguide in the same places. Otherwise you can't tell whether a change in the answer came from the box or from the mesh.

7. At a 10 nm mesh, how big is the error with a staircase mesh vs. a conformal mesh?

   *Answer:* Staircase: about 0.05. Conformal: about $10^{-4}$. Conformal is hundreds of times better here.

8. Name two ways to improve accuracy if you must use a staircase mesh.

   *Answer:* Use mesh overrides to refine the grid near the waveguide, and put a grid point exactly at every material interface.

9. Why is 220 nm the common SOI thickness for 1550 nm?

   *Answer:* Figure 3.10a shows the slab supports only one TE and one TM mode below about 240 nm. 220 nm is close to that limit, giving tight confinement while staying single-mode.

10. What happens to the single-mode cutoff thickness at 1310 nm, and why?

    *Answer:* It drops to about 220 nm. A shorter wavelength fits more easily into the silicon, so higher-order modes start being guided at smaller thicknesses.
