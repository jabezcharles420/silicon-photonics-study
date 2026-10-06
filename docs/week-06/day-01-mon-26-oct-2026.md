# Week 6 · Day 1 — Monday 26 Oct 2026

*Simple-English study version of Chrostowski & Hochberg §4.2 (Y-branch) and §5.3.1 (Nano-taper edge coupler). Study topic: tapers and adiabaticity.*

[:material-file-pdf-box: Download this day as PDF](day-01-mon-26-oct-2026.pdf){ .md-button }

## Before you start: the big picture

On a silicon photonic chip, light travels in tiny "wires" of glass-like silicon, called waveguides. Very often we need to **change the shape of the path the light is in**: make it split into two, merge two paths into one, or squeeze a huge beam from an optical fibre down into a wire 100 times smaller. Each of these is a *transition*. The big question for any transition is: does the light follow the new shape smoothly, or does it get "shaken up" and lose energy?

The answer is the idea of **adiabaticity**. A transition is **adiabatic** when the shape changes so slowly and gently that the light simply reshapes itself step by step and keeps all its energy in the same "pattern" (mode). Think of carrying a full cup of coffee: if you speed up and turn gently, the coffee stays in the cup; if you jerk, it spills. A **taper** is a waveguide whose width changes gradually along its length; it is the basic tool for making gentle, adiabatic transitions.

This packet shows two tapered devices. §4.2, the **Y-branch**, uses a carefully shaped, smoothly widening junction to split light 50/50 (and teaches a surprising fact about *combining* light). §5.3.1, the **nano-taper edge coupler**, uses a long, slowly narrowing silicon tip to let the light spread out until it matches the beam from a lens or fibre. In the second device you will see adiabaticity directly: a taper that is too short loses light; one that is long enough (about 100 µm) does not.

## Background you need

**Light as a wave.** Light is a wave of electric and magnetic fields wiggling in space and time. The **electric field** $E$ is the "height" of the wave at a point. It can be positive or negative. The **wavelength** $\lambda$ is the distance between two wave crests. This packet uses $\lambda = 1.55$ µm (1550 nm), the standard colour of infrared light for telecom. One µm (micrometre) is one millionth of a metre; one nm is one thousandth of a µm.

**Field versus intensity (power).** Our detectors measure the **intensity** $I$ (power per area), not the field. Intensity goes as the square of the field:

$$
I \propto |E|^{2}
$$

The symbol $\propto$ means "is proportional to". So if the field drops by a factor $\sqrt{2} \approx 1.41$, the power drops by a factor of 2. This square law is the key to the Y-branch story.

**Phase, coherence and interference.** The **phase** says where in its up-and-down cycle a wave is at a given point. Two waves are **in phase** when their crests line up, and **out of phase** when the crest of one meets the trough of the other. When two waves overlap, their *fields* add (not their powers). In phase: fields add up, so the result is big. This is **constructive interference**. Out of phase: fields cancel. This is **destructive interference**. Waves that keep a fixed phase relationship (for example, two halves of the same laser beam) are **coherent**. Waves whose phase relation jumps around randomly (for example, two separate lasers) are **incoherent**; on average they do not interfere, and their powers just add.

**Refractive index.** The **refractive index** $n$ of a material says how much slower light travels in it than in vacuum. Silicon has $n \approx 3.5$; silicon dioxide (glass, "**oxide**", SiO$_2$) has $n \approx 1.45$; air has $n = 1$.

**Waveguide.** A **waveguide** is a strip of high-index material (here silicon, 220 nm thick) surrounded by lower-index material (oxide or air). Light bouncing at the boundary from high to low index is trapped by **total internal reflection**, so it stays inside and follows the strip, the way water follows a pipe.

**Mode.** In a waveguide, light can only travel in certain stable cross-sectional patterns called **modes**. Each mode keeps its shape as it travels. The simplest is the **fundamental mode**: one bright blob in the middle. The **second-order mode** has two lobes with opposite signs of field (one lobe "up" while the other is "down"). A narrow "single-mode" waveguide can only *guide* the fundamental mode. Any light that does not fit into a guided mode goes into **radiation modes**: it leaks away out of the waveguide and is lost.

**Effective index.** Each mode travels at its own speed, described by the **effective index** $n_{\text{eff}}$. It is a kind of average of the indices the mode "sees". A mode squeezed tightly in silicon has $n_{\text{eff}}$ close to silicon's; a mode that spreads mostly into the oxide has $n_{\text{eff}}$ close to 1.45.

