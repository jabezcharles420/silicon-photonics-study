# Week 5 · Day 1 — Monday 19 Oct 2026

*Simple-English study version of Chrostowski & Hochberg §4.4 (Ring resonators) and §6.3 (Micro-ring modulators).*

[:material-file-pdf-box: Download this day as PDF](day-01-mon-19-oct-2026.pdf){ .md-button }

## Before you start: the big picture

A photonic chip moves information with light instead of electricity. Light travels along tiny "wires" made of silicon, called waveguides. To be useful, a chip must do two things with this light. It must **pick out** one colour (wavelength) from many, like a radio tuning to one station. And it must **switch** the light on and off very fast, to write ones and zeros onto it.

A **ring resonator** does both jobs with one simple shape: a small loop of waveguide sitting next to a straight waveguide. Some light leaks from the straight waveguide into the loop, goes round and round, and leaks back out. For most colours, nothing special happens. But for a few special colours, the light that went round the loop arrives back exactly "in step" with itself. Then the loop traps that colour, and it disappears from the straight waveguide. Think of pushing a child on a swing: if you push at exactly the swing's natural rhythm, energy builds up; if you push at a random rhythm, nothing much happens.

Section 4.4 explains how a ring works as a colour filter, and how we measure one. Section 6.3 adds electricity: if we can slightly change how fast light travels in the ring, we slide the special colour left and right. A laser sitting at a fixed colour then sees the ring's "trap" move onto it and off it. That switches the light on and off: a **ring modulator**. The section also explains the main trade-off: a sharper ring switches with less voltage, but it is slower.

## Background you need

### Light is a wave

Light is a wave of electric and magnetic fields. Like a water wave, it has crests and troughs. The distance between two crests is the **wavelength**, written $\lambda$ ("lambda"). Chips for telecom use infrared light with $\lambda \approx 1.55\ \mu\text{m}$ (1550 nm). We cannot see it. Changing the wavelength a little (say 1540 nm vs 1541 nm) is like changing the colour a little.

The number of crests passing a point per second is the **frequency** $f$. Often we use the **angular frequency** $\omega = 2\pi f$. In vacuum, $f = c/\lambda$, where $c = 3\times 10^{8}$ m/s is the speed of light. For 1550 nm, $f \approx 1.9\times 10^{14}$ Hz (about 194 THz). This is the *optical* frequency. Don't confuse it with the *modulation* frequency (a few GHz), which is how fast we switch the light on and off.

### Refractive index, effective index, group index

Light slows down inside materials. The **refractive index** $n$ says by how much: light moves at $c/n$. Silicon has $n \approx 3.5$; glass (silica) has $n \approx 1.45$.

In a **waveguide**, light is trapped in a silicon strip surrounded by glass. Part of the light sits in the silicon and part spills into the glass. So it "feels" an average index, called the **effective index** $n_{\text{eff}}$ (somewhere between 1.45 and 3.5).

There is a second index. A real light signal is a bundle of nearby wavelengths. The bundle as a whole (the "envelope", which carries the information) moves at speed $c/n_g$, where $n_g$ is the **group index**. In silicon waveguides $n_g$ is often around 4, larger than $n_{\text{eff}}$, because $n_{\text{eff}}$ itself changes with wavelength (this is called **dispersion**). For rings, $n_g$ controls the spacing between resonances, and $n_{\text{eff}}$ controls exactly where they sit.

### Phase and the propagation constant

The **phase** tells you where you are in the wave cycle (crest, trough, in between). It is an angle: one full cycle is $2\pi$ radians. As light travels a distance $L$ in a waveguide, its phase grows by

$$\phi = \beta L, \qquad \beta = \frac{2\pi n_{\text{eff}}}{\lambda}.$$

$\beta$ ("beta") is the **propagation constant**: phase gained per metre. Light with a shorter wavelength, or a higher index, gains phase faster.

### Interference

When two waves meet, they add. If crest meets crest (phases differ by $0, 2\pi, 4\pi, \dots$), they make a bigger wave: **constructive interference**. If crest meets trough (phases differ by $\pi$), they cancel: **destructive interference**. Every resonator and every interferometer works by this rule.

### Complex numbers as "arrows"

Engineers describe a wave's size and phase together with one complex number, $E = |E|\,e^{i\phi}$. Picture an arrow: its length $|E|$ is the wave's strength, and its angle $\phi$ is the phase. Adding two waves = adding two arrows tip-to-tail. Multiplying by $e^{i\phi}$ just rotates the arrow by angle $\phi$. The **complex conjugate**, written with a star ($t^{*}$), flips the angle's sign: if $t = |t|e^{i\theta}$, then $t^{*} = |t|e^{-i\theta}$. If $t$ is a plain real number, $t^{*} = t$.

### Field versus power

