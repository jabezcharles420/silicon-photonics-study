# Week 4 · Day 3 — Wednesday 14 Oct 2026

*Simple-English study version of Chrostowski & Hochberg §5.2 (Grating coupler: what it is, performance, theory, design methodology, experimental results)*

[:material-file-pdf-box: Download this day as PDF](day-03-wed-14-oct-2026.pdf){ .md-button }

## Before you start: the big picture

A silicon photonic chip carries light in tiny "wires" of silicon called **waveguides**. A typical one is about 0.5 µm wide and 0.22 µm tall. That is roughly 200 times thinner than a human hair. But light usually arrives at the chip through an **optical fibre**, whose light-carrying core is about 9 µm across. So we have a plumbing problem: we must connect a fat pipe (the fibre) to a very thin pipe (the waveguide), and they don't even point the same way. The fibre usually sits *above* the chip, looking down. The waveguide runs *flat along* the chip surface.

A **grating coupler** solves this. It is a patch of evenly spaced grooves cut into the silicon, like a tiny washboard. When light travelling along the waveguide hits the grooves, each groove scatters a little light upward. If the spacing is chosen correctly, all those small scattered waves add up in step and form one strong beam that leaves the chip at a chosen angle, straight into a fibre held above. It also works in reverse: light from the fibre comes down, hits the grooves, and is steered sideways into the waveguide.

Analogy: think of a row of people along a beach, each throwing a pebble into the water one after the other, at a steady rhythm, as a runner passes them. The ripples from all the pebbles merge into one big wave front heading out to sea at a definite angle. The angle depends on how fast the runner goes and how far apart the people stand. In a grating coupler, the "runner" is the light in the waveguide, the "people" are the grooves, and the merged wave front is the beam going to the fibre. Grating couplers are the most common way to get light on and off a silicon photonic chip, especially for testing many devices on a wafer, because the fibre can be placed anywhere on the surface. This packet explains how they work, how to measure how good they are, how to design one step by step, and how a real one performed.

## Background you need

### Light is a wave

Light is a wave of electric and magnetic fields. Like a water wave, it has crests and troughs. The distance from one crest to the next is the **wavelength**, written $\lambda$ (Greek "lambda"). In this packet, the wavelength in empty space (vacuum) is written $\lambda_0$ or just $\lambda$. Telecom light is near $\lambda_0 = 1550$ nm (1.55 µm), which is infrared and invisible to us. Another common telecom band is near 1310 nm.

### Refractive index: how much a material slows light

Light travels at speed $c$ in vacuum. In a material it travels slower, at $c/n$. The number $n$ is the **refractive index**. Air: $n \approx 1$. Glass (silicon dioxide, SiO$_2$, also called **oxide**): $n \approx 1.44$. Silicon: $n \approx 3.48$. When light slows down, its crests bunch up, so the wavelength *inside* the material becomes $\lambda_0 / n$. Example: 1550 nm light in silicon has a wavelength of about $1550/3.48 \approx 445$ nm.

### Phase, interference, and Huygens' idea

**Phase** says where you are in the wave cycle (crest, trough, or in between). When two waves meet:

- If crest meets crest, they add up. This is **constructive interference** (bright).
- If crest meets trough, they cancel. This is **destructive interference** (dark).

The **Huygens–Fresnel principle** says: every point that a wave touches acts like a tiny new source sending out little circular ripples ("wavelets"). The wave you see later is the sum of all these wavelets. A grating coupler is a direct use of this idea: every groove is a little source, and the outgoing beam goes in whatever direction their wavelets add up constructively.

### Wave vector: "how fast the phase changes in space"

It is useful to describe a wave by its **wave vector** $k$ (also called **wavenumber**). Its size is

$$k = \frac{2\pi}{\text{wavelength}}$$

It counts how many radians of phase the wave goes through per metre (one full cycle is $2\pi$ radians). It also points in the direction the wave travels. So it is an arrow (a **vector**). In vacuum, $k_0 = 2\pi/\lambda_0$. In a material with index $n$, $k = 2\pi n/\lambda_0 = n k_0$. A tilted wave's arrow can be split into a horizontal part $k_x$ and a vertical part $k_z$, just like splitting a force into components. Physicists also think of $k$ as the light's **momentum** (up to a constant). That is why people say the grating "gives momentum" to the light.

### Snell's law: bending at a boundary

When light crosses from a material with index $n_1$ into one with index $n_2$, it bends. **Snell's law** says

$$n_1 \sin\theta_1 = n_2 \sin\theta_2$$

where each angle is measured from the **surface normal** (the line perpendicular to the surface). Why: along the boundary the crests on both sides must line up, so the horizontal part of the wave vector, $n k_0 \sin\theta$, must be the same on both sides. That "the horizontal part must match" idea is exactly the idea behind the grating coupler too.

### Total internal reflection and waveguides

If light in a high-index material hits a boundary with a low-index material at a shallow enough angle, Snell's law has no solution. The light is then fully reflected. This is **total internal reflection**. A **waveguide** uses it: a high-index core (silicon) surrounded by low-index material (oxide or air) traps light, which bounces along inside. A **slab waveguide** is a flat sheet of silicon that confines light only in the vertical direction. It is infinitely wide sideways (approximately).

### Modes and effective index

Light in a waveguide can only travel in certain stable field patterns called **modes**. The simplest, with one smooth bump of light in the middle, is the **fundamental mode**. Each mode travels along the guide as if it were in a uniform material with some index between the core and cladding values. That number is the **effective index**, $n_{eff}$. Part of the mode's light sits in silicon (high index) and part leaks into oxide or air (low index), so $n_{eff}$ is a kind of weighted average. For a 220 nm silicon slab at 1550 nm, $n_{eff} \approx 2.85$.

The mode's wave vector along the guide is called the **propagation constant**, $\beta$:

$$\beta = n_{eff} k_0 = \frac{2\pi n_{eff}}{\lambda_0}$$

A thinner silicon layer holds the light less tightly, so more light leaks into the cladding and $n_{eff}$ goes down.

$n_{eff}$ also changes with wavelength. This is called **dispersion**.

### Polarization: TE and TM

Light's electric field points in some direction across the travel direction. That direction is its **polarization**. In a flat waveguide:

- **TE** (transverse electric): the electric field lies mostly in the plane of the chip (sideways). "Quasi-TE" means "mostly TE" in a real 3D guide.
- **TM** (transverse magnetic): the electric field points mostly up and down.

TE and TM modes have very different $n_{eff}$ in thin silicon. In free space, the matching terms are **s** and **p** polarization (field parallel to the surface, or in the plane of incidence).

### Silicon-on-insulator (SOI) wafer

The chip is made on an **SOI wafer**. From top to bottom:

```
   cladding (oxide, or air)          protects the device
   Si device layer, ~220 nm          the waveguides live here
   BOX (buried oxide), ~2 um         low-index layer under the guide
   Si substrate, ~hundreds of um     thick mechanical support
```

**Cladding** is the layer on top. **BOX** stands for buried oxide. **Etching** means removing material. A **full etch** cuts all the way through the 220 nm silicon. A **shallow etch** cuts only part of the way, for example 70 nm, leaving 150 nm.

### Diffraction gratings

A **grating** is a structure that repeats regularly with a **period** $\Lambda$ (capital "Lambda", the repeat distance). Light hitting a grating splits into a few beams at definite angles, called **diffraction orders** and labelled by an integer $m$ (1st order, 2nd order...). The grating behaves as if it adds or removes a fixed "kick" of wave vector, $K = 2\pi/\Lambda$, or a whole multiple $mK$. $K$ is the **grating vector**.

The **Bragg condition** is the rule that says which orders exist and at which angles: the horizontal phase of the incoming wave, minus a whole number of grating kicks, must match the horizontal phase of the outgoing wave. If an order is sent straight backward, the grating acts as a mirror. This is **Bragg reflection**.

### Decibels (dB)

Power ratios in optics are almost always given in **decibels**:

$$\text{ratio in dB} = 10 \log_{10}\left(\frac{P_{\text{out}}}{P_{\text{in}}}\right)$$

Handy values to remember:

| Power ratio | dB |
|---|---|
| 1 (all of it) | 0 dB |
| 0.79 | −1 dB |
| 0.5 (half) | −3 dB |
| 0.1 | −10 dB |
| 0.01 | −20 dB |
| 0.001 | −30 dB |

Negative dB means you lost power. "Loss of 3 dB" and "−3 dB" are used loosely to mean the same thing. Each −10 dB is another factor of 10 smaller.

### Fabry–Pérot oscillation

If light bounces back and forth between two partial mirrors, the bounced copies interfere. At some wavelengths they add, at others they cancel. The measured transmission then shows a ripple versus wavelength. This is a **Fabry–Pérot** effect (named after an instrument built from two mirrors). Two grating couplers at either end of a test waveguide can act as those two mirrors, which spoils measurements.

### Optical fibre