**Polarization: TE and TM.** The electric field points in a direction. In **TE** (transverse electric, here "quasi-TE") modes the field points mostly sideways, parallel to the chip surface. In **TM** modes it points mostly up-down, perpendicular to the chip. They behave differently because the waveguide is wider than it is tall.

**Decibels (dB).** Engineers measure power ratios in **decibels**:

$$
\text{loss (dB)} = -10 \log_{10}\left(\frac{P_{\text{out}}}{P_{\text{in}}}\right)
$$

Here $P_{\text{in}}$ is power going in and $P_{\text{out}}$ is power coming out. Useful values to remember:

| Loss in dB | Fraction of power kept |
|---|---|
| 0.3 dB | about 93% |
| 1 dB | about 79% |
| 3 dB | about 50% (half) |
| 10 dB | 10% |
| 70 dB | $10^{-7}$ (one ten-millionth) |

Plots often show this as a negative number (for example $-3$ dB), meaning "3 dB of loss". **Insertion loss** is the total loss of putting a device in the path. **Excess loss** is the extra loss beyond what an ideal device would have.

**Gaussian beam and numerical aperture.** The beam that comes out of a lens or a fibre has a smooth bell-shaped cross-section called a **Gaussian beam**. The **numerical aperture** (NA) of a lens measures how wide a cone of light it collects or focuses: $\text{NA} = n \sin\theta$, where $\theta$ is the half-angle of the cone and $n$ is the index of the medium (1 in air). A high NA means a steep cone, which focuses to a *small* spot. A low NA means a gentle cone and a *large* spot. A standard single-mode fibre has NA = 0.14, which is low, so its spot is large (about 10 µm across).

