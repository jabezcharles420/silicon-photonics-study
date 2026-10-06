# Week 3 · Day 4 — Thursday 8 Oct 2026

*Simple-English study version of Chrostowski & Hochberg, Silicon Photonics Design, §6.1–6.2*

[:material-file-pdf-box: Download this day as PDF](day-04-thu-8-oct-2026.pdf){ .md-button }

## Before you start: the big picture

A photonic chip sends data as light. To put data onto light, you must change the light quickly, billions of times per second. The device that does this is called a **modulator**. Most silicon modulators work by changing the *phase* of the light. Phase is how far along its wave cycle the light is. To shift the phase, you change how fast the light travels through a short piece of the light pipe (the **waveguide**).

How do you change the speed of light inside silicon, quickly, with electricity? Silicon has no strong "electro-optic" effect like some special crystals have. But silicon has a weaker trick. When you add or remove free electric charges (electrons and holes) inside it, its refractive index changes a little. This is called the **plasma dispersion effect**. Section 6.1 gives the formulas that say *how much* the index changes, and how much extra light is absorbed, for a given number of charges. Section 6.2 shows how to build a real device around this: a **pn-junction** placed across the waveguide. With a voltage you can sweep charges out of the light's path. That shifts the phase. Then the section asks how big the shift is, how much light is lost, and how fast the device can respond.

An everyday analogy: imagine a crowded hallway (the waveguide) with people walking through (the light). If you clear some furniture (free charges) out of the hallway, people walk at a slightly different speed. Furniture also trips some people up (absorption). The pn-junction is a machine that pushes furniture out of the hallway when you press a button (apply a voltage). The faster the machine can push furniture in and out, the faster you can send messages.

## Background you need

**Light as a wave.** Light is a wave of electric and magnetic fields. It wiggles up and down as it moves. The distance between two crests is the **wavelength**, $\lambda$. Telecom light uses $\lambda = 1550$ nm or $1310$ nm (nm = nanometre = $10^{-9}$ m). These are infrared, invisible to the eye. Silicon is transparent at these wavelengths, which is why it is useful.

**Refractive index $n$.** Light travels slower in a material than in vacuum. The refractive index tells you how much slower: speed $= c/n$, where $c$ is the speed of light in vacuum. Silicon has $n \approx 3.48$ at 1550 nm. A change $\Delta n$ means a small change in that number ($\Delta$, "delta", always means "change in").

**Phase and phase shift.** As light travels a length $L$, its wave goes through many cycles. The total "angle" it turns through is the **phase**, $\phi = 2\pi n L/\lambda$ (one full cycle is $2\pi$ radians). If you change $n$ by $\Delta n$, the phase changes by

$$\Delta\phi = \frac{2\pi\,\Delta n\,L}{\lambda}.$$

A shift of $\pi$ radians (half a cycle) turns a crest into a trough. That is the amount you need to switch light fully on or off in an interferometer (see next point).

**Interference and why phase matters.** If you split light into two paths and recombine it, the two waves add. In step (same phase): bright. Half a cycle apart ($\pi$ shift): they cancel, dark. A **Mach-Zehnder modulator** uses this: a phase shifter in one arm turns phase changes into brightness changes. A **ring modulator** is a loop of waveguide; a phase change shifts the colour at which the ring traps light. Both need a phase shifter, which is what Section 6.2 builds.

**Waveguide, mode, effective index.** A **waveguide** is a strip of high-index material (silicon) surrounded by low-index material (oxide or air). Light is trapped inside, like water in a pipe, by total internal reflection. The light settles into a fixed cross-sectional shape called a **mode**. Part of the mode sits in the silicon and part leaks into the surroundings. So the light "feels" an average index called the **effective index**, $n_{eff}$. This is the index that sets the phase. A **rib waveguide** is a silicon ridge (the rib) standing on a thinner silicon layer (the **slab**). The slab lets us make electrical contact from the side.

**Absorption coefficient $\alpha$.** When light is absorbed, its power falls exponentially with distance: $P(L) = P(0)\,e^{-\alpha L}$. $\alpha$ has units of 1/length, e.g. cm$^{-1}$. To convert to decibels: loss in dB $= 4.34\,\alpha L$. So $\alpha = 1$ cm$^{-1}$ is about 4.3 dB/cm.

**Decibels (dB).** A log scale for ratios: $10\log_{10}(P_{out}/P_{in})$. 3 dB means a factor of 2 in power. 10 dB means a factor of 10.

**Electrons and holes (carriers).** In a pure silicon crystal, almost all electrons are locked in chemical bonds. A few break free and can move; they carry current. When an electron leaves a bond, it leaves an empty spot. Neighbouring electrons can hop into that spot, so the empty spot itself moves around like a positive charge. We call it a **hole**. Electrons and holes are both called **free carriers**. Their number per cubic centimetre is the **carrier density**, written $N$ (electrons) and $P$ (holes), in cm$^{-3}$. Pure silicon at room temperature has only about $n_i \approx 10^{10}$ cm$^{-3}$ of each. This is the **intrinsic carrier density**. For comparison, silicon has about $5\times 10^{22}$ atoms per cm$^3$.

**Doping.** We add a tiny amount of impurity atoms on purpose. Phosphorus atoms each give away one extra free electron; these are **donors**, density $N_D$, and the silicon becomes **n-type**. Boron atoms each grab an electron, creating a free hole; these are **acceptors**, density $N_A$, and the silicon becomes **p-type**. Typical doping in a modulator: $10^{17}$ to $10^{18}$ cm$^{-3}$. Heavier doping ($10^{19}$–$10^{20}$, written p++ or n++) is used near the metal contacts to make good electrical connections. In n-type silicon, electrons are the **majority carriers** and holes are the rare **minority carriers**; in p-type it is the other way round. A useful rule: (electron density) × (hole density) $= n_i^2$ in equilibrium. So in p-type silicon with $N_A$ holes, the electron density is only $n_i^2/N_A$.

**The pn-junction.** Put p-type silicon next to n-type silicon. Near the boundary, electrons from the n side and holes from the p side meet and cancel (recombine). This leaves a thin zone with almost no free carriers: the **depletion region**, width $W_d$. The fixed, charged impurity atoms left behind create a built-in electric field and a **built-in voltage** $V_{bi}$ (around 0.7–1 V). If you apply a voltage that pulls the sides apart (**reverse bias**: + on n side, − on p side), the depletion region gets wider and more carriers are swept out. Very little current flows. If you push the other way (**forward bias**), current flows and carriers are injected. A depletion modulator uses reverse bias.

