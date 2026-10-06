# Week 3 · Day 3 — Wednesday 7 Oct 2026

*Simple-English study version of Chrostowski & Hochberg §6.5 (Active tuning), §6.6 (Thermo-optic switch) and §3.1.1 (Silicon: wavelength and temperature dependence of its refractive index).*

[:material-file-pdf-box: Download this day as PDF](day-03-wed-7-oct-2026.pdf){ .md-button }

## Before you start: the big picture

A silicon photonic chip guides light through tiny "wires" made of silicon, called waveguides. Many useful devices on such a chip work by **interference**: light is split into two paths and then recombined. Whether the two parts add up (bright output) or cancel (dark output) depends on how far "ahead" one part is compared with the other. This "ahead-ness" is called the **phase**.

The problem: once a chip is made, its shape is fixed. Tiny manufacturing errors shift the phase in ways nobody planned. And for a switch, we *want* to change the phase on command. So we need a knob that changes the phase with an electrical signal. That knob is called a **phase shifter**, and making it is called **active tuning**.

Think of two runners on two tracks who must arrive at the finish line at the same moment. If you can't change the length of the tracks, you can still slow one runner down a little by making their track a bit "muddier". In a waveguide, "mud" means a higher refractive index: light moves more slowly. This packet shows two ways to add "mud" electrically: (1) pump electric charges into the silicon (the **PIN phase shifter**), and (2) heat the silicon (the **thermal phase shifter**). It then shows how a heater turns an interferometer into an on/off **switch**, and finally gives the basic material facts about silicon's refractive index: how it changes with wavelength (colour) and with temperature.

## Background you need

### Light as a wave, and wavelength

Light is a wave of electric and magnetic fields. Like a water wave, it has crests and troughs. The distance from one crest to the next is the **wavelength**, written $\lambda$ (Greek "lambda"). Silicon photonics mostly uses infrared light with $\lambda \approx 1.55\ \mu\text{m}$ (1550 nm), invisible to the eye. A micrometre ($\mu$m) is a millionth of a metre; a nanometre (nm) is a thousandth of a micrometre.

### Refractive index

Light travels at speed $c \approx 3\times10^{8}$ m/s in empty space. Inside a material it travels more slowly, at $c/n$. The number $n$ is the **refractive index**. Air has $n \approx 1$, glass (silicon dioxide, "oxide") about 1.44, silicon about 3.48. A higher $n$ means slower light, and it also means more wave crests fit into a given length, because the wavelength inside the material shrinks to $\lambda/n$.

In a waveguide, the light is partly in the silicon and partly in the surrounding oxide. So it "feels" an average index called the **effective index**, $n_{\text{eff}}$. Many equations below just write $n$ for this.

**Dispersion** means that $n$ depends on wavelength. Different colours see slightly different indices.

### Phase and the propagation constant

As light travels a distance $L$ in a waveguide, its wave goes through many cycles. Each full cycle is $2\pi$ radians of **phase**. The phase gained per unit length is the **propagation constant**:

$$\beta = \frac{2\pi n}{\lambda}$$

So after a length $L$ the phase is $\beta L = 2\pi n L/\lambda$. The key idea of the whole packet: **if you change $n$ by a small amount $\Delta n$, the phase changes by $2\pi\,\Delta n\,L/\lambda$.** A phase change of $\pi$ (half a cycle) turns a crest into a trough. A change of $2\pi$ brings you back where you started.

Worked example: to get a $\pi$ phase shift with $\lambda = 1.55\ \mu$m and $\Delta n = 10^{-3}$, you need $L = \lambda/(2\Delta n) = 1.55/0.002 \approx 775\ \mu$m. Small index changes need long waveguides.

### Interference and the Mach-Zehnder interferometer (MZI)

A **Mach-Zehnder interferometer (MZI)** splits light into two arms (with a **y-branch** splitter), lets each arm travel a length ($L_1$ and $L_2$), then recombines them with a second y-branch.

```
             arm 1 (length L1)
          /--------------------\
in ------<                      >------ out
          \--------------------/
             arm 2 (length L2)
```

If the two waves arrive in step (phase difference $0, 2\pi, 4\pi, \dots$), they add up: maximum output. If they arrive exactly out of step (phase difference $\pi, 3\pi, \dots$), they cancel: minimum output. In between, the output varies smoothly like a cosine.

An **imbalanced** (or **unbalanced**, asymmetric) MZI has arms of different length, $\Delta L = L_2 - L_1 \neq 0$. Then the phase difference depends on wavelength, so the output spectrum (output versus wavelength) goes up and down periodically, like ripples. These ripples are called **fringes**.

### Free spectral range (FSR) and extinction ratio

The **free spectral range (FSR)** is the wavelength spacing between two neighbouring peaks of the fringe pattern. Moving from one peak to the next corresponds to a $2\pi$ change in phase difference. That is why "one FSR" and "a $2\pi$ phase shift" mean the same thing, and why shifting the spectrum by *half* an FSR means a $\pi$ phase shift.

The **extinction ratio** is how much brighter the peaks are than the dips. A deep dip (large extinction ratio) means the two arms cancel almost perfectly, which only happens if both arms carry equal amounts of light. If one arm loses light, cancellation is incomplete and the dips get shallower.

### Decibels (dB)

Optical power ratios are often given in **decibels**: $\text{dB} = 10\log_{10}(P_{\text{out}}/P_{\text{in}})$. Every $-10$ dB is a factor of 10 less power. So $-3$ dB is about half, $-30$ dB is one thousandth, $-40$ dB is one ten-thousandth. **Insertion loss** is how much power a device throws away. Losses along a waveguide are often given in dB/cm.

### Doping, carriers, and the PIN junction

Pure silicon conducts electricity poorly. **Doping** means adding a tiny amount of other atoms to supply mobile charges, called **carriers**. **N-type** doping supplies extra electrons (negative). **P-type** doping supplies **holes** (missing electrons that behave like positive charges). "N++" means *heavily* doped (very conductive); "N" means lightly doped.

A **PIN junction** is a P region and an N region with an **I**ntrinsic (undoped) region between them. The light travels in the intrinsic middle. When you push current forward through it (**forward bias**), electrons and holes flood into the middle. These **free carriers** lower silicon's refractive index (giving a phase shift) and also absorb some light (giving loss). This is the **free-carrier effect** (the book covers it in Sections 6.1 and 6.4).

### Heat flow and the thermo-optic effect