A standard single-mode **optical fibre** is a glass thread with a core (slightly higher index) about 9 µm across, inside a glass cladding. Its fundamental mode is a roughly bell-shaped (**Gaussian**) spot of light. For grating couplers, the fibre end is often **polished** at an angle so it can lie at a tilt, or several fibres are held side by side in a **fibre array** (ribbon).

### Simulation words: FDTD, PML, monitors

**FDTD** (finite-difference time-domain) is a computer method that chops space into a fine grid and steps Maxwell's equations (the laws of light) forward in time. You get the full light field everywhere. **2D FDTD** pretends the structure is infinitely long in one direction, which is much faster. **3D FDTD** is the real thing, but costs far more memory and time. A **PML** (perfectly matched layer) is an artificial absorbing border around the simulation, so light that leaves does not bounce back from the edge. A **power monitor** records how much power crosses a line or surface. A **mode expansion monitor** measures how much of that power is in one particular mode, such as the fibre's fundamental mode. A **parameter sweep** means running the simulation many times, changing one value each time.

### Mask layout words

To make a chip, the designer draws the shapes to be etched. This drawing is the **mask layout**, often saved in a file format called **GDS**. A **parameterized cell (PCell)** is a small program that draws a shape automatically from a few numbers you type in (period, wavelength, etc.).

> **Key takeaways:**
>
> - Light's wave vector $k = 2\pi n/\lambda_0$ measures how quickly phase changes in space. Inside a waveguide it is $\beta = n_{eff} k_0$.
> - At any boundary, the horizontal part of the wave vector must match. A grating can add or remove multiples of $K = 2\pi/\Lambda$ to make that matching possible.
> - Losses and reflections are given in dB: −3 dB is half the power, −10 dB is a tenth.

## 5.2 Grating coupler

> **In one sentence:** A grating coupler is a periodic set of grooves in the silicon that tips light out of the flat waveguide toward a fibre above the chip (or tips fibre light into the waveguide), and we judge it by how much light ends up where we want it.

### What is a grating coupler?

A grating coupler is a **periodic structure** (a pattern that repeats). It **diffracts** light: it takes light travelling *in plane* (along the chip, inside the waveguide) and redirects it *out of plane* (up into free space). It is mainly used as an **I/O device** (input/output device) between a fibre (or a free-space beam) and the sub-micrometre waveguides on an SOI chip.

The thickness of the silicon device layer and of the BOX are fixed by which wafer you buy (book Section 3.1). A cladding layer usually covers the silicon. It protects it and allows metal wiring layers to be built on top. In some uses, such as sensors that detect molecules touching the waveguide's outer field (the **evanescent field**, the part of the mode that pokes outside the core), the cladding is left as air or liquid instead.

**Figure 5.1 — Cross-section of a grating coupler.** The picture is a side view (a slice through the chip). The vertical axis is $z$ (up). The horizontal axis is $x$, the direction light travels in the waveguide. From top to bottom the layers are: cladding, Si, BOX, Si substrate. Inside the Si layer on the right is a row of rectangular teeth (the grating). On the left, a red bell curve labelled $P_{wg}$ shows the light mode travelling right inside the waveguide. Blue arrows show where the power goes:

- $P_{up}$: a big arrow going up and to the right. This is the useful light leaving toward the fibre.
- $P_{down}$: an arrow going down and left, into the BOX.
- $P_{sub}$: an arrow going down into the silicon substrate (lost).
- A curved arrow (labelled $P_{box}$ in the rendering) shows light bouncing off the BOX–substrate boundary back up toward the grating.

Dimension arrows mark the period $\Lambda$, the tooth width $w$, and the etch depth $ed$. An angle $\theta$ is marked between the outgoing beam and the vertical.

```
          P_up  /  (to fibre, at angle theta from vertical)
               /
 cladding     /
 ---------  _   _   _   _  ------------
 Si  ==>   | |_| |_| |_| |    <- teeth, period Lambda, etch depth ed
 --------------------------------------
 BOX        \  P_down
 --------------------------------------
 Si substrate  P_sub (lost)
```

*Lesson:* the grating does not send all the light up. Some goes down into the wafer and is wasted. Reflections from the layers below can also come back up. A good design maximizes $P_{up}$, and more precisely the part of it that fits into the fibre.

### The design parameters

- The coupler is built from a silicon waveguide core, a **top cladding** (oxide or air), a **bottom cladding** (the BOX), and a silicon **substrate**. The slab's effective index is $n_{eff}$.
- $\Lambda$ is the **period** of the grating: the distance from one tooth to the next.
- $W$ is the **width of a tooth** (for a uniform grating, where all teeth are the same).
- $ff$ is the **fill factor** (also called **duty cycle**): $ff = W/\Lambda$. It is the fraction of each period that is unetched tooth. Example: $\Lambda = 660$ nm, $W = 330$ nm gives $ff = 0.5$.
- $ed$ is the **etch depth**: how deep the grooves are cut.
- $\theta_c$ is the angle between the surface normal and the diffracted beam, measured *in the cladding*.
- $\theta_{air}$ is the same angle measured *in air*.
- $\theta_{fibre}$ is the same angle *in the fibre*. This equals the angle at which the fibre end is polished.

