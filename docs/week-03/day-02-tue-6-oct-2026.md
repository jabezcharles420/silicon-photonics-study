# Week 3 · Day 2 — Tuesday 6 Oct 2026

*Simple-English study version of Chrostowski & Hochberg §11.1 (Fabrication non-uniformity) and §3.2.11 (Waveguide loss).*

[:material-file-pdf-box: Download this day as PDF](day-02-tue-6-oct-2026.pdf){ .md-button }

---

## Before you start: the big picture

Imagine a bakery that makes thousands of cookies from the same recipe. On paper every cookie is identical. In reality, the oven is a little hotter at the back, the dough is a little thicker on one side of the tray, and no two cookies come out exactly the same. Cookies close together on the same tray are usually more alike than cookies from opposite corners, or from different days.

Silicon photonic chips have the same problem. A designer draws tiny glass-and-silicon "wires for light" (waveguides) and devices built from them, such as ring-shaped filters. The factory (the **foundry**) builds them, but the silicon layer is a few nanometres thicker in one place than another, and the lines come out a few nanometres wider or narrower. Many photonic devices are extremely sensitive to these tiny errors: a 5 nm change in thickness can shift the colour of light a filter selects by several nanometres. When a chip needs many devices to work at the *same* colour (wavelength), those shifts must be fixed afterwards, usually by heating each device a little. Heating costs electrical power, and that power costs money and creates heat.

Section 11.1 teaches you (1) how big these manufacturing variations are, (2) two simulation tricks to predict their effect before you build anything (lithography process contours and corner analysis), and (3) real measurements on 371 identical ring resonators that show how the mismatch between two devices grows with the distance between them. The practical lesson: put devices that must match close together. Section 3.2.11 then covers a related practical topic: why light gets weaker as it travels along a waveguide (loss), and how to convert between the different units used to describe that loss.

---

## Background you need

This section builds, from the ground up, every idea the packet uses without explaining it.

### Light is a wave; wavelength and frequency

Light is a travelling wave of electric and magnetic fields. Like a water wave, it has crests and troughs. The distance between two crests is the **wavelength**, written $\lambda$ (Greek "lambda"). The number of crests passing a point each second is the **frequency**, written $f$ or $\nu$. They are linked by the speed of light $c \approx 3\times 10^{8}$ m/s:

$$c = \lambda f$$

Silicon photonics mostly uses light with $\lambda \approx 1550$ nm (1.55 µm). This is infrared light, invisible to the eye, and it is the standard "colour" used in fibre-optic telecommunications. For scale: 1 µm (micrometre) = 1000 nm (nanometres); a human hair is about 70 µm wide.

Engineers describe a small shift of "colour" either as a wavelength shift (in nm or pm, where 1 pm = 0.001 nm) or as a frequency shift (in GHz). Near 1550 nm the conversion is:

$$\Delta\lambda \approx \frac{\lambda^{2}}{c}\,\Delta f$$

Worked example: $\Delta f = 1000$ GHz $= 10^{12}$ Hz gives $\Delta\lambda \approx (1.55\times10^{-6})^{2}\times 10^{12} / (3\times 10^{8}) \approx 8\times 10^{-9}$ m $= 8$ nm. So **100 GHz ≈ 0.8 nm** near 1550 nm. Keep this in mind; it helps you read the numbers below.

### Refractive index

Light travels slower in materials than in vacuum. The **refractive index** $n$ says how much slower: speed $= c/n$. Glass (silicon dioxide, "oxide") has $n \approx 1.44$; silicon has $n \approx 3.48$ at 1550 nm. Inside a material the wavelength also shrinks to $\lambda/n$.

### Waveguides, SOI, strip and rib

A **waveguide** is a "wire for light". It is a strip of high-index material (silicon) surrounded by low-index material (oxide or air). Light bouncing inside the silicon hits the boundary at a shallow angle and is fully reflected back (**total internal reflection**), so it stays trapped and follows the strip, even around bends.

Silicon photonic chips start from an **SOI wafer** (silicon-on-insulator): a thick silicon base, a layer of buried oxide, and on top a thin silicon layer, typically **220 nm** thick. Waveguides are carved into this top layer.

- A **strip waveguide** (also called a wire) is a rectangle of silicon, e.g. **500 nm wide × 220 nm tall**, fully etched down to the oxide.
- A **rib waveguide** is only partly etched: a 220 nm tall ridge sits on top of a thin leftover silicon **slab** (e.g. 90 nm thick) that extends sideways.

```
   strip (cross-section)          rib (cross-section)
        +-----+                        +-----+
        | Si  | 220 nm          +------+ Si  +------+  slab 90 nm
   =====+-----+=====            +-------------------+
        oxide                          oxide
       <-500->                        <-500->
```

**Cladding** is the material around the waveguide (oxide, or simply air if nothing is put on top).

### Modes, effective index, group index, TE/TM

Light in a waveguide does not take any shape it likes. Only certain stable field patterns, called **modes**, can travel without changing shape. A **single-mode** waveguide supports just one pattern (per polarization); a wide waveguide is **multi-mode** and supports several, which can cause trouble.

Part of the mode sits in the silicon and part leaks into the cladding. So the light "feels" an average index between 1.44 and 3.48. This average is the **effective index**, $n_{eff}$ (around 2.4–2.6 for the waveguides here). The phase of the light advances along the waveguide as if it were in a material of index $n_{eff}$. Crucially, $n_{eff}$ depends on the waveguide's width and thickness: a thicker or wider waveguide holds more of the light in silicon, so $n_{eff}$ goes up. This is the root of all the sensitivity in this packet.

The **group index**, $n_g$, describes how fast a *pulse* (a packet of light, or the information it carries) moves: speed $= c/n_g$. Because $n_{eff}$ changes with wavelength (this is called **dispersion**), $n_g$ is different from $n_{eff}$. The standard relation is $n_g = n_{eff} - \lambda\, dn_{eff}/d\lambda$. For silicon wires $n_g \approx 3.8$–$4.3$, noticeably bigger than $n_{eff}$.

**Polarization** is the direction the electric field points. **TE** (transverse electric) modes have the field mostly horizontal (along the width); **TM** (transverse magnetic) modes have it mostly vertical (along the thickness). TE light is more sensitive to width; TM light is more sensitive to thickness. That difference lets researchers separate the two causes of variation.

### Phase and interference

The **phase** is where the wave is in its cycle (crest, trough, or in between), measured as an angle; one full cycle is $2\pi$. When two waves meet, they add. If crests line up ("in phase"), they reinforce each other (**constructive interference**); if a crest meets a trough, they cancel (**destructive interference**). Resonators and gratings all rely on this.

### Ring (and racetrack) resonators, FSR, Q

A **ring resonator** is a waveguide bent into a closed loop placed next to a straight "bus" waveguide. Some light leaks from the bus into the ring through a **directional coupler** (two waveguides running side by side, very close, so light can hop across the gap). A **racetrack** is a ring stretched by inserting two straight sections, which makes the coupling region longer.

Light goes round and round the loop. If, after one lap, it comes back exactly in phase with itself, it builds up strongly. This happens when a whole number $m$ of wavelengths fits into the round-trip length $L$:

$$m\,\lambda_m = n_{eff}\,L$$

Here $m$ is an integer (the **azimuthal mode number**, i.e. how many wavelengths fit around the loop), $\lambda_m$ is the resonance wavelength for that $m$, and $n_{eff}L$ is the "optical length" of the loop. At these resonance wavelengths, light is pulled out of the bus, so the transmitted spectrum shows sharp **dips**.