Heat flows from hot to cold. How easily it flows through a material is the **thermal conductivity**, $k$, in W/(m·K). Silicon ($k=149$) and metals ($k\approx250$ for aluminium) conduct heat about 100 times better than oxide ($k=1.4$). So oxide acts like a blanket, and silicon acts like a copper plate.

The **thermo-optic effect**: when silicon gets warmer, its refractive index rises. For silicon, $dn/dT \approx 1.87\times10^{-4}$ per kelvin. A kelvin (K) step is the same size as a degree Celsius step. So heating by 10 K raises $n$ by about 0.0019. Small, but over hundreds of micrometres it is enough for a full $2\pi$ phase shift.

### The silicon-on-insulator (SOI) wafer

Silicon photonic chips are built on **silicon-on-insulator (SOI)** wafers: a thick silicon base (the **substrate**), then a layer of oxide (the **buried oxide, BOX**), then a thin silicon layer where the waveguides are etched, then a covering oxide (the **cladding**). Figure 3.1 below shows it.

A **strip waveguide** is a rectangle of silicon, here 500 nm wide and 220 nm tall. A **rib waveguide** is a thicker ridge sitting on a thin silicon "slab" that extends sideways. The slab lets you make electrical contact from the sides.

> **Key takeaways:**
>
> - Phase shift $= 2\pi\,\Delta n\,L/\lambda$: change the index, change the phase.
> - An MZI turns phase differences into brightness changes; one FSR shift equals a $2\pi$ phase shift.
> - Index can be changed electrically by injecting carriers (fast, lossy) or by heating (slow, lossless).
> - Oxide is a poor heat conductor; silicon and metal are good ones.

## 6.5 Active tuning

> **In one sentence:** There are two common ways to shift the phase of light electrically on a chip: injecting carriers into a PIN junction (fairly fast, but adds loss that changes with current) or heating the waveguide (no loss, but slow).

The book introduces two "knobs":

1. The **PIN junction waveguide.** It is moderately fast and efficient. The trade-off is **variable insertion loss**: the more you tune, the more light it absorbs.
2. The **thermal phase shifter** (a heater). It gives a **pure phase shift**: it changes phase with no change in brightness (amplitude). But heating and cooling take time, so it is slow.

Why speed differs: carriers can be added and removed in nanoseconds. Heat must physically spread through material, which typically takes microseconds or more.

### 6.5.1 PIN phase shifter

> **In one sentence:** Driving current through a PIN waveguide shifts the phase by about one FSR per 10 mA, but at high currents it absorbs so much light that interference disappears.

The forward-biased PIN waveguide from Section 6.4 (where it was used as a light attenuator) can also serve as a phase shifter. This is useful for tuning a Mach-Zehnder modulator or any circuit that needs a phase adjustment.

**How it was measured.** The PIN waveguide was placed inside an *imbalanced* MZI. Because of the imbalance, the output spectrum shows fringes. If the PIN section changes the phase in one arm, the fringes slide sideways in wavelength. By measuring the slide, you measure the phase shift.

The device details:

- Waveguide width: 500 nm.
- **Clearance**: 800 nm. This is the gap between the edge of the waveguide and the heavily doped contact regions (see Figure 6.18 for what "clearance" means). The doped contacts must stay away from the light, otherwise they would absorb it.
- Each arm contains a 3 mm long PIN junction in a rib waveguide.
- FSR of the interferometer: 55 nm.
- Light was coupled in and out using **grating couplers** (small gratings that send light between an optical fibre and the chip). Grating couplers only work well over a limited band, so the whole spectrum has a hump-shaped, roughly Gaussian envelope. That hump is a feature of the measurement, not of the PIN device.

**What happened at different currents:**

| Current | What you see | Meaning |
|---|---|---|
| 0 mA | Deep dips, extinction ratio about 40 dB | No extra loss in the PIN waveguide; both arms balanced |
| 5 mA | Spectrum shifted by half an FSR | A $\pi$ phase shift; extinction ratio drops to about 15 dB because of extra loss |
| 90 mA | Fringes nearly gone | One arm is so lossy (about 30 dB, per Figure 6.15) that essentially only the other arm carries light |

Read the table row by row: as current rises, the phase shift grows, but so does the loss.

**The figure of merit.** For PIN tuners the efficiency is quoted in **mA per FSR**: how much current you need for a full $2\pi$ shift. Here $\pi$ needs 5 mA, so $2\pi$ needs about **10 mA/FSR**. Smaller is better.

Why does the extinction ratio drop? Perfect cancellation needs equal light in both arms. Carriers absorb light in the tuned arm, so that arm gets weaker. The two waves can no longer cancel fully, so the dips become shallower (40 dB down to 15 dB). At 90 mA, the tuned arm is attenuated by about 30 dB (a factor of 1000). Almost all light comes from the other arm alone. With only one wave, there is nothing to interfere with, so the fringes vanish.

**Figure 6.17 — Transmission spectra of an MZI with a 3 mm PIN junction in each arm, at 0, 5 and 90 mA.**
The horizontal axis is wavelength from 1500 to 1580 nm. The vertical axis is transmission in dB (from about $-70$ to $+10$). Three curves:

- **0 mA (blue):** a clear ripple. A peak of about $-21$ dB near 1532 nm, a very deep dip of about $-61$ dB near 1551 nm, another peak of about $-23$ dB near 1568 nm. The deep dip is the 40 dB extinction ratio.
- **5 mA (green):** the pattern has slid sideways. Now there is a *peak* (about $-18$ dB) near 1548 nm, close to where the 0 mA curve had its *dip*. Peak where there was a dip means a half-FSR shift, i.e. a $\pi$ phase shift. The dip is now only about $-41$ dB, much shallower relative to the peak.
- **90 mA (red/orange):** a smooth, broad hump peaking around $-24$ dB near 1550 nm, with almost no ripple. The interference has been killed by loss.

Lesson: the PIN shifter really does shift phase (fringes move), but its loss grows with current. At large currents it stops being useful as a phase shifter.

> **Key takeaways:**
>
> - A forward-biased PIN waveguide in an MZI arm shifts the fringes; here $\pi$ at 5 mA, so about 10 mA/FSR.
> - The same carriers that shift the phase also absorb light, so extinction falls (40 dB to about 15 dB).
> - At 90 mA one arm loses about 30 dB, and interference disappears.
> - Grating couplers give the measured spectrum its overall hump shape.

### 6.5.2 Thermal phase shifter

> **In one sentence:** A heater warms the waveguide, which raises its index and shifts the phase; the power needed for a $2\pi$ shift (mW/FSR) is the key figure of merit and barely depends on heater length.