$E$ is the electric **field** (the wave's height). What a detector measures is **power** (or intensity), which goes as $|E|^{2}$. So if the field shrinks by a factor 0.9, the power shrinks by $0.9^{2} = 0.81$. Keep this in mind: in the ring equations, $A$ is a *power* factor, and $\sqrt{A}$ is the matching *field* factor.

### Loss and the attenuation coefficient

Waveguides are not perfect. Light is scattered by rough sidewalls, absorbed by dopants and metals, and leaks out of tight bends. Power falls off exponentially with distance: $P(L) = P(0)\,e^{-\alpha L}$. The number $\alpha$ ("alpha") is the **power attenuation coefficient**, in units of 1/length.

### Decibels (dB)

Optics people measure power ratios in **decibels**: $\text{dB} = 10\log_{10}(P_{\text{out}}/P_{\text{in}})$. Useful anchors:

| Ratio of powers | In dB |
|---|---|
| 1 (nothing lost) | 0 dB |
| 1/2 | −3 dB |
| 1/10 | −10 dB |
| 1/100 | −20 dB |
| 1/1000 | −30 dB |

Read it like this: every −10 dB is another factor of 10 less power. Losses add in dB. A waveguide loss of "3 dB/cm" means half the power is gone after 1 cm. To convert: $\alpha\ [1/\text{cm}] \approx \text{loss}[\text{dB/cm}]/4.34$.

### Directional coupler: $t$ and $\kappa$

Put two waveguides very close together (a gap of a few hundred nm). The light's edge in one guide overlaps the other guide, so some light hops across. This is a **directional coupler**. We describe it with two field numbers:

- $t$ = **straight-through coefficient**: the fraction of field that stays in its own guide.
- $\kappa$ ("kappa") = **cross-over coefficient**: the fraction of field that hops to the other guide.

If the coupler loses no light, the power must all go somewhere, so $|t|^{2} + |\kappa|^{2} = 1$. For example $t = 0.98$ gives $|\kappa|^{2} = 1 - 0.96 = 0.04$: 4% of the power crosses over each pass. A smaller gap or longer coupler gives a larger $\kappa$.

### Resonators and the quality factor Q

A **resonator** (or **cavity**) is any structure where a wave goes round and round and interferes with itself. Only certain wavelengths "fit": those for which one round trip adds a whole number of cycles. These are the **resonances**.

The **quality factor** $Q$ measures how sharp a resonance is and how long light stays trapped. Two equivalent pictures:

- Sharpness: $Q \approx \lambda/\Delta\lambda_{\text{FWHM}}$, where $\Delta\lambda_{\text{FWHM}}$ is the width of the resonance dip. $Q = 10\,000$ at 1550 nm means a dip about 0.155 nm wide.
- Storage: $Q$ is roughly how many optical cycles (times $2\pi$) the light survives in the cavity. High $Q$ = light lives long = sharp dip.

A bell with high $Q$ rings for a long time with a pure tone. A bell with low $Q$ goes "thud".

### Doped silicon, pn-junctions, and the plasma effect

Pure silicon has few free charges. **Doping** adds impurity atoms: **n-type** doping adds free electrons; **p-type** adds **holes** (missing electrons that act like positive charges). Where p-type meets n-type, we get a **pn-junction**. Near the junction, the electrons and holes cancel each other out, leaving a thin zone with no free carriers: the **depletion region**.

If we apply a voltage the "wrong" way (**reverse bias**), the depletion region gets wider. More carriers are swept out of the light's path.

Why does this matter for light? Free carriers change silicon's refractive index and absorb a little light. This is the **plasma dispersion effect** (the "plasma effect" of the previous book section). Fewer carriers means a slightly *higher* index and slightly *less* absorption. So a voltage changes $n_{\text{eff}}$ a tiny bit, and therefore changes the phase of light. That is a **phase shifter**.

### Capacitance and the RC limit

A reverse-biased pn-junction is like a tiny capacitor (two charge layers separated by the depletion zone). To change its voltage, current must flow through the silicon's resistance $R$ to charge the capacitance $C$. This takes time about $RC$. If you try to switch faster than this, the voltage can't follow. The resulting speed limit is the **RC cutoff frequency**, $f_{RC} = 1/(2\pi RC)$.

### Small-signal response and the 3 dB cutoff

To measure a modulator's speed, apply a small wiggle of voltage at frequency $f$ on top of a fixed DC bias, and see how strongly the light wiggles. At low $f$ the response is full. At high $f$ it fades. The frequency where the response power has dropped to half (−3 dB) is the **cutoff frequency** or **bandwidth**, $f_c$.

### Grating couplers and WDM

A **grating coupler** is a patch of tiny grooves on the chip that bends light up out of the chip into an optical fibre (or back down). It is how we get light on and off the chip for testing. It only works well over a range of wavelengths, which makes a broad hump in measured spectra.

**Wavelength-division multiplexing (WDM)** means sending many colours down one fibre, each carrying its own data. Rings are attractive for WDM because each ring only talks to its own colour.

## 4.4 Ring resonators

> **In one sentence:** A ring resonator is a closed loop of waveguide that is lightly coupled to one or two straight waveguides, so that it strongly reacts to a set of evenly spaced wavelengths and ignores all others.

A ring resonator is also called a **micro-ring resonator** or a **racetrack resonator**. It is a loop of optical waveguide plus some way for light to get in and out. The loop is usually a circle, or a **racetrack**: two half-circles (180° bends) joined by two short straight pieces. The straight pieces are there so that the ring runs parallel to the outside waveguide for a little while, which makes a directional coupler.

The outside straight waveguide is called the **bus waveguide**. There are two standard set-ups (the book's Figure 4.27; see also Figure 6.10 below):

- **All-pass** ring: one bus waveguide. Light enters at the "in" port and leaves at the "through" (thru) port. All light eventually passes; the ring only removes power at resonance through its own loss, and changes the phase.
- **Add-drop** ring: two bus waveguides, one on each side. Now there is also a **drop port**: at resonance, light can cross through the ring into the second waveguide and leave there. (An "add" port on the second waveguide lets you inject a colour, hence "add-drop".)

```
   All-pass                         Add-drop

   In ===========> Thru         Drop <========== (Add)
         .----.                         .----.
        (  ring )                      (  ring )
         '----'                         '----'
                                In ===========> Thru
```

A detailed review of rings is the paper by W. Bogaerts et al. (reference [10] in the book).

### 4.4.1 Optical transfer function

> **In one sentence:** These equations tell you, for any wavelength, how much light (and with what phase) comes out of the through and drop ports of a ring.

A **transfer function** is simply "output divided by input" as a function of wavelength. Let's build it up.

**Round-trip length.** One trip round a racetrack is

$$L_{rt} = 2\pi r + 2L_{c} \qquad (4.21)$$

- $r$ = bend radius of the half-circles.
- $L_{c}$ = length of each straight coupler section (there are two straight sections, hence $2L_c$).
- $2\pi r$ = the two half-circles together make one full circle.

If $L_c = 0$, the ring is a plain circle that touches the bus at a single point: it is **point coupled**.

*Example:* the ring measured in §4.4.2 has $r = 15\ \mu\text{m}$ and $L_c = 0.1\ \mu\text{m}$, so $L_{rt} = 2\pi(15) + 0.2 \approx 94.2 + 0.2 = 94.4\ \mu\text{m}$. That's less than a tenth of a millimetre.

**Round-trip phase and loss.** In one trip, the light gains phase and loses power:

$$\phi_{rt} = \beta L_{rt} \qquad (4.23\text{a})$$

$$A = e^{-\alpha L_{rt}} \qquad (4.23\text{b})$$

- $\phi_{rt}$ = phase gained in one round trip ($\beta$ = phase per metre, see Background).
- $A$ = fraction of *power* left after one round trip ($\alpha$ = power attenuation coefficient). $A = 1$ means no loss; $A = 0.9$ means 10% of the power is lost per trip.
- The field shrinks by $\sqrt{A}$ per trip (field = square root of power).

In this model, the phase gained while the light runs through the coupler region is counted inside $\phi_{rt}$. So the coupler itself is treated as a **point coupler**: an ideal "instant" splitter described only by $t$ and $\kappa$, with no extra phase on the straight-through path $t$ (this is the convention of the book's Equation (4.11a)).

**All-pass ring, through port.** The result is

$$\frac{E_{thru}}{E_{in}} = \frac{-\sqrt{A}+t\,e^{-i\phi_{rt}}}{-\sqrt{A}\,t^{*}+e^{-i\phi_{rt}}} \qquad (4.22)$$

What every symbol means:

- $E_{in}$, $E_{thru}$ = complex field at the input and the through port.
- $t$ = straight-through coefficient of the coupler; $t^{*}$ its complex conjugate.
- $\sqrt{A}$ = field survival per round trip.
- $e^{-i\phi_{rt}}$ = the "rotation" of the wave's phase arrow over one trip.

*Where does the shape come from?* The output is the sum of many waves. One part of the input never enters the ring; it goes straight past (weight $t$). Another part enters the ring, goes round once, and leaks out. Another goes round twice, and so on. Each extra lap multiplies by the same factor (loss $\sqrt{A}$, phase rotation, and coupling $t$). Adding up this endless chain is a **geometric series**, $1 + x + x^{2} + \dots = 1/(1-x)$. That's why the answer is a fraction with "1 minus something" hiding in the denominator.

*What does it say?* Look at **resonance**: the round-trip phase is a whole number of cycles, $\phi_{rt} = 2\pi m$, so $e^{-i\phi_{rt}} = 1$. If $t$ is real, the equation becomes

$$\frac{E_{thru}}{E_{in}} = \frac{t - \sqrt{A}}{1 - t\sqrt{A}}.$$

Now notice: if $t = \sqrt{A}$, the top is zero. **No light at all comes out.** The light that went straight past and the light leaking out of the ring are equal in size and opposite in phase, so they cancel perfectly. This special case is called **critical coupling** (it returns in §6.3.3). The coupler lets in exactly as much as the ring loses per trip.

Away from resonance, the ring's light comes back out of step, the cancellation fails, and almost all light passes ($|E_{thru}/E_{in}| \approx 1$). So the through-port spectrum is flat with sharp dips at each resonance.

*Small number example:* take $t = 0.98$ and $\sqrt{A} = 0.97$. At resonance: $(0.98 - 0.97)/(1 - 0.98\times0.97) = 0.01/0.0494 \approx 0.20$. The field is 0.20, so the power is $0.04$, or about −14 dB. A deep dip. Make $t = 0.97$ too, and the dip becomes infinitely deep (zero).

**Add-drop ring.** Now there are two couplers. The input coupler has $t_1, \kappa_1$; the drop coupler has $t_2, \kappa_2$. The two outputs are

$$\frac{E_{thru}}{E_{in}} = \frac{t_{1}-t_{2}^{*}\sqrt{A}\,e^{i\phi_{rt}}}{1-\sqrt{A}\,t_{1}^{*}t_{2}^{*}\,e^{i\phi_{rt}}} \qquad (4.24)$$

$$\frac{E_{drop}}{E_{in}} = \frac{-\kappa_{1}^{*}\kappa_{2}\,A^{1/4}\,e^{i\phi_{rt}/2}}{1-\sqrt{A}\,t_{1}^{*}t_{2}^{*}\,e^{i\phi_{rt}}} \qquad (4.25)$$

How to read them:

- The **denominator** is the same in both: $1 - \sqrt{A}\,t_1^{*}t_2^{*}e^{i\phi_{rt}}$. It is the "one lap" factor of the geometric series. In one lap the light loses $\sqrt{A}$ in field, passes *both* couplers on the straight-through path ($t_1$ and $t_2$), and rotates by $\phi_{rt}$. At resonance this denominator gets small, so the ring's response gets big. That's the resonance.
- **Through port (4.24):** same idea as the all-pass ring, but now the ring's loss includes leakage into the second waveguide (the $t_2$ factor).
- **Drop port (4.25):** to reach the drop port, light must cross *into* the ring ($\kappa_1$), travel *half* a lap to the other side, then cross *out* ($\kappa_2$). Half a lap gives half the phase, $e^{i\phi_{rt}/2}$, and half the field loss. Full-lap field loss is $\sqrt{A} = A^{1/2}$, so half a lap is $A^{1/4}$. That's why this odd-looking power appears.
- There is no "direct" path to the drop port, so it is dark off resonance and bright at resonance: the drop port shows **peaks** where the through port shows **dips**.

(Side note: Eq. 4.22 is written with $e^{-i\phi_{rt}}$ and Eqs. 4.24–4.25 with $e^{+i\phi_{rt}}$. This is just a sign convention for phase; the resulting power spectra are the same.)

Usually the design is **symmetric**: both couplers are identical, $t_1 = t_2 = t$ and $\kappa_1 = \kappa_2 = \kappa$. We also assume the couplers themselves lose no light (any real coupler loss is lumped into the ring's round-trip loss $A$). Then energy conservation gives

$$|\kappa|^{2} + |t|^{2} = 1 \qquad (4.26)$$

In words: the power that stays plus the power that crosses equals all the power.

The book implements these transfer functions in MATLAB code 6.4 (in the modulator chapter). In short, that code:

1. Takes the ring's design values ($r$, $L_c$, coupling $\kappa$, loss $\alpha$, the waveguide's index) and a list of wavelengths.
2. For each wavelength, computes $\beta$, then $\phi_{rt}$ and $A$ (Eqs. 4.21, 4.23).
3. Plugs these into Eqs. 4.22 or 4.24–4.25.
4. Outputs the through- and drop-port transmission (usually as power in dB) versus wavelength.

**Figure 4.28 — Measured spectrum and FSR of a ring modulator (fabricated via OpSIS-IME).** Two panels, both with wavelength from about 1.50 to 1.57 μm on the x-axis.

- *Panel (a), through-port spectrum (dB).* The blue line is measured transmission through the whole set-up (grating coupler in, ring, grating coupler out). It has a broad upside-down-bowl shape, peaking around −12 dB in the middle and falling to about −20 dB at the edges. That bowl is the grating couplers, which only work well near the centre wavelength; it is *not* the ring. On top of the bowl are about 28–30 sharp, evenly spaced downward spikes. These are the ring's resonances. Red circles mark the bottom of each dip found by software; dip depths range from about −22 dB to −38 dB (the deepest near 1.568 μm).
- *Panel (b), FSR (nm).* The spacing between neighbouring dips, plotted against wavelength. It grows smoothly from about 3.06 nm near 1.505 μm to about 3.36 nm near 1.57 μm.
- *Lesson:* A ring is a "comb" filter: dips repeat every few nm. The spacing is not perfectly constant; it grows with wavelength (partly because the FSR scales as $\lambda^2$, and partly because $n_g$ changes with wavelength). Varying dip depth shows the coupling and loss also change with wavelength, so the ring is closer to critical coupling at some wavelengths than others.

### 4.4.2 Ring resonator experimental results

> **In one sentence:** By measuring the spacing between a real ring's resonances, you can work out the group index of the waveguide it is made of.

The book measured a fabricated ring modulator (the one pictured in Figure 6.9). Its specs:

- Radius $r = 15\ \mu\text{m}$.
- **Rib waveguide**: a 500 nm wide ridge of silicon sitting on a thin 90 nm silicon "slab" (the slab is needed to make electrical contact to the doped regions).
- **Double-bus** (add-drop) design with straight bus waveguides. (Figure 6.9 shows a single-bus version.)
- A tiny racetrack straight section of $0.1\ \mu\text{m}$ for the directional couplers.

The through-port spectrum (Figure 4.28a) was measured using a pair of fibre grating couplers. A **peak-finding algorithm** (software that locates the bottom of each dip) found the resonance wavelengths.

**Free spectral range.** The **free spectral range** (FSR, written $\Delta\lambda$) is the wavelength gap between neighbouring resonances. It depends on wavelength in general (Figure 4.28b). The maths is the same as for the Mach-Zehnder interferometer (the book's Eq. 4.20), which gives $\Delta\lambda \approx \lambda^{2}/(n_g L)$. Rearranged:

$$n_{g} = \frac{\lambda^{2}}{L\,\Delta\lambda} \qquad (4.27)$$

- $\lambda$ = wavelength where you measure.
- $L$ = round-trip length of the ring.
- $\Delta\lambda$ = measured FSR at that wavelength.
- $n_g$ = group index of the waveguide.

*Why this shape?* Resonance needs $n_{\text{eff}} L/\lambda$ = a whole number $m$. Going to the next resonance means fitting one more (or one fewer) wave in the loop. A longer loop (bigger $L$) or "slower" light (bigger $n_g$) means a tiny change in wavelength already adds a whole extra wave, so the resonances crowd closer together. The $\lambda^2$ comes from the fact that the condition is about $1/\lambda$, and a change in $1/\lambda$ turns into a change in $\lambda$ via a factor $\lambda^2$. It is $n_g$, not $n_{\text{eff}}$, because $n_{\text{eff}}$ itself shifts as you change wavelength, and $n_g$ includes that effect.

*Worked example (generic numbers):* a ring with $L = 100\ \mu\text{m}$ and $n_g = 4$ at $\lambda = 1.55\ \mu\text{m}$ has FSR $= (1.55)^2/(4 \times 100)\ \mu\text{m} \approx 0.0060\ \mu\text{m} = 6.0$ nm. Smaller rings give larger FSR.

*Caution when using the book's numbers:* if you plug $\lambda = 1.55\ \mu\text{m}$, $\Delta\lambda \approx 3.2$ nm and $L \approx 94.4\ \mu\text{m}$ straight into Eq. 4.27, you get $n_g \approx 8$, about twice the typical value (~4) for silicon waveguides. The packet doesn't explain this; the physical length behind the measured FSR may differ from the simple $2\pi r$ estimate. The point to learn is the method: measure FSR, know $L$, get $n_g$.

The book compares the extracted $n_g$ with its waveguide model in Figure 3.21b (not in this packet). More on rings as modulators follows in §6.3.

> **Key takeaways:**
>
> - A ring is a loop of waveguide coupled to one (all-pass) or two (add-drop) bus waveguides; round-trip length is $L_{rt} = 2\pi r + 2L_c$.
> - Resonance happens when the round-trip phase is a whole number of cycles; the through port then shows a dip and the drop port a peak.
> - The transfer functions are geometric series over laps; the shared denominator gets small at resonance.
> - On resonance, an all-pass ring transmits zero when $t = \sqrt{A}$ (critical coupling).
> - The resonance spacing (FSR, ~3 nm for the measured ring) reveals the group index: $n_g = \lambda^2/(L\,\Delta\lambda)$.

## 6.3 Micro-ring modulators

> **In one sentence:** Put a pn-junction inside a high-Q ring; a voltage then nudges the ring's resonance sideways, and a laser parked on the steep edge of the dip gets switched between bright and dark.

A ring with a high $Q$ is a very narrow filter: it reacts strongly to one tiny band of wavelengths. Where that band sits is set by the round-trip phase $\phi_{rt}$. So if your laser sits just beside a resonance, a very small change in the ring's phase moves the dip onto or off the laser, and the transmitted power changes a lot.

That is the idea of the **micro-ring modulator**: build a pn-junction into the ring, and use the plasma effect (previous section of the book) to change the phase with a voltage. Because the resonance multiplies the effect of each lap, a ring needs far less phase change (and so less voltage or length) than a straight phase shifter. The book points to many papers on ring modulators and two review papers.

Both ring set-ups from §4.4 are used as modulators: all-pass and add-drop (Figure 6.10). The ring can again be a racetrack (two 180° bends plus two straight coupler sections).

**Why heaters?** A ring modulator only works in a narrow wavelength window near its resonance. But the resonance moves with temperature and with tiny fabrication errors. So real designs need **wavelength stabilisation**. In Figure 6.10a, one quarter of the ring (the part in the coupler region) holds a resistor **heater** instead of the pn-junction. Heating silicon raises its index, which lets you tune the ring onto the laser and hold it there. The price: only three quarters of the ring is modulated, so the **modulation efficiency** (resonance shift per volt) is lower than for a fully modulated ring.

The modulator's optical transfer function uses the same MATLAB code 6.4 as the plain ring.

**Figure 6.9 — Microscope image of a ring resonator modulator.** A top-down photo of a real chip.

- *Left:* three large gold metal pads in a column. They are arranged **ground-signal-ground (GSG)**: a standard layout so a high-speed microwave probe (three needle tips) can land on them and deliver the fast electrical signal.
- *Centre-left:* the ring. Thin metal lines run from the pads to it, and a line crosses it (an electrode or heater connection).
- *Beside the ring:* the straight bus waveguide.
- *Right:* two rows of grating couplers (tapered structures) for getting light from and to fibres, joined to the bus with curved waveguides. Extra pairs of grating couplers are test structures for checking the process.
- *Key number:* the grating couplers are 0.5 mm from the microwave probe pads, so the electrical probe and the optical fibres don't bump into each other during testing. No scale bar is drawn; the 0.5 mm is your size reference.
- *Lesson:* a real modulator is mostly "test infrastructure". The ring is tiny; pads and couplers take up most of the space, laid out so electrical and optical probing can happen at the same time.

**Figure 6.10 — Mask layouts of micro-ring modulators.** These are design drawings (the patterns sent to the factory), with different colours for different fabrication layers.

- *(a) All-pass, with a heater for wavelength tuning.* One straight red waveguide runs left ("In") to right ("Thru"). Below it is a circular ring. A hatched rectangle sits over the top arc of the ring, near the coupler: that's the heater. Green metal makes a large contact pad above, a round contact in the middle of the ring, and small vias (vertical connections) to the heater. An orange box outlines the device.
- *(b) Add-drop, fully modulated.* Two parallel straight waveguides: the bottom one "In" → "Thru", the top one carries light out to "Drop" (arrow pointing left). Between them is a racetrack-shaped ring. Hatched (doped / modulation) regions cover both straight sides of the racetrack. Green metal routes contacts to both sides, plus a small contact in the centre.
- *Lesson:* the two basic modulator designs. (a) trades some modulation efficiency for a heater to lock the wavelength; (b) puts modulation everywhere it can, and has a drop port.

### 6.3.1 Ring tuneability

> **In one sentence:** A simulation shows that reverse-biasing the junction shifts the resonance by 0.016 nm per volt, and because the dip is so sharp, that tiny shift changes transmission by about 8 dB.

Here the modulator uses a **reverse-biased pn-junction** (carrier depletion). The book joins two models:

1. A pn-junction model (MATLAB codes 6.2 and 6.1) that says how the carriers, and therefore $n_{\text{eff}}$ and loss, change with voltage.
2. The ring transfer functions (Eqs. 4.24 and 4.25).

Together (MATLAB codes 6.6 and 6.7), they give the ring's spectrum at each applied voltage.

**Figure 6.11 — Structure of the 1D analytic model for micro-ring modulators.** A tree of six boxes showing which program calls which. From top to bottom:

```
RingMod_spectrum_plot   voltage scan; small-signal bandwidth
        |
RingMod_spectrum        optical spectrum (transfer functions)
        |
RingMod                 design inputs -> transmission at 1 wavelength, 1 voltage
        |
neff_V                  mode overlap; depletion phase modulator
       /        \
pn_depletion     wg_TElike_1Dprofile_neff
(1D electrical:   (1D optical solver for TE-like mode;
 reverse-biased    uses wg_1D_mode_profile, wg_1D_analytic2)
 pn-junction)
```

How to read it, bottom up:

- `pn_depletion` solves the electrical problem: where the carriers are at a given voltage (in 1D, across the waveguide).
- `wg_TElike_1Dprofile_neff` solves the optical problem: the shape of the light in the waveguide (its **mode**) and its effective index. (The original figure text says "!D", a typo for "1D".)
- `neff_V` combines them by **mode overlap**: how much of the light actually sits where the carriers changed. This gives $n_{\text{eff}}$ (and loss) versus voltage.
- `RingMod` turns that into ring transmission at one wavelength and one voltage.
- `RingMod_spectrum` sweeps wavelength to get the full spectrum.
- `RingMod_spectrum_plot` sweeps voltage, plots the spectra, and also computes the small-signal bandwidth.
- *Lesson:* the simulation is modular. Physics at the bottom (carriers, light shape), device behaviour at the top (spectra, speed).

**The example design.** Fully modulated (no heater), add-drop, point-coupled ($L_c = 0$), radius $r = 10\ \mu\text{m}$, other values as defaults in MATLAB code 6.7. Results are in Figure 6.12.

**Figure 6.12 — Through-port (a) and drop-port (b) spectra at reverse bias 0, 1, 2, 3, 4 V.** Wavelength axis: 1540.7 to 1541 nm (a window only 0.3 nm wide).

- *(a) Through port.* Five dips, one per voltage. The 0 V dip is leftmost (minimum near 1540.80 nm, about −13.5 dB). Each extra volt moves it right: 1 V ≈ 1540.82 nm, 2 V ≈ 1540.84, 3 V ≈ 1540.86, 4 V ≈ 1540.88 nm (about −15 dB). Off resonance, transmission is near −0.5 dB. A grey dashed line through the minima is labelled **0.016 nm/V**. Dashed horizontal lines near −3, −4 and −11 dB and vertical arrows show how much the transmission at a fixed wavelength drops when the curve moves from 0 V (or 3 V) to 4 V.
- *(b) Drop port.* Five peaks, at the same wavelengths. Peak heights about −2.0 dB (0 V) to −1.6 dB (4 V). Off resonance, about −7 to −10 dB.
- *Lesson:* reverse bias moves the resonance to longer wavelength (a **red shift**), steadily, by 0.016 nm/V. Removing carriers raises the index, which raises the round-trip phase, so the resonance must move to a longer wavelength to fit a whole number of waves again. The dips also get slightly deeper with voltage (−13.5 to −15 dB), most likely because fewer carriers means less absorption, which changes the loss balance in the ring.

**What the numbers mean.**

- The **through port** is more sensitive to round-trip phase changes than the drop port: its dip has steeper sides and a bigger swing (about 13 dB from off-resonance to the bottom, vs about 5–8 dB for the drop peak). So the through port is used as the modulator output.
- The shift is small: 0.016 nm/V, so 0.064 nm for 4 V. But the ring has a **quality factor of about 10 000**, so its dip is only about $1540.9/10\,000 \approx 0.15$ nm wide. A 0.064 nm shift is almost half the dip width: a big deal.
- *Concrete example:* pick the wavelength where the 0 V curve is at −3 dB (the **3 dB insertion loss** point, ~1540.9 nm, on the right-hand side of the 0 V dip). Raise the reverse bias from 0 to 4 V. The dip slides right onto this wavelength, and transmission falls by about **8 dB** (from about −3 dB to about −11 dB). That is the on/off contrast of the modulator.

**The core trade-off.** To get more effect per volt, make $Q$ higher, e.g. by **reducing the coupling** $\kappa$, so the dip gets narrower and the same shift makes a bigger change. But high $Q$ means light stays in the ring longer (a long **photon lifetime**), and the ring can't respond faster than the light can enter and leave. So higher $Q$ limits speed, as the next section shows.

> **Key takeaways:**
>
> - A ring modulator = ring + pn-junction; the voltage changes $n_{\text{eff}}$, which moves the resonance.
> - Simulated example ($r = 10\ \mu\text{m}$, add-drop, $Q \approx 10\,000$): resonance shifts 0.016 nm/V toward longer wavelengths under reverse bias.
> - A 0–4 V swing gives ~8 dB transmission change at the 3 dB point, because the dip (~0.15 nm wide) is narrow compared with the shift.
> - Use the through port as output: it is more sensitive.
> - Heaters lock the wavelength but reduce the modulated fraction of the ring; higher $Q$ boosts efficiency but costs speed.

### 6.3.2 Small-signal modulation response

> **In one sentence:** A ring modulator's speed is limited by two delays, the electrical RC charging time and the time light lives in the ring, and they combine like resistors in parallel do for conductance.

The 3 dB **cutoff frequency** $f_c$ of the ring modulator's small-signal response depends on two things:

1. the **RC time constant** of the reverse-biased pn-junction (how fast you can change the voltage), and
2. the **photon lifetime** $\tau_p$ of the cavity (how fast the light in the ring can change).

They combine as

$$\frac{1}{f_{c}^{2}} = \frac{1}{f_{\tau_{p}}^{2}} + \frac{1}{f_{RC}^{2}} \qquad (6.16)$$

- $f_{\tau_p}$ = speed limit from photon lifetime alone.
- $f_{RC}$ = speed limit from the RC charging alone.
- $f_c$ = the overall speed limit.

*What it says:* the result is always lower than either limit alone, and is dominated by the *smaller* (slower) one. Squares appear because each effect acts like a simple first-order filter, and for such filters the delays add up "in quadrature" (like the sides of a right triangle). Example: $f_{\tau_p} = 20$ GHz and $f_{RC} = 40$ GHz give $1/f_c^2 = 1/400 + 1/1600 = 0.003125$, so $f_c \approx 17.9$ GHz. If one limit is much larger, the other one wins almost completely.

**Photon-lifetime limit.**

$$f_{\tau_p} = \frac{1}{2\pi\tau_{p}} \qquad (6.17)$$

A shorter lifetime gives a higher speed limit. (Same shape as $f_{RC} = 1/(2\pi RC)$: both are "one over $2\pi$ times a time".)

$$\tau_{p} = \frac{Q_{t}}{\omega_{o}} \qquad (6.18)$$

- $\tau_p$ = photon lifetime: roughly how long light stays in the ring (time for the stored energy to fall to $1/e$, about 37%).
- $Q_t$ = **total (loaded) quality factor** of the ring.
- $\omega_o = 2\pi c/\lambda$ = the *optical* angular frequency (about $1.22\times10^{15}$ rad/s at 1550 nm).

*Example:* $Q_t = 10\,000$ gives $\tau_p = 10\,000/1.22\times10^{15} \approx 8.2$ ps, so $f_{\tau_p} = 1/(2\pi \times 8.2\ \text{ps}) \approx 19$ GHz. This matches the book's "about 20 GHz".

**Where Q comes from.** Light leaves the ring in two ways: it is lost inside (absorbed/scattered), or it couples out to the bus waveguide(s). Each has its own $Q$, and the rates add:

$$\frac{1}{Q_{t}} = \frac{1}{Q_{c}} + \frac{1}{Q_{i}} \qquad (6.19)$$

- $Q_i$ = **intrinsic Q**: limited by loss inside the ring only.
- $Q_c$ = **coupling Q**: limited by leakage out through the coupler(s) only.
- Like two holes in a bucket: the water drains at the sum of both rates, so $1/Q$'s add. The total is always below the smaller one.

$$Q_{i} = \frac{2\pi n_{g}}{\lambda\alpha} \qquad (6.20)$$

- Less loss (smaller $\alpha$) gives higher $Q_i$. Higher $n_g$ (slower light, which spends more time per length) also raises it.
- *Example:* a doped waveguide with 20 dB/cm loss has $\alpha \approx 20/4.34 \approx 4.6\ \text{cm}^{-1} = 460\ \text{m}^{-1}$. With $n_g = 4$ and $\lambda = 1.55\ \mu\text{m}$: $Q_i = 2\pi(4)/(1.55\times10^{-6} \times 460) \approx 35\,000$.

For the **all-pass** ring:

$$Q_{c} = -\frac{\pi L_{rt}n_{g}}{\lambda\log_{e}|t|} \qquad (6.21)$$

- $\log_e|t|$ is the natural log of the through coefficient. Since $|t| < 1$, the log is negative, and the minus sign makes $Q_c$ positive.
- Weaker coupling ($|t|$ closer to 1, $\kappa$ smaller) makes $\log_e|t|$ closer to zero, so $Q_c$ grows. Less leakage = longer storage.
- A longer ring ($L_{rt}$) also raises $Q_c$: light spends more time between "chances" to leak out.
- *Example:* $r = 10\ \mu\text{m}$ ($L_{rt} \approx 62.8\ \mu\text{m}$), $n_g = 4$, $t = 0.98$ ($\log_e 0.98 \approx -0.0202$): $Q_c = \pi (62.8\times10^{-6})(4)/(1.55\times10^{-6}\times0.0202) \approx 25\,000$.

For the **add-drop** ring, divide $Q_c$ by 2, because there are two couplers to leak through. Continuing the example: $Q_c \approx 12\,600$; with $Q_i \approx 35\,000$, Eq. 6.19 gives $Q_t \approx 9\,300$, close to the book's ~10 000. (These example inputs are illustrative, not the book's exact defaults.)

**The book's result.** For the same design as §6.3.1, the pn-junction's RC limit $f_{RC}$ is over 40 GHz, and the photon-lifetime limit $f_{\tau_p}$ is about 20 GHz. So the total cutoff frequency at 1 V bias is $f_c \approx 15$ GHz, **mainly limited by the photon lifetime**.

**Figure 6.13 — Ring modulator small-signal bandwidth versus applied voltage.** X-axis: reverse bias 0 to 4 V. Y-axis: frequency (GHz, unlabelled), 10 to 100. Three curves:

| Curve | At 0 V | At 4 V | Trend |
|---|---|---|---|
| $\tau_p$ determined ($f_{\tau_p}$) | ~21 GHz | ~20 GHz | almost flat, tiny decrease |
| pn-junction determined ($f_{RC}$) | ~42 GHz | ~99 GHz | rises steadily |
| total $f_c$ | ~18–19 GHz | ~19–20 GHz | lowest curve, nearly flat |

Read the table like this: each row is one speed limit; the bottom row is the real one, and it hugs the top row.

- *Why does $f_{RC}$ rise with voltage?* More reverse bias widens the depletion region, which lowers the junction capacitance $C$, so $RC$ gets smaller and $f_{RC}$ gets bigger.
- *Why is $f_{\tau_p}$ almost flat?* $Q_t$ barely changes with voltage (the slight drop in carrier absorption changes $Q_i$ a little).
- *Lesson:* the photon lifetime is the bottleneck over the whole 0–4 V range. Improving the electrical side won't help much; to go faster, you must lower $Q$, which costs efficiency (§6.3.1).
- *Note:* the figure's $f_c$ reads about 19 GHz near 1 V, while the text quotes 15 GHz at 1 V. The packet doesn't reconcile these; the conclusion (lifetime-limited, roughly 15–20 GHz) is the same either way.

> **Key takeaways:**
>
> - Speed is set by two limits: electrical ($f_{RC}$) and optical ($f_{\tau_p}$), combined as $1/f_c^2 = 1/f_{\tau_p}^2 + 1/f_{RC}^2$.
> - $f_{\tau_p} = 1/(2\pi\tau_p)$ with $\tau_p = Q_t/\omega_o$: higher $Q$ means slower.
> - $1/Q_t = 1/Q_c + 1/Q_i$: loss inside and leakage out both shorten the photon lifetime.
> - Add-drop rings have half the $Q_c$ of the same all-pass ring (two couplers).
> - In the book's example, $Q \approx 10\,000$ gives $f_{\tau_p} \approx 20$ GHz, which dominates over $f_{RC} > 40$ GHz; total ~15 GHz.

### 6.3.3 Ring modulator design

> **In one sentence:** Designing a ring modulator is a recipe: decide what performance you need, learn what your factory can make, compute the Q and size, then simulate the coupler and draw the mask.

**Step 1 — Decide what you want.** List the target characteristics:

- **modulation bandwidth** (speed),
- **FSR** (resonance spacing; matters for WDM channel spacing),
- **extinction ratio** (how dark "off" is compared with "on"),
- **drive voltage**,
- **double-bus vs single-bus** architecture,
- whether to use the **drop port or through port** as output.

**Critical coupling.** A common target. As shown in §4.4.1, the through port goes to zero on resonance when the input coupling exactly matches all the ring's other losses (the internal loss, plus the output coupler's leakage if there is a second bus). Then all power is either absorbed in the ring or goes to the drop port. This is **complete destructive interference**, and gives the highest **extinction ratio**.

**Why a second bus waveguide?** In a double-bus ring, the second waveguide acts as a deliberate, controllable extra "loss" (it "loads" the ring). This helps you balance losses to hit critical coupling and a high extinction ratio. It is especially handy when you don't know the dopants' absorption loss in advance (*a priori*). It also lets you set $Q$, and therefore the bandwidth. The downside: it is sub-optimal. If you need lower $Q$ anyway, it is better to get it by adding more pn-junction loss (for example, more doping in the light's path). That also makes the junction more efficient (more resonance shift per volt, in pm/V), rather than "wasting" light into a drop port.

**Fill factor.** The **pn-junction phase-shifter fill factor** is the fraction of the ring's circumference that contains the pn-junction. Figure 6.10a shows a fill factor below 100%: a quarter of the ring is a heater instead. Fill factor is also limited by mask layout and manufacturing rules (e.g. the coupler region, contacts).

**Step 2 — Learn the fabrication process.** Find:

- **Waveguide propagation loss**, from scattering, doping absorption, metal absorption, and bend radiation and mode-mismatch losses. Bend losses get larger for small rings, which are exactly the ones with large FSR. So big FSR fights low loss.
- **Slab thickness** of the rib waveguide (e.g. 150, 90, or 50 nm).
- **pn-junction properties**, especially its RC time constant.
- **Process variations** and any needed **fabrication bias** (a deliberate offset in the drawn size to make up for what the factory systematically does, e.g. lines coming out narrower).
- The junction itself can be optimised: doping levels, **junction offset** (where the p/n boundary sits in the waveguide), etc.

**Step 3 — Compute the design.**

1. From the target bandwidth, compute the needed quality factor (via Eqs. 6.16–6.18).
2. From the needed $Q$ and FSR, compute the radius and coupling coefficients (Eqs. 4.27, 6.19–6.21).
3. Check and optimise the optical transfer function.
4. Build a **time-domain model** (book §9.5). It can predict **eye diagrams** (overlaid traces of the bit stream showing how cleanly ones and zeros are separated), extinction ratio, energy efficiency, and the effect of the DC bias point.

**Step 4 — Physical structure.** Find the actual directional-coupler **gap** that gives the needed coupling coefficient. This is typically done with **3D FDTD** (finite-difference time-domain: a full simulation of Maxwell's equations on a 3D grid). It is slow, so only the coupler by itself is simulated in 3D (book §§4.1.4 and 9.4.2). With all physical parameters known, the mask layout is drawn.

**Figure 6.14 — Cross-section of a PIN junction in a rib waveguide.** A slice through the waveguide, as if cut with a knife.

```
          |<- WG width ->|
 +-------+   +----------+   +-------+
 |  P++  |   |    i     |   |  N++  |
 |       |___|   (rib)  |___|       |
 |       |  i (slab)        |       |
 +-------+------------------+-------+
         |<->| clearance
```

- *Left (blue):* **P++**, heavily doped p-type silicon, where a metal contact connects.
- *Middle (orange):* **i**, intrinsic (undoped) silicon. It includes the thin slab and the raised **rib** in the centre, where the light travels.
- *Right (red):* **N++**, heavily doped n-type silicon with the other contact.
- *"Waveguide width":* the width of the raised rib.
- *"Clearance":* the distance from the edge of the heavily doped region to the rib.
- *Lesson:* heavy doping absorbs light, so it must be kept away from the rib (large clearance). But a far-away contact adds electrical resistance (slower RC). The clearance is a trade-off between optical loss and electrical speed. A PIN (p-intrinsic-n) junction is a variant of the pn-junction with an undoped zone in the middle.

> **Key takeaways:**
>
> - Start with specs: bandwidth, FSR, extinction ratio, voltage, single/double bus, through/drop output.
> - Critical coupling (input coupling = all other losses) gives zero on-resonance transmission and the best extinction ratio.
> - A second bus helps reach critical coupling when losses are unknown, but adding junction loss is a better way to lower $Q$.
> - Know the process: loss sources, slab thickness, junction RC, variations; then compute $Q$, radius, couplings; build a time-domain model.
> - Only the coupler needs slow 3D FDTD; then draw the mask.

## Glossary

| Term | Plain meaning |
|---|---|
| 3 dB cutoff frequency ($f_c$) | Modulation frequency where the response has fallen to half power. The device's "speed". |
| 3D FDTD | Full computer simulation of light on a 3D grid, step by step in time. Accurate but slow. |
| Add-drop ring | Ring with two bus waveguides; has through and drop output ports. |
| All-pass ring | Ring with one bus waveguide; only a through port. |
| Bus waveguide | Straight waveguide that passes next to the ring. |
| Complex conjugate ($^{*}$) | Same number with the sign of its phase angle flipped. |
| Critical coupling | Input coupling equals all other ring losses; on resonance the through port goes to zero. |
| Cross-over coefficient ($\kappa$) | Fraction of field that hops to the other waveguide in a coupler. |
| Decibel (dB) | Log scale for power ratios: $10\log_{10}(P_2/P_1)$; −3 dB = half, −10 dB = one tenth. |
| Depletion region | Zone near a pn-junction emptied of free carriers; widens with reverse bias. |
| Directional coupler | Two waveguides close together so light leaks between them. |
| Dispersion | The index (and so speed) depends on wavelength. |
| Doping | Adding impurity atoms to silicon to provide free electrons (n) or holes (p). |
| Drop port | Output of the second bus in an add-drop ring; bright only at resonance. |
| Effective index ($n_{\text{eff}}$) | The average index the guided light feels; sets the phase per length. |
| Extinction ratio | Ratio of "on" to "off" power of a modulator. |
| Eye diagram | Overlay of many bit periods of a signal; an open "eye" means clean ones and zeros. |
| Fabrication bias | Deliberate size offset in the drawing to compensate for systematic factory errors. |
| Field ($E$) | The wave's amplitude; power goes as $|E|^2$. |
| Fill factor | Fraction of the ring's length covered by the pn-junction. |
| Free spectral range (FSR, $\Delta\lambda$) | Wavelength spacing between neighbouring resonances. |
| Grating coupler | Grooved patch that couples light between the chip and a fibre. |
| Group index ($n_g$) | Index that sets the speed of a light pulse/envelope; controls FSR and $Q$. |
| GSG pads | Ground-signal-ground metal pads for a high-speed probe. |
| Heater | Resistor near the ring; heating shifts the resonance for tuning. |
| Hole | Missing electron in a crystal; acts as a positive free charge. |
| Insertion loss | Power lost when the light passes through the device. |
| Interference | Waves adding: in step = bigger (constructive), out of step = cancel (destructive). |
| Intrinsic (i) | Undoped silicon. |
| Mask layout | The drawing of all layers sent to the chip factory. |
| Mode | A stable light pattern that travels along a waveguide without changing shape. |
| Modulation efficiency | How much resonance shift (or phase change) you get per volt. |
| Modulator | Device that switches/encodes data onto light. |
| Peak-finding algorithm | Software that locates the resonance dips in a measured spectrum. |
| Phase ($\phi$) | Position in the wave's cycle, measured as an angle (full cycle = $2\pi$). |
| Photon lifetime ($\tau_p$) | How long light stays stored in the ring. |
| Plasma dispersion effect | Free carriers change silicon's index and absorption. |
| pn-junction / PIN junction | Boundary between p- and n-doped silicon (PIN: with an undoped zone between). |
| Point coupler | Ideal coupler of zero length, described only by $t$ and $\kappa$. |
| Propagation constant ($\beta$) | Phase gained per unit length, $2\pi n_{\text{eff}}/\lambda$. |
| Quality factor ($Q$, $Q_t$, $Q_i$, $Q_c$) | Sharpness/storage time of a resonance; total, intrinsic (loss), coupling (leakage). |
| Racetrack resonator | Ring made of two half-circles joined by straight sections. |
| RC time constant | Time to charge a capacitance through a resistance; limits electrical speed. |
| Red shift | Move toward longer wavelength. |
| Resonance | Wavelength at which one round trip adds a whole number of cycles. |
| Reverse bias | Voltage applied to widen a pn-junction's depletion region. |
| Rib waveguide | Silicon ridge on top of a thin silicon slab. |
| Ring resonator | Closed waveguide loop coupled to bus waveguide(s). |
| Round-trip attenuation ($A$) | Fraction of power surviving one lap. |
| Round-trip phase ($\phi_{rt}$) | Phase gained in one lap, $\beta L_{rt}$. |
| Slab | Thin silicon layer beside a rib, used for electrical contact. |
| Small-signal response | Output wiggle for a small input wiggle, versus frequency. |
| Straight-through coefficient ($t$) | Fraction of field that stays in its own waveguide at a coupler. |
| Through port | Output end of the input bus waveguide. |
| Transfer function | Output divided by input, as a function of wavelength (or frequency). |
| Wavelength ($\lambda$) | Distance between wave crests; "colour" of light. |
| WDM | Sending many wavelengths, each with its own data, in one fibre. |

## Check yourself

1. What is the round-trip length of a racetrack ring with $r = 10\ \mu\text{m}$ and $L_c = 5\ \mu\text{m}$?

   *Answer:* $L_{rt} = 2\pi(10) + 2(5) \approx 62.8 + 10 = 72.8\ \mu\text{m}$.

2. Why does the through port of a ring show dips, while the drop port shows peaks?

   *Answer:* At resonance, light builds up in the ring. At the through port it cancels the directly transmitted light (destructive interference), making a dip. The drop port has no direct path, so it only gets light when the ring is full, i.e. at resonance: a peak.

3. For an all-pass ring with real $t$, what condition gives zero transmission on resonance, and what is it called?

   *Answer:* $t = \sqrt{A}$: the coupler's straight-through field equals the ring's field survival per lap. This is critical coupling.

4. In Eq. 4.25, why does $A^{1/4}$ appear instead of $\sqrt{A}$?

   *Answer:* To reach the drop port, light travels only half a lap. Full-lap field loss is $A^{1/2}$, so half a lap is $A^{1/4}$.

5. A ring has $L = 50\ \mu\text{m}$ and you measure FSR = 12 nm at 1.55 μm. What is $n_g$?

   *Answer:* $n_g = \lambda^2/(L\Delta\lambda) = (1.55)^2/(50 \times 0.012) = 2.40/0.60 \approx 4.0$.

6. The resonance shifts only 0.016 nm/V, yet 4 V gives ~8 dB change. Why?

   *Answer:* With $Q \approx 10\,000$ the dip is only ~0.15 nm wide, so a 0.064 nm shift moves a steep edge of the dip across the laser wavelength.

7. If $f_{\tau_p} = 20$ GHz and $f_{RC} = 100$ GHz, what is $f_c$ roughly, and what limits it?

   *Answer:* $1/f_c^2 = 1/400 + 1/10\,000 = 0.0026$, so $f_c \approx 19.6$ GHz. It is limited by the photon lifetime.

8. Why does increasing $Q$ improve modulation efficiency but reduce speed?

   *Answer:* Higher $Q$ means a narrower dip, so a small shift gives a big power change. But $\tau_p = Q_t/\omega_o$ grows, so the light takes longer to respond and $f_{\tau_p}$ falls.

9. Why is $Q_c$ halved for an add-drop ring?

   *Answer:* Light can leak out through two couplers instead of one, so the coupling leak rate doubles.

10. In Figure 6.14, what is the trade-off set by the "clearance"?

    *Answer:* Larger clearance keeps the light-absorbing P++/N++ regions away from the light (lower loss) but adds series resistance (higher RC, slower).