- If the waveguide gets a bit thicker, $n_{eff}$ rises, so $\lambda_m$ rises: the resonance shifts to longer wavelength. This is why rings are such good (and such fragile) detectors of fabrication errors.
- The spacing between neighbouring dips is the **free spectral range (FSR)**. The spectrum repeats every FSR, so a ring cannot tell apart wavelengths that differ by exactly one FSR.
- The **quality factor (Q)** measures how sharp a dip is: $Q \approx \lambda / (\text{dip width})$. A Q of 10 000 at 1550 nm means a dip about 0.15 nm wide.

### Bragg gratings and the stopband

A **Bragg grating** is a waveguide whose width wiggles periodically, like the teeth of a comb (**corrugation**). Each wiggle reflects a tiny bit of light. At one particular wavelength (the **Bragg wavelength**) all those small reflections add up in phase and the grating becomes a mirror. Around that wavelength there is a band of colours that is reflected instead of transmitted, called the **stopband**. In a transmission plot it appears as a wide, deep dip. The width of the stopband is the grating's **bandwidth**. Theory (the book's Equation 4.33) says that a longer grating has the same or a *narrower* bandwidth, never a wider one. Keep this in mind for Figure 11.1.

### Grating couplers

A **fibre grating coupler (GC)** is a patch of etched lines on the chip that scatters light upward out of the chip into an optical fibre held above it, or the reverse. It works best at one **central (peak) wavelength** and has a bell-shaped transmission versus wavelength. Its etched lines are only partly etched, so its behaviour depends strongly on **etch depth**.

### Decibels (dB)

Optical power ratios are given in **decibels**:

$$\text{ratio in dB} = 10\log_{10}\left(\frac{P_{out}}{P_{in}}\right)$$

−3 dB means half the power survives; −10 dB means one tenth; −20 dB means one hundredth; −40 dB means one ten-thousandth. Losses add in dB: two couplers losing 5.5 dB each lose 11 dB in total. Loss per length is given in **dB/cm**.

### How chips are made: lithography and etching

To make a waveguide, the foundry coats the wafer with a light-sensitive polymer (**photoresist**), shines light through a **mask** carrying the drawn pattern (**lithography**), develops the resist, and then **etches** away the silicon that is not protected. Because the patterns are close to the wavelength of the light used for printing, the printed shapes come out blurred: sharp corners get rounded, narrow gaps may close, and lines can come out a bit wider or narrower depending on the light dose (**over- or under-exposure**). The **etch depth** (how deep you cut) also varies. If two masks are used, they may not line up perfectly (**overlay error**).

A **wafer** is the round disc (often 200 mm across) that is processed. It is cut into many rectangular **dies** (chips). Variations happen at every scale: **within a device**, **across a chip**, **within a wafer**, **wafer-to-wafer**, and **batch-to-batch** (between production runs).

### Statistics you will need

- **Standard deviation (σ, "sigma")**: a measure of spread. For a bell-shaped (**Gaussian** or **normal**) distribution, about 68% of values lie within ±1σ of the average and 99.7% within ±3σ. So "±10 nm (3σ)" means almost all wafers are within 10 nm of the target; σ itself is about 3.3 nm.
- **Median**: the middle value when data are sorted. Half the values are below, half above. It is less affected by a few extreme values than the average (**mean**).
- **Quartiles**: the 25% and 75% points of sorted data. The range between them holds the central 50% of the data (the **interquartile range**, IQR).
- **Box plot**: a compact picture of a distribution. The box spans the 25%–75% quartiles, a mark inside shows the median, "whiskers" extend to cover most of the rest, and points beyond are drawn individually as **outliers**. **Notches** on the box show the uncertainty (95% confidence interval) of the median.
- **Probability distribution function (p.d.f.)**: a curve showing how likely each value is. Tall where values are common, low where they are rare.
- **Correlation**: two quantities are correlated if they tend to move together. Here, "spatially correlated" means that nearby points on a chip tend to have similar errors.
- **"n choose 2"**: the number of distinct pairs you can form from $n$ items, $n(n-1)/2$.

### WDM, tuning, and trimming

**Wavelength division multiplexing (WDM)** sends many data channels down one waveguide or fibre, each on its own wavelength, like many radio stations sharing the air. Filters and modulators must then sit exactly on their assigned wavelengths. If fabrication shifts them, they must be pulled back. The usual method is **thermal tuning**: a small metal **heater** above the device warms it. Silicon's index rises with temperature, so the resonance moves to longer wavelength. **Trimming** means correcting a device's wavelength (by heating or by a permanent change) after fabrication. A heater's efficiency is quoted, for example, in mW per FSR: how much electrical power shifts the resonance by one full FSR.

> **Key takeaways:**
>
> - Devices like rings and gratings select wavelengths through interference, so they depend on $n_{eff}$, which depends on waveguide width and thickness.
> - A few nanometres of geometry error shift the selected wavelength by nanometres.
> - Shifts are fixed by heating, which costs power; statistics (σ, median, box plots) let us predict how much.

---

## 11.1 Fabrication non-uniformity

> **In one sentence:** Because chips are never built exactly as drawn, photonic devices on the same chip end up at slightly different wavelengths, and silicon thickness is the biggest culprit.

### Why this matters

Many photonic chips need several components to agree precisely on two things: their **central wavelength** (the colour they act on) and their waveguide **propagation constants** (how fast the phase advances along the waveguide; this is $2\pi n_{eff}/\lambda$). Examples are ring modulators and optical filters in a WDM system. If the factory makes them slightly different, they disagree. To build a working system, you need to know how big the disagreement will be. That tells you which fix to use (for example, thermal tuning) and how much it will cost in electrical power.

### What studies have found

Researchers have measured variation at many scales: inside a single device (for example in **CROWs**, coupled-resonator optical waveguides, which are chains of rings that must all match), within one wafer, between wafers, and between batches. The conclusion is consistent:

1. **The biggest cause is the variation in silicon layer thickness.**
2. **The second cause is lithography**, which changes the waveguide width.

Some key numbers:

- Zortman and co-workers found that thickness variation across a 10 cm span of wafer shifted TE ring resonances by **±1000 GHz** (about ±8 nm at 1550 nm). Width variation only caused **±200 GHz** (about ±1.6 nm). So thickness matters about five times more.
- By measuring both TE rings (width-sensitive) and TM rings (thickness-sensitive), they worked backwards to find the actual dimension errors: about **±5 nm in thickness** and **±5 nm in width** (or ring diameter).
- Another study used TE Bragg gratings in both strip and rib waveguides and also found thickness variations of about **±5 nm**, which caused resonance shifts of up to **10 nm**. The two studies agree.

Why is thickness so damaging? The waveguide is only 220 nm thick but 500 nm wide. A 5 nm change is a bigger fraction of 220 nm than of 500 nm, and the light is squeezed hardest in the thin vertical direction, so $n_{eff}$ reacts more strongly to it. Notice the amplification: a 5 nm geometry error gives a wavelength error of several nm.

### Example: Bragg gratings that get worse with length

The book shows a striking example with Bragg gratings. All have a **20 nm corrugation width** ($\Delta W$, how much the width wiggles), on strip waveguides **500 nm wide** with **air cladding**. Their lengths range from **325 µm to 4.9 mm**.

Theory (Equation 4.33, from Chapter 4) says: as a grating gets longer, its bandwidth should stay the same, or shrink if the coupling per period is weak. Why? A longer grating has more periods to add up the reflections, so the "mirror" gets more selective, not less.