The three angles differ because the beam bends (Snell's law) each time it crosses between materials of different index.

### How we measure a grating coupler

For an *output* coupler (light goes waveguide → fibre): $P_{wg}$ is the power coming in along the waveguide, $P_{up}$ is the power going up, $P_{down}$ is the power going down into the wafer. Not drawn: the fibre, and $P_{fibre}$, the power that actually ends up in the fibre's fundamental mode. $P_{fibre}$ is smaller than $P_{up}$, because the upward beam's shape never perfectly matches the fibre's mode.

Six numbers describe performance:

1. **Directionality.** How much of the input goes up: $10\log_{10}(P_{up}/P_{wg})$ in dB.
2. **Insertion loss (coupling efficiency).** How much ends up in the fibre's fundamental mode: $IL = 10\log_{10}(P_{fibre}/P_{wg})$. This is the most important number. Example: if 50% reaches the fibre, $IL = 10\log_{10}(0.5) = -3$ dB.
3. **Penetration loss.** How much is lost downward into the substrate: $10\log_{10}(P_{down}/P_{wg})$. (The book's wording says "power lost in the substrate, $P_{sub}$", but writes the formula with $P_{down}$. Both refer to the downward-lost light.)
4. **Reflection to the waveguide** (**back reflection** or **optical return loss**). The grating's index changes act like small mirrors, so some light bounces back into the waveguide: $10\log_{10}(P_{back-wg}/P_{wg})$. This is unwanted. On a test chip, light goes in through one grating and out through another. If both reflect, light bounces back and forth between them and causes Fabry–Pérot ripples in the measured spectrum. Designers usually want this reflection suppressed by **20–30 dB** (that is, only 1% to 0.1% reflected).
5. **Reflection to the fibre.** For an *input* coupler, some light bounces back up into the fibre: $10\log_{10}(P_{back-fibre}/P_{in-fibre})$, also called optical return loss. This is unwanted because light returning into the laser can make the laser unstable.
6. **1 dB or 3 dB bandwidth.** The coupler works best at one wavelength. The **1 dB (or 3 dB) bandwidth** is the range of wavelengths over which the insertion loss stays within 1 dB (or 3 dB) of its best value. Wider is usually better.

> **Key takeaways:**
>
> - A grating coupler redirects light between the flat waveguide and a fibre above the chip, using a row of etched teeth defined by period $\Lambda$, fill factor $ff = W/\Lambda$, and etch depth $ed$.
> - Light can go up (wanted), down into the substrate (lost), back into the waveguide (reflection), or up but with the wrong shape (mode mismatch).
> - Insertion loss $IL = 10\log_{10}(P_{fibre}/P_{wg})$ is the headline number. Back reflection should be 20–30 dB down.

## 5.2.1 Performance

> **In one sentence:** Grating couplers lose light mainly in three ways — light leaking down into the substrate, the beam shape not matching the fibre, and light bouncing back — and each has a known fix.

Many research groups have worked hard on making grating couplers more efficient. The three main losses are:

1. **Penetration loss (light going down).** A grating is roughly symmetric up/down, so it naturally throws light both ways. With a **shallow etch**, about **30%** of the energy goes into the substrate. With a **full etch**, this can exceed **50%**. Fix: put a mirror under the grating, buried in the substrate. This can be a metal layer, or a **distributed Bragg reflector (DBR)**, which is a stack of alternating thin layers whose small reflections all add up in step to make a strong mirror.
2. **Mode mismatch (~10% loss).** A simple uniform grating sends out light that is strong at the start and fades along the grating (exponential decay), because the waveguide light is used up as it goes. A fibre mode is a symmetric bell shape. The two shapes don't overlap perfectly, which costs about 10%. Fix: **apodize** the grating (change the tooth strength gradually along its length) or **chirp** it (change the period gradually), so the output beam becomes bell-shaped.
3. **Back reflection.** Discussed below, after Figure 5.2.

**Figure 5.2 — Output grating coupler, two cases.** Each panel shows a waveguide with teeth on top, with light coming in from the left. Above it, each tooth sends out semicircular wavelets into the air. Dashed lines join the wavelet crests that line up, which shows the direction of the outgoing beam.

- **(a) Case 1:** the light's wavelength inside the grating equals the period, $\lambda_0/n_{eff} = \Lambda$. The wavelets from all teeth are in step directly above, so the beam goes **straight up** (first diffraction order). But the second diffraction order goes **straight back** along the waveguide, as a reflection.
- **(b) Case 2:** the wavelength inside the grating is shorter than the period, $\lambda_0/n_{eff} < \Lambda$. Now the wavelets line up along a *tilted* front, so the beam leaves **at an angle**. There is no second-order back-reflection.

Both panels label the grating vector $K = 2\pi/\Lambda$ and the propagation constant $\beta = n_{eff}k_0 = 2\pi n_{eff}/\lambda_0$.

*Lesson:* aiming the beam exactly vertical makes the grating also act as a mirror back into the waveguide. Tilting the beam a little avoids that.

Back to loss 3. For a well-designed **shallow-etch** grating, back reflection is small (e.g. **−30 dB**, i.e. 0.1%), so it does not matter much as a loss. In a **full-etch** grating it can be as high as **30%**. To kill the strong Bragg reflection, the light is coupled at a small angle. This is called a **detuned grating** (Figure 5.2b). That is why grating couplers are almost never designed for perfectly vertical light (Figure 5.2a).

> **Key takeaways:**
>
> - Shallow etch: about 30% lost downward. Full etch: over 50% down and up to 30% reflected back. Shallow etch is gentler and usually better.
> - Mode mismatch with the fibre costs about 10%. It can be reduced by apodizing or chirping the grating.
> - A small tilt away from vertical ("detuning") removes the strong back-reflection, so couplers are designed for angled fibres.

## 5.2.2 Theory

> **In one sentence:** The outgoing beam angle is set by one rule — the waveguide's phase rate $\beta$, minus the grating's kick $K = 2\pi/\Lambda$, must equal the horizontal phase rate of the outgoing beam — which gives $n_{eff} - n_c \sin\theta_c = \lambda/\Lambda$.

### The picture in words (Huygens)

Each tooth scatters a little light. Light reaches each next tooth a bit later, so each tooth's wavelet starts with a phase delay. Along the waveguide, light gains phase at rate $\beta$. Over one period, that is $\beta\Lambda$ of phase.

- If $\beta\Lambda = 2\pi$ exactly (wavelength in the grating equals the period, Fig. 5.2a), each tooth fires in step with the one before it, shifted by exactly one full cycle. The wavelets add up directly overhead, so the beam goes straight up (green line in the book's figure). The second order goes straight back into the waveguide (red line). That back-reflection is bad: it causes Fabry–Pérot bouncing between the input and output couplers. To avoid it, the grating is **detuned** and the fibre is tilted slightly from vertical.
- If the in-grating wavelength is shorter than the period (Fig. 5.2b), each tooth is slightly *more* than one cycle behind the previous. To stay in step, the beam must tilt so the extra delay is made up by the path difference in air. The beam leaves at an angle, and no second-order reflection exists.

### The picture in arrows (wave vectors)

The gratings here are **one-dimensional**: they vary only along $x$. Even the curved, focusing gratings later in this section behave locally like 1D gratings with a built-in lens. The incoming light is a guided mode of a slab waveguide (book Section 3.2.2), travelling along $x$, perpendicular to the teeth.

**Figure 5.3 — Bragg condition, part 1.** An $x$–$z$ diagram. A thick black arrow from the origin points right along $x$. This is $\beta = n_{eff}k_0 = 2\pi n_{eff}/\lambda_0$, the "waveguide propagation constant". Blue arrows point left: one of length $K = 2\pi/\Lambda$ ("Grating, m=1"), and a longer one $2K$ ("Grating, m=2"). *Lesson:* the grating can subtract whole numbers of $K$ from the light's horizontal wave vector. Different orders $m$ subtract different amounts.

The waveguide's propagation constant is

$$\beta = \frac{2 \pi n_{eff}}{\lambda_{0}} \qquad (5.1)$$

where $\lambda_0$ is the vacuum wavelength and $n_{eff}$ is the slab's effective index. The grating's repeat is described by $K = 2\pi/\Lambda$. Higher orders use $m \cdot K$, with $m = 1, 2, 3, \dots$

The general **Bragg condition** is

$$\beta - k_{x} = m \cdot K \qquad (5.2)$$

What it says: start with the waveguide's horizontal phase rate $\beta$. Subtract $m$ grating kicks. What is left, $k_x$, is the horizontal part of the outgoing wave's vector. In words: "the grating makes up the difference between how fast phase runs in the waveguide and how fast it runs along the surface for the outgoing beam."

The outgoing wave travels in the cladding, with index $n_c$ (air in the figures).

**Figure 5.4 — Bragg condition, part 2.**

- **(a)** Same black $\beta$ arrow pointing right. A blue $K$ arrow starts at the tip of $\beta$ and points back left. Where it ends, a red dashed vertical line rises. That line is at position $k_x = \beta - mK$ (with $m = 1$).
- **(b)** Adds a green half-circle above the $x$ axis, centred at the origin, with radius $k_0 = 2\pi/\lambda_0$ (labelled $n_1 = 1$, for air). A green arrow goes from the origin to where the red dashed line meets the circle. That arrow is the outgoing beam's wave vector. The angle between it and the vertical $z$ axis is $\theta = \sin^{-1}(k_x/k_0)$.

*Lesson:* the outgoing light in air can only have a wave vector of length exactly $k_0$ (it must sit on the circle). The grating sets its horizontal part $k_x$. The beam's direction is then fixed: you just read off where the dashed line hits the circle. If $k_x$ were larger than the radius, there would be no crossing and no beam would come out in that order.

```
            z
            |     /  outgoing beam, length k0
     circle |    /   (tip on the circle)
   radius k0|   /
            |  / theta (from vertical)
            | /
            |/
   ---------o-----------+------------> x
            |<--- beta ------------->|
                        |<--- K -----|
                        ^ k_x = beta - K
```

The outgoing light has a wave vector of size

$$k = \frac{2 \pi n_{c}}{\lambda} \qquad (5.3)$$

(for air, $n_c = 1$, so $k = k_0$). Its horizontal part is $k_x = k \sin\theta_c$. So the angle is

$$\sin\theta_{c} = \frac{k_x}{k} \qquad (5.4)$$

*(Note: the printed packet continues this line as "$= n_{eff}\,\lambda/\Lambda$", which appears to be a typo. Substituting $k_x = \beta - K$ correctly gives $\sin\theta_c = (n_{eff} - \lambda/\Lambda)/n_c$, which is the same as Equation 5.5 below.)*

Put $k_x = \beta - K$ (first order, $m = 1$) into $k_x = k\sin\theta_c$, then divide everything by $k_0 = 2\pi/\lambda$:

$$\frac{2\pi n_{eff}}{\lambda} - \frac{2\pi}{\Lambda} = \frac{2\pi n_c}{\lambda}\sin\theta_c$$

Divide by $2\pi/\lambda$ and rearrange. This gives the simplified Bragg condition:

$$n_{eff} - n_{c} \cdot \sin\theta_{c} = \frac{\lambda}{\Lambda} \qquad (5.5)$$

What each piece means:

- $n_{eff}$: how fast phase runs in the grating region (in units of vacuum $k_0$).
- $n_c \sin\theta_c$: how fast phase runs *along the surface* for a beam tilted at $\theta_c$ in the cladding.
- $\lambda/\Lambda$: the grating's kick, in the same units.

Check with case 1: vertical beam, $\theta_c = 0$, gives $n_{eff} = \lambda/\Lambda$, i.e. $\Lambda = \lambda/n_{eff}$. The period equals the wavelength inside the grating. That matches Figure 5.2a.

**Figure 5.5 — Bragg condition, part 3 (up and down).** Now there are two half-circles centred at the origin. Upper green half-circle: air, $n_1 = 1$, radius $k_0$. Lower purple half-circle: oxide, $n_2 = n_{SiO_2}$, which has a *larger* radius $n_{SiO_2}k_0$ because oxide has a higher index. (The rendering labels the purple radius with $\beta$; read it simply as "the circle for light in oxide".) The same red dashed line at $k_x = \beta - mK$ crosses both circles. A green arrow up to the upper crossing is the beam going up into air. A purple arrow down to the lower crossing is the beam going down into the oxide/substrate.

*Lesson:* the same grating sends a beam *down* too, with the same $k_x$. Because the lower circle is bigger, the downward beam makes a *smaller* angle with the vertical. This downward beam is the penetration loss from §5.2.1.

For the angle in air, $\theta_{air}$, use Snell's law. The horizontal part is the same in cladding and air: $n_c \sin\theta_c = 1 \cdot \sin\theta_{air}$. So

$$n_{eff} - \sin\theta_{air} = \frac{\lambda}{\Lambda} \qquad (5.6)$$

Finally, the diagram shows diffraction into the substrate too. In the oxide, the beam's angle is smaller (closer to straight down) than the angle in air.

> **Key takeaways:**
>
> - Bragg condition: $\beta - k_x = mK$. The grating supplies the missing phase so the waveguide light can leave as a free beam.
> - Simplified: $n_{eff} - n_c\sin\theta_c = \lambda/\Lambda$, or with the air angle, $n_{eff} - \sin\theta_{air} = \lambda/\Lambda$.
> - The outgoing wave vector must lie on a circle of radius $n k_0$. Where the line $k_x = \beta - K$ hits that circle gives the angle. The same line also hits the (bigger) oxide circle, so light also goes down.
> - A period equal to the in-grating wavelength gives a vertical beam plus strong back-reflection. A slightly different period gives a tilted beam and no back-reflection.

## 5.2.3 Design methodology

> **In one sentence:** Design a grating coupler by (1) writing down what the factory fixes and what you want, (2) computing the period from the Bragg condition, (3) checking and fine-tuning it with 2D then 3D FDTD simulations, and (4) drawing it automatically as a compact, focusing layout.

### The overall recipe

The method follows one published approach. The steps are:

1. **Know your limits and goals.** Find what the fabrication process allows, and decide what you want.
2. **Analytic design.** Use the Bragg condition (§5.2.2) to calculate a first design on paper.
3. **Simulate and optimize.** Use 2D and 3D FDTD simulations to check how well it works and improve it.
4. **Draw the mask layout** from the final numbers.

An idea by Van Laere and colleagues lets you turn a long straight grating into a compact, curved, **focusing** one with no loss in efficiency (explained later). The whole flow, including the Bragg calculation, was built into two software tools: Mentor Graphics **Pyxis** (layout drawing) and **Lumerical FDTD** (simulation). Pyxis can draw the coupler directly from the numbers you give it.

### Two kinds of input numbers

- **Process-determined parameters** are fixed by the foundry (the chip factory) and its wafers: etch depth, cladding material, layer thicknesses, and **minimum feature size** (the smallest shape the factory can reliably make). These are listed in the foundry's **design rules** (book Sections 10.1.1 and 10.1.6).
- **Design-intent parameters** are chosen by you: central wavelength $\lambda$, incident angle, and polarization.

### Design goals to decide

- The polarization of the incoming beam (s or p) and the polarization you want in the waveguide (quasi-TE or quasi-TM).
- The central wavelength.
- The 3 dB bandwidth: do you want a narrow-band or wide-band coupler?
- The incident angle, typically **10°–30°**. Your lab equipment matters here: mechanical stages may only allow angles below about 40° (book Section 12.2). In practice, though, the angle that gives the best performance usually decides how you set up the equipment, not the other way round.
- The required optical return loss (how small reflections must be).

### The worked example used in this section

Goals:

- quasi-TE polarization,
- central wavelength 1550 nm,
- angle in air $\theta_{air} = 20°$.

The beam bends when it enters the oxide (Snell's law, $1 \cdot \sin 20° = 1.44 \sin\theta_c$):

$$\theta_c = \arcsin\left(\frac{\sin 20°}{1.44}\right) = \arcsin\left(\frac{0.342}{1.44}\right) = \arcsin(0.2375) \approx 13.7°$$

So the beam is at 13.7° inside the oxide cladding. A polished fibre (whose glass has about the same index as oxide) should be polished at this same 13.7°.

Process (based on the book's Table 10.1): shallow grating etch $ed = 70$ nm; full etch for the strip waveguide and the focusing taper; silicon thickness 220 nm; oxide cladding; minimum feature size 200 nm.

### Analytic grating coupler design

> **In one sentence:** Average the effective indices of the teeth and the grooves, then put the result into the Bragg condition to get the period — here about 660 nm.

First, find the effective indices of the two silicon thicknesses in the grating (using the slab method of book Section 3.2.2). We treat the grating as infinitely wide. That is fair because a real grating is about **10 µm** wide, much more than the 1.55 µm wavelength. (An example 1D layout is in Figure 5.6.)

Call the tooth's effective index $n_{eff1}$ (full 220 nm silicon) and the groove's $n_{eff2}$ (thinner, etched silicon). The grating region's average effective index is

$$n_{eff} = ff \cdot n_{eff1} + (1 - ff) \cdot n_{eff2} \qquad (5.7)$$

This is a weighted average. The light spends a fraction $ff$ of each period in the tooth and a fraction $1 - ff$ in the groove, so its average phase rate is the weighted mix. It is an approximation, but a good starting point.

Numbers at $\lambda_0 = 1550$ nm:

- 220 nm slab (tooth): $n_{eff1} \approx 2.848$.
- Shallow-etched region, $220 - 70 = 150$ nm thick (groove): $n_{eff2} \approx 2.534$. It is lower because a thinner slab holds the light less tightly.
- Start with $ff = 0.5$:

$$n_{eff} = 0.5 \times 2.848 + 0.5 \times 2.534 = 2.691$$

**Figure 5.6 — Mask layout of a 1D grating coupler, and with a taper.** Top-down views, drawn in a single (pink) silicon layer, on a faint grid. (a) A rectangle of about 25 straight, evenly spaced vertical stripes (the teeth), about 10–12 µm wide, joined on the right to a solid wide waveguide block. (b) The same grating followed by a long **linear taper**: a shape that narrows steadily from the grating's ~10 µm width to a sub-micron single-mode waveguide (~0.5 µm). The caption says the taper is several hundred microns long. Scale bars are about 10 µm. *Lesson:* a straight grating makes a wide beam that must be squeezed down slowly to the narrow waveguide. That taper is far bigger than the grating itself, which wastes chip space. This motivates the focusing design later.

Now get the period from the Bragg condition (5.6), solved for $\Lambda$:

$$\Lambda = \frac{\lambda}{n_{eff} - \sin\theta_{air}} \qquad (5.8)$$

Worked numbers:

$$\Lambda = \frac{1550 \text{ nm}}{2.691 - \sin 20°} = \frac{1550}{2.691 - 0.342} = \frac{1550}{2.349} \approx 660 \text{ nm}$$

So the teeth repeat every 660 nm, each tooth being 330 nm wide (ff = 0.5). That is above the 200 nm minimum feature size, so it can be made.

How good is this paper design? The published study found it is very close to the best uniform grating that full FDTD optimization finds. FDTD did not improve the insertion loss much. The real central wavelength came out slightly off target, typically by 0–10 nm, but you can simply shift the laser wavelength a little to compensate. So this quick method is very useful when you need a coupler for a given process, wavelength and polarization. The numbers can go straight into the layout, or be refined by simulation as described next.

### Design using 2D FDTD simulations

> **In one sentence:** Simulate the paper design to learn how well it actually works, how sensitive it is, and how to improve it — mostly in fast 2D, with a final 3D check.

The paper design gives shapes but not performance. FDTD is used to:

1. find the efficiency of the analytic design, including the best place to put the input beam;
2. see how each physical parameter matters (BOX thickness, fill factor, fibre angle, etch depth);
3. check other measures, such as back reflections and sensitivity to fabrication errors (e.g. etch depth);
4. optimize the design.

**2D FDTD** is the normal choice for gratings because it needs much less memory and time. After a 2D design is done, **3D** simulation confirms it.

**Figure 5.7 — 2D FDTD setups.** Two side-view simulation pictures of the layer stack: substrate and oxide (black), silicon layer with the grating teeth (red outline with notches), cladding, and a fibre region on top. An orange rectangle marks the simulation area, with PML borders. Yellow lines are monitors.

- **(a) Input coupler:** a purple arrow points down from the fibre: a **mode source** launches the fibre's mode toward the grating. A monitor on the waveguide at the left measures how much light gets into the waveguide.
- **(b) Output coupler:** a purple arrow points along the waveguide: the source launches the waveguide mode into the grating. Monitors measure what reaches the fibre.

*Lesson:* you can simulate the coupler in either direction, and you need the right monitor to count only the useful light.

What is in the simulation: the silicon wafer at the bottom, the 220 nm silicon layer on a **2 µm BOX**, and a protective oxide cladding on top. The PML border makes outgoing light behave as if it travels away forever, so it does not bounce back and corrupt the result. The yellow monitors are **frequency-domain power monitors**: they record the power flowing through them at each wavelength. In the book's colour figure, green is the optical fibre (light green: core; dark green: fibre cladding). The fibre is modelled as polished and lying on top of the cladding.

- For an **input** coupler, the fundamental TE mode is launched from the fibre core. Power monitors record insertion loss and reflection back to the fibre.
- For an **output** coupler, the fundamental TE mode is launched in the waveguide. A **mode expansion monitor** measures how much power enters the fibre's *fundamental mode*. This matters because, due to mode mismatch, not all light reaching the fibre goes into that mode, and only that mode is useful.

The simulation script has four parts. The code listings are not in this packet, but the book describes them as:

1. **Listing 5.1 — initial settings:** define parameters (wavelength, layer thicknesses, period, fill factor, etch depth, angle, etc.).
2. **Listing 5.2 — draw the structure:** build the layers and the grating teeth in the simulator.
3. **Simulation setup:** set the simulation region, the source and the monitors. Two versions: **Listing 5.3** uses a free-space **Gaussian beam** source (a bell-shaped beam, like a fibre mode in air); **Listing 5.4** models coupling with an actual optical fibre.
4. **Listing 5.5 — run:** run the simulation, including parameter sweeps, and plot the transmission versus wavelength.

The simulations here are for an **input** coupler (Figure 5.7a). Later (book Section 9.6) both directions are simulated to get back reflections. These feed **S-parameters** (book Section 9.3.2): a compact table of how much light (amplitude and phase) goes from each port to each other port. Circuit simulators use them to model the coupler as a black box.

### Position of the beam

> **In one sentence:** Where you put the fibre along the grating matters; the best spot is a few microns in from the start, and you can be off by about ±2.3 µm before losing 1 dB.

You must sweep the fibre's position to find the best spot. **Figure 5.8** shows the result.

**Figure 5.8 — Efficiency versus fibre position.** A single smooth hump-shaped curve. Horizontal axis: fibre position from 2 to 8 µm, where $x = 0$ means the fibre centre is right at the start of the grating. Vertical axis: insertion loss in dB, from −4.5 to −2.5. The curve peaks at about −2.7 dB near 4.5–5 µm, crosses −3 dB at about 2.8 µm and 6.2 µm, and falls to about −4.6 dB at 8 µm.

*Lesson:* the best fibre position is about **5 µm** from the start of the grating (the book's number; the plot's peak looks closer to 4.5 µm). Why not at 0? Because the waveguide light is radiated gradually along the grating, so the upward beam's centre lies a few microns inside the grating. The curve's width also shows **alignment sensitivity**: the **1 dB alignment tolerance** is **±2.3 µm**. That is how much you can misplace the fibre before losing 1 dB more.

### Results

> **In one sentence:** The simulated paper design reaches −2.7 dB insertion loss at 1548 nm, very close to the 1550 nm target, with back reflection below −10 dB.

**Figure 5.9 — Efficiency and reflection versus wavelength.** Horizontal axis: wavelength 1.45–1.65 µm. Vertical axis: dB, 0 to −16. A solid "Transmission" curve rises to a peak near 1.55 µm and falls on both sides, reaching about −9.5 dB at 1.45 µm and −11 dB at 1.65 µm. A dashed "Reflection" curve wiggles between about −17 and −15 dB at short wavelengths and rises to about −10.5 dB at 1.65 µm.

The book reports: **insertion loss −2.7 dB** (about 54% of the light reaches the fibre) at a **central wavelength of 1548 nm**. (The figure description reads the peak as about −1.4 dB; the text's −2.7 dB matches Figure 5.8 and is the number to remember.) So the Bragg-condition theory predicted the central wavelength very well: only 2 nm off.

The **return loss** stays below −10 dB across the coupler's bandwidth (less than 10% reflected). That is quite a lot of reflection. Part of it comes from the **fibre–air interface**: the jump in index from glass (1.44) to air (1) reflects some light. **Index matching** — filling the gap with a glue or liquid whose index matches the glass — would reduce it.

### Polarization

> **In one sentence:** A grating built for TE light barely couples TM light, so it also works as a polarization filter.

Grating couplers are naturally **polarization sensitive**. TE and TM modes have very different effective indices in a thin silicon slab. By Equation 5.5, a different $n_{eff}$ means the Bragg condition is met at a very different wavelength or angle. So a grating designed for TE simply does not match TM at the design wavelength.

**Figure 5.10 — TE versus TM transmission.** Same axes (1.45–1.65 µm; 0 to −18 dB). The solid TE curve peaks at about −1.3 dB near 1.55 µm (bell shape). The dashed TM curve stays low and flat, around −12 to −15 dB, with small wiggles.

*Lesson:* the TE-designed coupler passes TE and blocks TM by more than about 10 dB. It acts as a **polarizer** (a polarization filter). That is useful (it cleans up polarization) but also means the fibre's polarization must be set correctly to get light in.

### Design parameters

> **In one sentence:** Every geometric parameter mainly shifts the wavelength where the coupler works best, as predicted by $\lambda = \Lambda(n_{eff} - n_c\sin\theta_c)$.

Parameters that affect performance: period, fill factor, incident angle, incident (fibre) position, etch depth, SiO$_2$ BOX thickness, SiO$_2$ cladding thickness, and number of grating periods. Of these, the etch depth and the oxide thicknesses are set by the fabrication process.

Their main effect is to move the **central wavelength**. Solve the Bragg condition for $\lambda$:

$$\lambda = \Lambda\,(n_{eff}(\lambda) - n_{c} \cdot \sin\theta_{c}) \qquad (5.9)$$

Read it as: the central wavelength grows with the period $\Lambda$, grows with $n_{eff}$, and shrinks as the angle $\theta_c$ grows. The note $n_{eff}(\lambda)$ is a reminder that $n_{eff}$ itself depends on wavelength (dispersion). So when the central wavelength shifts, $n_{eff}$ shifts too, and a simple one-shot calculation is only approximate.

Quick check with the example: $\Lambda = 660$ nm, $n_{eff} = 2.691$, $\sin\theta_{air} = 0.342$ (using the air form): $\lambda = 660 \times 2.349 \approx 1550$ nm. Good.

### Grating period

The period has the **biggest** effect on the central wavelength (it multiplies everything in Equation 5.9). In a sweep (Listing 5.5), all else was held fixed and the period was changed from **620 nm to 700 nm**. The central wavelength moved from **1483 nm to 1608 nm**.

The **tuning coefficient** $\delta\lambda/\delta\Lambda$ (how many nm the wavelength moves per nm change in period) is

$$\frac{\delta\lambda}{\delta\Lambda} = \frac{1608 - 1483}{700 - 620} = \frac{125}{80} \approx 1.56 \text{ nm/nm}$$

So making the period 1 nm longer moves the peak about 1.56 nm to the red (longer wavelength).

**Figure 5.11 — Period sweep.** Five bell-shaped curves of efficiency (linear scale, 0 to ~0.55, i.e. fraction of power) versus wavelength (1.45–1.65 µm), one per period: 620, 640, 660, 680, 700 nm. Their peaks march steadily to the right: about 1.485, 1.51, 1.545, 1.58 and 1.615 µm. Peak heights: about 0.49, 0.55, 0.55, 0.47, 0.37. *Lesson:* the period is a clean, almost linear "tuning knob" for wavelength. Efficiency is best around 640–660 nm (the designed value) and drops further away, because other parameters were optimized for the design point.

### Fill factor

The fill factor changes $n_{eff}$ through Equation 5.7. A bigger $ff$ means more of each period is thick tooth, so $n_{eff}$ goes up. By Equation 5.9, the peak then moves to longer wavelength.

The sweep varied $ff$ from **0.3 to 0.6**, all else fixed. The central wavelength moved from **1522 nm to 1560 nm** — only 38 nm. The tuning coefficient, defined per nm of tooth width, $\delta\lambda/\delta W$, is **0.215 nm/nm**. That is much weaker than the period's 1.56 nm/nm. So the period has a much stronger effect on wavelength than the fill factor.

**Figure 5.12 — Fill factor sweep.** Five bell curves (efficiency 0 to ~0.55) for $ff$ = 0.3, 0.375, 0.45, 0.525, 0.6. Peaks shift right from about 1.52 µm to about 1.57 µm. Peak efficiencies all stay around 0.51–0.55. The curves get slightly wider as $ff$ increases. *Lesson:* fill factor is a fine-tuning knob for wavelength. It barely changes peak efficiency here, but it changes bandwidth a little.

### Etch depth

The etch depth also acts through $n_{eff}$. A deeper etch leaves thinner silicon in the grooves. Thinner silicon has a lower effective index, so $n_{eff2}$ drops, and the average $n_{eff}$ drops. Equation 5.9 says the central wavelength is proportional to $n_{eff}$, so the central wavelength goes *down* as etch depth goes up. (The book says "inversely proportional"; more precisely, it decreases as the etch gets deeper.) The coupler is similarly sensitive to the total SOI silicon thickness.

**Figure 5.13 — Etch depth sweep.** Five bell curves (efficiency 0 to ~0.55) for $ed$ = 60, 65, 70, 75, 80 nm. As the etch gets deeper, the peaks shift left (to shorter wavelengths), from roughly 1558 nm (60 nm etch) to roughly 1543 nm (80 nm etch). Peak efficiency stays near 0.51–0.545. The deepest etch gives the broadest curve.

This leftward shift is a **blueshift** (toward shorter, "bluer" wavelengths), as the analysis predicted. The book gives the tuning coefficient $\delta\lambda/\delta ed$ as **1.9 nm/nm**: each extra nm of etch moves the peak by about 1.9 nm (in magnitude, toward shorter wavelength). *Lesson:* etch depth is not in the designer's hands — it is set by the factory — but small factory errors in it (a few nm) move the coupler's peak noticeably.

### Incident angle

The **incident angle** is the angle between the incoming (or outgoing) beam and the surface normal.

- **Positive angle:** the beam and the waveguide light travel in the same horizontal direction (the beam tilts "forward").
- **Negative angle:** they travel in opposite directions.

You can quote the angle **in free space** (useful for free-space measurements, book Section 12.1.1) or **in the cladding** (e.g. oxide). Which one matches the fibre?

- With a **lensed fibre** (a fibre with a tiny lens on its tip, held in air), the light's angle in air equals the fibre's tilt.
- With **polished fibres or fibre arrays** (glass touching the cladding), the fibre polish angle equals the angle in the cladding, assuming fibre glass and cladding have the same index. Snell's law links the two angles.

The angle changes the central wavelength through Equation 5.9 (bigger angle, smaller $\lambda$). Sweeping the air angle from **15° to 25°** moved the central wavelength from **1586 nm to 1512 nm**. Tuning coefficient:

$$\frac{\delta\lambda}{\delta\theta} \approx \frac{1512 - 1586}{25 - 15} = -7.4 \approx 7 \text{ nm per degree (in magnitude)}$$

**Figure 5.14 — Angle sweep.** Five bell curves (efficiency 0 to 0.6) for $\theta_{air}$ = 15°, 17.5°, 20°, 22.5°, 25°. Peaks move left as the angle grows: about 1.585, 1.57, 1.555, 1.54, 1.525 µm. Peak heights rise slightly, from about 0.49 to 0.56. The curve shape stays the same. *Lesson:* tilting the fibre is a convenient way to tune the wavelength in the lab: about 7 nm per degree. Tilting more also helps efficiency a little here.

### Parameter sensitivity

All of period, fill factor (tooth width), etch depth, SOI thickness and angle move the central wavelength. **Table 5.1** collects the tuning (sensitivity) coefficients. They also tell you how much fabrication errors will shift your coupler (book Section 11.1.3).

**Table 5.1 — Grating coupler sensitivity to geometry parameters.** Each row says how many nm the central wavelength moves per unit change of that parameter.

| Parameter | Sensitivity coefficient |
|---|---|
| Period, $\Lambda$ | 1.56 nm/nm |
| Width, $W$ | 0.215 nm/nm |
| Etch depth, $ed$ | 1.9 nm/nm |
| SOI thickness | 1.82 nm/nm |
| Incident angle, $\theta$ | 7 nm/° |

How to read it: if the factory's silicon layer is 5 nm thicker than planned, expect the peak to move by about $5 \times 1.82 \approx 9$ nm. If you tilt the fibre by 2°, expect about 14 nm. The vertical dimensions (etch depth and SOI thickness, about 1.8–1.9 nm/nm) matter as much as the period, while tooth width matters least.

### Cladding and buried oxide

> **In one sentence:** Light reflected from the layer boundaries above and below the grating interferes with the main beam, so the BOX and cladding thicknesses make the efficiency rise and fall in waves — and a 2 µm BOX happens to be a good choice.

The thicknesses of the BOX and of the cladding strongly affect insertion loss, through interference of reflections at the layer boundaries.

**Figure 5.15 — Reflections at the interfaces.** A side view of the stack: cladding, Si (with grating), BOX, Si substrate. A big light-blue arrow $P_{in}$ comes down from the top-right (from the fibre). A red bell curve $P_{wg}$ shows light travelling left in the waveguide. Four blue curved arrows show reflections, numbered top to bottom:

- $P_{reflection1}$: at the top surface of the cladding.
- $P_{reflection2}$: at the grating / silicon top surface.
- $P_{reflection3}$: at the bottom of the silicon (Si/BOX boundary).
- $P_{reflection4}$: at the BOX/substrate boundary.

*Lesson:* the layers form little "mirror pairs". Light bouncing in each pair interferes, and whether the bounces add or cancel depends on the layer thickness.

For the lowest insertion loss you want:

- reflections 1 and 2 (above the grating) to **cancel** (destructive interference), so less light is turned away at the top;
- reflections 3 and 4 (below the grating) to **add** (constructive interference), so the light heading down gets sent back up in step with the upward beam. The BOX then acts like a mirror that boosts the upward beam.

Why do thickness changes cause waves in the efficiency? The extra path of a bounce inside a layer of thickness $d$ is about $2d$ (down and back). Each time that extra path grows by one wavelength-in-the-material, the interference cycles from add to cancel and back. So the efficiency rises and falls periodically with thickness.

**BOX sweep (Figure 5.16).** BOX thickness was varied from 1 to 3 µm. The insertion loss oscillates like a sine wave, controlled by the interference of reflections 3 and 4. Wafer makers choose the BOX thickness to give constructive interference. There is a peak at **2 µm**, and 2 µm also works well for both **1310 nm and 1550 nm**. That is why 2 µm BOX is a common standard among silicon photonics foundries.

**Figure 5.16 — Efficiency versus BOX thickness.** Horizontal: BOX 1–3 µm. Vertical: efficiency in dB, about −8.5 to −2. The curve swings regularly up and down: peaks of about −2.6 dB (near 1.4, 1.95 and 2.55 µm) and dips of about −8.3 dB in between. Repeat distance is about 0.55–0.6 µm. Swing is about 5.7 dB. *Lesson:* choosing the wrong BOX thickness can cost about 5–6 dB — a huge loss (more than 70% of the light). The BOX is a hidden but very important design parameter.

A sanity check with the round-trip idea: in oxide, 1550 nm light has wavelength $1550/1.44 \approx 1076$ nm. A round trip adds $2d$, so one full cycle happens every $d$ change of about $1076/2 \approx 540$ nm. (The angle makes it a little longer.) That matches the ~0.55–0.6 µm repeat seen in the plot.

**Cladding sweep (Figure 5.17).** Similarly, the phase between reflections 1 and 2 changes with cladding thickness. Here, cladding thickness means the height from the silicon/BOX boundary to the top surface of the cladding. Lowest loss happens where reflections 1 and 2 cancel; highest loss where they add. The best cladding thickness depends on the angle and the wavelength.

**Figure 5.17 — Efficiency versus cladding thickness.** Horizontal: cladding 1–3 µm. Vertical: dB, −3.5 to −2. The curve oscillates between about −2.15 dB and −3.3 dB, with a repeat of roughly 0.65–0.7 µm. Swing is about 1.1 dB. *Lesson:* the cladding matters too, but much less than the BOX.

Comparing Figures 5.16 and 5.17: the BOX swing (~5.7 dB) is much larger than the cladding swing (~1.1 dB). The reason: reflections 3 and 4 are stronger (silicon/oxide and oxide/silicon-substrate boundaries have a big index jump, 3.48 versus 1.44) than reflections 1 and 2 (the top surface has a smaller index jump).

### Compact design – focusing

> **In one sentence:** Instead of a straight grating plus a long taper, curve the grating lines into ellipse arcs that focus the light straight into the narrow waveguide, making the coupler much smaller with no efficiency loss.

So far the gratings were straight. A straight grating makes a beam about as wide as the fibre mode (~9 µm). A **taper** must then shrink it to a 0.5 µm waveguide. To do this without losing light (adiabatically, i.e. gently), the taper must be longer than **100 µm**. That is too big for compact circuits.

Better: use **confocal gratings** (Figure 5.18). The grating lines are curved into **ellipses** that share a common **focal point**. (An ellipse is a stretched circle. It has two special points called foci. Here all the ellipses share one focus.) That shared focus is where the light is collected — at the start of the narrow waveguide. Like a curved mirror focusing sunlight to a point, the curved teeth focus the light toward the waveguide.

The grating lines follow this equation:

$$q \cdot \lambda_{0} = n_{eff}\sqrt{y^{2} + z^{2}} - z \cdot n_{t} \cdot \cos(\theta_{c}) \qquad (5.10)$$

Symbols:

- $q$: an integer, one for each grating line (line 1, line 2, ...).
- $(y, z)$: a point on the chip surface, measured from the focal point; $z$ is along the waveguide direction and $y$ is sideways.
- $n_{eff}$: effective index of the grating.
- $\sqrt{y^2 + z^2}$: straight-line distance from the focal point to that point.
- $n_t$: refractive index of the environment above (the cladding/top medium).
- $\theta_c$: angle between the fibre and the chip *surface* (note: from the surface, not the normal — that is why it uses $\cos$ instead of $\sin$).
- $\lambda_0$: vacuum wavelength.

What it says: think of light travelling from the focal point out to the grating line inside the slab. Its phase is $n_{eff}k_0 \times$ (distance), so the first term is that phase in "wavelength units". The second term is the phase the tilted fibre beam has at that point along $z$. For all teeth to radiate in step toward the fibre *and* focus to the same point, the difference must be a whole number $q$ of wavelengths. Each $q$ gives one curve. It is the Bragg condition (5.5), written for curved lines around a point. Far from the focus, in a small patch, the lines are nearly straight with spacing given by 5.5.

The curves can be written in **parametric form** using an angle variable $t$ (going around the ellipse), here with $x$ along the waveguide (playing the role of $z$ above):

$$x = \sqrt{\frac{q \cdot \lambda_{0} \cdot n_{t} \cdot \cos(\theta_{c}) + q^{2} \cdot \lambda_{0}^{2}}{n_{eff}^{2} - n_{t}^{2} \cdot \cos^{2}(\theta_{c})}} \cdot \cos(t) + \frac{q \cdot \lambda_{0} \cdot n_{t} \cdot \cos(\theta_{c})}{n_{eff}^{2} - n_{t}^{2} \cdot \cos^{2}(\theta_{c})} \qquad (5.11)$$

$$y = \sqrt{\frac{q^{2} \cdot \lambda_{0}^{2}}{n_{eff} - n_{t}^{2} \cdot \cos^{2}(\theta_{c})}} \cdot \sin(t) \qquad (5.12)$$

How to read these: $x = a\cos t + x_0$ and $y = b\sin t$ is the standard recipe for an ellipse with half-widths $a$ (along $x$) and $b$ (along $y$), whose centre is shifted along $x$ by $x_0$. As $t$ goes from 0 to $2\pi$, the point $(x, y)$ traces the ellipse. Only a slice of each ellipse (a fan-shaped arc) is actually drawn. Bigger $q$ gives a bigger ellipse — the next grating line out.

*Caution on the printed formulas:* they appear to contain typos (e.g. the denominator in 5.12 should almost certainly be $n_{eff}^2$, not $n_{eff}$, and the numerator under the root in 5.11 mixes terms of different units). Working it out directly from 5.10 (writing $a = n_{eff}$, $c = n_t\cos\theta_c$) gives an ellipse with centre offset $x_0 = q\lambda_0 c/(a^2 - c^2)$, half-width along $x$ of $q\lambda_0 a/(a^2 - c^2)$, and half-width along $y$ of $q\lambda_0/\sqrt{a^2 - c^2}$. The offset term in 5.11 agrees with this. If you implement the layout yourself, derive from 5.10.

**Figure 5.18 — Mask layout of a focusing grating coupler.** Top view on a dotted grid, with a 2 µm scale bar. On the left: about 30–35 curved pink lines (grating teeth), nested arcs that form a fan shape, all curving around a focus on the right. On the right: a short triangular taper narrowing into a thin straight output waveguide (~0.4–0.5 µm wide). The whole device is only about 16–18 µm long and about 10–12 µm wide at the grating end. *Lesson:* compared with Figure 5.6 (grating plus a taper hundreds of µm long), the focusing coupler is tiny, because the curved teeth do the job of the taper.

The Bragg condition for curved gratings can also be written in **polar coordinates** (distance $r$ from the focus, and angle $\phi$):

$$n_{eff} \cdot k_{0} \cdot r = n_{c} \cdot k \cdot r\,\sin(\theta)\,\cos(\phi) + 2\pi N \qquad (5.13)$$

Here $k_0$ is the free-space wave vector, $r$ is the distance from the focal point, $\phi$ is the angle between the line to the point and the $z$-axis (the waveguide direction), $\theta$ is the beam angle, and $N$ is an integer. Left side: phase gained travelling distance $r$ in the slab. Right side: phase of the tilted fibre beam at that point (its horizontal component along the direction to the point is $k\sin\theta\cos\phi$), plus a whole number of cycles. Same idea as 5.10, in different coordinates.

Key fact: if a straight grating and an elliptical grating have the same period and fill factor, they have nearly the same coupling efficiency. **Curving the lines does not hurt efficiency.** So the design flow is:

1. Design and optimize a straight grating with 2D simulation.
2. Draw the focusing version with the same period and fill factor.
3. Double-check with 3D FDTD (described just below).

### Mask layout

> **In one sentence:** A script (a PCell) draws the whole focusing coupler automatically from a handful of numbers.

The layout is drawn by a script that implements the equations above. It is written for the Mentor Graphics **Pyxis** layout tool as a **PCell**. Figure 5.18 is its output, and the script is Listing 5.8 (not included in the packet). It can make couplers for any period and fill factor, so it works for any wavelength, polarization and angle.

Inputs to Listing 5.8:

- wavelength,
- period,
- fill factor,
- cladding refractive index,
- incident angle (defined in air),
- waveguide width,
- slab waveguide effective index,
- number of segments used to draw each curve (more segments means smoother arcs).

A second pair of scripts goes one step further:

- **Listing 5.7** does the analytic calculation (the effective indices, as in Equation 5.7).
- **Listing 5.6** designs and draws the coupler from **physical** inputs (wafer thicknesses, etc.) plus **design-intent** inputs (wavelength, polarization, angle).

Its inputs: wavelength, etch depth, silicon thickness, incident angle (in air), waveguide width, cladding refractive index, polarization, and fill factor. The default fill factor of 0.5 is just a starting point, not necessarily the best. You should optimize it with FDTD as described earlier in §5.2.3.

### 3D simulation

> **In one sentence:** 2D simulations are good for exploring, but a full 3D simulation of the drawn layout is needed to confirm the design — and it agrees well.

2D simulations are used for the first optimization and are a good approximation. But a 3D simulation is needed to verify the design. 3D needs much more memory and time.

For the 3D run, the mask layout was exported and imported directly into the FDTD solver, so the simulated shape is exactly what will be made.

**Figure 5.19 — 2D versus 3D efficiency.** Efficiency (linear, 0 to 0.45) versus wavelength 1.1–1.5 µm. (Note: this example coupler was designed for the **1310 nm** band, not 1550 nm.) Two bell curves: "2D" peaks at about 0.435–0.44 near 1.31–1.32 µm; "3D" peaks at about 0.40 at nearly the same wavelength, and is slightly narrower. Both fall to near zero by about 1.38–1.39 µm.

*Lesson:* 3D matches 2D well. The peak wavelength is almost the same, and 3D shows a slightly lower efficiency (about 40% versus 44%). The book explains the difference by the limited size of the 3D simulation. In 2D, the third dimension is assumed infinite, so effects of the grating's finite width are ignored.

> **Key takeaways:**
>
> - Recipe: fix process limits and goals, compute $n_{eff}$ (weighted average, Eq. 5.7) and $\Lambda = \lambda/(n_{eff} - \sin\theta_{air})$ (Eq. 5.8), simulate in 2D, verify in 3D, draw with a script. Example: $n_{eff} = 2.691$, $\Lambda \approx 660$ nm, 20° in air, giving −2.7 dB at 1548 nm.
> - Best fibre position is ~5 µm into the grating, with ±2.3 µm for 1 dB extra loss. TE-designed gratings block TM by over 10 dB.
> - Wavelength sensitivities: period 1.56, width 0.215, etch depth 1.9, SOI thickness 1.82 nm/nm, angle 7 nm/°.
> - BOX thickness causes ~5.7 dB swings through interference; 2 µm BOX is a good, standard choice. Cladding swings are smaller (~1.1 dB).
> - Curving the teeth into confocal ellipses replaces a >100 µm taper with a ~20 µm device, with no efficiency penalty.

## 5.2.4 Experimental results

> **In one sentence:** A real coupler made in a foundry worked as predicted in shape, but measured about 1.9 dB worse than simulated, mainly because of a gap between the fibre ribbon and the chip.

Optimizing a grating coupler means sweeping many parameters: period, duty cycle, angle, and so on. This search can be automated, for example with a **genetic algorithm** (a search method that mimics evolution: try many designs, keep the best, mix and slightly change them, repeat).

A coupler was designed for the **OpSIS-IME** foundry process (a shared fabrication service). Its numbers:

| Quantity | Value |
|---|---|
| Grating period | 650 nm |
| Duty cycle (tooth width) | 350 nm |
| Simulated insertion loss | −2.74 dB |
| Simulated 3 dB bandwidth | 79.8 nm |
| Measured insertion loss | −4.64 dB |
| Measured 3 dB bandwidth | 74.9 nm |

Read the table as "design, then prediction, then reality". In plain terms: the simulation predicted about 53% of the light gets through ($10^{-0.274}$); the measurement found about 34% ($10^{-0.464}$).

**Figure 5.20 — Simulation versus measurement.** Horizontal: wavelength 1500–1600 nm. Vertical: dB, −12 to −2. The smooth "Simulation" curve peaks at about −2.8 dB near 1548 nm, falling to about −7 dB at 1500 nm and −7.7 dB at 1600 nm. The slightly noisy "Measurement" curve has the same general shape but sits lower: a broad top of about −4.6 dB between roughly 1540 and 1555 nm, about −8.5 dB at 1500 nm, and about −11 dB at 1600 nm.

*Lesson:* the simulation predicts the shape and the peak wavelength well. The measurement is about 1.9 dB worse and slightly narrower.

Why the difference? The simulation assumed the fibre tip touches the chip (zero gap). In the real setup there was a gap between the **fibre ribbon** (fibre array) and the chip. Over a gap, the beam spreads and its angle and position shift a little, so less light lands in the right place with the right shape. This explains both the higher loss and the narrower bandwidth.

> **Key takeaways:**
>
> - Real device (OpSIS-IME): period 650 nm, tooth 350 nm. Simulated −2.74 dB and 79.8 nm bandwidth; measured −4.64 dB and 74.9 nm.
> - The simulation gets the spectrum's shape and centre right; the extra measured loss comes mostly from the fibre-to-chip gap that the model ignored.
> - Parameter optimization can be automated with methods such as a genetic algorithm.

## Glossary

| Term | Plain meaning |
|---|---|
| 1 dB / 3 dB bandwidth | Range of wavelengths where the loss stays within 1 dB (or 3 dB) of its best value |
| Alignment tolerance (1 dB) | How far the fibre can be moved before losing 1 dB more light (here ±2.3 µm) |
| Apodization | Gradually changing the grating's strength along its length to shape the output beam |
| Back reflection | Light bounced back the way it came (into the waveguide or fibre) |
| BOX (buried oxide) | Glass layer (about 2 µm) between the silicon device layer and the silicon substrate |
| Bragg condition | Rule linking period, effective index, wavelength and angle: $\beta - k_x = mK$ |
| Bragg reflection | Strong reflection from a grating when a diffraction order points straight back |
| Blueshift / redshift | Move toward shorter / longer wavelength |
| Chirp | Gradually changing the grating period along its length |
| Cladding | Low-index material around or on top of the waveguide core |
| Confocal grating | Grating whose curved lines are ellipses sharing one focal point |
| Constructive / destructive interference | Waves adding up (crests together) / cancelling (crest on trough) |
| Decibel (dB) | Log scale for power ratios: $10\log_{10}(P_2/P_1)$; −3 dB = half |
| Design-intent parameters | Choices made by the designer: wavelength, angle, polarization |
| Design rules | The foundry's list of what can be made (sizes, layers, etc.) |
| Detuned grating | Grating whose period is chosen so the beam leaves at an angle, avoiding back-reflection |
| Diffraction order ($m$) | One of the discrete beams produced by a grating; order $m$ uses $m$ grating kicks |
| Directionality | Fraction of the waveguide light that goes up: $P_{up}/P_{wg}$ |
| Dispersion | Change of a material's or mode's index with wavelength |
| Distributed Bragg reflector (DBR) | Stack of alternating thin layers that acts as a strong mirror |
| Duty cycle | Same as fill factor |
| Effective index ($n_{eff}$) | The single index a guided mode "feels"; between core and cladding index |
| Ellipse / focal point | Stretched circle / special point inside it toward which the shape focuses |
| Etch depth ($ed$) | How deep the grooves are cut into the silicon |
| Evanescent field | The part of a guided mode that extends outside the core |
| Fabry–Pérot oscillation | Ripple in transmission caused by light bouncing between two reflectors |
| FDTD | Simulation method stepping the laws of light on a grid in time |
| Fill factor ($ff$) | Fraction of each period occupied by the tooth: $W/\Lambda$ |
| Foundry | Factory that fabricates chips for customers |
| Fundamental mode | The simplest guided light pattern, one smooth bump |
| Gaussian beam | Beam with a bell-shaped cross-section, like a fibre's light |
| Genetic algorithm | Search method that evolves good designs by keeping, mixing and mutating the best |
| Grating coupler | Periodic grooves that redirect light between a waveguide and a beam above the chip |
| Grating vector ($K$) | The grating's "kick": $K = 2\pi/\Lambda$ |
| Huygens–Fresnel principle | Every point on a wave acts as a source of new wavelets |
| Index matching | Filling a gap with material of matching index to stop reflections |
| Insertion loss (coupling efficiency) | Fraction of light reaching the fibre's fundamental mode, in dB |
| Lensed fibre | Fibre with a tiny lens at its tip, used in air |
| Mask layout (GDS) | Drawing of the shapes to be etched on the chip |
| Minimum feature size | Smallest shape the factory can reliably make (here 200 nm) |
| Mode | Stable light pattern that travels along a waveguide |
| Mode expansion monitor | Simulation tool measuring power in one specific mode |
| Mode mismatch | Loss because the beam shape doesn't match the fibre mode |
| Optical return loss | Reflected power relative to input, in dB |
| PCell (parameterized cell) | Script that draws a layout shape from input numbers |
| Penetration loss | Light lost downward into the substrate |
| Period ($\Lambda$) | Distance from one grating tooth to the next |
| PML (perfectly matched layer) | Absorbing border in a simulation so light doesn't reflect off the edge |
| Polarization (TE/TM, s/p) | Direction of light's electric field; TE in-plane, TM vertical |
| Polarizer | Device that passes one polarization and blocks the other |
| Polish angle | Angle at which the fibre end is cut and polished |
| Process-determined parameters | Values fixed by the factory: etch depth, thicknesses, materials |
| Propagation constant ($\beta$) | Wave vector of a guided mode: $\beta = 2\pi n_{eff}/\lambda_0$ |
| Refractive index ($n$) | How much a material slows light: speed $= c/n$ |
| S-parameters | Table of how much light goes from each port to each other port |
| Shallow / full etch | Partial cut into the silicon / cut all the way through |
| Snell's law | $n_1\sin\theta_1 = n_2\sin\theta_2$, describes bending at a boundary |
| SOI (silicon-on-insulator) | Wafer with thin silicon on glass on a thick silicon base |
| Substrate | Thick silicon base of the wafer |
| Surface normal | Line perpendicular to a surface; angles are measured from it |
| Taper | Waveguide that gradually narrows to change the mode size |
| Tuning (sensitivity) coefficient | How many nm the peak wavelength moves per unit change of a parameter |
| Wave vector ($k$) | Arrow whose length $2\pi n/\lambda_0$ is the phase rate, pointing in the travel direction |
| Wavelength ($\lambda$) | Distance between wave crests; $\lambda_0$ in vacuum |

## Check yourself

1. Why does a straight grating need a taper several hundred microns long, and how does a focusing grating avoid it?

   *Answer:* A straight grating makes a ~10 µm wide beam (to match the ~9 µm fibre mode) that must be squeezed gently to a 0.5 µm waveguide, which needs over 100 µm of taper. A focusing grating curves its teeth into confocal ellipses, so the light is focused straight to the waveguide's start, giving a ~16–18 µm device with no efficiency penalty.

2. Using $n_{eff1} = 2.848$, $n_{eff2} = 2.534$, $ff = 0.5$ and $\theta_{air} = 20°$, compute the period for 1550 nm.

   *Answer:* $n_{eff} = 0.5(2.848) + 0.5(2.534) = 2.691$. $\Lambda = 1550/(2.691 - 0.342) = 1550/2.349 \approx 660$ nm.

3. What goes wrong if a grating is designed to emit perfectly vertically?

   *Answer:* The second diffraction order then goes straight back into the waveguide (Bragg reflection). This causes Fabry–Pérot ripples between the input and output couplers. A small tilt (detuning) removes it.

4. A coupler has insertion loss −3 dB. What fraction of the waveguide light reaches the fibre's fundamental mode?

   *Answer:* About half (50%), since $10\log_{10}(0.5) \approx -3$.

5. The silicon layer comes out 4 nm thicker than planned. Roughly how far does the peak wavelength move, and which way?

   *Answer:* About $4 \times 1.82 \approx 7$ nm. Thicker silicon raises $n_{eff}$, so by $\lambda = \Lambda(n_{eff} - n_c\sin\theta_c)$ the peak moves to longer wavelength (redshift).

6. Why does the efficiency go up and down as the BOX thickness changes, and why is 2 µm popular?

   *Answer:* Reflections at the Si/BOX and BOX/substrate boundaries interfere; changing the thickness changes their relative phase, so they alternately add (boosting the upward beam) or cancel. 2 µm gives constructive interference and works well at both 1310 and 1550 nm.

7. Why does a TE-designed grating coupler act as a polarizer?

   *Answer:* TM light has a very different effective index, so it does not satisfy the Bragg condition at the design wavelength and angle. Its coupling is more than about 10 dB weaker.

8. Which parameter shifts the central wavelength most per nm: period or tooth width? Give the numbers.

   *Answer:* Period: 1.56 nm/nm, versus tooth width: 0.215 nm/nm. Period is about 7 times stronger.

9. The measured coupler had −4.64 dB loss but the simulation said −2.74 dB. Give the main reason.

   *Answer:* The simulation assumed no gap between the fibre and the chip. In reality the fibre ribbon sat some distance above the chip, so the beam spread and missed the ideal spot, adding loss and narrowing the bandwidth.

10. In the k-diagram (Figure 5.4b), what happens if $k_x = \beta - K$ is larger than the radius $k_0$ of the air circle?

    *Answer:* The vertical line never meets the circle, so there is no allowed outgoing angle: that order cannot radiate into air (it stays trapped or goes elsewhere).