**A pn-junction is a capacitor.** The depletion region is an insulating gap between two conducting regions (the p and n sides). That is exactly a parallel-plate capacitor. A capacitor plus the resistance of the wires feeding it is an **RC circuit**. It cannot charge or discharge faster than about the time $RC$. This limits the speed of the modulator.

**Permittivity $\epsilon$.** How strongly a material "stores" electric field. $\epsilon_0 = 8.85\times10^{-12}$ F/m is the value for vacuum; silicon's **relative permittivity** is $\epsilon_s \approx 11.7$.

**Thermal voltage $k_BT/q$.** $k_B$ is Boltzmann's constant, $T$ is temperature in kelvin, and $q = 1.6\times10^{-19}$ C is the charge of one electron. $k_BT/q \approx 0.0259$ V at room temperature. It is the natural voltage scale of thermal jiggling. Factors like $e^{qV/k_BT}$ appear whenever carriers must climb over an energy barrier.

**Log-log plots.** Both axes use powers of ten. A power law $y = a x^b$ appears as a straight line with slope $b$. Slope 1 means "doubling $x$ doubles $y$".

> **Key takeaways:**
>
> - Phase shift $\Delta\phi = 2\pi\,\Delta n\,L/\lambda$: a tiny index change over a long enough length gives a useful phase shift.
> - Free carriers are electrons (n-type, from donors) and holes (p-type, from acceptors).
> - A reverse-biased pn-junction sweeps carriers out of a depletion region, and acts as a capacitor.

## 6.1 Plasma dispersion effect

> **In one sentence:** adding free electrons or holes to silicon lowers its refractive index and makes it absorb more light, and simple formulas fitted to experiments tell you exactly how much.

### 6.1.1 Silicon, carrier density dependence

> **In one sentence:** these are the "conversion tables" from number of carriers to change in index and change in absorption.

**Why do free carriers change the index?** Free carriers behave a bit like a gas of charged particles, a **plasma**. The light's electric field shakes them back and forth. Shaken charges re-radiate, and this re-radiated light adds to the original light in a way that lowers the refractive index. Some of the shaking energy is lost when carriers bump into the crystal, and that loss is absorption. "Dispersion" here just means "change in refractive index". So **plasma dispersion effect** = "free carriers change the index".

In 1987, Soref and Bennett predicted the size of this effect in silicon. It is the basis of almost all silicon modulators. You change the number of carriers in the waveguide, either by **injecting** carriers (forward-biased PIN diode, Section 6.4) or by **removing** them (reverse-biased pn-junction, Section 6.2).

The formulas below are **phenomenological**. That means they are curve fits to measured data, not derived from deep theory. They are simple and widely used.

**Change in refractive index** (equation 6.1):

$$\Delta n\ (\text{1550 nm}) = -8.8\times 10^{-22}\,\Delta N - 8.5\times 10^{-18}\,\Delta P^{0.8}$$

$$\Delta n\ (\text{1310 nm}) = -6.2\times 10^{-22}\,\Delta N - 6\times 10^{-18}\,\Delta P^{0.8} \qquad (6.1)$$

**Change in absorption** (equation 6.2), in cm$^{-1}$:

$$\Delta\alpha\ (\text{1550 nm}) = 8.5\times 10^{-18}\,\Delta N + 6\times 10^{-18}\,\Delta P$$

$$\Delta\alpha\ (\text{1310 nm}) = 6\times 10^{-18}\,\Delta N + 4\times 10^{-18}\,\Delta P \qquad (6.2)$$

What the symbols mean:

- $\Delta N$ = change in free-electron density, in cm$^{-3}$.
- $\Delta P$ = change in free-hole density, in cm$^{-3}$.
- $\Delta n$ = change in silicon's refractive index (no units).
- $\Delta\alpha$ = change in absorption coefficient, in cm$^{-1}$.

What the equations say:

- The **minus signs** in $\Delta n$: more carriers means a *lower* index. Fewer carriers means a *higher* index.
- The **plus signs** in $\Delta\alpha$: more carriers means *more* absorption.
- Electrons enter the index formula linearly ($\Delta N^1$). Holes enter as $\Delta P^{0.8}$, a power a bit less than 1. So doubling the holes gives a bit less than double the effect.
- The 1310 nm coefficients are smaller than the 1550 nm ones. The effect grows with wavelength (more on this below).

**Worked example (1550 nm).** Add $10^{18}$ cm$^{-3}$ of electrons:
$\Delta n = -8.8\times10^{-22}\times10^{18} = -8.8\times10^{-4}$.
Add $10^{18}$ cm$^{-3}$ of holes instead: $(10^{18})^{0.8} = 10^{14.4} \approx 2.5\times10^{14}$, so $\Delta n = -8.5\times10^{-18}\times2.5\times10^{14} \approx -2.1\times10^{-3}$.
So the same number of holes changes the index about **2.4 times** more than electrons.
Absorption: electrons give $\Delta\alpha = 8.5$ cm$^{-1}$ (about 37 dB/cm); holes give $6$ cm$^{-1}$ (about 26 dB/cm).

Are these numbers big or small? The index change is about $10^{-3}$, compared with silicon's index of 3.48. That is a change of only about 0.03%. Tiny! That is why silicon modulators need lengths of millimetres (Mach-Zehnder) or a resonance to amplify the effect (rings). Note also that $10^{18}$ cm$^{-3}$ is still only about 1 carrier for every 50,000 silicon atoms.

**Holes are the better deal.** Holes give a *larger* index shift and a *smaller* absorption than electrons. You want lots of phase change with little loss. So designers prefer to work with holes. In practice they shift the junction off-centre in the waveguide (an **offset junction**) so more of the light overlaps the region where holes are removed. This is used in Mach-Zehnder and ring modulators.

**The 2011 update (equations 6.3 and 6.4).** Newer measurements gave slightly different fits. The index change:

$$\Delta n\ (\text{1550 nm}) = -5.4\times 10^{-22}\,\Delta N^{1.011} - 1.53\times 10^{-18}\,\Delta P^{0.838}$$

$$\Delta n\ (\text{1310 nm}) = -2.98\times 10^{-22}\,\Delta N^{1.016} - 1.25\times 10^{-18}\,\Delta P^{0.835} \qquad (6.3)$$