**Figure 11.1 — Measured transmission of Bragg gratings of increasing length.** Four stacked plots show transmitted power (in dB, from 0 down to about −40 dB) against wavelength (1510 to 1530 nm). Each is labelled by its number of periods $N$:

| Periods $N$ | Approx. length | Dip centre | Dip depth | Stopband width |
|---|---|---|---|---|
| 1 000 | 325 µm | ~1522.5 nm | ~−32 dB | ~1.5–2 nm |
| 3 000 | ~1 mm | ~1519 nm | ~−35 dB | ~3–4 nm |
| 9 000 | ~3 mm | ~1518 nm (1515–1521) | ~−42 dB | ~6 nm |
| 15 000 | 4.9 mm | ~1517.5 nm (1514.5–1520.5) | below −40 dB | ~6 nm, widest |

Read the table row by row: as the grating gets longer (going down), the dip gets deeper, much wider, and the centre wanders. The longer ones also show ripples (wiggles) on the edges and inside the dip. (The caption's "= 325 nm" has lost its symbol; since 1000 periods make 325 µm, it is most likely the grating period, 325 nm.)

The lesson: **the stopband becomes broader as the grating gets longer, the opposite of what theory predicts.** The reason is fabrication. Along a 5 mm long grating, the waveguide width and thickness slowly change. So the beginning of the grating reflects one wavelength and the end reflects a slightly different one. The total grating acts like many short gratings in series, each tuned a little differently, and together they block a wider band. The centre wavelength also differs between the four devices because each sits at a different place on the chip.

```
 ideal long grating            real long grating
 one narrow stopband           many shifted stopbands add up
   ----\  /----                  ----\        /----
        \/                            \______/
                                      (wide, rippled)
```

### 11.1.1 Lithography process contours

> **In one sentence:** Lithography simulators can predict not just the "typical" printed shape but also its smallest and largest likely versions, so you can see in advance which designs are hard to manufacture.

**Computational lithography** (introduced in the book's Section 4.5.4) means simulating the printing process in a computer: you input your drawn mask layout, and it outputs the shape that will actually appear on the wafer, with rounded corners and blurred edges.

These models can do more than predict one shape. They can also produce **process contours**: outlines for the range of likely outcomes. Typically there are three:

- the **nominal** contour (what you get on a typical day),
- a **minimum** contour (e.g. under-exposure: features come out smaller),
- a **maximum** contour (e.g. over-exposure: features come out bigger).

These help in two ways:

1. **Spotting risky designs.** Some structures are very sensitive to small edge shifts, for example directional couplers with very small gaps (the gap might close) or **slot waveguides** (two silicon rails with a very narrow gap between them where light is concentrated). Seeing the contours tells you whether the design will survive.
2. **Realistic optical simulation.** You can export the simulated shapes and run optical simulations on them instead of on idealized rectangles (as in Section 4.5.4).

**Figure 11.2 — Simulated lithography contours of a Bragg grating.** Panel (a) shows a long stretch of grating; panel (b) zooms in on about 5 periods. Grey rectangular blocks are the drawn design: a waveguide with square "teeth" on its sides. Over them, three red lines show the simulated printed edges (nominal, min, max). The red lines are not square at all; they are smooth, wavy curves that follow the period of the teeth. Corners are rounded off, and narrow parts are pulled back. The lesson: **what you draw is not what you get.** A drawn square-tooth grating becomes a nearly sinusoidal wiggle, and its tooth size (and thus its strength) is smaller than drawn. The spread between the three red lines shows how much this varies with exposure.

> **Key takeaways:**
>
> - Lithography blurs shapes; corners round and small features shrink.
> - Simulators give nominal, minimum and maximum contours that show the likely range.
> - Use them to flag fragile designs (tiny gaps, slots) and to feed realistic shapes into optical simulations.

### 11.1.2 Corner analysis

> **In one sentence:** Corner analysis is a simple way to test a design against manufacturing variation by simulating it at the typical values and at the extreme ("corner") values of each process parameter.

#### The idea

Every fabrication step has a target and a spread. **Process corners** is a basic **design of experiments (DoE)** technique: instead of simulating every possible combination, you simulate a small, well-chosen set of combinations at the edges of the expected range. Usually the range is **±3σ**, which covers 99.7% of cases if the variation is Gaussian.

Example: the SOI layer is specified as **220 nm thick, with a ±10 nm 3σ variation**. So nearly all wafers will be between 210 and 230 nm.

Parameters that can vary include:

- **lithography line-width** (waveguide width),
- **etch depth**,
- **mask overlay** (misalignment between two masks),
- **doping concentration** (how many impurity atoms were added to make silicon conduct, used in modulators),
- **thickness of deposited layers** (e.g. oxide or metal).

You can also include operating conditions that are not part of fabrication: **temperature**, **voltage**, and other "stimulus and environmental" parameters.

#### Naming the corners

This method comes from electronic chip design. There, each parameter has three levels, named after their effect on transistor speed:

- **T** = typical (nominal),
- **S** = slow (one extreme),
- **F** = fast (the other extreme).

In photonics, think of S and F simply as "low end" and "high end" of a parameter.

With **two** parameters, there are 3 × 3 = 9 combinations:

| Type | Labels | Count | Meaning |
|---|---|---|---|
| Nominal | TT | 1 | both typical |
| Corners | SS, FF, SF, FS | 4 | both at an extreme |
| Edges | TS, TF, ST, FT | 4 | one typical, one extreme |

Read the table: the first letter is parameter 1's level, the second is parameter 2's. You run one simulation for each of the 9 and then look at all results together to see how sensitive the device is. The same idea extends to any number of parameters.

#### Example 1: strip waveguide (2 parameters)

Nominal: **500 nm × 220 nm**. Thickness varies 220 ± 10 nm; width varies 500 ± 10 nm. These define a square in the width–height plane, and the corners of the square are the extreme cases.

#### Example 2: rib waveguide (3 parameters)

Now three parameters vary, each by **±10 nm (3σ)**:

- waveguide width: **490, 500, 510 nm**,
- total height: **210, 220, 230 nm**,
- slab height: **80, 90, 100 nm**.

**Figure 11.3 — Process corners drawn as a box.** Panel (a) is a square with "width" (490–510) on the horizontal axis and "height" (210–230) on the vertical axis. A big purple dot in the centre marks the nominal design (500, 220). Four blue dots sit at the four corners of the square, and four red dots sit at the middle of each side (the "edges"). Panel (b) adds a third axis, "etch depth" (which sets the slab thickness, 80–100), turning the square into a cube. Blue dots sit at the cube's 8 corners, and red and orange dots sit at the middle of edges and faces. The box is the range of devices the process can produce; the dots are the cases you simulate. The lesson: **a few well-placed simulations stand in for the whole cloud of possible devices.**

```
 height
  230  o-----o-----o     o = simulated point
       |           |     centre = nominal (500, 220)
  220  o     O     o     corners = SS, SF, FS, FF
       |           |     side midpoints = edges
  210  o-----o-----o
      490   500   510   width
```

**Figure 11.4 — Effective index and group index at all corners for the rib waveguide.** Two plots, both with wavelength from 1500 to 1580 nm on the horizontal axis. Each line is one corner simulation.

- Panel (a), **effective index**: all lines slope gently downward (the index falls as wavelength rises; this is dispersion). The top line goes from about 2.655 at 1500 nm to 2.595 at 1580 nm; the bottom line from about 2.560 to 2.490. So at any one wavelength the corners differ in $n_{eff}$ by roughly 0.1.
- Panel (b), **group index**: again parallel downward-sloping lines, from about 3.95→3.92 (top) to 3.855→3.81 (bottom). The spread is about 0.14.

How big is a 0.1 change in $n_{eff}$? For a ring, the resonance shifts roughly in proportion: $\Delta\lambda/\lambda \approx \Delta n_{eff}/n_g$. With $\Delta n_{eff} = 0.1$ and $n_g \approx 3.9$, $\Delta\lambda \approx 1550 \times 0.1/3.9 \approx 40$ nm. That is huge compared with a ring's FSR of a few nm. (This is a rough estimate to show scale, not a number from the book.) The lesson from the figure: **fabrication tolerances shift the absolute index a lot, but the slope (dispersion) is almost the same for every corner.**

#### Caveats and comparison with experiment

In a rib waveguide, the slab height is not independent. It equals the original SOI thickness minus the etch depth. So if the SOI layer is thicker, *both* the rib height and the slab get thicker. The two are **partially correlated**. A careful analysis could include this correlation. Treating them as independent, as done here, includes combinations that cannot really occur together (e.g. thick rib with thin slab from the same thick SOI), so it gives a **worst-case** prediction: the real spread is probably smaller.

The book compares Figure 11.4b with measured group indices in its Figure 3.21b (from an earlier chapter): the measurements fall inside the predicted range. So the corner analysis is a trustworthy envelope.

#### How many simulations?

With $N$ parameters, each at 3 levels, the full set is

$$\text{number of simulations} = 3^{N}$$

For $N = 3$: $3^3 = 27$ simulations (this is what Figure 11.4 used). This grows fast: $N = 6$ would need 729.

A cheaper option keeps only the nominal case and the true corners (every parameter at an extreme, no "edge" cases):

$$\text{number of simulations} = 2^{N} + 1$$

The $2^N$ counts the corners (each parameter is either S or F), and the $+1$ is the nominal. For $N = 3$: $2^3 + 1 = 9$, namely TTT, SSS, SSF, SFS, SFF, FSS, FSF, FFS, FFF. That is a third of the work. The assumption is that the worst cases are at the corners, which is usually true when the response changes smoothly in one direction with each parameter.

> **Key takeaways:**
>
> - Corner analysis simulates the nominal design plus the extreme combinations of each process parameter (usually ±3σ).
> - Full analysis needs $3^N$ runs; the reduced version needs $2^N + 1$.
> - For the rib waveguide, ±10 nm errors shift $n_{eff}$ by about 0.1 and $n_g$ by about 0.14, while the dispersion slope barely changes.
> - Ignoring correlations gives a worst-case (pessimistic) envelope; measurements fall inside it.
> - Corner analysis treats each device alone; it says nothing about how *neighbouring* devices compare. That is the next section.

### 11.1.3 On-chip non-uniformity, experimental results

> **In one sentence:** Measuring 371 identical ring resonators on one chip shows that the wavelength mismatch between two devices grows roughly in proportion to the distance between them, so devices that must match should be placed close together.

(The book notes that a version of this section was published as a 2014 OFC conference paper by Chrostowski, Wang, Flueckiger, Wu, Wang and Talebi Fard, "Impact of fabrication non-uniformity on chip-scale silicon photonic integrated circuits".)

#### Why distance matters

Corner analysis (11.1.2) looks at one isolated device and asks "how far could it be from nominal?". That answers the question for **absolute** variation: wafer-to-wafer and batch-to-batch. But on one chip, neighbouring devices are built from the same patch of silicon at the same moment, so their errors are **correlated**: if one is 3 nm too thick, its neighbour probably is too. Their *difference* is then much smaller than the corner analysis would suggest. This section measures that effect. The practical message: **if components must match, make the layout compact.** That reduces (but does not eliminate) the cost of trimming.

#### The experiment

- **371 identical racetrack resonators** on a **16 mm × 9 mm** chip, made by the **IME A\*STAR** foundry (Singapore). The chip came from near the centre of the wafer.
- Each test cell (Figure 11.5) contains:
  - two fibre grating couplers designed for **1550 nm, quasi-TE** light ("quasi" because in a real waveguide the field is mostly, not perfectly, horizontal);
  - **220 nm × 500 nm** SOI strip waveguides;
  - a TE racetrack resonator with **12 µm radius**;
  - a directional coupler **4.5 µm long** with a **200 nm gap**.
- Devices were between **60 µm and 18 mm** apart.
- Every resonator was compared with every other one: $\text{(371 choose 2)} = \frac{371 \times 370}{2} = 68\,635$ pairs.
- More than **1300** of those pairs were less than **200 µm** apart, enough to get good statistics on close neighbours.

**Figure 11.5 — Test cell layout, and how far apart the devices are.** The main picture is the mask layout: a racetrack ring at the top, coupled to a straight bus waveguide below it, which runs left and right to two grating couplers (fan-shaped patches filled with fine lines). The two couplers are **127 µm** apart. That is the standard spacing (pitch) of fibres in a **fibre array**, a block holding several fibres side by side; matching it lets one fibre array connect to both couplers at once, so a machine can test hundreds of devices automatically. The inset is a histogram: horizontal axis is the distance between two resonators (0 to about 18 mm), vertical axis is how many pairs have that distance (up to 3000). The counts are spread fairly evenly from 0 to about 10 mm (bumpy, between about 1100 and 2400), peak at about 3000 around 12.5 mm, then fall to near zero at 18 mm. The lesson: **the data set covers all distances, from very close to across the whole chip**, so we can study mismatch as a function of distance.

#### Measurement details

**Figure 11.6 — A typical measured spectrum.** Horizontal axis: wavelength, 1.495 to 1.595 µm. Vertical axis: transmitted power, about −10 to −35 dB. The overall shape is a broad hill peaking near 1.552 µm at about −11 dB. This hill is the combined response of the two grating couplers (each passes light best near its central wavelength). On top of the hill are about 13 sharp downward spikes, each marked with a red circle: these are the ring resonances. Neighbouring spikes are about **7 nm** apart (the FSR). The lesson: **from one sweep you can read both the coupler's central wavelength and insertion loss (the hill) and the ring's resonance wavelengths (the dips).**

Measurement facts and what they mean:

- Spectra were sampled every **10 pm** (0.01 nm) for speed. So no wavelength in this study is known better than 10 pm. Coarse sampling also means the very bottom of narrow dips can be missed, so the measured dip depth (**extinction ratio**) is underestimated; this does not matter here.
- **Q** was typically **10 000–30 000**, so dips were about 0.05–0.15 nm wide, wide enough to be caught with 10 pm sampling.
- Fibre-to-fibre **insertion loss** (total loss from the input fibre to the output fibre) was about **11 dB**. This is rather high because the fibres were held relatively far above the chip, to avoid crashing into it during automated testing.
- A **peak-finding algorithm** (a program that locates the minima) found the resonances.

#### Ring resonators: sorting out which dip is which

A problem appeared: the wavelength variation across the chip (up to about 10 nm) was **larger than the FSR (7 nm)**. Since the spectrum repeats every FSR, you cannot just look at a dip at 1550 nm on one ring and a dip at 1551 nm on another and say "this ring is 1 nm off". The second ring's dip might actually be a different mode (a different $m$) that has been shifted by almost a whole FSR. It is like two clocks that you can only read modulo one hour. The authors solved this in three steps.

**Step 1: compute the group index of each ring from its FSR.**

$$\mathrm{FSR} = \frac{c}{n_{g} L} \qquad (11.1)$$

- $\mathrm{FSR}$ here is the spacing between resonances **in frequency** (Hz).
- $c$ is the speed of light in vacuum.
- $n_g$ is the group index of the ring's waveguide.
- $L$ is the round-trip length of the ring.

Why this shape? Light takes time $n_g L / c$ to go round once. Resonances occur at frequencies where a whole number of cycles fits in one round trip, so neighbouring resonances are separated by one over the round-trip time. Group index (not effective index) appears because moving from one resonance to the next changes both the wavelength *and* $n_{eff}$, and $n_g$ accounts for both. In wavelength units the same law reads $\Delta\lambda_{FSR} = \lambda^2/(n_g L)$.

Worked example: the round trip of this racetrack is about two half-circles of radius 12 µm plus two straight 4.5 µm sections: $L \approx 2\pi(12) + 2(4.5) \approx 84$ µm. With FSR ≈ 7 nm at 1550 nm, $n_g \approx \lambda^2/(\mathrm{FSR}\cdot L) = (1.55\ \mu\text{m})^2/(0.007\ \mu\text{m} \times 84\ \mu\text{m}) \approx 4.1$, a typical value for a 500 × 220 nm silicon wire. (This is our own check using numbers in the text.) Since $L$ is known exactly from the mask, measuring the FSR gives $n_g$ for every ring.

**Step 2: plot $n_g$ against resonance wavelength for every dip of every ring.**

**Figure 11.7 — Group index versus resonance wavelength, 15 modes, 371 rings.** Horizontal axis: resonance wavelength, about 1.46 to 1.58 µm. Vertical axis: extracted group index (the tick labels are printed in shortened form, ".205" to ".25", so exact values can't be read). The thousands of points do not form a shapeless cloud. They group into about 15 separate clusters, one per mode number $m$. Within each cluster, the points line up along a **downward-sloping diagonal line**: rings whose resonance sits at a longer wavelength have a slightly lower group index. A thick black line is drawn through one cluster (around 1.528 µm), and the points belonging to it are circled.

Why do the points line up? Two facts combine:

- (a) The resonance wavelength depends on $n_{eff}$: $m\lambda_m = n_{eff}(\lambda_m)\,L$. A ring with a fatter waveguide has higher $n_{eff}$, so its mode-$m$ resonance moves to a longer wavelength.
- (b) The same geometry change that alters $n_{eff}$ *also* alters $n_g$, in a consistent way.

So one physical cause (geometry) moves both quantities together, and every ring's mode $m$ lands on the same line. Different $m$ give different, parallel lines. The lesson: **$n_g$ acts as a fingerprint that tells you which mode a dip belongs to, even when the shifts exceed one FSR.**

**Step 3: pick one mode.** Choose a line (as drawn in Figure 11.7) and select, for each ring, the data point closest to it. Now you have the same mode $m$ for all 371 rings, and you can compare their wavelengths directly.

#### Results: a map of the chip

The largest spread of resonance wavelength across the chip is about **10 nm**.

**Figure 11.8 — Map of resonance wavelength deviation across the chip.** The horizontal axis is position x (0 to about 15.5 mm), the vertical axis is position y (0 to 9 mm). The grey shading shows how far each spot's resonance is from the chip average (the "0" contour is the mean). The scale runs from about −2 nm (dark) to +4 nm (light). Small blue dots mark the actual ring locations; they are not evenly spread but sit in lines and clusters wherever space was free on the layout. The map is darker (shorter wavelength, about −1 to −2 nm) at the bottom-left and along the bottom edge, lighter (up to +4 nm) at the upper-left and in patches at the upper-right, and medium (0 to +2 nm) across the middle. The lesson: **the wavelength changes smoothly with position, like a landscape with gentle hills**, which is exactly what you expect if the silicon thickness varies smoothly across the wafer.

#### Results: mismatch versus distance

For each of the 68 635 pairs, the authors computed the difference in resonance wavelength and plotted it against the distance between the two rings.

**Figure 11.9 — Wavelength mismatch versus distance, all 68 635 pairs.** Horizontal axis: distance between the two rings (0 to 18 mm). Vertical axis: wavelength mismatch (0 to 9 nm). The purple dots form a fan or cone: tight near zero distance, spreading upward as distance increases. Box plots summarize each distance bin (1 mm bins up to 6 mm, then 6–9, 9–12, 12–15, 15–18 mm). In these box plots, the box covers the middle 50% of the pairs, the circle inside is the median, the whiskers reach up to 1.5 times the box height (but not beyond the data), red "+" marks are outliers, and notches show the 95% confidence interval of the median. Approximate readings:

| Distance bin (mm) | Median mismatch (nm) | Middle 50% (nm) |
|---|---|---|
| 0–1 | ~0.5 | ~0.3–0.7 |
| 1–2 | ~0.7 | ~0.5–1.0 |
| 2–3 | ~0.9 | ~0.6–1.4 |
| 3–4 | ~1.2 | ~0.8–1.9 |
| 4–5 | ~1.6 | ~1.0–2.4 |
| 5–6 | ~1.7 | ~1.0–2.5 |
| 6–9 | ~1.8 | ~0.9–2.7 |
| 9–12 | ~1.4 | ~0.8–2.6 |
| 12–15 | ~3.4 | ~2.2–4.2 |
| 15–18 | ~3.9 | ~3.0–5.2 |

Read down the table: typical mismatch and its spread both grow with distance, steadily up to about 5–6 mm, then less regularly. The lesson: **the worst-case mismatch between two rings grows roughly linearly with their distance.** For example, rings **1 mm** apart differ by at most **2–3 nm**; rings **4 mm** apart by up to **5 nm**.

**Figure 11.10 — Probability distributions of the mismatch for each distance range.** Horizontal axis: wavelength mismatch, 0 to 8 nm. Vertical axis: probability density on a logarithmic scale ($10^{-3}$ to above $10^{-1}$). Six curves, one per distance bin (0–1, 1–2, 2–3, 3–4, 4–5, 5–6 mm). Each curve rises to a peak at small mismatch and then falls. Moving from the 0–1 mm curve to the 5–6 mm curve:

- the peak moves right (from ~0.4 nm to ~1.0 nm) and gets lower (from ~0.4 to ~0.2),
- the tail reaches further out: the density drops to $10^{-2}$ at about 1.8 nm for 0–1 mm, but only at about 4.8 nm for 5–6 mm.

The lesson: **the further apart two rings are, the wider the range of mismatches you should expect.**

Two notable features of these distributions:

- They are **not Gaussian** (not bell-shaped). You can see this from the many outliers in the box plots and from the shape of the curves. So you cannot simply quote "mean ± σ" and trust the bell-curve rules.
- Curiously, for big enough distance ranges (e.g. 4–5 mm) the distribution becomes nearly **uniform** (every mismatch up to some value about equally likely) with a sharp maximum cutoff.

For distances of **6 mm or more**, the data show "**bunching**" (clumps). This is probably an artefact of where the rings were placed: not at random positions, but squeezed in wherever there was room on a crowded layout, and with limited samples.

The data also show that **no two rings on the chip differ by more than about 9 nm**. Beyond about 6 mm separation, the mismatch stops growing and **saturates** at the "uncorrelated" worst case: the two devices are so far apart that their errors are effectively independent, so being even further apart makes no difference.

#### A formula for the typical mismatch

**Figure 11.11 — Zoom on 0–3 mm with 100 µm bins.** Horizontal axis: distance 0 to 3 mm. Vertical axis: wavelength mismatch, 0 to 4 nm. Purple dots are pairs, red "+" are outliers (up to about 4 nm near 3 mm). Box plots every 100 µm show the median rising from about 0.35 nm (near 0 mm) to about 0.6 nm (1.5 mm) to about 1.0 nm (3 mm), with boxes and whiskers widening (upper whisker reaches about 3.7 nm at 3 mm). A black straight line (the fit below) goes from about 0.35 nm at 0 mm to about 0.95 nm at 3 mm. A cyan line with circles tracks the bin medians and wiggles around the black line. The lesson: **at short range the median mismatch grows linearly with distance**, which means fabrication errors are correlated over short distances.

The median increases linearly up to about 5 mm. The straight-line fit at short distances is:

$$\bar{\lambda}_{ring} = 0.20\ \mathrm{nm/mm} \cdot d + 0.37\ \mathrm{nm} \qquad (11.2)$$

- $\bar{\lambda}_{ring}$ is the expected (median/average) wavelength mismatch between two rings.
- $d$ is their distance in mm.
- $0.20$ nm/mm is the slope: each extra millimetre of separation adds 0.2 nm of typical mismatch.
- $0.37$ nm is the intercept: the mismatch you get even for rings right next to each other.

Check against the figure: at $d = 3$ mm, $0.20 \times 3 + 0.37 = 0.97$ nm, matching the black line's end point.

What does the intercept mean? Even two neighbouring rings, built side by side, differ by 0.37 nm on average. This is **intrinsic**, very local variation (for example, random roughness or tiny local width differences), which no amount of compact layout can remove.

How much heater power does that cost? Follow the chain:

1. Mismatch as a fraction of the FSR: $0.37\ \text{nm} / 7\ \text{nm} \approx 0.053$ FSR.
2. One FSR corresponds to a phase change of $2\pi$ around the ring. So $0.053 \times 2\pi \approx 0.1\pi$. That is the "intrinsic variation of ~0.1π".
3. With a heater efficiency of **0.8 mW per FSR**, the power to fix it is $0.053 \times 0.8\ \text{mW} \approx 0.04$ mW.

So on average **about 0.04 mW per pair** of neighbouring rings that must be matched. That is small. This number helps predict tuning power for circuits like a **two-ring Vernier filter** (two rings with slightly different FSRs used together, which must be aligned to each other). But for rings on **opposite sides of the chip**, the worst case is a full FSR of tuning (0.8 mW per ring here), about 20 times more, because their mismatch can be as large as the FSR or larger.

#### Grating couplers

The same method was applied to the grating couplers, using the "hill" in each spectrum. In Figure 11.6 the coupler's peak wavelength is $\lambda_{FGC} = 1.555$ µm and the insertion loss is about 11 dB for the two couplers together.

**Figure 11.12 — Map of grating coupler central-wavelength deviation.** Same chip axes as Figure 11.8 (x 0–15.5 mm, y 0–9 mm). Grey shading shows deviation from the mean coupler wavelength, about ±2 nm. Blue dots mark measured coupler locations: a dense column along the left edge, clusters near the top centre and middle-right, and sparse points along the right edge. The lesson: **coupler wavelengths also vary smoothly with position, but by a smaller amount (about ±2 nm) and with a different pattern from the rings.**

**Figure 11.13 — Coupler wavelength mismatch versus distance.** Like Figure 11.9 but for coupler pairs: distance 0 to ~16 mm on the horizontal axis, mismatch 0 to 9 nm on the vertical axis. Purple dots fan out with distance; red "+" outliers stand at each distance from about 4.5 nm to over 9 nm. Box medians rise slowly from about 0.7 nm (1 mm) to about 1.9 nm (15 mm); boxes widen (about 0.5–1.8 nm at 1 mm to 0.8–2.4 nm at 15 mm). A black line fitted over 1–5 mm rises from about 0.8 nm to 1.2 nm. The lesson: **coupler mismatch also grows with distance, but more gently than for rings.**

The fit for the couplers, valid from 0 to 5 mm, is:

$$\bar{\lambda}_{FGC} = 0.10\ \mathrm{nm/mm} \cdot d + 0.80\ \mathrm{nm} \qquad (11.3)$$

Compare with the ring formula (11.2): the coupler slope is half as large (0.10 vs 0.20 nm/mm), but the intercept is about twice as large (0.80 vs 0.37 nm). So neighbouring couplers differ more than neighbouring rings, but the difference grows more slowly with distance.

Because rings and couplers vary with different spatial patterns and statistics, their variations probably have **different physical causes**. Both are sensitive to SOI thickness, but grating couplers are also very sensitive to **etch depth** (their teeth are only partly etched), whereas the strip-waveguide rings are fully etched and so do not depend on etch depth. Simulations (**FDTD**, finite-difference time-domain, a method that solves the equations of light step by step on a grid) give these sensitivities of the coupler's central wavelength:

| Parameter | Sensitivity | Meaning |
|---|---|---|
| SOI thickness | 1.82 nm/nm | 1 nm thicker silicon moves the peak by 1.82 nm |
| Etch depth | 1.9 nm/nm | 1 nm deeper etch moves the peak by 1.9 nm |
| Grating finger width | 0.215 nm/nm | 1 nm wider teeth move the peak by only 0.2 nm |

Read the table: thickness and etch depth matter about nine times more than tooth width. Example: a ±5 nm thickness error alone would move the coupler peak by about ±9 nm.

**Figure 11.14 — Coupler insertion loss.** Panel (a): insertion loss of every measured coupler, plotted against its measurement file number (0 to about 400). Most values sit between about −10 and −10.5 dB. Two green lines mark the ±3σ limits at **−8.2 dB** and **−12.2 dB**. A few points, circled in red, fall below −12.2 dB, some as low as about −17 dB: these are outliers ("dropouts"), likely defective devices. Panel (b): map of insertion-loss deviation across the chip (x 0–16 mm, y 0–9 mm), scale from −1 dB to +0.5 dB. Most of the chip is near 0 dB, but the loss gets worse (down to about −1 dB) toward the bottom-right corner. The lesson: **coupler loss is mostly uniform, with a few bad devices and a smooth, systematic degradation toward one corner.**

#### What to do with these results

- **System power budgets.** You can estimate the power needed to trim large arrays of micro-ring resonators or **Mach–Zehnder switches** (interferometer-based switches that also need phase matching).
- **Layout rule.** Devices that must be wavelength-matched should be placed as close together as possible. For example, in a transmitter made of ring modulators and ring filters (the book's Section 13.1), put the rings next to each other so their wavelengths match and little tuning energy is needed.
- **Process monitoring and improvement.** Foundries can use these variability numbers to track and improve their process.
- **Choosing and sorting chips.** You can pick the best chips for experiments, and **bin** chips (sort them into grades) before packaging based on expected performance.

> **Key takeaways:**
>
> - Silicon thickness is the dominant source of variation (about ±5 nm), followed by width; a few nm of geometry error shifts wavelengths by several nm.
> - Corner analysis ($3^N$ or $2^N + 1$ simulations) predicts the absolute (worst-case) spread for a single device.
> - On one chip, errors are spatially correlated: ring mismatch ≈ $0.20\,\text{nm/mm}\cdot d + 0.37$ nm, saturating at a worst case of about 9–10 nm beyond ~6 mm.
> - Even adjacent rings differ by ~0.37 nm (≈ 0.04 mW of heater power per pair); far-apart rings may need a full FSR of tuning.
> - Grating couplers vary differently (0.10 nm/mm · d + 0.80 nm), mostly due to thickness and etch depth. Lesson: keep matched devices close together.

---

## 3.2.11 Waveguide loss

> **In one sentence:** Light gets weaker as it travels along a silicon waveguide for several reasons, mostly scattering from rough sidewalls, and the loss can be quoted in dB/cm, as an attenuation coefficient in 1/m, or as the imaginary part of a complex refractive index.

### Where the loss comes from

**Propagation loss** is the fraction of power lost per unit length. For silicon waveguides there are five main contributions:

1. **Absorption by nearby metal.** Metals absorb light strongly. If part of the mode's field reaches a metal layer (for example a heater or wire above the waveguide), power is soaked up. Measured example: a 500 × 220 nm strip waveguide with metal **600 nm above** it had an *extra* loss of **1.8 ± 0.2 dB/cm**. That is as large as the normal loss of the waveguide itself, so metal must be kept far enough away.

2. **Sidewall scattering.** Etching leaves the side walls slightly rough, with bumps a few nm high. Each bump scatters a little light out of the waveguide, like a smudge on a window. For 500 × 220 nm waveguides this typically costs **2–3 dB/cm**, and it is usually the dominant loss. The roughness can be measured with an **atomic force microscope (AFM)**, a tool that scans a tiny sharp tip over the surface to map its height. One study measured **2.8 nm rms** roughness (rms = root-mean-square, a kind of average size of the bumps). Once the roughness is known, the loss can be simulated. Why do narrow silicon waveguides suffer so much? Their high index contrast squeezes the light hard against the walls, so the field at the rough surface is strong.

3. **Material loss.** Pure silicon barely absorbs light at 1550 nm (the photons don't have enough energy to excite electrons across silicon's band gap). So for **passive** (undoped) devices, material absorption is negligible. It becomes significant in **doped** silicon, where free electrons and holes absorb light (covered in the book's Section 6.1.1, on modulators).

4. **Surface-state absorption.** At an untreated silicon surface, the crystal stops abruptly and leaves "dangling" chemical bonds. These create electronic states that can absorb light. Covering the surface properly (**passivation**, e.g. growing or depositing oxide) removes most of them. The effect is real enough that unpassivated waveguides have been deliberately used to build light **detectors**.

5. **Reflections and phase noise from roughness.** Sidewall roughness does not only throw light out. It also reflects a little light backward along the waveguide and adds small random phase changes that depend on wavelength. These can cause unwanted ripples in the spectra of devices (compare the ripples seen in the long gratings of Figure 11.1).

### Reducing loss: go wider

Making the waveguide **wider** reduces loss, because less of the light touches the rough sidewalls. Example: **0.27 dB/cm** was reported in **2 µm wide, 250 nm high rib waveguides**, about ten times better than a 500 nm strip. The catch: wide waveguides are **multi-mode**. If light accidentally gets into the higher modes, signals get distorted. So you connect them to normal single-mode waveguides through **gradual tapers** (slow, smooth changes of width), which keep the light in the fundamental mode. Such wide low-loss waveguides suit **long routes**, e.g. **global routing** across the chip, while narrow waveguides are used inside compact devices and bends.

```
 single-mode      taper          wide, low-loss route        taper
 ==========>=====/                                 \=====>==========
  500 nm         \_____________ 2 um _______________/
```

### Converting between loss units

Loss is usually quoted in **dB/cm**, but physics equations and simulators often want other forms.

**(1) Attenuation coefficient in 1/m.** If power decays exponentially along the waveguide,

$$P(z) = P_0\, e^{-\alpha z},$$

then $\alpha$ (in m$^{-1}$) is the **attenuation (absorption) coefficient**. The relation to the dB version is:

$$\alpha\,[\mathrm{m}^{-1}] = \frac{\alpha\,[\mathrm{dB/m}]}{10\log_{10}(e)} = \frac{\alpha\,[\mathrm{dB/m}]}{4.34} \qquad (3.9\mathrm{a})$$

Where does 4.34 come from? Converting $e^{-\alpha z}$ to dB gives $10\log_{10}(e^{-\alpha z}) = -\alpha z \cdot 10\log_{10}(e) = -4.34\,\alpha z$. So the loss in dB is 4.34 times the exponent. Divide by 4.34 to go back.

Worked example: 3 dB/cm = 300 dB/m. Then $\alpha = 300/4.34 \approx 69\ \text{m}^{-1}$. Check: after 1 cm, $e^{-69 \times 0.01} = e^{-0.69} \approx 0.5$, half the power, which is indeed −3 dB.

**(2) Imaginary part of the refractive index.** A lossy material can be described by a **complex refractive index** $n + ik$. The real part $n$ sets the speed of light, as before. The imaginary part $k$ (the **extinction coefficient**) makes the wave's amplitude shrink as it travels. The conversion is:

$$k = \frac{\lambda \cdot \alpha\,[\mathrm{dB/m}]}{4\pi \cdot 4.34} \qquad (3.9\mathrm{b})$$

- $\lambda$ is the free-space wavelength (in m),
- $\alpha\,[\mathrm{dB/m}]/4.34$ is just $\alpha$ in 1/m from (3.9a),
- $4\pi$ comes from the physics: the field decays as $e^{-2\pi k z/\lambda}$, so the power (field squared) decays as $e^{-4\pi k z/\lambda}$. Matching this to $e^{-\alpha z}$ gives $\alpha = 4\pi k/\lambda$, i.e. $k = \lambda\alpha/(4\pi)$.

Worked example: 3 dB/cm at $\lambda = 1.55$ µm: $k = (1.55\times10^{-6} \times 300)/(4\pi \times 4.34) \approx 8.5 \times 10^{-6}$. This is tiny compared with $n \approx 3.5$, which tells you that per wavelength the loss is minute; it only adds up over thousands of wavelengths (centimetres). This form is handy because many simulation tools take loss as an imaginary index.

> **Key takeaways:**
>
> - Typical 500 × 220 nm strip waveguides lose 2–3 dB/cm, mainly from sidewall roughness scattering.
> - Metal too close (e.g. 600 nm above) adds about 1.8 dB/cm; doping and unpassivated surfaces also add absorption.
> - Wider waveguides (e.g. 2 µm rib: 0.27 dB/cm) cut loss but are multi-mode, so use tapers; good for long on-chip routes.
> - Convert units with $\alpha[\text{m}^{-1}] = \alpha[\text{dB/m}]/4.34$ and $k = \lambda\alpha/(4\pi)$.

---

## Glossary

| Term | Plain meaning |
|---|---|
| A\*STAR / IME | A Singapore research foundry that fabricated the test chip |
| Atomic force microscope (AFM) | Instrument that maps surface height by scanning a tiny tip over it |
| Attenuation coefficient ($\alpha$) | Rate at which power decays: $P = P_0 e^{-\alpha z}$, in 1/m |
| Azimuthal mode number ($m$) | Number of wavelengths that fit around a ring at resonance |
| Batch-to-batch variation | Differences between separate production runs |
| Binning (chips) | Sorting chips into grades based on measured or expected performance |
| Box plot | Chart showing median, middle 50% (box), spread (whiskers) and outliers |
| Bragg grating | Waveguide with periodic wiggles that reflects a band of wavelengths |
| Bus waveguide | Straight waveguide that carries light past a ring |
| Central (peak) wavelength | The wavelength at which a device works best or resonates |
| Cladding | Material surrounding a waveguide core (oxide or air) |
| Complex refractive index ($n + ik$) | Index whose imaginary part $k$ describes loss |
| Computational lithography | Computer simulation of how the drawn pattern will print on the wafer |
| Corner analysis (process corners) | Simulating a design at typical and extreme values of each process parameter |
| Correlation | Tendency of two quantities to change together |
| Corrugation width ($\Delta W$) | How much the width of a grating waveguide wiggles |
| CROW | Coupled-resonator optical waveguide: a chain of coupled rings |
| Decibel (dB) | Logarithmic unit for power ratios: $10\log_{10}(P_{out}/P_{in})$ |
| Design of experiments (DoE) | Planned choice of test cases to learn the most with few runs |
| Die / chip | One rectangular piece cut from a wafer |
| Directional coupler | Two waveguides close together so light transfers between them |
| Dispersion | Change of index with wavelength |
| Doping | Adding impurity atoms to silicon to make it conduct |
| Effective index ($n_{eff}$) | Average index the mode "feels"; sets phase speed in a waveguide |
| Etch depth | How deep the silicon is cut during etching |
| Extinction coefficient ($k$) | Imaginary part of the refractive index; measures absorption |
| Extinction ratio | Depth of a dip in a spectrum |
| FDTD | Finite-difference time-domain: grid-based simulation of light |
| Fibre array | Block holding several optical fibres at a fixed spacing (e.g. 127 µm) |
| Foundry | Factory that manufactures chips for designers |
| Free spectral range (FSR) | Spacing between neighbouring resonances of a resonator |
| Gaussian (normal) distribution | Bell-shaped distribution; 99.7% within ±3σ |
| Grating coupler (GC, FGC) | Etched patch that couples light between chip and fibre |
| Group index ($n_g$) | Index that sets the speed of pulses/information: speed $= c/n_g$ |
| Heater efficiency | Electrical power needed to shift a resonance, e.g. mW per FSR |
| Insertion loss | Total power lost passing through a device or path, in dB |
| Interquartile range | Range containing the middle 50% of data |
| Lithography | Printing a pattern onto the wafer using light and a mask |
| Mach–Zehnder switch | Switch that splits light into two arms and recombines it |
| Mask overlay | Alignment error between two lithography masks |
| Median | Middle value of sorted data |
| Mode | Stable field pattern that travels along a waveguide unchanged |
| Multi-mode | Supporting more than one mode |
| Nominal | The intended, design-target value |
| Outlier | Data point far outside the usual range |
| Passivation | Treating a surface (e.g. with oxide) to remove absorbing defects |
| Polarization (TE/TM) | Direction of the electric field: mostly horizontal (TE) or vertical (TM) |
| Probability distribution function (p.d.f.) | Curve showing how likely each value is |
| Process contours | Simulated nominal, minimum and maximum printed outlines |
| Propagation constant | Rate of phase advance along a waveguide, $2\pi n_{eff}/\lambda$ |
| Propagation loss | Power lost per length of waveguide, e.g. dB/cm |
| Quality factor (Q) | Sharpness of a resonance: wavelength divided by dip width |
| Quasi-TE | Mostly (not perfectly) TE-polarized mode |
| Racetrack resonator | Ring stretched with straight sections |
| Refractive index ($n$) | How much slower light travels in a material than in vacuum |
| Rib waveguide | Partly etched waveguide: a ridge on a thin silicon slab |
| Ring resonator | Looped waveguide that traps light at certain wavelengths |
| rms roughness | Root-mean-square (typical) height of surface bumps |
| Sidewall scattering | Loss caused by rough waveguide walls throwing light out |
| Single-mode | Supporting only one mode |
| Slab | Thin layer of silicon left beside a rib waveguide |
| Slot waveguide | Two silicon rails with a narrow gap that holds the light |
| SOI | Silicon-on-insulator: thin silicon on oxide on a silicon base |
| Standard deviation ($\sigma$) | Measure of spread of a set of values |
| Stopband | Wavelength band that a Bragg grating reflects |
| Strip waveguide | Fully etched rectangular silicon waveguide (e.g. 500 × 220 nm) |
| Taper | Gradual change in waveguide width |
| Thermal tuning | Heating a device to shift its wavelength |
| Trimming | Correcting a device's wavelength after fabrication |
| TT / SS / FF etc. | Corner labels: typical, slow (low), fast (high) for each parameter |
| Vernier filter | Two rings with slightly different FSRs used together |
| Wafer | Round disc of material on which many chips are made |
| Wavelength ($\lambda$) | Distance between crests of a wave |
| WDM | Wavelength division multiplexing: many channels on different wavelengths |

---

## Check yourself

1. **Which fabrication parameter causes the largest device variation, and which comes second?**

   *Answer:* Silicon (SOI) thickness variation is the largest; lithography (waveguide width) variation is second. Zortman et al. found ±1000 GHz from thickness versus ±200 GHz from width.

2. **Theory says a longer Bragg grating should have the same or narrower bandwidth. Why did the measured gratings in Figure 11.1 get *wider* stopbands as they got longer?**

   *Answer:* Along a long grating the waveguide's width and thickness drift, so different parts reflect slightly different wavelengths. Added together, they block a broader band. The centre wavelength also differs between devices.

3. **You have 4 process parameters. How many simulations does a full corner analysis need, and how many does the reduced version need?**

   *Answer:* Full: $3^4 = 81$. Reduced (nominal plus corners): $2^4 + 1 = 17$.

4. **Why does treating rib height and slab height as independent give a worst-case result?**

   *Answer:* Both depend on the same SOI thickness, so they are partly correlated. Treating them as independent includes combinations that can't really happen together, which exaggerates the spread.

5. **Why couldn't the authors directly compare resonance wavelengths between rings, and how did they solve it?**

   *Answer:* The chip-wide variation (~10 nm) was larger than the FSR (7 nm), so they couldn't tell which dip was which mode. They computed $n_g$ from each ring's FSR ($\mathrm{FSR} = c/(n_g L)$), plotted $n_g$ against wavelength, saw each mode forming its own line, and picked the points on one line.

6. **Using Equation (11.2), what is the expected mismatch between two rings 2 mm apart?**

   *Answer:* $0.20 \times 2 + 0.37 = 0.77$ nm.

7. **Show how the book gets about 0.04 mW of heater power per pair of neighbouring rings.**

   *Answer:* Intercept mismatch 0.37 nm ÷ FSR 7 nm ≈ 0.053 FSR. Times 0.8 mW/FSR ≈ 0.04 mW.

8. **Why do grating couplers and rings show different variation patterns across the chip?**

   *Answer:* They respond to different physical causes. Both depend on SOI thickness, but grating couplers also depend strongly on etch depth (1.9 nm/nm), which does not affect the fully etched rings.

9. **What layout rule follows from this whole section?**

   *Answer:* Place devices that must be wavelength-matched as close together as possible, to reduce mismatch and therefore tuning power.

10. **A waveguide has 2 dB/cm loss. Express it as $\alpha$ in 1/m, and say what limits loss in narrow strip waveguides.**

    *Answer:* 2 dB/cm = 200 dB/m, so $\alpha = 200/4.34 \approx 46\ \text{m}^{-1}$. In 500 × 220 nm strips, sidewall roughness scattering (typically 2–3 dB/cm) dominates; wider waveguides reduce it.