**Ways to build a heater.** A heater is just a **resistor**: current flows through it and it gets hot (Joule heating). The book lists three placements:

1. **Metal resistor above the waveguide.** Heat flows down from the metal, through the waveguide, to the substrate. The metal is kept 1–2 $\mu$m above the waveguide. Closer would be better for heat, but metal absorbs light strongly, so it must stay out of the light's reach.
2. **Resistor inside the waveguide.** The silicon waveguide itself is doped and carries the current, so the heat is made right where the light is. This is more efficient, but the doping causes some optical loss. It is usually built as an **N++/N/N++** structure (Figure 6.18): two heavily doped N++ contact regions on opposite sides of the waveguide, and a lightly doped N region in between, including the waveguide. Current flows *across* the waveguide, at right angles to the light. Because you need contacts on both sides, you need a rib waveguide (the slab connects the rib to the contacts). The book uses this approach in a system in Section 13.1.3.
3. **Resistor beside the waveguide**, with current flowing *along* the waveguide (parallel to the light). It can be in the silicon slab of a rib waveguide or a nearby metal strip.

**Figure 6.18 — Cross-section of an N++/N/N++ resistor in a rib waveguide.**
From left to right: a red block labelled N++ (contact), then an orange lightly doped N region made of a flat slab with a raised rib in the middle, then another red N++ block. The "Clearance" arrow marks the distance from the N++ edge to the rib wall. "Waveguide width" marks the width of the rib. No numbers are given.

```
          <-W->
          +---+
 +-----+  | N |  +-----+
 | N++ |--+   +--| N++ |
 +-----+    N    +-----+
 <-clearance->
```

Lesson: the contacts (N++) conduct easily, so almost all the electrical resistance, and therefore almost all the heat, is in the lightly doped N region, which includes the waveguide. The heat is made exactly where the light is. The clearance keeps the very lossy N++ regions away from the light.

**The figure of merit: mW/FSR.** Heater efficiency is quoted as **tuning efficiency** in **mW per FSR**: the electrical power needed for a $2\pi$ phase shift. Smaller is better.

A surprising fact: this number is **nearly independent of heater length**. Here is why, from first principles:

- Phase shift $= 2\pi\,(dn/dT)\,\Delta T\,L/\lambda$. For $2\pi$ you need $\Delta T \cdot L = \lambda/(dn/dT)$, a fixed number.
- For a long straight heater, each micrometre of length is the same 2D cross-section. The temperature rise is set by the *power per unit length*: $\Delta T \propto P/L$.
- So $\Delta T \cdot L \propto P$. The length cancels. Only total power matters.

A short heater needs a higher temperature, a long heater a lower one, but both use the same power. This holds for straight heaters that you can model as a 2D cross-section.

**Ways to do better:**

- **Compact heaters**, e.g. folding the waveguide back and forth under one heater. The heat is concentrated on more waveguide. These need full 3D thermal modelling.
- **Remove material** that carries heat away, so the heat stays near the waveguide:

| Technique | Demonstrated efficiency |
|---|---|
| Undercut the back of the substrate under the heater | 3.9 mW/FSR |
| Etch vertical trenches beside the phase shifter | 0.8 mW/FSR |
| Under-etch the waveguide for thermal isolation | 0.49 mW/FSR |

Read it as: the better you insulate the waveguide from the heat sink, the less power you need. Compare with the simple heaters simulated below (36 and 83 mW/FSR).

#### Modelling the heat: the steady-state heat equation