Same shape as before: a coefficient times a power of the carrier density. The powers are now fitted too (1.011 for electrons, about 0.84 for holes). Quick check at 1550 nm, $10^{18}$ cm$^{-3}$: electrons give about $-8.5\times10^{-4}$, holes about $-1.9\times10^{-3}$. Very close to the 1987 values.

**Figure 6.1 — Change in index versus carrier density (equation 6.3).** A log-log plot. The x-axis is carrier density from $10^{17}$ to $10^{20}$ cm$^{-3}$. The y-axis is the size of the index change, from about $10^{-5}$ to a few times $10^{-2}$. There are four straight lines: electrons and holes, each at 1550 nm and 1310 nm. The two hole lines ("Free holes") sit above the two electron lines ("Free electrons"). At $10^{17}$ cm$^{-3}$, holes at 1550 nm give about $3\times10^{-4}$, electrons at 1550 nm about $9\times10^{-5}$. For each carrier type, the 1550 nm line sits above the 1310 nm line. Lessons:

- Straight lines on log-log axes mean power laws, as in the equation.
- Holes give the larger index change, especially at the low densities ($10^{17}$–$10^{18}$) used in modulators.
- The hole lines are less steep (power 0.84 < 1), so the gap between holes and electrons shrinks at very high densities.
- The effect is stronger at the longer wavelength (1550 nm).

**Change in absorption, 2011 version** (in cm$^{-1}$):

$$\Delta\alpha\ (\text{1550 nm}) = 8.88\times 10^{-21}\,\Delta N^{1.167} + 5.84\times 10^{-20}\,\Delta P^{1.109}$$

$$\Delta\alpha\ (\text{1310 nm}) = 3.48\times 10^{-22}\,\Delta N^{1.229} + 1.02\times 10^{-19}\,\Delta P^{1.089} \qquad (6.4)$$

Now the powers are slightly *above* 1. So absorption grows a little faster than linearly with carrier density. Check at $10^{18}$ cm$^{-3}$, 1550 nm: electrons give about 9 cm$^{-1}$, holes about 5 cm$^{-1}$. Again close to the older formula.

**Figure 6.2 — Change in absorption versus carrier density (equation 6.4).** Another log-log plot. x-axis: $10^{17}$ to $10^{20}$ cm$^{-3}$. y-axis: $\Delta\alpha$ from 1 to about 1000 cm$^{-1}$ (the lowest curves start a bit below 1). Four straight lines. Electrons at 1550 nm are the top line, from about 0.6 cm$^{-1}$ at $10^{17}$ to over $10^3$ at $10^{20}$. Holes at 1550 nm sit below that. At 1310 nm the curves are lower at low density. The electron-1310 line is steeper, so it crosses above the hole-1550 line somewhere near $5\times10^{17}$–$10^{18}$ cm$^{-3}$. Lessons:

- Absorption rises steadily (power law) with carrier density.
- At 1550 nm, electrons absorb more than holes: one more reason to prefer holes.
- At very high densities ($10^{19}$–$10^{20}$, like contact regions) the loss is hundreds of cm$^{-1}$, i.e. thousands of dB/cm. That is why heavily doped contacts must be kept away from the light.

**Wavelength dependence (equation 6.5).** A simple theory of free carriers, the **Drude model**, treats them as free charged balls shaken by the light and slowed by friction. It predicts that both the index change and the absorption grow as $\lambda^2$. Why $\lambda^2$? Longer wavelength means slower shaking (lower frequency). Free charges respond more strongly to slow shaking; the response scales as $1/\text{frequency}^2$, which is $\propto \lambda^2$. Putting this $\lambda^2$ into equations 6.1 and 6.2 gives:

$$\Delta n(\lambda) = -3.64\times 10^{-10}\lambda^{2}\,\Delta N - 3.51\times 10^{-6}\lambda^{2}\,\Delta P^{0.8}$$

$$\Delta\alpha(\lambda) = 3.52\times 10^{-6}\lambda^{2}\,\Delta N + 2.4\times 10^{-6}\lambda^{2}\,\Delta P \quad [\text{cm}^{-1}] \qquad (6.5)$$

Here $\lambda$ is in **metres**. Check: at $\lambda = 1.55\times10^{-6}$ m, $\lambda^2 = 2.4\times10^{-12}$ m$^2$. Then $3.64\times10^{-10}\times2.4\times10^{-12} \approx 8.8\times10^{-22}$. That is exactly the 1550 nm electron coefficient in equation 6.1. So equation 6.5 is just equation 6.1/6.2 with the wavelength scaling made explicit. It lets you use any wavelength, not just the two fitted ones.

