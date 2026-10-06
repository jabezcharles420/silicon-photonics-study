# Week 2 · Day 3 — Wednesday 30 Sep 2026

*Simple-English study version of Chrostowski & Hochberg §4.3 (Mach–Zehnder interferometer) and §3.2.9–3.2.10 (wavelength dependence and compact models for waveguides).*

[:material-file-pdf-box: Download this day as PDF](day-03-wed-30-sep-2026.pdf){ .md-button }

---

## Before you start: the big picture

A photonic chip moves light around in tiny "wires" made of silicon, called **waveguides**. To do anything useful with that light (switch it, encode data on it, pick out one colour) we need devices that treat different colours, or different settings, differently. Today's reading covers one of the most important such devices and the waveguide facts that it depends on.

The first part (§4.3) is the **Mach–Zehnder interferometer** (MZI). Picture a running track that splits into two lanes and then merges again. Two runners start together, one takes each lane, and they meet again at the merge. If the lanes have different lengths, the runners arrive out of step. With light, "in step" means the two waves add up (bright output), and "out of step" means they cancel (dark output). By changing the lane lengths, or how fast light travels in one lane, we can turn the output up and down. That is the basis of optical switches and of the modulators that put internet data onto light.

The second part (§3.2.9–3.2.10) explains a quieter but crucial fact: how fast light travels in a waveguide depends on its colour (wavelength), on the waveguide's width, on temperature, and more. There are two different "speeds" to keep track of. We need both, because the MZI's behaviour (and that of ring resonators) is set by them. The last section shows how engineers wrap all of this up in a short formula, a **compact model**, so that they can design whole circuits without re-running heavy simulations every time.

> **Key takeaways:**
>
> - An MZI splits light into two paths and recombines it; the output depends on the difference in "delay" between the paths.
> - The speed of light in a waveguide depends on wavelength, width, temperature, etc.
> - Two indices matter: the effective index (sets phase) and the group index (sets pulse speed and the spacing of spectral features).
> - Compact models are short fit formulas that capture this behaviour for circuit design.

## Background you need

### Light is a wave

Light is a wave of electric and magnetic fields that wiggle as it travels. Like any wave, it has:

- a **wavelength** $\lambda$: the distance between two crests. On silicon chips we usually use infrared light with $\lambda \approx 1.55\ \mu\text{m}$ (1550 nm). This band near 1550 nm is called the **C-band**, used in fibre-optic communication;
- a **frequency** $f$: how many crests pass a point per second;
- a speed: in vacuum, $c \approx 3 \times 10^{8}$ m/s, and $c = f\lambda$.

### Refractive index

Inside a material, light slows down. The **refractive index** $n$ says by how much: the speed is $c/n$. Glass (silica, SiO$_2$) has $n \approx 1.44$; silicon has $n \approx 3.47$ near 1550 nm. A larger $n$ means slower light. Inside the material the wavelength also shrinks to $\lambda/n$.

### Waveguides and modes

A **waveguide** is a strip of high-index material (silicon) surrounded by low-index material (oxide or air). Light stays trapped in the strip by **total internal reflection**: light hitting a boundary from the high-index side at a shallow angle bounces back completely. So the strip acts like a pipe for light.

Inside such a narrow pipe, light can only travel in a few fixed patterns, called **modes**. Think of a guitar string that can only vibrate in certain shapes. The simplest pattern is the **fundamental mode** (one bright blob in the middle). More complicated patterns are **higher-order modes**. A **single-mode** waveguide supports only the fundamental mode. **TE** (transverse electric) means the electric field points mainly sideways, parallel to the chip surface; "TE-like" admits that in a real waveguide this is only approximately true.

Two common silicon waveguide shapes appear today:

- a **strip waveguide**: a plain rectangle of silicon, here 220 nm tall and some hundreds of nm wide (e.g. 220 × 550 nm);
- a **rib waveguide** (also called ridge): a raised rib sitting on a thinner layer of silicon, the **slab**. Here the full height is 220 nm and the slab is 90 nm thick.

```
   strip                    rib
   +-----+                 +-----+
   | Si  | 220 nm          | Si  | 220 nm
 --+-----+--         +-----+     +-----+
   oxide             |  Si slab  90 nm |
                     +-----------------+
                          oxide
```

### Effective index

The mode is partly in the silicon and partly leaks into the oxide around it. So it "feels" an average index somewhere between 1.44 and 3.47. This average is the **effective index** $n_{eff}$. A mode squeezed mostly in the silicon has a high $n_{eff}$; a mode that spreads into the oxide has a lower one. Wider waveguides hold the light more tightly in silicon, so they have a higher $n_{eff}$.

### Phase and the propagation constant

As light travels a distance $L$, its wave goes through many cycles. The **phase** $\phi$ counts how far through its cycle the wave is, in radians ($2\pi$ = one full cycle). In a waveguide the phase grows by

$$\phi = \beta L, \qquad \beta = \frac{2\pi n_{eff}}{\lambda}.$$

$\beta$ is the **propagation constant**: radians of phase per metre. It is just "number of wavelengths per metre" ($n_{eff}/\lambda$) times $2\pi$.

### Writing waves with complex exponentials

Engineers write a wave's phase using Euler's formula $e^{-i\phi} = \cos\phi - i\sin\phi$. You can picture $e^{-i\phi}$ as an arrow of length 1 that rotates as $\phi$ grows. Multiplying a field by $e^{-i\beta L}$ means "rotate its phase by $\beta L$". Multiplying by a real number less than 1 shrinks the arrow (loss). The length of the arrow is called the magnitude, written $|\cdot|$.