To predict the temperature, we solve the **steady-state heat equation** (also called **Poisson's equation**):

$$-\nabla\cdot\left(k\nabla T\right) = Q \qquad (6.25)$$

Symbols:

- $T$ — temperature at each point (K or °C).
- $k$ — thermal conductivity (W/(m·K)); different in each material.
- $Q$ — heat generated per unit volume (W/m³); non-zero only inside the heater.
- $\nabla T$ — the **gradient** of $T$: an arrow pointing toward hotter places, whose length says how fast $T$ changes with position.
- $k\nabla T$ — heat flows *down* the gradient, at a rate proportional to $k$. So $-k\nabla T$ is the **heat flux** (W/m²), the flow of heat (Fourier's law).
- $\nabla\cdot$ — the **divergence**: how much flow leaves a tiny box, minus how much enters.

What it says: "In steady state (nothing changing with time), the net heat flowing out of any tiny box equals the heat made inside it." Where there is no heater, $Q=0$, so whatever heat comes in must go out. It is like water flowing through pipes: no water piles up anywhere.

**The simulation setup (MATLAB PDE Toolbox, Listing 6.12).** The book used MATLAB's Partial Differential Equation Toolbox (its graphical interface), then edited the generated code to pull out the useful numbers. The code is not reproduced here; what it does:

1. Draw the 2D cross-section (all lengths in $\mu$m). Shapes are drawn in order so the waveguide and metal sit "on top" of the oxide:
   - $y=0$ is the bottom of the waveguide.
   - Oxide: $y$ from $-2$ to $2$, $x$ from $-50$ to $50$.
   - Metal: 1 $\mu$m above the waveguide top: $y$ from 1.22 to 1.72, $x$ from $-0.5$ to $0.5$ (500 nm thick, 1 $\mu$m wide).
   - Waveguide: 500 nm × 220 nm strip: $y$ from 0 to 0.22, $x$ from $-0.25$ to $0.25$.
   - Silicon substrate: 100 $\mu$m thick: $y$ from 0 to $-100$ (as written in the book; physically it lies below the oxide, starting at the oxide bottom $y=-2$, as the figures show), $x$ from $-50$ to $50$.
2. Set the **boundary conditions** (what happens at the edges of the simulated region):
   - **Dirichlet** condition (temperature fixed): at the bottom of the substrate, $T=0$. This models the chip sitting on a **heat sink** (a big block that stays at constant temperature). All results are temperature rises *above* the heat sink.
   - **Neumann** condition (heat flux fixed): on all other edges, the flux $-\mathbf{n}\cdot(k\nabla T)$ is set to zero, where $\mathbf{n}$ is the outward direction perpendicular to the edge. Zero flux means **insulating**: no heat escapes through the top or sides. Convection (air carrying heat away) and radiation are ignored.
3. Set the heat source in the metal.
4. Set the material conductivities.
5. Solve, then plot the temperature map and a line cut.

**The heat source.** The metal heater is 500 nm thick, 1000 nm wide and 100 $\mu$m long, and dissipates $Q_{\text{tot}} = 10$ mW. The heat per unit volume is total power divided by volume:

$$Q = \frac{Q_{\text{tot}}}{V} = \frac{0.01\ \text{W}}{0.5\cdot 1\cdot 100\times 10^{-18}\ \text{m}^{3}}$$

Worked out: the volume is $0.5\times1\times100 = 50\ \mu\text{m}^3 = 50\times10^{-18}$ m³ (one $\mu$m³ is $10^{-18}$ m³). So $Q = 0.01/(5\times10^{-17}) = 2\times10^{14}$ W/m³. That is huge per cubic metre, but the volume is tiny.

**Material properties:**

| Material | Thermal conductivity $k$ [W/(m·K)] |
|---|---|
| Silicon | 149 |
| Silicon dioxide (oxide) | 1.4 |
| Aluminium (metal heater) | 250 |

Because the geometry is drawn in micrometres, the conductivities are also converted to micrometre units (e.g. silicon becomes $149\times10^{-6}$ in W/($\mu$m·K)). Mixing units would give wrong answers by factors of a million.

**Figure 6.19 — Temperature in the wafer cross-section with the heater directly above the waveguide.**

*Panel (a)*, a 2D colour map zoomed near the devices ($x$ from $-5$ to $5$ $\mu$m, $y$ from $-4$ to $2$ $\mu$m). The colour goes from white (0) through yellow and orange to dark red (above 40). Black contour lines (lines of equal temperature) form nested ovals around the metal heater. The heater (around $y\approx1.2$–$1.7$) is the hottest spot, above 40 °C. The waveguide at $(0,0)$ sits in a red/orange zone, around 23 °C. A blue line at $y=-2$ marks where the oxide meets the silicon substrate; below it everything is pale, nearly 0. (The caption places the metal at (0, 1.5), which is roughly its centre; its bottom edge is at 1.22.)

*Panel (b)*, temperature along the vertical line $x=0$:

- $y=-5$ to $-2$ (substrate): flat at about 0.
- $y=-2$ to $0$ (oxide below the waveguide): rises in a straight line to about 23 °C.
- Across the waveguide ($y=0$ to 0.22): nearly flat, a small step.
- $y=0.22$ to 1.22 (oxide between waveguide and metal): rises steeply.
- At the metal (from $y\approx1.22$): flat at the top, about 42–44 °C, staying there to $y=2$ because the top is insulating.

```
 T(°C)
 44 |                           ______ metal
    |                         /
 23 |              ___wg____/
    |            /
  0 |___________/
    +------------+----+-----+------> y (um)
   -5          -2     0    1.22   2
```

Lesson: the temperature changes almost entirely inside the oxide. Inside silicon and metal it is nearly flat.

**What the simulation tells us:**

- Silicon and metal conduct heat about 100 times better than oxide. So the temperature is nearly uniform *inside* the metal and *inside* the waveguide. (Like water in a wide pipe: little "pressure drop" across it.)
- For the same reason, the whole substrate is almost at one temperature. The top of the substrate (the silicon–oxide interface) is only about 1.1 °C above the heat sink. Nearly all the temperature drop is across the oxide.
- The substrate thickness hardly matters. A real substrate is about 700 $\mu$m thick, versus 2 $\mu$m of oxide and 0.22 $\mu$m of waveguide. Yet a 10 $\mu$m or a 700 $\mu$m substrate gives very similar results, because silicon conducts so well that its thickness adds little resistance to heat flow.
- Temperature rise: **44 °C in the metal** and **23 °C in the waveguide.** Only about half the heater's temperature rise reaches the waveguide.

#### From temperature to tuning efficiency

Using the heat equation result and the rule that one FSR is a $2\pi$ phase shift, the book gives:

$$\text{efficiency [mW/FSR]} = \frac{Q_{\text{tot}}\,\lambda}{\frac{dn}{dT}\,\Delta T} \qquad (6.26)$$

Symbols: $Q_{\text{tot}}$ is the heater power, $\lambda$ the wavelength, $dn/dT$ the thermo-optic coefficient, $\Delta T$ the temperature rise *in the waveguide*.

Where it comes from: the phase shift is $2\pi\,(dn/dT)\,\Delta T\,L/\lambda$. Temperature rise is proportional to power, so the power that gives exactly $2\pi$ is

$$P_{2\pi} = Q_{\text{tot}}\cdot\frac{\lambda}{\frac{dn}{dT}\,\Delta T\,L}$$

In Equation (6.26) the heater length $L$ is absorbed by reading $Q_{\text{tot}}$ as power per unit length (the simulation is a 2D cross-section). This is exactly the "length cancels" argument from above.

Worked check: 10 mW over 100 $\mu$m is 0.1 mW/$\mu$m. With $\lambda = 1.55\ \mu$m, $dn/dT = 1.87\times10^{-4}$/K and $\Delta T = 23$ K:

$$\frac{0.1 \times 1.55}{1.87\times10^{-4}\times 23} = \frac{0.155}{0.0043} \approx 36\ \text{mW}$$

This matches the book's result: **36 mW/FSR** for a heater directly above the waveguide.

**Heater beside the waveguide.** The same calculation for a metal heater placed to the side, 2 $\mu$m away from the strip waveguide, gives **83 mW/FSR**, more than twice as much power. The heat now spreads in all directions and much of it goes straight down to the substrate without passing the waveguide.

**Figure 6.20 — Temperature in the cross-section with the heater beside the waveguide.**

*Panel (a)*, 2D colour map. The waveguide is a small rectangle at $(0,0)$. The metal heater is a larger rectangle at about $(2.75, 0.25)$, spanning $x$ from 2.25 to 3.25. The hottest region (above 25 °C, dark red) is the heater. Contour lines are packed tightly near the heater and spread out further away. The substrate below $y=-2$ is cool; the coolest places are the bottom and the far left/right edges.

*Panel (b)*, temperature along the horizontal line $y=0.11$ (through the middle of the waveguide):

- At $x=-5$: about 2 °C.
- Rises slowly to the waveguide, where there is a flat plateau of about **10 °C** ($x$ from about $-0.5$ to $0.5$; the flat part is the high-conductivity silicon).
- Rises steeply to about 20 °C at the heater edge ($x\approx2.25$), then a flat peak of about **31 °C** inside the metal.
- Falls to about 12.5 °C at $x=5$.

```
 T(°C)
 31 |                    ___ metal
    |                  /     \
 10 |        __wg__  /        \___
  2 |_______/      \/               (12.5 at x=5)
    +---------+---------+-----+---> x (um)
   -5         0       2.75    5
```

Lesson: the waveguide only gets about 10 °C while the heater reaches about 31 °C. Less of the heat reaches the light, so efficiency is worse. (Check with Eq. 6.26: $0.155/(1.87\times10^{-4}\times 10) \approx 83$ mW, matching the book's 83 mW/FSR.)

> **Key takeaways:**
>
> - A heater is a resistor; it can sit above, inside (N++/N/N++), or beside the waveguide.
> - Figure of merit is mW/FSR (power for $2\pi$); for straight heaters it is nearly independent of length.
> - Oxide is a thermal blanket: almost all the temperature drop is across it; silicon and metal are nearly isothermal.
> - Simulated: heater above gives 44 °C in metal, 23 °C in waveguide, 36 mW/FSR; heater 2 $\mu$m to the side gives 83 mW/FSR.
> - Removing heat paths (undercuts, trenches, under-etching) can reach 3.9, 0.8 and 0.49 mW/FSR.

## 6.6 Thermo-optic switch

> **In one sentence:** Put a heater on one arm of an MZI, and the output goes up and down like a cosine as you raise the temperature, so you can switch light on and off with heat.

**The idea.** The MZI (book Section 4.3) becomes a **thermo-optic switch** if one arm is made warmer than the other. A resistive heater on one arm does this. Warming the lower arm by $\Delta T$ raises its index by $(dn/dT)\,\Delta T$, with $dn/dT = 1.87\times10^{-4}\ \text{K}^{-1}$ for silicon (from Section 3.1.1 below). That adds phase to the lower arm only, changing the phase *difference*, and therefore the output brightness.

**Step 1: the heated arm's propagation constant.**

$$\beta_{2} = \frac{2\pi\left(n_{2}+\frac{dn}{dT}\,\Delta T\right)}{\lambda} \qquad (6.27)$$

- $\beta_2$ — phase per unit length in arm 2 (the heated arm).
- $n_2$ — effective index of arm 2 at the starting temperature.
- $\frac{dn}{dT}\Delta T$ — the extra index caused by heating.

It is just $\beta = 2\pi n/\lambda$ with $n$ replaced by the heated index. (The book uses silicon's material $dn/dT$ for the waveguide's effective index, a simple approximation.)

**Step 2: plug into the MZI output formula.** The book's Equation (4.19) gives the ideal MZI output as $\frac{I_i}{2}\left[1+\cos(\beta_1 L_1 - \beta_2 L_2)\right]$. Inserting Eq. (6.27):

$$I_{o}(\Delta T) = \frac{I_i}{2}\left[1+\cos\left(\beta_{1}L_{1}-\frac{2\pi\left(n_{2}+\frac{dn}{dT}\Delta T\right)}{\lambda}L_{2}\right)\right] \qquad (6.28a)$$

- $I_i$ — input intensity (power); $I_o$ — output intensity.
- $\beta_1 L_1$ — total phase collected in arm 1; the second term is the phase in arm 2.
- The bracket is $1+\cos(\text{phase difference})$, which swings between 0 and 2. So $I_o$ swings between 0 (full cancellation) and $I_i$ (everything comes out). The factor $\frac{1}{2}$ makes the maximum equal the input.

**Step 3: identical arms.** If both arms have the same cross-section, $n_1 = n_2 = n$, and the formula simplifies:

$$I_{o}(\Delta T) = \frac{I_i}{2}\left[1+\cos\left(\frac{2\pi n}{\lambda}\Delta L-\frac{2\pi\left(\frac{dn}{dT}\Delta T\right)}{\lambda}L_{2}\right)\right] \qquad (6.29a)$$

Now the phase difference has two clear parts:

1. $\frac{2\pi n}{\lambda}\Delta L$ — from the length difference $\Delta L$ between the arms. It depends on wavelength, which produces fringes in the spectrum.
2. $\frac{2\pi}{\lambda}\frac{dn}{dT}\Delta T\,L_2$ — from the heating. It depends on temperature and on the length of the heated arm.

(Sign conventions for $\Delta L$ only move the fringes; the shape is the same.) The output is a **sinusoidal** function of both wavelength and temperature. Heat, and the fringes slide; heat more, and any fixed wavelength cycles bright, dark, bright.

**Worked example: how many kelvin per full cycle?** With the parameters of Figure 6.21 ($L_1 = 500\ \mu$m, $\Delta L = 100\ \mu$m, so $L_2 = 600\ \mu$m) and $\lambda = 1.55\ \mu$m, the heating term reaches $2\pi$ when

$$\Delta T_{2\pi} = \frac{\lambda}{\frac{dn}{dT}\,L_2} = \frac{1.55}{1.87\times10^{-4}\times 600} \approx 13.8\ \text{K}$$

So about 14 K of heating cycles the output through one full period, and about 7 K switches it from fully on to fully off. This matches the roughly 14–15 K period in Figure 6.22.

**Figure 6.21 — MZI spectrum with arm 2 at $\Delta T = 0$ K and $\Delta T = 5$ K.**
Parameters: $L_1 = 500\ \mu$m, $\Delta L = 100\ \mu$m, waveguide loss $\alpha = 3$ dB/cm, lossless y-branches, and a wavelength-dependent effective index from the book's Equation (3.7) (a formula from Chapter 3 for how $n_{\text{eff}}$ changes with wavelength; not part of this packet). The horizontal axis is wavelength from 1.54 to 1.56 $\mu$m; the vertical axis is normalised transmission from 0 to 1 (linear, not dB).

- **$\Delta T = 0$ K (solid blue):** a regular cosine ripple. Peaks near 0.95 at about 1.5425, 1.549 and 1.5555 $\mu$m; dips near 0.02 at about 1.546, 1.5525 and 1.559 $\mu$m. Peak spacing (the FSR) is about 6.5 nm. Contrast is better than 15 dB.
- **$\Delta T = 5$ K (dashed green):** the same ripple, shifted about 2.5 nm toward longer wavelength (a **red-shift**).

Lesson: heating one arm slides the whole fringe pattern. Check: 5 K is $5/13.8 \approx 0.36$ of a full cycle, and $0.36\times6.5\ \text{nm}\approx2.4$ nm, matching the 2.5 nm shift. Peaks do not reach exactly 1 because of the 3 dB/cm waveguide loss.

**Figure 6.22 — Transmission versus temperature increase (0 to 50 K) for the same MZI, at a fixed wavelength.** Two cases:

- **"One arm" (solid blue):** only one arm heated. The output oscillates strongly: starts near 0.65, peaks at about 0.96 near 4 K, falls to 0 near 9 K, peaks again near 17 K, zero near 24 K, peak near 31 K, zero near 38 K, peak near 45 K, ending near 0.18 at 50 K. Period about 14–15 K. Full on/off switching.
- **"Both arms" (dashed green):** the whole substrate heated, so both arms warm equally. The output changes slowly: starts near 0.65, rises to a maximum of about 0.96 near 17 K, then falls to about 0.09 at 50 K.

Why the "both arms" curve is so slow: heating both arms equally adds the same index change to both. The phase *difference* then only changes because one arm is longer by $\Delta L$. Repeat the worked example with $\Delta L = 100\ \mu$m instead of $L_2 = 600\ \mu$m: the period becomes about $1.55/(1.87\times10^{-4}\times100) \approx 83$ K, six times longer. 

Lessons:

- To make a switch, heat *one* arm. Heat on *both* arms (a common-mode change, e.g. the room or chip temperature drifting) mostly cancels out.
- But not completely: an imbalanced MZI still drifts with overall chip temperature. A few kelvin of chip warming can noticeably change the output. This is why on-chip temperature matters in photonics.

> **Key takeaways:**
>
> - A heater on one MZI arm adds phase $2\pi\,(dn/dT)\,\Delta T\,L_2/\lambda$, making the output a cosine of temperature.
> - With $L_2 = 600\ \mu$m, about 14 K gives a full cycle; about 7 K switches fully on to fully off.
> - In the spectrum, 5 K slides the fringes about 2.5 nm to longer wavelength.
> - Heating both arms equally changes the output only slowly (only $\Delta L$ matters), so a switch must heat one arm.

## 3.1.1 Silicon

> **In one sentence:** Silicon's refractive index falls slightly as wavelength increases and rises as temperature increases; this section gives the models and numbers that the tuning calculations above rely on.

This section describes how silicon's refractive index depends on **wavelength** and on **temperature**. (How it depends on free carriers is in Section 6.1.1, the basis of the PIN shifter.)

**Figure 3.1 — Cross-section of a silicon-on-insulator (SOI) wafer.**
A stack of four layers, from top to bottom:

| Layer | Material | Thickness |
|---|---|---|
| Cladding oxide | Silicon dioxide | (not given) |
| Device layer ("SOI") | Silicon | 220 nm |
| Buried oxide (BOX) | Silicon dioxide | 2 $\mu$m |
| Substrate | Silicon | about 700 $\mu$m |

A small axis sign shows $z$ pointing up (thickness direction) and $x, y$ lying in the wafer plane.

Lesson: the waveguides are carved from the thin 220 nm silicon layer. The 2 $\mu$m BOX keeps the light from leaking into the thick substrate below. This is the same stack used in the heater simulations: oxide around the waveguide, and a thick silicon substrate acting as the heat sink. The substrate is over 300 times thicker than the BOX, yet (as Section 6.5.2 showed) its thickness barely affects the heat flow.

### Silicon – wavelength dependence

> **In one sentence:** Silicon's index drops a little as wavelength gets longer, and it can be described by a simple slope, a Sellmeier formula, or (for simulations) a Lorentz model.

Devices are designed for many wavelengths, so we must include how the index of silicon (and of oxide) changes with wavelength. Otherwise we cannot correctly predict **dispersion effects** (effects caused by different wavelengths seeing different indices).

**Simplest model: a straight line.** Silicon's index changes by about $-7.6\times10^{-5}$ per nm of wavelength. The minus sign means $n$ goes *down* as $\lambda$ goes *up*. Example: from 1500 nm to 1600 nm, $n$ drops by $100\times7.6\times10^{-5} = 0.0076$, for instance from about 3.48 to about 3.47. Small, but it matters for precise designs.

**Better model: the Sellmeier equation.**

$$n^{2}(\lambda) = \epsilon + \frac{A}{\lambda^{2}} + \frac{B\lambda_{1}^{2}}{\lambda^{2}-\lambda_{1}^{2}} \qquad (3.1)$$

- $\epsilon$, $A$, $B$, $\lambda_1$ — constants chosen to fit measured data.
- $\lambda_1$ — the wavelength of a material **resonance**, where the material strongly absorbs light (for silicon, in the ultraviolet/visible, far shorter than 1.55 $\mu$m).

Why this shape: the electrons in a material behave like tiny springs that are shaken by the light. Near the resonance the response is strong, so the index changes quickly. Far from it, the effect fades. That is why the last term grows large as $\lambda$ approaches $\lambda_1$, and why $n$ creeps up at shorter wavelengths.

**Simulation-friendly model: the Lorentz model.** The Sellmeier formula cannot be used directly in **FDTD** simulations (finite-difference time-domain: a method that steps Maxwell's equations forward in time on a grid). Instead a **Lorentz model** is used:

$$n^{2}(\lambda) = \epsilon + \frac{\epsilon_{\text{Lorentz}}\,\omega_{0}^{2}}{\omega_{0}^{2}-2i\delta_{0}\,\frac{2\pi c}{\lambda}-\left(\frac{2\pi c}{\lambda}\right)^{2}} \qquad (3.2)$$

- $\omega = 2\pi c/\lambda$ — the light's **angular frequency** (radians per second). The formula is written in $\lambda$, but it is really a function of frequency.
- $\omega_0$ — the resonance frequency of the "spring".
- $\delta_0$ — the **damping** (friction on the spring). It multiplies $i$ (the imaginary unit), so it makes $n^2$ complex; the imaginary part means absorption (loss).
- $\epsilon$ — background contribution from everything else; $\epsilon_{\text{Lorentz}}$ — the strength of this resonance.

This is exactly the physics of a driven, damped mass on a spring, the classic model of how atoms respond to light. A model written as a function of frequency like this can be turned into a time-stepping rule, which FDTD needs.

**Why use it:** the same silicon model can be used in both **eigenmode** calculations (book Section 2.1: solving for the shape and $n_{\text{eff}}$ of the light patterns a waveguide supports) and FDTD calculations (Section 2.2.1). Using the same material in both tools keeps simulations consistent.

**Fitted values** (matched to measured silicon data from Palik's handbook over 1.15 to 1.8 $\mu$m):

| Parameter | Value |
|---|---|
| $\epsilon$ | 7.9874 |
| $\epsilon_{\text{Lorentz}}$ | 3.6880 |
| $\omega_0$ | $3.9328\times10^{15}$ rad/s |
| $\delta_0$ | 0 |

Worked example at $\lambda = 1.55\ \mu$m:

- $\omega = 2\pi c/\lambda = 2\pi\times3\times10^{8}/(1.55\times10^{-6}) \approx 1.216\times10^{15}$ rad/s.
- $\omega^2 \approx 1.48\times10^{30}$; $\omega_0^2 \approx 1.547\times10^{31}$.
- Lorentz term: $3.688\times\frac{1.547}{1.547-0.148} \approx 3.688\times1.106 \approx 4.08$.
- $n^2 \approx 7.987 + 4.08 = 12.07$, so $n \approx 3.474$.

That is silicon's well-known index near 1550 nm. The resonance $\omega_0$ corresponds to a wavelength $2\pi c/\omega_0 \approx 0.48\ \mu$m, far below 1.55 $\mu$m, as expected.

Two more properties:

- The model satisfies the **Kramers–Kronig relations**. These are rules, following from **causality** (a material cannot respond before light arrives), that tie the refractive index and the absorption together. Any physically real material obeys them, and an FDTD model must too or the simulation can misbehave.
- With $\delta_0 \to 0$ the model is **lossless** (no absorption). That suits silicon at these infrared wavelengths, where it is transparent.

The book also gives a Lumerical script (Listing 3.1, not included in this packet) that defines this material in the simulation software: it enters the four fitted parameters above as a Lorentz material so both the mode solver and FDTD use it.

**Figure 3.2 — Silicon's refractive index at room temperature (300 K), measured data and Lorentz fit.**
Horizontal axis: wavelength from about 1.1 to 1.7 $\mu$m. Vertical axis: index from 3.47 to about 3.54. Open circles are 8 measured points (Palik), for example about 3.538 at 1.10 $\mu$m, 3.519 at 1.20 $\mu$m, 3.488 at 1.40 $\mu$m, 3.478 at 1.53 $\mu$m and 3.466 at 1.68 $\mu$m. The solid line is the Lorentz model: smooth, steadily falling, curving upward (falling faster at short wavelength). One point near 1.38 $\mu$m (3.501) sits clearly above the line, an outlier in the data.

Lesson: the index falls by only about 0.07 across this whole range, and the Lorentz model tracks the data well. The fall is steeper at shorter wavelength because we are closer to the resonance.

### Silicon – temperature dependence

> **In one sentence:** Heating silicon raises its refractive index by about $1.87\times10^{-4}$ per kelvin, which shifts device spectra and makes thermal tuning possible.

**Why the index changes with temperature.** Three physical effects, all inside the crystal:

- The **distribution of carriers** (electrons and holes) changes: at higher temperature more of them are in higher-energy states.
- The **distribution of phonons** changes. A **phonon** is a packet of vibration of the crystal lattice, i.e. a unit of heat motion of the atoms. More heat means more phonons.
- The **bandgap shrinks**. The **bandgap** is the minimum energy needed to free an electron so it can conduct. Silicon's bandgap shrinks slightly when it gets warmer. A smaller bandgap moves silicon's strong absorption closer to our wavelength, which, like moving closer to the spring resonance above, raises the index.

Practical result: a slight temperature change shifts the transmission spectrum of devices such as **ring resonators** (a waveguide loop where light circulates and resonates at specific wavelengths) and MZIs. This is a nuisance (devices drift) but also useful: it is how we thermally tune devices (Sections 6.5.2 and 6.6).

**The numbers.** The book quotes two forms:

- A normalised coefficient: $\frac{1}{n}\frac{dn}{dT} = 5.2\times10^{-5}\ \text{K}^{-1}$. (The book calls this $\beta$, but note it is a different $\beta$ from the propagation constant used in Section 6.6.)
- A direct measurement: $\frac{dn}{dT} = 1.87\times10^{-4}\ \text{K}^{-1}$ at 1500 nm.

They agree: multiply the first by $n \approx 3.48$ and you get $5.2\times10^{-5}\times3.48 \approx 1.8\times10^{-4}$ per K.

What it means physically: heating by 1 K raises the index from, say, 3.4760 to 3.4762. Tiny. But in Section 6.6 we saw that over 600 $\mu$m, just 14 K produces a full $2\pi$ phase shift. Silicon's thermo-optic coefficient is large compared with many other optical materials (for example, it is roughly 20 times larger than that of silica glass), which is why heaters work so well on silicon chips, and also why silicon devices are so sensitive to temperature drift.

> **Key takeaways:**
>
> - Standard SOI stack: 220 nm silicon on 2 $\mu$m buried oxide on about 700 $\mu$m silicon substrate, with oxide cladding.
> - Silicon's index falls with wavelength, about $-7.6\times10^{-5}$ per nm; near 1550 nm $n \approx 3.47$–3.48.
> - The Lorentz model (fitted: $\epsilon=7.9874$, $\epsilon_{\text{Lorentz}}=3.6880$, $\omega_0=3.9328\times10^{15}$, $\delta_0=0$) works in both mode solvers and FDTD, obeys Kramers–Kronig, and is lossless when $\delta_0 = 0$.
> - Thermo-optic coefficient: $dn/dT = 1.87\times10^{-4}$/K (or $(1/n)\,dn/dT = 5.2\times10^{-5}$/K); caused by changes in carriers, phonons and bandgap.

## Glossary

| Term | Plain meaning |
|---|---|
| Active tuning | Changing a device's optical behaviour after manufacture with an electrical signal |
| Angular frequency ($\omega$) | How fast a wave oscillates, in radians per second; $\omega = 2\pi c/\lambda$ |
| Bandgap | Minimum energy needed to free an electron in a semiconductor so it can conduct |
| Boundary condition | A rule saying what happens at the edges of a simulated region |
| Buried oxide (BOX) | The 2 $\mu$m oxide layer under the silicon device layer in an SOI wafer |
| Carriers / free carriers | Mobile electric charges (electrons and holes) that can move through silicon |
| Cladding | Material surrounding a waveguide core, here oxide |
| Clearance | Distance between the waveguide and the heavily doped contact regions |
| Damping ($\delta_0$) | "Friction" in the Lorentz model; causes absorption |
| Decibel (dB) | Logarithmic power ratio, $10\log_{10}(P_2/P_1)$; $-10$ dB is a factor of 10 down |
| Dirichlet condition | Boundary condition that fixes the value (here, temperature) |
| Dispersion | Refractive index depending on wavelength |
| Divergence ($\nabla\cdot$) | Net outflow from a tiny region |
| Doping | Adding impurity atoms to silicon to supply carriers; N = electrons, P = holes, ++ = heavy |
| Effective index ($n_{\text{eff}}$) | The average index that light in a waveguide experiences |
| Eigenmode solver | Software that finds the light patterns (modes) a waveguide supports |
| Extinction ratio | Ratio between maximum and minimum output of an interferometer |
| FDTD | Finite-difference time-domain: simulation that steps light's equations forward in time on a grid |
| Forward bias | Driving current through a junction in its easy-conduction direction |
| Free-carrier effect | Free carriers lowering silicon's index and absorbing light |
| Free spectral range (FSR) | Wavelength spacing between neighbouring fringe peaks; equals a $2\pi$ phase change |
| Fringes | The periodic peaks and dips in an interferometer's output |
| Gradient ($\nabla T$) | Arrow pointing toward increasing temperature, sized by how fast it increases |
| Grating coupler | Small grating that couples light between a fibre and the chip; works over a limited band |
| Heat equation (Poisson's equation) | $-\nabla\cdot(k\nabla T) = Q$: heat made in a region equals heat flowing out (steady state) |
| Heat flux | Rate of heat flow per unit area, $-k\nabla T$ |
| Heat sink | A large body held at constant temperature that absorbs heat |
| Hole | A missing electron that acts like a positive charge |
| Imbalanced (unbalanced) MZI | MZI with arms of different length |
| Insertion loss | Power lost by passing through a device |
| Interference | Waves adding (in step) or cancelling (out of step) |
| Kramers–Kronig relations | Causality-based rules linking a material's index and absorption |
| Lorentz model | Damped-spring model of how a material's index depends on frequency |
| Mach-Zehnder interferometer (MZI) | Device that splits light into two arms and recombines it |
| mA/FSR, mW/FSR | Current or power needed for a $2\pi$ phase shift; figures of merit for tuners |
| Neumann condition | Boundary condition that fixes the flux (here zero: insulating) |
| Phase | Position within a wave cycle; one full cycle is $2\pi$ |
| Phase shifter | Device that changes the phase of light on command |
| Phonon | A packet of vibration of the crystal lattice (heat motion) |
| PIN junction | P-doped, intrinsic (undoped), N-doped regions side by side |
| Propagation constant ($\beta$) | Phase gained per unit length, $2\pi n/\lambda$ |
| Red-shift | Spectrum moving toward longer wavelength |
| Refractive index ($n$) | How much slower light is in a material than in vacuum |
| Resonance | Frequency at which a material responds (absorbs) strongly |
| Rib waveguide | Silicon ridge on a thin silicon slab, allowing side contacts |
| Ring resonator | Waveguide loop that resonates at specific wavelengths |
| Sellmeier equation | Fitting formula for index versus wavelength |
| SOI (silicon-on-insulator) | Wafer: thin silicon on oxide on thick silicon substrate |
| Strip waveguide | Simple rectangular silicon waveguide (here 500 × 220 nm) |
| Substrate | The thick silicon base of the wafer |
| Thermal conductivity ($k$) | How easily heat flows through a material, W/(m·K) |
| Thermal phase shifter (heater) | Resistor that warms a waveguide to shift its phase |
| Thermo-optic coefficient ($dn/dT$) | Change of index per kelvin of temperature |
| Thermo-optic switch | MZI switched on/off by heating one arm |
| Tuning efficiency | Power (or current) needed for a $2\pi$ phase shift |
| Wavelength ($\lambda$) | Distance between wave crests; about 1.55 $\mu$m here |
| Y-branch | Waveguide splitter/combiner shaped like a Y |

## Check yourself

1. Why does the extinction ratio of the MZI drop from 40 dB to about 15 dB when 5 mA flows through the PIN shifter?

   *Answer:* The injected carriers absorb light in that arm. The two arms now carry unequal power, so they cannot cancel completely at the dips.

2. The PIN shifter gives a $\pi$ shift at 5 mA. What is its efficiency in mA/FSR, and how do you see the $\pi$ shift in the spectrum?

   *Answer:* About 10 mA/FSR. The fringes slide by half an FSR, so a peak appears where there used to be a dip.

3. Why is a heater's mW/FSR nearly independent of its length?

   *Answer:* For a $2\pi$ shift you need a fixed product $\Delta T\cdot L$. For a straight heater, $\Delta T$ is proportional to power per length. So $\Delta T\cdot L$ is proportional to total power, and $L$ cancels.

4. In the simulation, the metal rises 44 °C but the waveguide only 23 °C, and the substrate top only about 1.1 °C. Why?

   *Answer:* Oxide conducts heat about 100 times worse than silicon or metal, so almost all the temperature drop occurs across the oxide layers. Silicon and metal stay nearly uniform in temperature.

5. Use Eq. (6.26) to estimate the efficiency if the waveguide warmed by 10 K per 0.1 mW/$\mu$m (heater beside the waveguide).

   *Answer:* $0.1\times1.55/(1.87\times10^{-4}\times10) \approx 83$ mW/FSR, matching the book.

6. Name three ways to make a thermal phase shifter more efficient and their demonstrated values.

   *Answer:* Substrate back-side undercut (3.9 mW/FSR), vertical trenches beside the heater (0.8 mW/FSR), under-etching the waveguide (0.49 mW/FSR). All reduce heat leaking away from the waveguide.

7. For the MZI with $L_2 = 600\ \mu$m at 1.55 $\mu$m, how much heating of one arm switches the output from fully on to fully off?

   *Answer:* A full cycle needs $\lambda/((dn/dT)L_2) \approx 13.8$ K, so on to off ($\pi$) takes about 7 K.

8. Why does heating both arms (Figure 6.22, dashed) change the output so slowly?

   *Answer:* Both arms get the same index change, so only the length difference $\Delta L = 100\ \mu$m contributes to the phase difference. The period becomes about 83 K instead of about 14 K.

9. Why does the book use a Lorentz model instead of the Sellmeier equation for silicon?

   *Answer:* The Lorentz model can be used directly in FDTD (it obeys Kramers–Kronig), and the same model can be used in eigenmode solvers, keeping simulations consistent.

10. Check that $(1/n)\,dn/dT = 5.2\times10^{-5}$/K agrees with $dn/dT = 1.87\times10^{-4}$/K.

    *Answer:* Multiply by $n\approx3.48$: $5.2\times10^{-5}\times3.48\approx1.8\times10^{-4}$/K, close to $1.87\times10^{-4}$/K.