**Mode overlap.** When light in one shape (say a fibre's beam) hits a waveguide whose mode has another shape, only the "matching part" gets in. The fraction that gets in is the **overlap integral**, a standard formula:

$$
\eta = \frac{\left| \int E_{1}^{*} \, E_{2} \, dA \right|^{2}}{\int |E_{1}|^{2} \, dA \cdot \int |E_{2}|^{2} \, dA}
$$

$E_1$ and $E_2$ are the two field patterns, $E_1^*$ is the complex conjugate (a technical detail for handling phase), and $dA$ is a small patch of area over the cross-section. The top measures how much the two patterns "look alike, point by point". The bottom normalizes by the size of each. So $\eta$ is between 0 (no match) and 1 (perfect match). Mismatch in shape, size or position all reduce $\eta$. The loss from this is called **mode-mismatch loss**.

**Near field and far field.** The **near field** is the light pattern right at the output facet of a device. The **far field** is the pattern far away, described by angles. It tells you how fast the beam spreads (its **divergence**). A small spot spreads quickly (large angle); a large spot spreads slowly.

**Simulation tools.** **FDTD** (finite-difference time-domain) is a computer method that solves Maxwell's equations (the basic laws of light) step by step on a fine grid in space and time. **3D FDTD** is accurate but slow. **2.5D FDTD** (also called varFDTD) first squashes the vertical direction into an effective index, then simulates in 2D; it is much faster and fairly accurate for flat chip devices. A **mode solver** finds the modes of a fixed cross-section. A **GDS** file is the standard file format for chip layouts (the drawn shapes).

**Adiabatic.** A slow, gentle change in a waveguide's shape is **adiabatic** if the light stays in the same mode (for example, the fundamental) throughout, with no energy kicked into other modes or radiation. The longer and more gradual the taper, the more adiabatic it is.

## 4.2 Y-branch

> **In one sentence:** A Y-branch is a smoothly widening junction that splits one waveguide into two with equal power, but when used backwards it only keeps the light that adds up *in phase*, so it cannot add up power from unrelated sources.

### What it does

A **Y-branch** has one waveguide on one side and two on the other, like the letter Y on its side. Used left-to-right, it is a **splitter**: it divides light equally into two waveguides. Used right-to-left, it is a **combiner**: it merges light from two waveguides into one.

**Figure 4.21 — Y-branch layout (GDS file YBranch_Compact.gds).** A top-down drawing of the device, with a 1 µm scale bar. On the left is a straight input waveguide. It flows into a transition region that widens into a smooth, bulb-like symmetric shape. This is a *taper*: a gradual widening so the light can spread out gently before it splits. From the right of the bulb, two curved arms branch off, one curving up, one down. Between the arms, at the centre, is a small teardrop-shaped notch where the two arms separate. Lesson: the whole device is only a few µm long, and its exact outline is not a simple Y; it was carefully shaped by computer optimization to keep losses low.

```
                 ______________ out 1
   in   ______ /  ___
   ====|_______  (   notch
               \ ---
                 -------------- out 2
        input  taper  two arms
```

### The splitter: easy to understand

Send in light with intensity $I_i$ and field $E_i$ (the "i" means input). By symmetry, half the power goes into each arm:

$$
I_{1} = I_{2} = \frac{I_{i}}{2}
$$

Because power goes as the field squared, each arm's field is the input field divided by $\sqrt{2}$:

$$
E_{1} = E_{2} = \frac{E_{i}}{\sqrt{2}}
$$

Check: $\left(E_i/\sqrt{2}\right)^2 = E_i^2/2$. Half the power in each arm, so total power is conserved.

### Not really a three-port device

The book's key point: **you cannot think of a Y-branch as just three ports** (one in, two out). You must think about *modes*. The single wide waveguide on the "combined" side can carry (at least) two kinds of light patterns:

- the fundamental mode (one blob), which is what continues on in the single-mode output waveguide;
- the second-order mode (two lobes of opposite sign), or radiation modes, which are lost once the waveguide narrows to single-mode.

So the Y-branch is really a system with two modes on each side: two arms on one side, and two modes (fundamental + second-order/radiation) on the other. That makes it a **50/50 beam-splitter** in *both* directions, just like a half-silvered mirror.

### The combiner: the surprise

Now send light into only **one** arm, with intensity $I_1$ and field $E_1$. The same 50/50 rule applies: half the light goes into the fundamental mode of the combined waveguide, and half into the second-order (or radiation) mode, which is lost. So the useful output is:

$$
I_{i} = \frac{I_{1}}{2}, \qquad E_{i} = \frac{E_{1}}{\sqrt{2}}
$$

Light from one arm loses half its power on the way through. The Y-branch is not a lossless funnel.

Why? Think in fields. The output's fundamental mode is symmetric. Light in just one arm is lopsided. A lopsided pattern can be written as "half symmetric + half antisymmetric" (just like $1 = \tfrac{1}{2}(1+1) + \tfrac{1}{2}(1-1)$ for the two arms). Only the symmetric half fits the fundamental mode.

Now work out the three combiner cases with fields. Let each arm carry field $E$ (power $E^2$ each, total input power $2E^2$). The field in the output fundamental mode is the sum of the arm fields divided by $\sqrt{2}$:

- **Two in-phase inputs:** $(E + E)/\sqrt{2} = \sqrt{2}\,E$. Power $= 2E^2$, which is *all* the input power. Constructive interference. Ideally 100% (0 dB loss).
- **Two out-of-phase inputs:** $(E - E)/\sqrt{2} = 0$. Power $= 0$. Destructive interference. All the light goes to the second-order mode or radiates away.
- **One input only:** $(E + 0)/\sqrt{2}$. Power $= E^2/2$, half of that arm's power (3 dB loss).

Two important practical rules follow:

1. **You cannot use a Y-branch to combine two incoherent beams to get more power.** With incoherent light (say two separate lasers), the phase difference wanders randomly between "in phase" and "out of phase". On average you get half the total power, so you gain nothing over using one beam alone.
2. **If only one port of a combiner has light, the output is half of that input.**

### Real Y-branches and how they were optimized

Real Y-branches are not perfect 50/50 splitters. They have **excess loss**: some light scatters out at the junction. To reduce it, the geometry is optimized with FDTD. The book's design used a **genetic algorithm**: a search method inspired by evolution. It tries many shapes, keeps the best ones, mixes and slightly mutates them, and repeats. The "genes" were the widths of the Y-branch at several points along its length. The result, shown in Figure 4.21, has an insertion loss below **0.3 dB** (about 93% of the light gets through, counting both outputs together). That is the shape of the smooth taper you see in the layout.

### Simulating it (Listing 4.12)

The simulation can be run in 2.5D or 3D FDTD. The book's script (Listing 4.12) does the following:

1. Loads the GDS layout of the Y-branch.
2. Sets up the simulation region, the materials, a mode source (light launched in a chosen waveguide mode), and monitors that measure the output.
3. Runs four simulations: one splitter case and three combiner cases (one input; two inputs in phase; two inputs out of phase).
4. Uses a **mode-expansion monitor** at the output. This performs mode overlap integrals to find how much power ended up in the fundamental mode specifically (not just total power).
5. Plots field pictures and loss versus wavelength, and saves movies. The movies help you *see* where light is lost.

Input: the layout, wavelength range (1.5–1.6 µm), which ports are excited and with what phase. Output: field maps and insertion loss curves (Figures 4.22–4.25).

**Figure 4.22 — Y-branch as a splitter. (a) Field profile. (b) Insertion loss.** Panel (a) is a colour map of the light intensity seen from above, about 16 µm long and 8 µm tall. Light enters on the left in one waveguide (at $y = 0$). Around $x \approx 2$–3 µm it spreads out in the taper and then cleanly separates into two bright beams in the upper and lower arms. Little light escapes. Panel (b) shows insertion loss into *one* output versus wavelength from 1.5 to 1.6 µm. It stays between about $-3.29$ dB and $-3.24$ dB (best near 1.545 µm). Lesson: each arm gets about half the light. 3 dB is the ideal for a 50/50 split; the extra ~0.25–0.29 dB is the device's excess loss. The curve is very flat: the device works across the whole 100 nm band.

**Figure 4.23 — Y-branch as a combiner with one input. (a) Field profile. (b) Insertion loss.** Panel (a): light enters through only one arm and goes towards the single waveguide. You can see ripples (interference fringes) along the waveguide in the input section and the junction. They show that two modes are excited at the output, the fundamental and the second-order TE mode, which travel at different speeds and beat against each other. Panel (b): the loss into the fundamental mode, found by mode overlap, is between about $-3.28$ and $-3.22$ dB across 1.5–1.6 µm. Lesson: just as the theory says, light from one arm loses half its power (slightly more than 3 dB). The lost half went into the second-order mode.

**Figure 4.24 — Y-branch as a combiner with two in-phase inputs. (a) Field profile. (b) Insertion loss.** Panel (a): light comes in through both arms, in phase, and merges into one strong beam in the single waveguide. Panel (b): the loss is only about $-0.27$ to $-0.22$ dB, best (about $-0.22$ dB, roughly 95% transmitted) near 1.545 µm. Lesson: coherent, in-phase light combines with constructive interference and ideally nearly 100% of the power comes out. The small deviation from 0 dB is the **excess loss** of the device. (The book text says this excess loss is plotted in "Figure 4.23b"; it is actually panel (b) of Figure 4.24 that shows it.)

**Figure 4.25 — Y-branch as a combiner with two out-of-phase inputs. (a) Field profile. (b) Insertion loss.** Panel (a): two input arms, light with opposite phases, merging into one output waveguide. The light does not form the fundamental mode; what remains is a higher-order pattern. Panel (b): the power in the fundamental mode is about $-69$ to $-71$ dB (lowest about $-70.7$ dB near 1.555 µm). Lesson: 70 dB means only about one ten-millionth of the power ends up in the fundamental mode. Destructive interference is almost perfect. All the power goes into the second-order TE mode or radiates away. This near-perfect cancellation is exactly what makes interferometers work.

### Looking ahead: the Mach-Zehnder interferometer

With this understanding of Y-branches, the book next (§4.3) treats interference of coherent beams in a **Mach-Zehnder interferometer** (MZI).

**Figure 4.26 — Mach-Zehnder interferometer layout example.** A top-down layout with a 40 µm scale bar. The whole device is roughly 560–600 µm long and 120–160 µm tall. From left to right: an input waveguide; a first Y-branch (splitter); two arms, the top going straight across and the bottom dropping down through a rounded 90° bend, running parallel, and then bending back up; a second Y-branch (combiner); and an output waveguide. Lesson: an MZI is just "splitter, two paths, combiner". If the two paths give the light the same phase, the combiner sees in-phase inputs and passes nearly all the light (Figure 4.24). If they differ by half a wave, it sees out-of-phase inputs and blocks it (Figure 4.25). Changing the phase in one arm therefore switches the light on and off. This is the basis of modulators, switches and sensors.

> **Key takeaways:**
>
> - A Y-branch splits power 50/50: each output gets $I_i/2$ and field $E_i/\sqrt{2}$.
> - It must be understood with modes: the combined side carries a fundamental and a second-order (or radiation) mode, so it acts as a 50/50 beam-splitter in both directions.
> - As a combiner: in-phase coherent inputs give ~100% out; out-of-phase give ~0% (about $-70$ dB in simulation); one input alone gives 50% (3 dB). You cannot boost power by combining incoherent beams.
> - A genetic-algorithm-optimized, gently tapered shape gives under 0.3 dB insertion loss; simulations show about 3.25 dB per arm as a splitter and about 0.22 dB excess loss as an in-phase combiner, flat across 1.5–1.6 µm.

## 5.3.1 Nano-taper edge coupler

> **In one sentence:** A nano-taper edge coupler narrows the silicon waveguide slowly (adiabatically) to a tiny 180 nm tip, so the light is pushed out of the silicon and swells into a big, soft spot that matches a lens or high-NA fibre at the edge of the chip, with a best-case loss of about 1 dB if the taper is at least 100 µm long.

### The problem it solves

A silicon waveguide mode is tiny, about 0.5 µm across. A standard fibre's beam is about 10 µm across. If you just butt them together, the overlap is terrible and most light is lost. An **edge coupler** sits at the polished or etched side edge (**facet**) of the chip and makes the chip's mode bigger so it matches the outside beam. (The book's Figure 5.21b, not included in this packet, shows the geometry.)

The trick is surprising: to make the mode *bigger*, you make the silicon *narrower*. This is called a **nano-taper** or **inverse taper**. Here is why. A wide silicon strip holds light tightly. As the strip gets thinner, it becomes too small to hold the light, and the mode spills out into the surrounding oxide. At a 180 nm wide tip, most of the light is actually in the oxide, spread over a region a few µm wide. Think of a narrow rope in a pool, with a floating mat of light around it: the thinner the rope, the wider the mat spreads.

The taper must be **adiabatic**: narrow so slowly that the light stays in the fundamental mode the whole way and simply grows, without being kicked into radiation.

```
  chip side (top view)                         edge (facet)
  ==========\                                     |
  normal     \______________________________ tip  |  ) ) )  beam to
  waveguide   slowly narrowing silicon (taper)    |         lens/fibre
  ==========/   light spreads out into oxide ->   |
                <---------- length L ---------->
```

The book shows two ways to estimate how well this works: a fast mode-overlap method and a full 3D FDTD method.

### Mode overlap calculation approach

**The idea.** If the taper is adiabatic, the light arriving at the tip is simply the fundamental mode of the tip's cross-section. So we can skip simulating the taper and just (1) compute the mode of the tip, and (2) compute its overlap with the Gaussian beam from a lens. That gives the coupling efficiency.

The tip: a silicon waveguide **180 nm wide, 220 nm thick, surrounded by oxide**, at $\lambda = 1.55$ µm, quasi-TE.

**Figure 5.22 — Mode of a 180 × 220 nm nano-taper ($n_{\text{eff}} = 1.46$).** Panel (a) shows the electric field intensity in the cross-section, zoomed in (about ±0.8 µm across). The small black rectangle is the silicon core. The brightest spots are two lobes at the left and right edges of the rectangle. This is typical of a quasi-TE mode: the sideways-pointing field jumps up just outside the silicon walls. The field spreads well beyond the core, to about ±0.6 µm sideways and ±0.45 µm up-down. Panel (b) shows the energy density on a log (dB) scale over ±2 µm. It fades slowly outward, still at $-40$ dB at the edges, and the contours are slightly wider sideways than vertically. Lesson: the mode lives mostly in the oxide. Its effective index, 1.46, is almost equal to that of oxide itself ($\approx 1.45$), compared with about 3.5 for silicon. The silicon is now only a weak "guide rail".

**Matching to a lens beam.** We want to couple to a Gaussian beam, for example from a **lensed fibre** (a fibre with a lens shaped on its end), a lens assembly with a fibre attached, or a high-NA lens. In the simulation, Gaussian beams are made by ideal lenses with various numerical apertures.

**Figure 5.23 — Gaussian beam from a lens with NA = 0.4 (optimal for TE).** A colour map (in dB, from $-5$ to $-30$) of a smooth beam that is brightest at the centre and fades evenly outward, about 2 µm in scale. Lesson: compare with Figure 5.22. The Gaussian is round and smooth; the taper's mode has two lobes, a rectangular core, and an uneven, slightly flattened shape. They do not match perfectly, so we expect some **mode-mismatch loss** even with perfect alignment.

As a rough guide (standard Gaussian-beam physics, not from the book), the waist radius of a focused beam is about $w_0 \approx \lambda / (\pi \, \text{NA})$. For NA = 0.4: $w_0 \approx 1.55 / (3.14 \times 0.4) \approx 1.2$ µm, which is the same size range as the taper's mode.

**Listing 5.9** (not reproduced) does the overlap calculation:

1. Uses a mode solver to find the tip's mode (Figure 5.22).
2. Creates Gaussian beams for a range of lens NAs.
3. Computes the overlap integral between the mode and each beam.
4. Plots coupling efficiency (dB) versus NA and picks the best NA.

**Figure 5.24 — Coupling efficiency versus lens NA (TE and TM).** The horizontal axis is lens NA from 0.1 to 0.8; the vertical axis is coupling in dB from $-4$ to 0. The TE curve (solid) rises steeply from $-4$ dB at NA ≈ 0.17, peaks at about $-1.15$ dB around NA = 0.4–0.45, then slowly falls to about $-2.25$ dB at NA = 0.8. The TM curve (dashed) starts at higher NA, peaks at about $-1.35$ dB at NA ≈ 0.55, and ends at about $-1.75$ dB. They cross near NA = 0.6 (about $-1.4$ dB). Lesson: too small an NA means a beam that is too big; too large an NA means one that is too small. There is a best size. The best coupling needs **relatively large NAs: 0.4 for TE and 0.55 for TM**. Compare with conventional single-mode fibre, NA = 0.14: the taper's mode is much smaller than a normal fibre's. Fibres with NA around 0.4–0.55 do exist; they are called **high-NA fibres**. Even at the best NA, about 1.1–1.4 dB is lost purely from shape mismatch.

**Alignment sensitivity.** What if the fibre is slightly off-centre? We can simulate this by shifting one mode relative to the other and redoing the overlap.

**Figure 5.25 — Coupling versus misalignment in $x$ and $y$.** Horizontal axis: misalignment from $-2$ to $+2$ µm. Vertical axis: coupling in dB, 0 to $-10$. Four bell-shaped curves:

| Curve | Peak (perfect alignment) | How fast it drops |
|---|---|---|
| x-misalignment, TE | about $-0.9$ dB | widest; about $-3$ dB at ±1 µm, $-10$ dB at ±2 µm |
| y-misalignment, TE | about $-1.0$ dB | narrower; about $-4$ dB at ±1.5 µm, $-10$ dB at ±1.75 µm |
| x-misalignment, TM | about $-1.6$ dB | narrowest; $-10$ dB at about ±1.6 µm |
| y-misalignment, TM | about $-1.6$ dB | almost identical to x, TM |

Read each row as: "at zero shift we get the peak; moving the fibre by this much costs this much". Lesson: the book's headline is that **a 0.6 µm misalignment adds 1 dB of excess loss**. That is less than one hundredth of a hair's width, so the fibre or lens must be positioned very precisely (this is why packaging is hard). TE is also more forgiving than TM, especially sideways ($x$).

**Limitations of the mode overlap approach.** It ignores:

- **reflections** at the waveguide-to-oxide and oxide-to-air boundaries (any change in refractive index reflects a little light back);
- **propagation in the short oxide region** between the silicon tip and the etched oxide facet (the light can spread or change there);
- **propagation in the gap** between the facet and the fibre (the beam diverges in the air);
- **the taper itself**, which must be long enough to be adiabatic and loss-less. The overlap method simply *assumes* this.

The last point is the heart of today's topic: the overlap method cannot tell you *how long* a taper must be. For that you need a full simulation.

**Figure 5.26 — Near-field at the output, in air (200 µm taper, 3D FDTD).** A colour map of the field just outside the chip facet, over ±3 µm in both directions (one axis along the chip surface, the other perpendicular to the wafer). A single bright spot (normalized peak about 0.9) sits at the centre and fades in roughly circular rings, spreading about ±1.5 µm. There is faint background noise (about 0.1–0.2) at the edges. Lesson: the long taper has turned the tiny silicon mode into a smooth, round, Gaussian-like spot a few µm wide, which is what a lensed or high-NA fibre wants. This is the **near-field profile**: what a fibre touching (or very close to) the chip would see.

**Figure 5.27 — Light travelling down a 20 µm taper (top and side views, 3D FDTD).** Two colour maps. Horizontal axis: position along the taper, from about $-18$ µm to 0 µm. The **oxide–air interface is at $y = 0$** (the chip edge). Vertical axis: ±3 µm, sideways in panel (a) (top view) and up-down in panel (b) (side view). On the left, the light is tightly confined in the silicon. Moving right, the silicon narrows and the bright region gradually widens, both sideways and vertically. At the tip and facet the light has spread into a much larger, dimmer spot, with some light radiating into the cladding and air. All along there are periodic ripples (fringes). Lesson: you can *see* the mode growing as the taper narrows. The ripples are **standing waves caused by reflection at the oxide–air interface**: reflected light travelling back interferes with the forward light. They are exactly the reflection effect the overlap method ignored.

### FDTD approach

The second method is a full **3D FDTD** simulation (Figures 5.26 and 5.27). It includes everything: the adiabatic taper, the tip, the oxide, and the air.

- **Listing 5.10** (not reproduced) builds the 3D model of taper + tip + oxide + air, launches the waveguide mode, runs FDTD, and records the field at the output in the air (the near field) as well as the field along the taper.
- **Listing 5.11** (not reproduced) takes that FDTD near field and computes its overlap with Gaussian beams from ideal lenses of various NAs, giving the best coupling and the best NA, just like the first method.
- The simulation could be extended to include the optical fibre itself.

**Figure 5.28 — Far field at the output (200 µm taper).** Panel (a) is a 2D map of intensity versus angle (horizontal and vertical, ±40°): concentric slightly elliptical rings around a bright centre, a bit more stretched vertically. Panel (b) shows slices through it: a "vertical far-field" curve and a "horizontal far-field" curve, both bell-shaped with peak 1 at 0°, fading to near zero around ±45–50°. The horizontal one is slightly narrower. Lesson: the far field tells you how fast the beam spreads after leaving the chip. This matters when choosing a lens, because the lens must capture this cone. The book quotes a **full-width at half-maximum (FWHM)** of about **40°**. FWHM is the width of the curve measured where it is at half its peak height. (The curves are read by eye, so exact numbers from the plot are rough.) A small spot of ~2–3 µm diverging at ~40° is consistent with needing a lens of NA around 0.4, much steeper than standard fibre's 0.14. The beam is slightly asymmetric: it spreads a bit more vertically than horizontally.

**Figure 5.29 — Coupling efficiency versus lens NA for different taper lengths.** Horizontal axis: lens NA 0.1 to 0.9. Vertical axis: coupling in dB, $-4$ to 0. Five curves:

| Taper length $L$ | Peak coupling | Best NA |
|---|---|---|
| 10 µm | about $-1.5$ dB | about 0.6 |
| 20 µm | about $-1.3$ dB | about 0.5 |
| 30 µm | about $-1.2$ dB | about 0.45 |
| 100 µm | about $-0.95$ dB | about 0.4 |
| 200 µm | about $-0.9$ dB | about 0.38 |

Read each row as "with a taper this long, the best you can do is this loss, using a lens of this NA". At high NA (above about 0.75) all curves come together, ending around $-3$ to $-3.5$ dB at NA = 0.9.

Lesson, and the main point about adiabaticity: **short tapers lose light and give a smaller, messier spot** (which needs a higher NA). A short taper changes shape too abruptly; some light is thrown out of the fundamental mode into radiation instead of smoothly growing. As $L$ grows, the loss drops and then levels off. Going from 100 µm to 200 µm barely helps. So **the taper must be at least about 100 µm long** to avoid loss caused by the taper itself. Beyond that, the taper is effectively adiabatic. The best simulated insertion loss is about **1 dB** (about 79% of the light coupled), and the remaining loss is mostly the shape mismatch between the taper's spot and a Gaussian beam.

> **Key takeaways:**
>
> - An inverse (nano-)taper narrows the silicon to a 180 × 220 nm tip; the mode then lives mostly in the oxide ($n_{\text{eff}} = 1.46$, almost the oxide index) and becomes a few µm wide.
> - Mode overlap (fast) assumes an adiabatic taper; it gives best coupling of about $-1.15$ dB (TE, NA 0.4) and $-1.35$ dB (TM, NA 0.55), needing high-NA fibres (standard fibre NA is 0.14).
> - Alignment is tight: 0.6 µm of misalignment adds 1 dB of loss; TE is more tolerant than TM.
> - Full 3D FDTD includes reflections (visible as ripples), the oxide and air gaps, and the taper itself; it gives a ~40° FWHM far field.
> - Adiabaticity in numbers: tapers of 10–30 µm lose extra light; at least ~100 µm is needed, giving a best-case loss of about 1 dB.

## Glossary

| Term | Plain meaning |
|---|---|
| 2.5D FDTD (varFDTD) | Faster simulation that flattens the vertical direction into an effective index, then solves in 2D. |
| 3D FDTD | Full, accurate, slow simulation of light in all three dimensions. |
| Adiabatic | Changing so slowly that light stays in the same mode with no loss to other modes. |
| Coherent | Waves with a fixed phase relation that can interfere steadily. |
| Combiner | Device that merges light from two waveguides into one. |
| Constructive interference | Waves in phase add up to a bigger wave. |
| dB (decibel) | Log scale for power ratios; 3 dB = half, 10 dB = one tenth. |
| Destructive interference | Waves out of phase cancel each other. |
| Divergence | How fast a beam spreads out after leaving its source. |
| Edge coupler | Structure at the chip's side edge that couples light to a fibre or lens. |
| Effective index ($n_{\text{eff}}$) | The "average" refractive index a mode experiences; sets its speed. |
| Electric field ($E$) | The wave's "height"; can be positive or negative. |
| Excess loss | Loss beyond what an ideal device would have. |
| Facet | The cut or etched edge face of the chip where light exits. |
| Far field | Beam pattern far from the device, measured in angles. |
| FDTD | Finite-difference time-domain: simulation that solves the laws of light step by step on a grid. |
| Fundamental mode | The simplest guided light pattern: one central blob. |
| FWHM | Full width at half maximum: width of a peak measured at half its height. |
| Gaussian beam | Smooth, bell-shaped beam from a lens or fibre. |
| GDS | Standard file format for chip layout drawings. |
| Genetic algorithm | Optimization that mimics evolution: keep, mix and mutate the best designs. |
| High-NA fibre | Fibre with a small, tightly focused mode (large numerical aperture). |
| Incoherent | Waves with randomly varying phase; their powers just add on average. |
| Insertion loss | Total power lost by putting a device in the light path. |
| Intensity ($I$) | Power per area; proportional to $\lvert E \rvert^2$. |
| Inverse taper / nano-taper | Waveguide that narrows to a tiny tip so the mode spreads out and grows. |
| Lensed fibre | Optical fibre with a lens formed on its end. |
| Mach-Zehnder interferometer (MZI) | Splitter, two paths, combiner; output depends on the phase difference of the paths. |
| Mode | A stable light pattern that a waveguide can carry without changing shape. |
| Mode-expansion monitor | Simulation tool that measures how much power is in each mode. |
| Mode-mismatch loss | Loss because two light patterns have different shapes or sizes. |
| Mode overlap (integral) | Calculation of how well two light patterns match; gives the coupling fraction. |
| Mode solver | Program that finds the modes of a waveguide cross-section. |
| Near field | Light pattern right at the device's output face. |
| Numerical aperture (NA) | $n \sin\theta$; how steep a light cone a lens or fibre uses. High NA, small spot. |
| Oxide (SiO$_2$) | Silicon dioxide, glass; index about 1.45. |
| Phase | Where a wave is in its up-down cycle. |
| Quasi-TE / TE | Mode with electric field mostly parallel to the chip surface. |
| Radiation modes | Light that is not guided and leaks away. |
| Refractive index ($n$) | How much slower light goes in a material than in vacuum. |
| Second-order mode | Guided pattern with two lobes of opposite sign. |
| Splitter | Device that divides light from one waveguide into two. |
| Standing wave | Fixed ripple pattern from forward and reflected waves interfering. |
| Taper | Waveguide whose width changes gradually along its length. |
| TM | Mode with electric field mostly perpendicular to the chip surface. |
| Waveguide | Strip of high-index material that traps and guides light. |
| Y-branch | Y-shaped junction used as a 50/50 splitter or combiner. |

## Check yourself

1. A Y-branch splitter gets input field $E_i$. What field and power go into each arm?

   *Answer:* Field $E_i/\sqrt{2}$ in each arm, so power $I_i/2$ each, because power goes as field squared.

2. Why is it wrong to treat the Y-branch as a simple three-port device?

   *Answer:* The combined waveguide carries at least two modes (fundamental and second-order or radiation). The device is really two modes in, two modes out, a 50/50 beam-splitter in both directions.

3. You feed light into only one input of a Y-branch combiner. How much reaches the output waveguide, and where does the rest go?

   *Answer:* Half (about 3 dB loss). The other half goes into the second-order mode or radiation and is lost.

4. Can you double your power by combining two separate lasers with a Y-branch?

   *Answer:* No. They are incoherent, so their phase difference wanders; on average only half the total power gets out, no more than one laser alone.

5. In the simulations, two out-of-phase inputs gave about $-70$ dB in the fundamental mode. What does that mean physically?

   *Answer:* Only about $10^{-7}$ of the power is in the fundamental mode: near-perfect destructive interference. Almost all the light goes into the second-order mode or radiation.

6. Why does narrowing the silicon at the edge coupler make the mode *bigger*?

   *Answer:* A thin silicon strip is too small to hold the light tightly, so the mode spills into the oxide and spreads out. At 180 nm, $n_{\text{eff}} = 1.46$, nearly the oxide index, showing the light is mostly in the oxide.

7. What lens NA gives the best coupling to the 180 × 220 nm tip, and how does that compare with standard fibre?

   *Answer:* About 0.4 for TE and 0.55 for TM, much higher than standard single-mode fibre's 0.14. You need high-NA fibres or lenses.

8. How much misalignment adds 1 dB of loss?

   *Answer:* About 0.6 µm.

9. Name two things the mode-overlap method ignores that FDTD includes.

   *Answer:* Any two of: reflections at the waveguide–oxide and oxide–air interfaces; propagation through the short oxide region; propagation in the gap to the fibre; the taper itself (whether it is long enough to be adiabatic).

10. What does Figure 5.29 teach about adiabaticity?

    *Answer:* Short tapers (10–30 µm) lose extra light and need higher NA. At about 100 µm or more the taper is effectively adiabatic; going longer barely helps. The best-case loss is about 1 dB.