**Figure 6.3 — Index change (a) and absorption change (b) versus wavelength.** Two panels. x-axis: wavelength from 1.1 to 2.0 µm (linear). y-axes are logarithmic: about $10^{-4}$ to $10^{-2}$ for the index change, and 1 to 100 cm$^{-1}$ for absorption. (The image's panel labels may appear swapped relative to the caption; the y-ranges tell you which is which.) Each panel has six solid lines from equation 6.5: electrons and holes at $10^{17}$, $10^{18}$, and $10^{19}$ cm$^{-3}$. Each step of 10× in density moves a pair of lines up by about one decade. All lines rise with wavelength: over this range, $\lambda^2$ grows by about $(2.0/1.1)^2 \approx 3.3$ times. Markers show data points: crosses (×) from equations 6.1/6.2, which sit right on the lines; circles and triangles from the 2011 data, which sit slightly above or below. In the index panel, holes are above electrons. In the absorption panel, electrons are above holes. Lessons:

- The $\lambda^2$ model matches the fitted data well.
- Longer wavelength gives a stronger effect, both for index (good) and absorption (bad).
- The 1987 and 2011 fits differ only a little.

> **Key takeaways:**
>
> - More free carriers means lower index and more absorption; removing carriers does the opposite.
> - At 1550 nm and $10^{18}$ cm$^{-3}$: $|\Delta n| \approx 10^{-3}$ (holes ~2× electrons), $\Delta\alpha \approx 5$–$9$ cm$^{-1}$.
> - Holes give more index change and less absorption than electrons, so designs favour holes (offset junctions).
> - Both effects scale as $\lambda^2$ (Drude model), so they are stronger at 1550 nm than at 1310 nm.
> - The index change is tiny (~0.03% of silicon's index), so devices must be long or resonant.

## 6.2 pn-Junction phase shifter

> **In one sentence:** put a pn-junction across a rib waveguide, apply a reverse voltage to sweep carriers out of the light's path, and calculate the resulting phase shift, loss and speed.

### 6.2.1 pn-Junction carrier distribution

> **In one sentence:** for a given voltage, we work out where the free electrons and holes are inside the waveguide, using a simple 1D model.

The device is a **carrier-depletion phase modulator**. Picture a rib waveguide seen end-on. The left part of the rib is p-type, the right part is n-type, and the boundary (the junction) runs along the waveguide near its centre. Far out on each side, in the slab, are heavily doped regions (p++ and n++) that touch the metal contacts. Light travels into the page.

```
   metal                                         metal
     |          p side   |  n side                 |
   [p++]=====[ p  ][  p  |  n  ][ n  ]=========[n++]
                    rib (w wide)
            <----- y ----->   junction at y_offset
```

**Figure 6.4 — pn-junction in a rib waveguide.** Three panels lined up one above the other, with dashed vertical lines linking the same positions.

- **(a) Doping (impurities).** Rib of width $w$ on a slab. From left to right: a heavily doped $N_{A++}$ region, a p region with acceptor density $N_A$, an n region with donor density $N_D$, and a heavily doped $N_{D++}$ region. The junction is at position 0, shifted from the rib centre by $y_{offset}$. The distances $d_{p++}$ and $d_{n++}$ mark how far the heavy doping sits from the junction.
- **(b) Carriers.** Same cross-section, now showing free carriers: p++, p, then a light-blue **depletion region** of width $W_d$ around the junction (no free carriers), then n, n++.
- **(c) 1D carrier profile along $y$.** Hole density $p$ (red) is flat at $N_A$ on the p side, falls to 0 in the depletion region, and is tiny ($p_{n0}$) on the n side. Electron density $n$ (blue) is tiny ($n_{p0}$) on the p side, 0 in the depletion region, and jumps to $N_D$ on the n side. Marked positions: $y_{p++}$, $y_p$, $0$, $y_n$, $y_{n++}$.

Lesson: the light's mode sits in the rib. Where the depletion region overlaps the mode, carriers are missing. Change the voltage, change the width of that empty zone, change the index the light feels.

**Simplifying assumptions.**

1. **Abrupt (step) junction.** In reality, dopants spread out (diffuse) during fabrication, so the doping changes gradually. We pretend it jumps sharply from p to n at the edge of the lithography mask. This makes the maths easy.
2. **Short device compared with the diffusion length.** The **diffusion length** is how far a minority carrier wanders before it recombines. The junction regions are much narrower than this. So we assume the minority carrier density changes in a straight line between the edge of the depletion region and the heavily doped region.

**Depletion width (equation 6.6).**

$$W_{d} = \sqrt{\frac{2\epsilon_{0}\epsilon_{s}(N_{A}+N_{D})(V_{bi}-V)}{q\,N_{A}N_{D}}} \qquad (6.6)$$

- $W_d$: width of the carrier-free region.
- $\epsilon_0\epsilon_s$: permittivity of silicon.
- $N_A, N_D$: acceptor and donor densities.
- $V_{bi}$: built-in voltage; $V$: applied voltage; $q$: electron charge.

What it says: the width grows like the **square root** of $(V_{bi}-V)$. With the sign convention here, a reverse bias is a negative $V$, which makes $V_{bi} - V$ larger and the depletion region wider. Heavier doping (bigger $N_A N_D$ in the bottom) makes the region *narrower*: there are more fixed charges per unit volume, so a thin layer is enough to hold the voltage. The square root appears because the field builds up linearly across the charged layer, so the voltage (area under the field) grows like width squared.

**Built-in voltage (equation 6.7).**

$$V_{bi} = \frac{k_{B}T}{q}\ln\frac{N_{A}N_{D}}{n_{i}^{2}} \qquad (6.7)$$

$k_BT/q \approx 0.026$ V is the thermal voltage, and $n_i \approx 10^{10}$ cm$^{-3}$ is the intrinsic carrier density. The log comes from Boltzmann statistics: carriers spread over an energy barrier, and the barrier height is set by how different the carrier densities on the two sides are.

**Illustrative example** (my numbers, not the book's): $N_A = N_D = 10^{18}$ cm$^{-3}$. Then $N_AN_D/n_i^2 = 10^{36}/10^{20} = 10^{16}$, $\ln(10^{16}) \approx 36.8$, so $V_{bi} \approx 0.026\times36.8 \approx 0.95$ V. Putting this into 6.6 at $V=0$ (with $\epsilon_s = 11.7$) gives $W_d \approx 50$ nm. That is about a tenth of the 500 nm rib width. A few volts of reverse bias roughly doubles it. So the empty zone is small compared with the mode: only part of the light sees the change.

**Edges of the depletion region (equation 6.8).**

$$y_{p} = y_{offset} - \frac{W_{d}}{1+N_{A}/N_{D}} \qquad (6.8a)$$

$$y_{n} = y_{offset} + \frac{W_{d}}{1+N_{D}/N_{A}} \qquad (6.8b)$$

The depletion region does not have to be centred on the junction. The negative charge removed from the p side must equal the positive charge removed from the n side (charge balance): $N_A \times (\text{p-side width}) = N_D \times (\text{n-side width})$. So the region reaches further into the *more lightly* doped side. If $N_A = N_D$, each side gets $W_d/2$. The term $y_{offset}$ is where the junction sits relative to the rib centre.

**Electron density (equation 6.9).**

$$n(y, V) = \begin{cases}
\frac{n_{p0}}{1+\left(1-\frac{y_{p}-y}{y_{p}-y_{p++}}\right)\left(e^{qV/k_{B}T}-1\right)} & \text{for } y_{p++} < y < y_{p}\\
0 & \text{for } y_{p} < y < y_{n}\\
N_{D} & \text{for } y_{n} < y < y_{n++}
\end{cases} \qquad (6.9)$$

**Hole density (equation 6.10).**

$$p(y, V) = \begin{cases}
N_{A} & \text{for } y_{p++} < y < y_{p}\\
0 & \text{for } y_{p} < y < y_{n}\\
\frac{p_{n0}}{1+\left(1-\frac{y-y_{n}}{y_{n++}-y_{n}}\right)\left(e^{qV/k_{B}T}-1\right)} & \text{for } y_{n} < y < y_{n++}
\end{cases} \qquad (6.10)$$

(The printed book has a typo in the last line of 6.10: the denominator should be $y_{n++}-y_n$, mirroring equation 6.9, as written here.)

How to read them, region by region:

- **On the p side** (between the p++ contact region and the depletion edge): holes are the majority, density $N_A$, one per acceptor atom. Electrons are the minority, tiny.
- **In the depletion region:** both are zero. That is the definition of "depleted".
- **On the n side:** electrons are the majority, density $N_D$. Holes are the minority, tiny.
- **The minority-carrier formula.** The fraction like $\frac{y_p - y}{y_p - y_{p++}}$ runs from 0 at the depletion edge to 1 at the heavily doped edge. So the bracket $\left(1 - \text{fraction}\right)$ runs from 1 to 0. At the heavily doped edge the density equals its equilibrium value $n_{p0}$. At the depletion edge it is changed by the exponential factor $e^{qV/k_BT}$, which comes from the voltage changing the barrier. Between the two, it varies smoothly. This is the "linear distribution" assumption in action.

Equilibrium minority densities (equation 6.11), from the rule $n \times p = n_i^2$:

$$n_{p0} = \frac{n_{i}^{2}}{N_{A}} \qquad (6.11a)$$

$$p_{n0} = \frac{n_{i}^{2}}{N_{D}} \qquad (6.11b)$$

With $N_A = 10^{18}$ and $n_i = 10^{10}$: $n_{p0} = 10^{20}/10^{18} = 100$ cm$^{-3}$. Compare that with $10^{18}$ majority holes. Minority carriers are utterly negligible for the optics. **The optical effect comes from the majority carriers vanishing inside the growing depletion region.** For the optics, these profiles give $\Delta N = n(y,V)$ and $\Delta P = p(y,V)$, which go into equations 6.1–6.5.

**MATLAB code 6.1** (not reproduced). What it does:

1. Takes the doping levels, geometry and junction offset as inputs.
2. For each voltage, computes $V_{bi}$ (6.7), $W_d$ (6.6) and the depletion edges (6.8).
3. Fills in $n(y)$ and $p(y)$ across the waveguide using 6.9–6.11.
4. Outputs the carrier profiles versus position, one set per voltage.

> **Key takeaways:**
>
> - A reverse-biased pn-junction creates a carrier-free zone of width $W_d \propto \sqrt{V_{bi}-V}$.
> - The zone extends further into the lighter-doped side (charge balance).
> - Outside the zone, majority carriers equal the doping; minority carriers are negligible ($n_i^2/N$).
> - Changing the voltage changes how many carriers sit where the light is.

### 6.2.2 Optical phase response

> **In one sentence:** weight the carrier-induced index and loss changes by where the light actually is, to get the change in effective index, phase and loss versus voltage.

Equations 6.1 and 6.2 tell us the index and loss change *at each point* in the silicon core ($n_{co}$ is the core index). But the light is spread out. It is bright in the middle of the rib and dim at the edges. Carriers removed where the light is bright matter a lot; carriers removed where it is dark hardly matter. So we take a **weighted average**, with the light's intensity as the weight.

$$n_{eff}(V) = n_{eff,i} + \frac{\int E^{*}(y)\,\Delta n(y, V)\,E(y)\,dy}{\int E^{*}(y)\,E(y)\,dy}\cdot\frac{dn_{eff}}{dn_{co}}$$

$$\alpha_{pn}(V) = \frac{\int E^{*}(y)\,\Delta\alpha(y, V)\,E(y)\,dy}{\int E^{*}(y)\,E(y)\,dy} \qquad (6.12)$$

Symbols:

- $E(y)$: the electric field of the mode across the waveguide (1D profile). $E^*$ is its complex conjugate; $E^*E = |E|^2$ is the light intensity at position $y$.
- $\Delta n(y,V)$, $\Delta\alpha(y,V)$: local index and absorption change from the carriers at that point and voltage.
- The fraction (integral on top divided by integral on the bottom) is "average of $\Delta n$, weighted by intensity". This is called an **overlap integral**.
- $n_{eff,i}$: effective index of the same waveguide with no doping at all.
- $dn_{eff}/dn_{co}$: how much the mode's effective index moves when the core index moves. The book says it is very close to 1 for silicon strip and rib waveguides, so you can mostly ignore it.
- $\alpha_{pn}$: the free-carrier loss felt by the mode.

The field $E(y)$ comes from the **effective index method** (MATLAB function 3.11, from an earlier chapter). This method squashes a 2D waveguide cross-section into an equivalent 1D problem.

Then the change in effective index and phase:

$$\Delta n_{eff}(V) = n_{eff}(V) - n_{eff}(0)$$

$$\Delta\phi(V)\;[\pi\cdot\text{cm}^{-1}] = \frac{0.02\,\Delta n_{eff}(V)}{\lambda} \qquad (6.13)$$

Where does 0.02 come from? Start from $\Delta\phi = 2\pi\,\Delta n_{eff}\,L/\lambda$. Measure the phase in units of $\pi$ and take $L = 1$ cm $= 0.01$ m: $\Delta\phi/\pi = 2\times0.01\times\Delta n_{eff}/\lambda = 0.02\,\Delta n_{eff}/\lambda$, with $\lambda$ in metres. So the result is "how many $\pi$'s of phase shift per cm of device". Example: to get a shift of $\pi$ in 1 cm at 1550 nm you need $\Delta n_{eff} = \lambda/0.02 = 1.55\times10^{-6}/0.02 \approx 7.8\times10^{-5}$.

**Example design (MATLAB code 6.2).**

- Rib width $w = 500$ nm, rib thickness $t = 220$ nm, slab thickness $t_{slab} = 90$ nm. These are standard silicon photonics dimensions.
- Because holes have the stronger index effect (equation 6.1), the junction is shifted **50 nm** off the waveguide centre. This puts more of the depletion action on the hole side, under the brightest light, and improves **modulation efficiency** (phase shift per volt).

Code 6.2 computes the carrier profiles (code 6.1), converts them into $\Delta n$ and $\Delta\alpha$ with the plasma-dispersion formulas, does the overlap integrals (6.12), and outputs $\Delta n_{eff}$, loss and phase versus voltage. MATLAB code 6.3 plots the results.

**Figure 6.5 — Effective index change and free-carrier loss versus reverse voltage.** x-axis: reverse voltage 0 to 10 V. Left y-axis (blue curve): $\Delta n_{eff}$, from 0 up to about $2.65\times10^{-4}$ at 10 V (about $1.9\times10^{-4}$ at 5 V). Right y-axis (green curve): loss in dB/cm, falling from about 10.2 dB/cm at 0 V to about 5.9 dB/cm at 10 V (about 7.2 at 5 V). Both curves change fast at low voltage and flatten at high voltage. Lessons:

- More reverse voltage removes more carriers, so the index goes *up* (fewer carriers, less negative $\Delta n$) and the loss goes *down*.
- The flattening comes from $W_d \propto \sqrt{V}$: each extra volt widens the depletion region less than the previous one.
- Even at high voltage, several dB/cm of loss remains, from the doped regions the depletion does not reach.

**Figure 6.6 — Phase change versus reverse voltage.** x-axis: 0 to 10 V. y-axis: phase shift for a 1 cm long device, in units of $\pi$ (0 to 4). The curve starts at 0 and rises, steep at first, then flattening, reaching about $3.5\pi$ at 10 V. A dashed marker shows a phase of $\pi$ (value 1) at **1.6 V**.

So a 1 cm long phase shifter needs 1.6 V for a $\pi$ shift. This gives the standard figure of merit $V_\pi \cdot L = 1.6$ V·cm. **$V_\pi$** is the voltage for a $\pi$ phase shift. Multiplying by length gives a number that does not depend on how long you build the device: a 2 mm device would need about $1.6/0.2 = 8$ V (if the curve were linear; in reality it is not quite linear). Smaller $V_\pi L$ is better. Note that the phase curve has the same shape as $\Delta n_{eff}$ in Figure 6.5, as equation 6.13 says it must (phase is just $\Delta n_{eff}$ times a constant).

> **Key takeaways:**
>
> - The mode feels an intensity-weighted average of the local index change (overlap integral).
> - $\Delta\phi/\pi$ per cm $= 0.02\,\Delta n_{eff}/\lambda$; a $\pi$ shift in 1 cm at 1550 nm needs $\Delta n_{eff} \approx 7.8\times10^{-5}$.
> - Example design: 500 × 220 nm rib, 90 nm slab, 50 nm junction offset gives $V_\pi L = 1.6$ V·cm.
> - Reverse bias raises $n_{eff}$ and lowers the loss (about 10 to 6 dB/cm over 0–10 V); both effects flatten at high voltage.

### 6.2.3 Small-signal response

> **In one sentence:** the junction is a capacitor fed through resistive silicon, and its RC time sets how fast it can switch.

"Small-signal" means we look at small wiggles of voltage around a fixed DC bias, so the circuit behaves like a simple linear R and C.

$$R_{j}\;[\Omega\cdot\text{m}] = \left(\frac{w}{2}+y_{p}\right)R_{srp}+\left(\frac{w}{2}-y_{n}\right)R_{srn}-\left(\frac{w}{2}+y_{p++}\right)R_{ssp}+\left(y_{n++}-\frac{w}{2}\right)R_{ssn}$$

$$C_{j}\;[\text{F/m}] = t_{rib}\sqrt{\frac{q\,\epsilon_{0}\epsilon_{s}}{2(1/N_{D}+1/N_{A})(V_{bi}-V)}} \qquad (6.14)$$

**Resistance.** Current flows sideways from the contact, through the slab, through the rib, to the junction. Each region contributes "length of path × **sheet resistance**". Sheet resistance ($R_s$, in ohms per square) is the resistance of a square piece of a thin layer; it depends on the doping and the layer thickness. The four sheet resistances are:

- $R_{srp}$, $R_{srn}$: the p-doped and n-doped **rib**.
- $R_{ssp}$, $R_{ssn}$: the p-doped and n-doped **slab**.

The terms in brackets are the lengths of each part of the path. For example, $\frac{w}{2} - y_n$ is the distance from the depletion edge on the n side to the rib edge. (Positions on the p side are negative numbers, which is why the signs look odd; each bracket works out to a positive distance.) The units Ω·m mean "resistance times waveguide length": a longer device has more parallel paths, so its resistance is lower, $R = R_j / L$.

**Capacitance.** This formula is just a parallel-plate capacitor in disguise. If you put equation 6.6 into $\epsilon_0\epsilon_s/W_d$, you get exactly the square root above. So

$$C_j = \frac{\epsilon_0 \epsilon_s\, t_{rib}}{W_d}$$

Here the plate area per unit length $= t_{rib}$ (the height of the rib), and plate gap $= W_d$. Wider depletion region means lower capacitance. Units F/m: capacitance per metre of device; a longer device has proportionally more capacitance.

**Cutoff frequency (equation 6.15).**

$$f_{c} = \frac{1}{2\pi R_{j}C_{j}} \qquad (6.15)$$

An RC circuit responds well to slow signals but cannot keep up with fast ones. At $f_c$ the response has dropped by 3 dB (half the power). This is the **3 dB cutoff frequency**, or **bandwidth**. Notice the device length cancels: $R \propto 1/L$ and $C \propto L$, so the product $R_jC_j$ is in seconds and does not depend on length.

**Results.** For the design above, $f_c = 35$ GHz at 0 V and 51 GHz at 1 V (reverse). Higher reverse voltage widens the depletion region, which lowers *both* $C_j$ (bigger gap) and $R_j$ (the current path through undepleted silicon gets shorter). So $f_c$ rises with voltage.

**Figure 6.7 — Cutoff frequency versus reverse voltage.** x-axis: 0 to 10 V. y-axis: cutoff frequency, roughly 40 to 160 (GHz). The curve rises from roughly 42 at 0 V to about 115 at 5 V and about 152 at 10 V. It is steep at first, then flattens (again the $\sqrt{V}$ behaviour of $W_d$). (The plotted value at 0 V looks a little higher than the 35 GHz quoted in the text; take the trend as the lesson.) Lesson: the junction itself is fast, tens to over a hundred GHz.

**So is RC ever the bottleneck?** The junction's own RC is usually *not* what limits a silicon modulator. RC becomes a problem when you use a **long** junction (big total capacitance, e.g. a few mm in a Mach-Zehnder) driven from a source with a fixed **source impedance**, typically 50 Ω. Now the resistance is the fixed 50 Ω, not the tiny junction resistance, and the capacitance is large. Example: 50 Ω × 2 pF = 100 ps, so $f_c \approx 1.6$ GHz, much too slow. The fix is a **travelling-wave electrode**: the metal lines are designed as a transmission line so the electrical signal travels alongside the light, instead of charging the whole capacitor at once.

**Design trade-off.** You can lower $R_j$ by using higher doping and by placing the heavily doped contact regions closer to the junction. But heavily doped silicon absorbs a lot of light (Figure 6.2), so contacts too close to the mode add optical loss. Speed versus loss is a key trade-off. The book analyses this for the PIN junction in Section 6.4 (Figure 6.16); the pn-junction behaves similarly.

> **Key takeaways:**
>
> - $C_j = \epsilon_0\epsilon_s t_{rib}/W_d$ (parallel plate); $R_j$ = sum of path lengths × sheet resistances.
> - $f_c = 1/(2\pi R_jC_j)$ is independent of length: 35 GHz at 0 V, 51 GHz at 1 V here, rising with reverse bias.
> - The junction itself is fast; long devices driven by 50 Ω sources are RC-limited, hence travelling-wave electrodes.
> - Moving contacts closer lowers R but raises optical loss.

### 6.2.4 Numerical TCAD modelling of pn-junctions

> **In one sentence:** instead of the simple 1D formulas, use 2D computer simulation of both the electrical charges and the light, calibrated against a real measured device.

**Why go beyond the 1D model?** The 1D model of 6.2.1 and the effective-index optics of 6.2.2 are fast and give good intuition. But they ignore how carriers are distributed vertically, and they need many input numbers you may not know well (sheet resistances, contact resistances). **TCAD** (Technology Computer-Aided Design) tools solve the semiconductor equations numerically on a 2D grid of the real cross-section. They should be more accurate.

**The example device.** The geometry copies a published modulator by T. Baehr-Jones et al.: a rib waveguide with the pn-junction in the centre, using the paper's peak doping levels and doping-region sizes. The doping profile is built from simple analytic shapes (a **process simulation**, which simulates the fabrication steps, could also be used). To make the model match reality, the authors **calibrated** it: they adjusted the size and position of the doping shapes until the simulated capacitance-versus-voltage curve matched the measured one.

**The workflow, step by step** (Lumerical scripts, Listings 6.8–6.10, not reproduced):

1. **Define everything** (Listing 6.8): waveguide geometry, doping, contacts, simulation regions.
2. **Electrical simulation** (Listing 6.9): for each voltage from $-0.4$ to $4$ V, solve for the 2D distribution of electrons and holes. Export the charge density map at each voltage.
3. **Capacitance.** The capacitance is $C = dQ/dV$: how much stored charge changes per volt. A **charge monitor** adds up all the carriers in the simulation volume to give the total charge $Q$. Run at $V$ and $V + \Delta V$ and take the difference:

   $$C_{n,p} = \frac{Q_{n,p}(V+\Delta V)-Q_{n,p}(V)}{\Delta V}$$

   $C_n$ uses the electron charge and $C_p$ the hole charge. They should come out equal; if they do not, the simulation has not converged properly (a good built-in sanity check). The total charge is sensitive to the **mesh** (the size of the grid cells), especially at the junction where carriers change sharply. So a **mesh override** (finer grid there) is used.

4. **Resistance.** Put a metal contact right at the junction, splitting the device into its n half and p half. Simulate each half: apply a voltage, measure the current, get the resistance. Here the total series resistance is **2 Ω**.
5. **Optical simulation** (Listing 6.10): load the carrier maps, convert them to index and absorption changes with equation 6.5 (or similar), solve for the optical mode at each voltage, and get $n_{eff}$ versus voltage, like Figure 6.5. Both the real part (index, gives phase) and the imaginary part (absorption, gives loss) are included.
6. **Export** the results to a file. They feed a **compact model**: a small, fast description of the phase shifter (phase and loss versus voltage, plus R and C) that a circuit simulator can use. It is used later for a ring modulator (Figure 9.13) or a travelling-wave modulator; the compact model is built in Listing 9.3.

**Figure 6.8 — Capacitance of the pn-junction modulator versus voltage.** x-axis: voltage from about $-0.3$ to 4 V (positive = reverse bias). y-axis: capacitance, 1.4 to 2.8 (pF, matching the "∼2 pF" in the text). Two curves: TCAD simulation (blue dashed with circles) and experiment (green solid). Both start near 2.6 at $-0.3$ V, are about 2.25 at 0 V, and fall to about 1.4–1.5 at 4 V. They agree closely near 0 V; above about 1 V the measured capacitance stays slightly higher than the simulation (about 1.5 vs 1.4 at 4 V). Lessons:

- The capacitance is about 2 pF and drops with reverse bias, because the depletion region widens (equation 6.6), just as the parallel-plate picture predicts.
- The calibrated simulation matches the real device well, which builds trust in the rest of the model.

A rough consistency check (my arithmetic from the two quoted numbers): $R \approx 2$ Ω and $C \approx 2$ pF give $RC \approx 4$ ps, so $f_c = 1/(2\pi\times4\text{ ps}) \approx 40$ GHz. That is the same tens-of-GHz range as Section 6.2.3.

> **Key takeaways:**
>
> - 2D TCAD simulation is more accurate than the 1D model, and is calibrated against measured C–V data.
> - Workflow: define → carrier maps vs voltage → capacitance from $dQ/dV$ → resistance → optical mode vs voltage → compact model.
> - Example device: about 2 pF and 2 Ω, with good simulation–experiment agreement.
> - Use a fine mesh at the junction; check that $C_n = C_p$ as a convergence test.

> **Key takeaways (Section 6.2 overall):**
>
> - A reverse-biased pn-junction across a rib waveguide is a fast, low-current phase shifter.
> - Its performance is summed up by $V_\pi L$ (1.6 V·cm in the example), loss (several dB/cm), and bandwidth (tens of GHz).
> - Offsetting the junction to favour holes improves efficiency.
> - Simple analytic models give insight; TCAD gives accuracy; both feed a compact model for circuit design.

## Glossary

| Term | Plain meaning |
|---|---|
| Abrupt (step) junction | Model where doping jumps sharply from p-type to n-type at one line. |
| Absorption coefficient ($\alpha$) | How fast light power decays with distance; units 1/length (cm$^{-1}$). |
| Acceptor | Impurity atom (e.g. boron) that creates a free hole; density $N_A$. |
| Bandwidth / 3 dB cutoff frequency ($f_c$) | Frequency where the response has fallen to half power; how fast the device can go. |
| Built-in voltage ($V_{bi}$) | Voltage that appears naturally across a pn-junction, about 0.7–1 V. |
| Capacitance | How much charge a structure stores per volt. |
| Carrier / free carrier | A mobile charge: an electron or a hole. |
| Carrier density | Number of carriers per cm$^3$. |
| Charge monitor | Simulation tool that adds up all charge in a volume. |
| Compact model | Small, fast summary of a device's behaviour for circuit simulation. |
| Decibel (dB) | Log unit for power ratios; 3 dB = factor 2, 10 dB = factor 10. |
| Depletion region | Zone around a pn-junction with almost no free carriers; width $W_d$. |
| Diffusion length | Average distance a minority carrier travels before recombining. |
| Donor | Impurity atom (e.g. phosphorus) that gives a free electron; density $N_D$. |
| Doping | Adding impurity atoms to control the number of free carriers. |
| Drude model | Simple theory treating free carriers as charged balls with friction; predicts $\lambda^2$ scaling. |
| Effective index ($n_{eff}$) | The average refractive index the guided light feels. |
| Effective index method | Trick that turns a 2D waveguide into an equivalent 1D problem. |
| Hole | Missing electron in a bond; moves like a positive charge. |
| Intrinsic carrier density ($n_i$) | Carrier density in pure silicon, about $10^{10}$ cm$^{-3}$. |
| Majority / minority carrier | The common / rare carrier type in a doped region. |
| Mach-Zehnder modulator | Interferometer with two arms; a phase shift in one arm changes output brightness. |
| Mesh / mesh override | The simulation grid; an override makes it finer in a chosen region. |
| Mode | Stable cross-sectional light pattern that travels along a waveguide. |
| Modulation efficiency | Phase shift obtained per volt (better = lower $V_\pi L$). |
| Modulator | Device that puts data on light by changing it quickly. |
| n-type / p-type | Silicon doped to have extra electrons / extra holes. |
| Offset junction | pn-junction placed off the waveguide centre (here 50 nm) to favour holes. |
| Overlap integral | Intensity-weighted average of a quantity over the mode. |
| Permittivity ($\epsilon_0\epsilon_s$) | How strongly a material stores electric field; silicon $\epsilon_s \approx 11.7$. |
| Phase ($\phi$) | Where the wave is in its cycle; $\pi$ = half a cycle. |
| Phenomenological | Fitted to measurements rather than derived from theory. |
| Plasma dispersion effect | Change of silicon's index and absorption caused by free carriers. |
| pn-junction | Boundary between p-type and n-type silicon. |
| Process simulation | Simulation of fabrication steps to predict doping profiles. |
| RC time constant | Resistance × capacitance; sets how fast a circuit can charge. |
| Refractive index ($n$) | How much slower light travels in a material than in vacuum. |
| Reverse / forward bias | Voltage that widens / narrows the depletion region. |
| Rib waveguide / slab | Silicon ridge (rib) standing on a thinner silicon layer (slab). |
| Ring modulator | Loop resonator whose resonance shifts with phase changes. |
| Sheet resistance | Resistance of a square of a thin layer (ohms per square). |
| Small-signal | Small voltage wiggles around a fixed bias, so the circuit acts linear. |
| Source impedance | Built-in resistance of the driving electronics, typically 50 Ω. |
| TCAD | Software that numerically simulates semiconductor devices. |
| Travelling-wave electrode | Metal transmission line that carries the signal alongside the light, avoiding RC limits. |
| $V_\pi$, $V_\pi L$ | Voltage for a $\pi$ phase shift; times length, a figure of merit (lower is better). |
| Wavelength ($\lambda$) | Distance between wave crests; 1550 nm or 1310 nm here. |

## Check yourself

**1. If you remove free holes from a region of silicon, does its refractive index go up or down? And its absorption?**

*Answer:* The index goes up (the $\Delta n$ formulas have minus signs, so removing carriers gives a positive change) and the absorption goes down.

**2. Why do silicon depletion modulators favour holes, and how is that put into practice?**

*Answer:* Holes give a larger index change and less absorption than electrons (e.g. at $10^{18}$ cm$^{-3}$, 1550 nm: $\Delta n \approx -2.1\times10^{-3}$ for holes vs $-8.8\times10^{-4}$ for electrons). Designers offset the junction from the waveguide centre (50 nm in the example) so more hole depletion overlaps the light.

**3. Using equation 6.5, by roughly what factor is the plasma dispersion effect stronger at 1550 nm than at 1310 nm?**

*Answer:* $(1550/1310)^2 \approx 1.4$.

**4. What happens to the depletion width if you go from 1 V to 4 V of extra reverse bias (ignoring $V_{bi}$)? Why?**

*Answer:* It roughly doubles, since $W_d \propto \sqrt{V_{bi}-V}$ and $\sqrt{4} = 2$. The square root is why the curves in Figures 6.5–6.7 flatten at high voltage.

**5. Why are minority carriers ignored when computing the optical effect?**

*Answer:* Their density is $n_i^2/N \approx 10^{20}/10^{18} = 100$ cm$^{-3}$, vastly smaller than the $10^{17}$–$10^{18}$ cm$^{-3}$ majority carriers whose removal causes the effect.

**6. What $\Delta n_{eff}$ is needed for a $\pi$ phase shift over 1 mm at 1550 nm?**

*Answer:* $\Delta\phi = 2\pi\,\Delta n\,L/\lambda = \pi$ gives $\Delta n = \lambda/(2L) = 1.55\times10^{-6}/(2\times10^{-3}) \approx 7.8\times10^{-4}$.

**7. The example has $V_\pi L = 1.6$ V·cm. What does that mean in practice?**

*Answer:* A 1 cm device needs 1.6 V of reverse bias for a $\pi$ phase shift; a shorter device needs proportionally more voltage (roughly, since the response is not perfectly linear).

**8. Why does the cutoff frequency rise with reverse bias?**

*Answer:* The wider depletion region lowers the capacitance ($C_j = \epsilon_0\epsilon_s t_{rib}/W_d$) and shortens the resistive path, lowering $R_j$; $f_c = 1/(2\pi R_jC_j)$ goes up (35 GHz at 0 V, 51 GHz at 1 V).

**9. If the junction itself can reach tens of GHz, why do long Mach-Zehnder modulators need travelling-wave electrodes?**

*Answer:* A long device has a large total capacitance, and with a 50 Ω driver the RC time becomes long; travelling-wave electrodes let the signal propagate with the light instead of charging one big lumped capacitor.

**10. In the TCAD workflow, how is capacitance found, and what checks the simulation is trustworthy?**

*Answer:* From $C = \Delta Q/\Delta V$ using total charge at two nearby voltages. The electron-based and hole-based values should be equal (convergence check), a fine mesh is used at the junction, and the simulated C–V curve is fitted to measured data (Figure 6.8).