### Field versus intensity

The equations work with the electric **field** $E$ (the wave's amplitude, an arrow with length and angle). What a detector measures is the **intensity** or power $I$, which is proportional to the field squared: $I \propto |E|^2$. So if the field is divided by $\sqrt{2}$, the power is divided by 2.

### Interference

When two waves meet, their fields add as arrows. If the arrows point the same way (phases equal), they add up: **constructive interference**, bright. If they point opposite ways (phase difference $\pi$), they cancel: **destructive interference**, dark. In between, you get something in between. Because power is the field squared, two equal fields in step give *four times* the power of one alone, and two out of step give zero.

### Loss

Real waveguides lose some light (scattering from rough sidewalls, absorption). The power decays as $e^{-\alpha L}$, where $\alpha$ is the **propagation loss** per unit length. Since power is field squared, the field decays as $e^{-\alpha L/2}$. That is why $\alpha/2$ appears in the field equations.

### Splitters and combiners

A **Y-branch** is a waveguide that forks into two (or two that merge into one). Used as a **splitter**, it sends half the power into each arm. A **directional coupler** does a similar job by placing two waveguides close together so light leaks from one to the other. Used backwards, either one is a **combiner**.

### Derivatives and Taylor expansions

A derivative $dn/d\lambda$ says how fast $n$ changes when $\lambda$ changes a little. The second derivative $d^2n/d\lambda^2$ says how fast that slope itself changes (the curvature).

A **Taylor expansion** approximates a smooth curve near a point $x_0$ by a polynomial: $f(x) \approx f(x_0) + f'(x_0)(x - x_0) + \tfrac{1}{2}f''(x_0)(x - x_0)^2 + \dots$. "First order" keeps up to the straight-line term; "second order" adds the curvature term. Over a small range this is very accurate.

### Phase velocity, group velocity and pulses

A single, endless pure-colour wave has crests that move at the **phase velocity** $v_p$. But real signals are **pulses**: short bursts made by adding many nearby colours together. The pulse's envelope (the "lump" carrying the information) moves at a different speed, the **group velocity** $v_g$.

Analogy: in a crowd of joggers, individual runners (crests) may drift forward or backward through the group, but the crowd as a whole (the pulse) moves at its own speed. If different colours travel at different speeds, the crests and the envelope move at different rates.

### Dispersion

**Dispersion** means "the index depends on wavelength". It has two sources:

- **material dispersion**: silicon's own index changes with wavelength;
- **waveguide dispersion**: even if silicon's index were fixed, a longer wavelength spreads further out of the silicon into the oxide, lowering $n_{eff}$. This comes from the geometry.

Dispersion is why a pulse spreads out as it travels: its different colours arrive at different times.

### Two ways to change the index on purpose

- The **thermo-optic effect**: heating silicon raises its refractive index. Slow (microseconds) but simple: put a small heater on the waveguide.
- The **plasma dispersion effect**: adding or removing free electrons and holes (charge carriers) in silicon changes its index. This can be done electrically in nanoseconds or faster, so it is used for high-speed modulators.

### Resonators (preview)

A **ring resonator** is a waveguide bent into a closed loop, placed next to a straight "bus" waveguide. Light at certain wavelengths goes round the loop and builds up (resonates); other wavelengths pass by. It is covered properly in §4.4, but its figure appears in today's packet.

> **Key takeaways:**
>
> - Light is a wave; phase grows as $\beta L$ with $\beta = 2\pi n_{eff}/\lambda$.
> - Power is field squared; fields add as arrows, which gives interference.
> - The effective index is the average index the mode feels; it depends on geometry and wavelength.
> - Pulses move at the group velocity, which differs from the phase velocity whenever there is dispersion.

## 4.3 Mach–Zehnder interferometer

> **In one sentence:** An MZI splits light into two waveguide arms and recombines it, and the output power goes up and down like a cosine as the phase difference between the arms changes.

### The layout

The device (the book's Figure 4.26, not included in this packet) is simple:

```
               arm 1: length L1, index n1
           +------------------------------+
  In ---- <  splitter          combiner    > ---- Out
           +------------------------------+
               arm 2: length L2 = L1 + dL, index n2
```

Light comes in, a splitter divides it equally into an upper and a lower arm, and a combiner merges the arms again. The splitter and combiner can be any type, for example Y-branches or directional couplers.

### The simple model

The book uses a model borrowed from a free-space **beam-splitter** (a half-silvered mirror for a flat, "plane" wave). It works for single-mode waveguides. We don't care about the detailed shape of the light inside each waveguide. We treat each arm as carrying a single number: one field value with a size and a phase.

### Step 1: split

The input has intensity $I_i$ and field $E_i$. An ideal splitter sends half the power to each arm. Half the power means the field is divided by $\sqrt{2}$:

$$E_1 = \frac{E_i}{\sqrt{2}}, \qquad E_2 = \frac{E_i}{\sqrt{2}}.$$

Check: $|E_1|^2 + |E_2|^2 = |E_i|^2/2 + |E_i|^2/2 = |E_i|^2$. No power is lost.

### Step 2: travel along the arms

Each arm has:

- a propagation constant $\beta_1 = 2\pi n_1/\lambda$ or $\beta_2 = 2\pi n_2/\lambda$, where $n_1, n_2$ are the effective indices of the two arms;
- a length $L_1$ or $L_2 = L_1 + \Delta L$, where $\Delta L$ is the extra length of the lower arm;
- a power loss $\alpha_1$ or $\alpha_2$ per unit length, so $\alpha/2$ for the field (as explained in the background; the book's Equation 3.9).

At the end of each arm, just before the combiner, the fields are:

$$E_{o1} = E_1 e^{-i\beta_1 L_1 - \frac{\alpha_1}{2}L_1} = \frac{E_i}{\sqrt{2}} e^{-i\beta_1 L_1 - \frac{\alpha_1}{2}L_1} \qquad (4.16\text{a})$$

$$E_{o2} = E_2 e^{-i\beta_2 L_2 - \frac{\alpha_2}{2}L_2} = \frac{E_i}{\sqrt{2}} e^{-i\beta_2 L_2 - \frac{\alpha_2}{2}L_2} \qquad (4.16\text{b})$$

**What this says:** each field starts at $E_i/\sqrt{2}$. The exponent has two parts. The imaginary part $-i\beta L$ rotates the phase by $\beta L$ (how many radians the wave went through). The real part $-\frac{\alpha}{2}L$ shrinks the field because of loss. You can split it as $e^{-i\beta L} \cdot e^{-\alpha L/2}$: "rotate" times "shrink".

### Step 3: combine

The combiner adds the two fields and again divides by $\sqrt{2}$ (an ideal Y-branch combiner, the splitter used backwards):

$$E_o = \frac{1}{\sqrt{2}}(E_{o1} + E_{o2}) = \frac{E_i}{2}\left(e^{-i\beta_1 L_1 - \frac{\alpha_1}{2}L_1} + e^{-i\beta_2 L_2 - \frac{\alpha_2}{2}L_2}\right) \qquad (4.17)$$

The two factors of $1/\sqrt{2}$ multiply to $1/2$.

### Step 4: output power

Power is the field magnitude squared. Since $|E_i/2|^2 = I_i/4$:

$$I_o = \frac{I_i}{4}\left|e^{-i\beta_1 L_1 - \frac{\alpha_1}{2}L_1} + e^{-i\beta_2 L_2 - \frac{\alpha_2}{2}L_2}\right|^2 \qquad (4.18)$$

This is the full answer, including loss. If the losses matter, you just put numbers into this formula on a computer.

### Step 5: the lossless case

To see the behaviour clearly, assume no loss ($\alpha_1 = \alpha_2 = 0$). Call the two phases $A = \beta_1 L_1$ and $B = \beta_2 L_2$. The trick is to pull out the average phase:

$$e^{-iA} + e^{-iB} = e^{-i\frac{A+B}{2}}\left(e^{-i\frac{A-B}{2}} + e^{+i\frac{A-B}{2}}\right) = e^{-i\frac{A+B}{2}} \cdot 2\cos\frac{A-B}{2}.$$

(The last step uses $e^{ix} + e^{-ix} = 2\cos x$.) The front factor has magnitude 1, so it disappears when we take $|\cdot|^2$. That gives:

$$I_o = \frac{I_i}{4}\left|2\cos\frac{\beta_1 L_1 - \beta_2 L_2}{2}\right|^2 \qquad (4.19\text{a})$$

$$= I_i \cos^2\frac{\beta_1 L_1 - \beta_2 L_2}{2} \qquad (4.19\text{b})$$

$$= \frac{I_i}{2}\left[1 + \cos(\beta_1 L_1 - \beta_2 L_2)\right] \qquad (4.19\text{c})$$

The last line uses the identity $\cos^2 x = \frac{1}{2}(1 + \cos 2x)$.

**What this says:** only the *phase difference* $\Delta\phi = \beta_1 L_1 - \beta_2 L_2$ between the arms matters.

- $\Delta\phi = 0$ (or any multiple of $2\pi$): $\cos = 1$, so $I_o = I_i$. All the light comes out. The two arrows line up.
- $\Delta\phi = \pi$: $\cos = -1$, so $I_o = 0$. The arrows point opposite ways and cancel. (The light isn't destroyed: in a Y-branch combiner it is thrown out into the substrate as radiation; in a 2-output coupler it goes to the other output.)
- In between: the output varies smoothly, like a cosine, between 0 and $I_i$.

### Why the output changes with wavelength: the free spectral range

If the arms have different lengths ($L_1 \neq L_2$, an **imbalanced** MZI), then the phase difference depends on wavelength, because $\beta = 2\pi n/\lambda$. As you sweep the wavelength, $\Delta\phi$ sweeps through many multiples of $2\pi$, and the output goes bright–dark–bright–dark. The output spectrum is a sinusoid.

The distance between two neighbouring bright peaks is called the **free spectral range** (FSR). For identical waveguides in the two arms (same $n$, only the length differs):

$$\text{FSR}\ [\text{Hz}] = \frac{c}{n_g \Delta L} \qquad (4.20\text{a})$$

$$\text{FSR}\ [\text{m}] = \frac{\lambda^2}{n_g \Delta L} \qquad (4.20\text{b})$$

Symbols: $c$ is the speed of light in vacuum; $\Delta L$ is the length difference; $n_g$ is the **group index** of the waveguide (explained in §3.2.9 below). The first form gives the FSR as a frequency spacing; the second as a wavelength spacing.

**Why this shape?** The peaks happen each time the extra path $\Delta L$ adds one more full cycle of phase. Making $\Delta L$ longer makes the phase difference change faster with wavelength, so peaks are closer together (smaller FSR). Note that the formula uses $n_g$, not $n_{eff}$. That is because, as the wavelength changes, $n_{eff}$ itself also changes, and $n_g$ is exactly the quantity that includes this effect (see Equation 3.5).

**Worked example.** Take $\lambda = 1.55\ \mu\text{m}$, $n_g = 4.2$ (typical for a strip waveguide, see Figure 3.22), and $\Delta L = 100\ \mu\text{m}$:

$$\text{FSR} = \frac{(1.55 \times 10^{-6})^2}{4.2 \times 100 \times 10^{-6}} \approx 5.7 \times 10^{-9}\ \text{m} = 5.7\ \text{nm}.$$

In frequency: $c/(n_g \Delta L) = 3\times10^{8}/(4.2 \times 10^{-4}) \approx 7.1 \times 10^{11}$ Hz $\approx 714$ GHz. So every 5.7 nm in wavelength the output goes through one full bright–dark cycle.

**Why it's useful:** this regular ripple is a handy measurement tool. Measure the FSR, and if you know $\Delta L$ you can work out $n_g$. For a modulator, you can see how far the ripple shifts when you apply a voltage; that gives the **tunability**, in picometres of shift per volt (pm/V).

### Using the MZI as a switch or modulator

Equation 4.19 also varies like a cosine with the effective indices $n_1$ and $n_2$. So instead of changing wavelength, you can keep the wavelength fixed and change the index of one arm:

- with the **thermo-optic effect** (a heater on one arm) you make a **thermo-optic switch** (book §3.1.1 and §6.6);
- with the **plasma dispersion effect** (moving charge carriers in or out) you make a fast **Mach–Zehnder modulator** (book §6.1.1), which turns an electrical data signal into light switching on and off.

A phase change of $\pi$ in one arm moves the output from fully on to fully off.

### Figure 4.27 (ring resonators)

**Figure 4.27 — Ring and racetrack resonators: (a) all-pass, (b) add-drop.** This figure belongs to the next section (§4.4) but appears in today's packet.

- **(a) All-pass ring.** One straight bus waveguide runs left to right, with ports labelled "In" and "Through". A circular ring sits just above it. Where they come close is the **coupling region**. Two numbers describe it: $\kappa_1$ (the **cross-coupling coefficient**: how much field jumps between bus and ring) and $t_1$ (the **self-coupling** or transmission coefficient: how much stays in its own waveguide). It is called "all-pass" because all light eventually exits through the one output; the ring only changes how much at each wavelength.
- **(b) Add-drop racetrack.** A **racetrack** is a ring stretched into a rounded rectangle (longer straight sections give stronger coupling). It sits between two bus waveguides. The bottom one has "In" and "Through" ports, with coupling $\kappa_1, t_1$. The top one has a "Drop" port (light leaves to the left), with coupling $\kappa_2, t_2$. At resonance, light is picked out of the bottom bus and sent to the Drop port.

```
 (a) all-pass               (b) add-drop
       ___                  Drop <------------
      /   \                       (=======)    k2, t2
      \___/   k1, t1              (=======)    k1, t1
  In ---------> Through     In ---------------> Through
```

**Lesson:** these are the two basic resonator layouts. At every point where a resonator meets a waveguide, two coefficients ($\kappa$, $t$) describe the coupling, and those are the key design knobs. Like the MZI, the ring's spectrum repeats with an FSR set by the group index.

> **Key takeaways:**
>
> - MZI output: $I_o = I_i\cos^2(\Delta\phi/2)$; only the phase difference between the arms matters.
> - An imbalanced MZI ($\Delta L \neq 0$) gives a sinusoidal spectrum with period $\text{FSR} = \lambda^2/(n_g \Delta L)$.
> - Measuring the FSR is a practical way to find the group index and modulator tunability (pm/V).
> - Changing one arm's index (by heat or by carriers) makes switches and modulators.
> - Ring resonators (all-pass, add-drop) are described by coupling coefficients $\kappa$ and $t$.

## 3.2.9 Wavelength dependence

> **In one sentence:** A waveguide's effective index falls as wavelength rises, and that slope creates a second, larger index, the group index, which sets how fast pulses travel and how far apart the peaks of interferometers and resonators are.

### What was simulated

The book uses a simulation script (Script 3.15, run in a mode-solver program, not reproduced in this packet). In outline it:

1. defines the waveguide cross-section (silicon on oxide, 220 nm thick, here a rib with a 90 nm slab);
2. loops over a range of wavelengths (a **wavelength sweep**);
3. at each wavelength, solves for the mode and records its effective index $n_{eff}$;
4. from the list of $n_{eff}$ values, computes the group index (Equation 3.5) and plots both.

Input: geometry, materials, wavelength range. Output: $n_{eff}(\lambda)$ and $n_g(\lambda)$ curves (Figure 3.21).

### Two speeds, two indices

$$v_p(\lambda) = \frac{c}{n_{eff}}, \qquad v_g(\lambda) = \frac{c}{n_g} \qquad (3.4)$$

- $v_p$ is the **phase velocity**: how fast the wave crests move. It is set by the effective index $n_{eff}$.
- $v_g$ is the **group velocity**: how fast a pulse (and so the information and energy) moves. It is set by the **group index** $n_g$.
- Both depend on $\lambda$, which is why they are written as functions of $\lambda$.

The group index is very important in chip design. It is $n_g$, not $n_{eff}$, that sets the **mode spacing**, i.e. the free spectral range, in resonators and interferometers. That is exactly why $n_g$ appeared in the MZI's FSR formula (4.20).

### Figure 3.20

**Figure 3.20 — Effective index of the TE modes versus width of a rib waveguide (220 nm silicon, 90 nm slab).** The horizontal axis is the rib width, from 200 to 800 nm. The vertical axis is the effective index, from 2.0 to 2.8. Four curves are shown, all TE modes:

| Curve | Behaviour | Approximate values |
|---|---|---|
| Top (fundamental mode) | Rises steadily, flattening out | 2.20 at 200 nm, 2.50 at 450 nm, 2.73 at 800 nm |
| Second (next mode) | Flat, then rises after a cutoff width | ~2.09–2.10 up to ~460 nm, 2.20 at 600 nm, 2.36 at 800 nm |
| Third | Almost constant | ~2.10–2.11 throughout |
| Fourth | Almost constant | ~2.09–2.10 throughout |

How to read it: each row is one mode; the numbers say how strongly that mode is held by the rib.

**Lesson:**

- The fundamental mode's $n_{eff}$ grows with width because a wider rib holds more of the light in silicon.
- The second mode only becomes a real rib-guided mode above a **cutoff** width (around 460–480 nm). Below that, it is not held by the rib.
- The flat curves near 2.1 are modes living mostly in the 90 nm slab. The slab is the same whatever the rib width, so their index hardly changes. The number ~2.1 is roughly the effective index of the slab by itself.
- Practical point: to stay single-mode in this rib, keep the width below roughly 460 nm (the book does not state a rule here, but this is what the plot implies).

### From effective index to group index

$$n_g(\lambda) = n_{eff}(\lambda) - \lambda\,\frac{dn_{eff}}{d\lambda} \qquad (3.5)$$

Symbols: $n_g$ is the group index; $n_{eff}$ the effective index; $dn_{eff}/d\lambda$ the slope of the effective index versus wavelength.

**What it says:** the group index equals the effective index plus a correction for how quickly $n_{eff}$ changes with colour. In silicon waveguides $n_{eff}$ *drops* as $\lambda$ rises, so the slope is negative, and $-\lambda\,dn_{eff}/d\lambda$ is *positive*. Therefore $n_g > n_{eff}$: pulses travel slower than the crests.

**Why that shape?** Where does it come from? Peaks of an interferometer occur when the phase $\beta L = 2\pi n_{eff} L/\lambda$ steps by $2\pi$. How fast this phase changes with wavelength depends both on the explicit $1/\lambda$ and on $n_{eff}$ changing with $\lambda$. Doing the derivative gives exactly $n_{eff} - \lambda\,dn_{eff}/d\lambda$. So $n_g$ is "the index that the phase *effectively* responds with when you change colour".

**Worked example** (using Equation 3.7 below, where the slope is $-0.85$ per µm and $n_{eff} = 2.57$ at 1.55 µm):

$$n_g = 2.57 - 1.55 \times (-0.85) = 2.57 + 1.32 \approx 3.89.$$

This matches Figure 3.21b (about 3.86–3.91). Notice: the group index (~3.9) is much larger than the effective index (~2.6) and even larger than bulk silicon's 3.47. This is because of strong waveguide dispersion: as wavelength grows the mode spreads quickly into the oxide.

### Simulation versus experiment

The book compares the simulated group index with one measured on a real ring resonator. Agreement is good only if:

- **(a)** the simulation **mesh** (the grid of points the computer uses to describe the cross-section) is fine enough, here 10 nm;
- **(b)** both **material dispersion** (silicon's own index changing with $\lambda$) and **waveguide dispersion** (geometry) are included.

Leaving out either kind of dispersion gives the wrong group index (see Figure 3.21 for how big the error is).

### Group velocity dispersion

If $n_g$ itself changes with wavelength, different colours inside a pulse travel at different speeds. The pulse spreads out as it goes. This is **group velocity dispersion**. It is measured by the **dispersion parameter**:

$$D(\lambda) = \frac{d\left(\frac{n_g}{c}\right)}{d\lambda} = -\frac{\lambda}{c}\,\frac{d^2 n_{eff}}{d\lambda^2} \qquad (3.6)$$

Symbols: $n_g/c = 1/v_g$ is the time a pulse takes to travel one metre. So $D$ is "how much extra delay per metre you get per unit change in wavelength". It is usually quoted in ps/(nm·km): picoseconds of spread per nanometre of signal bandwidth per kilometre of waveguide.

**Why the second form?** Differentiate Equation 3.5:

$$\frac{dn_g}{d\lambda} = \frac{dn_{eff}}{d\lambda} - \frac{dn_{eff}}{d\lambda} - \lambda\frac{d^2 n_{eff}}{d\lambda^2} = -\lambda\frac{d^2 n_{eff}}{d\lambda^2}.$$

Divide by $c$ and you get (3.6). So $D$ depends on the *curvature* of $n_{eff}(\lambda)$: one more derivative than $n_g$. The same simulation data give it for free.

### Effect of width

The book also simulates the fundamental TE-like mode for several widths, to see how width changes the wavelength dependence. Figure 3.22 is for strip waveguides (e.g. the standard 220 × 550 nm strip), and Figure 3.23 is for rib waveguides with a 90 nm slab. Both figures are described in the next section, where they appear.

> **Key takeaways:**
>
> - $v_p = c/n_{eff}$ (crest speed) and $v_g = c/n_g$ (pulse speed).
> - $n_g = n_{eff} - \lambda\,dn_{eff}/d\lambda$; in silicon waveguides $n_g$ (~3.9–4.4) is much bigger than $n_{eff}$ (~2.2–2.7).
> - $n_g$ sets the FSR of interferometers and resonators.
> - Accurate $n_g$ needs a fine mesh (10 nm) and both material and waveguide dispersion.
> - Pulse spreading is described by $D = -(\lambda/c)\,d^2 n_{eff}/d\lambda^2$.

## 3.2.10 Compact models for waveguides

> **In one sentence:** Instead of re-running a slow simulation every time, designers fit the waveguide's index to a short polynomial in wavelength (and temperature, width, …) and use that formula when designing circuits.

### Why compact models?

For designing devices (e.g. ring resonators) and whole systems, you want to know $n_{eff}$ at any wavelength or temperature instantly. A **compact model** is a short formula with a few **phenomenological** parameters: numbers chosen to match the data, not derived from deep theory. When there is no obvious physical formula, a Taylor expansion (a polynomial around a central point) is a good, general choice.

### Figure 3.21

**Figure 3.21 — Effective and group index of the rib waveguide (220 nm silicon, 90 nm slab) versus wavelength, with experiment.**

- **Panel (a), effective index.** Horizontal axis: wavelength 1.51–1.60 µm. One simulated line, falling in a straight line from about 2.61 (at 1.51 µm) to about 2.525 (at 1.60 µm).
- **Panel (b), group index.** Three curves:

| Curve | At ~1.51 µm | At end of range | Shape |
|---|---|---|---|
| Experiment, 30 µm ring | ~3.92 | ~3.885 (at 1.57 µm) | Falling, with small ripples (measurement noise) |
| Simulation, dispersive silicon | ~3.91 | ~3.858 (at 1.60 µm) | Smooth straight decline |
| Simulation, constant $n_{Si} = 3.47$ | ~3.77 | ~3.755 (at 1.60 µm) | Smooth, much lower |

How to read the table: compare each simulation row with the experiment row.

**Lesson:** both indices fall as wavelength rises. The simulation that uses silicon's real, wavelength-dependent index matches the measurement closely. The simulation that pretends silicon's index is a constant 3.47 underestimates $n_g$ by about 0.13 (roughly 3–4%). That may sound small, but it would put every predicted FSR off by the same percentage. So material dispersion must be included.

### A first-order model

For the waveguide of Figure 3.21, a straight line is good enough:

$$n_{eff}(\lambda) = 2.57 - 0.85\,(\lambda\,[\mu\text{m}] - 1.55) \qquad (3.7)$$

Symbols: $\lambda$ is in micrometres; 1.55 µm is the centre point; 2.57 is $n_{eff}$ at that centre; $-0.85$ per µm is the slope $dn_{eff}/d\lambda$.

**Example:** at $\lambda = 1.56$ µm, $n_{eff} = 2.57 - 0.85 \times 0.01 = 2.5615$. A 10 nm change in wavelength changes $n_{eff}$ by less than 0.01, but that is still enough to shift the phase in a long waveguide by many radians. And as shown above, this one line also gives $n_g \approx 3.89$.

### A model in wavelength and temperature

The index also depends on temperature $T$. The recipe:

1. Simulate $n_{eff}$ at many wavelengths and at several temperatures $T_i$.
2. At each temperature, fit a second-order Taylor polynomial in wavelength.
3. Each of the three resulting coefficients changes with temperature, so fit each of them with a second-order polynomial in temperature.

The result is:

$$n_{eff}(\lambda, T) = N_0(T) + N_1(T)\left(\frac{\lambda - \lambda_0}{\sigma_\lambda}\right) + N_2(T)\left(\frac{\lambda - \lambda_0}{\sigma_\lambda}\right)^2 \qquad (3.8)$$

with

$$N_0(T) = n_0 + n_1\left(\frac{T - T_0}{\sigma_T}\right) + n_2\left(\frac{T - T_0}{\sigma_T}\right)^2$$

$$N_1(T) = n_3 + n_4\left(\frac{T - T_0}{\sigma_T}\right) + n_5\left(\frac{T - T_0}{\sigma_T}\right)^2$$

$$N_2(T) = n_6 + n_7\left(\frac{T - T_0}{\sigma_T}\right) + n_8\left(\frac{T - T_0}{\sigma_T}\right)^2$$

Symbols:

- $\lambda_0$, $T_0$: the centre wavelength and centre temperature that the expansion is built around;
- $\sigma_\lambda$, $\sigma_T$: scaling constants. Dividing by them turns $\lambda - \lambda_0$ and $T - T_0$ into dimensionless numbers of order 1, so the fit coefficients all have similar sizes and the fit is numerically well behaved;
- $N_0(T)$: the index at the centre wavelength (it changes with temperature);
- $N_1(T)$: the slope with wavelength (it also changes with temperature);
- $N_2(T)$: the curvature with wavelength;
- $n_0, \dots, n_8$: nine fitted numbers. These nine numbers are the whole model.

**What it says:** "a quadratic in wavelength, whose three coefficients are each a quadratic in temperature." Altogether this is a polynomial in both variables. Once you have the nine numbers, you can get $n_{eff}$ at any wavelength and temperature near the centre point instantly. Equation 3.7 is the simplest special case: drop temperature and curvature, and keep $N_0 = 2.57$ and a slope.

### Figure 3.22 (strip waveguide)

**Figure 3.22 — Effective and group index of 220 nm strip waveguides versus wavelength, for widths 400–600 nm.**

| Width | $n_{eff}$ at 1.5 µm | $n_{eff}$ at 1.6 µm | $n_g$ (roughly flat) |
|---|---|---|---|
| 400 nm | 2.32 | 2.16 | ~4.37 → 4.36 |
| 450 nm | 2.42 | 2.29 | ~4.27 |
| 500 nm | 2.51 | 2.39 | ~4.17–4.18 |
| 550 nm | 2.56 | 2.47 | ~4.10 |
| 600 nm | 2.59 | 2.53 | ~4.04–4.05 |

How to read it: each row is one width; the first two numbers show how $n_{eff}$ drops across the wavelength range, and the last column gives the group index.

**Lesson:**

- $n_{eff}$ falls with wavelength for every width, and wider waveguides have higher $n_{eff}$ (light held more in silicon).
- Narrow waveguides have a *steeper* fall in $n_{eff}$ (400 nm drops 0.16; 600 nm drops only 0.06). In a narrow guide, a longer wavelength pushes much more light out into the oxide.
- That steeper slope means a larger $n_g$, which is why $n_g$ goes *down* as width goes *up*: from about 4.37 (400 nm) to about 4.05 (600 nm).
- $n_g$ barely changes with wavelength here: low group velocity dispersion over this range.
- Strip waveguides have higher group indices (~4.0–4.4) than the rib waveguides below (~3.8–3.9).

### Figure 3.23 (rib waveguide)

**Figure 3.23 — Effective and group index of rib waveguides (220 nm silicon, 90 nm slab) versus wavelength, for widths 400–600 nm.**

| Width | $n_{eff}$ at 1.5 µm | $n_{eff}$ at 1.6 µm | $n_g$ at 1.5 µm | $n_g$ at 1.6 µm |
|---|---|---|---|---|
| 400 nm | 2.51 | 2.425 | 3.89 | 3.815 |
| 450 nm | 2.56 | 2.475 | 3.905 | 3.845 |
| 500 nm | 2.61 | 2.53 | 3.91 | 3.855 |
| 550 nm | 2.645 | 2.565 | 3.90 | 3.855 |
| 600 nm | 2.67 | 2.60 | 3.885 | 3.85 |

How to read it: same as before, but now both indices are given at each end of the wavelength range.

**Lesson:**

- As before, both indices fall as wavelength rises, and $n_{eff}$ rises with width.
- Unlike the strip, the group index does not simply fall with width. It is highest around 500 nm and lower on both sides. So $n_g$ depends on width in a more complicated way in a rib.
- In the rib, $n_g$ changes more with wavelength than in the strip (the 400 nm rib falls from 3.89 to 3.815, the steepest slope).
- The group indices span a small range (~3.8–3.9), smaller than the strip's (~4.0–4.4): the rib is less sensitive to width.

### How much to put in the model

Many more parameters can be included in a compact model: wavelength, temperature, silicon thickness, waveguide width, slab thickness of a rib (ridge) waveguide, **carrier density** (how many free electrons and holes are present, relevant to modulators), and **optical nonlinearity** (index changes caused by the light's own intensity). Each extra variable adds coefficients. The designer must decide how complex the model needs to be for the problem at hand: no more than needed, but enough to be accurate.

### Example use: grating design

One use is designing an optical **grating** (a waveguide whose width is periodically varied to reflect certain wavelengths) so that it has a desired spectrum. Because such a design necessarily varies the waveguide width, the compact model must include both wavelength and width dependence. This is worked out in the book's §4.5.2.

> **Key takeaways:**
>
> - A compact model is a short fit formula (often a Taylor polynomial) for $n_{eff}$.
> - For the 220 nm rib: $n_{eff} \approx 2.57 - 0.85(\lambda - 1.55)$, which also gives $n_g \approx 3.89$.
> - Equation 3.8 uses nine numbers to capture both wavelength and temperature dependence.
> - Strip: $n_g$ falls with width (4.37 → 4.05). Rib: $n_g$ ~3.8–3.9, peaking near 500 nm width.
> - Ignoring silicon's material dispersion underestimates $n_g$ by ~0.13; choose model complexity to suit the task.

## Glossary

| Term | Plain meaning |
|---|---|
| Add-drop resonator | A ring or racetrack between two bus waveguides; at resonance it moves light from the input bus to a "drop" port. |
| All-pass resonator | A ring next to a single bus waveguide; all light leaves through one port, but the ring changes the phase/amount at each wavelength. |
| Beam-splitter | A device (e.g. half-silvered mirror) that divides one beam into two. |
| Bus waveguide | The straight waveguide that carries light past a resonator. |
| C-band | The wavelength band around 1530–1565 nm used in fibre communications. |
| Carrier density | Number of free electrons and holes per volume in a semiconductor. |
| Combiner | A device that merges two waveguides into one. |
| Compact model | A short formula with fitted parameters that predicts a device's behaviour quickly. |
| Constructive / destructive interference | Waves adding up (in step) / cancelling (out of step). |
| Coupling coefficient ($\kappa$) | Fraction of field that crosses between two neighbouring waveguides. |
| Cutoff | The width (or wavelength) at which a mode starts or stops being guided. |
| Directional coupler | Two waveguides placed close together so light transfers between them. |
| Dispersion | Index (and so speed) depending on wavelength. |
| Dispersion parameter ($D$) | How much a pulse's delay changes per unit wavelength per length; measures pulse spreading. |
| Effective index ($n_{eff}$) | The average refractive index that a guided mode "feels"; sets the phase speed. |
| Free spectral range (FSR) | The spacing between repeating peaks in the spectrum of an interferometer or resonator. |
| Fundamental mode | The simplest light pattern a waveguide carries, one bright spot. |
| Grating | A waveguide with a periodic change (e.g. width) that reflects certain wavelengths. |
| Group index ($n_g$) | $n_{eff} - \lambda\,dn_{eff}/d\lambda$; sets the pulse speed and the FSR. |
| Group velocity ($v_g$) | Speed of a pulse (information, energy): $c/n_g$. |
| Group velocity dispersion | Group velocity changing with wavelength, which spreads pulses. |
| Imbalanced MZI | An MZI whose two arms have different lengths. |
| Intensity ($I$) | Optical power; proportional to the field squared. |
| Mach–Zehnder interferometer (MZI) | Device that splits light into two arms and recombines it, so the output depends on the phase difference. |
| Material dispersion | Wavelength dependence of the material's own refractive index. |
| Mesh | The grid of points a simulation uses; finer mesh, more accurate result. |
| Mode | A stable pattern in which light travels along a waveguide. |
| Modulator | Device that puts an electrical signal onto light by changing its intensity or phase. |
| Optical nonlinearity | Index changes caused by the intensity of the light itself. |
| Phase | Position within a wave's cycle, in radians. |
| Phase velocity ($v_p$) | Speed of the wave crests: $c/n_{eff}$. |
| Phenomenological parameter | A fitted number that matches data, not derived from first-principles theory. |
| Plasma dispersion effect | Change in silicon's index caused by free electrons and holes; used in fast modulators. |
| Propagation constant ($\beta$) | Phase gained per metre: $2\pi n_{eff}/\lambda$. |
| Propagation loss ($\alpha$) | Fraction of power lost per unit length (power decays as $e^{-\alpha L}$). |
| Racetrack resonator | A ring stretched to have straight sections, giving longer coupling regions. |
| Refractive index ($n$) | How much a material slows light: speed $= c/n$. |
| Rib (ridge) waveguide | A silicon rib on top of a thinner silicon slab. |
| Ring resonator | A looped waveguide where certain wavelengths build up by circulating. |
| Self-coupling coefficient ($t$) | Fraction of field that stays in its own waveguide at a coupling region. |
| Single-mode | A waveguide that carries only the fundamental mode. |
| Slab | The thin silicon layer under and beside a rib waveguide. |
| Splitter | Device dividing light from one waveguide into two. |
| Strip waveguide | A plain rectangular silicon waveguide. |
| Taylor expansion | Approximating a curve near a point by a polynomial (constant, slope, curvature, …). |
| TE mode | Mode with its electric field mainly parallel to the chip surface. |
| Thermo-optic effect | Index change with temperature; used for heater-based tuning and switches. |
| Tunability (pm/V) | How far a spectrum shifts per volt applied. |
| Waveguide | A strip of high-index material that traps and guides light. |
| Waveguide dispersion | Wavelength dependence of $n_{eff}$ caused by the geometry (mode spreading). |
| Y-branch | A waveguide fork that splits or combines light 50/50. |

## Check yourself

**1. In a lossless MZI, what is the output power when the phase difference between the arms is $\pi$? When it is $2\pi$?**

*Answer:* $I_o = I_i\cos^2(\Delta\phi/2)$. For $\Delta\phi = \pi$, $\cos^2(\pi/2) = 0$, so no light comes out. For $2\pi$, $\cos^2\pi = 1$, so all the light comes out.

**2. Why does the field get divided by $\sqrt{2}$, not 2, at a 50/50 splitter?**

*Answer:* Power is the field squared. Half the power means $|E|^2$ halves, so $E$ is divided by $\sqrt{2}$.

**3. Why does $\alpha/2$ appear in the field equations when $\alpha$ is the loss?**

*Answer:* $\alpha$ is the loss of power (intensity). Since power is field squared, the field decays half as fast in the exponent: $e^{-\alpha L/2}$.

**4. An imbalanced MZI has $\Delta L = 200\ \mu\text{m}$ and $n_g = 4.0$. What is its FSR at 1.55 µm?**

*Answer:* $\lambda^2/(n_g\Delta L) = (1.55\times10^{-6})^2/(4.0 \times 2\times10^{-4}) \approx 3.0\times10^{-9}$ m, i.e. about 3 nm.

**5. Which index sets the FSR: effective or group? Why?**

*Answer:* The group index. As you change wavelength to go from one peak to the next, $n_{eff}$ itself changes too; $n_g = n_{eff} - \lambda\,dn_{eff}/d\lambda$ includes this extra effect.

**6. Using $n_{eff}(\lambda) = 2.57 - 0.85(\lambda - 1.55)$, estimate $n_g$ at 1.55 µm.**

*Answer:* $n_g = 2.57 - 1.55 \times (-0.85) \approx 3.89$.

**7. Why is the group index of a silicon waveguide (~3.9–4.4) larger than the index of bulk silicon (3.47)?**

*Answer:* Strong waveguide dispersion: $n_{eff}$ falls quickly with wavelength because longer wavelengths spread into the oxide. The term $-\lambda\,dn_{eff}/d\lambda$ is large and positive, which pushes $n_g$ above both $n_{eff}$ and silicon's own index.

**8. In Figure 3.21b, what goes wrong if silicon's index is treated as a constant 3.47?**

*Answer:* The simulated group index is about 3.76 instead of about 3.89, well below the measured value. Material dispersion must be included to predict $n_g$ correctly.

**9. For a strip waveguide, does $n_g$ go up or down when you make it wider? Why?**

*Answer:* Down (about 4.37 at 400 nm to about 4.05 at 600 nm). A wider guide holds light more firmly, so $n_{eff}$ changes less with wavelength, making the correction term in $n_g$ smaller.

**10. How many fitted numbers does the wavelength–temperature compact model (3.8) have, and what does each group of three describe?**

*Answer:* Nine ($n_0$ to $n_8$). $n_0$–$n_2$ give the index at the centre wavelength vs temperature; $n_3$–$n_5$ give the wavelength slope vs temperature; $n_6$–$n_8$ give the wavelength curvature vs temperature.
