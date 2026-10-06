# Week 7 · Day 1 — Monday 2 Nov 2026

*Simple-English study version of Chrostowski & Hochberg §5.2.2 (Grating couplers: theory)*

[:material-file-pdf-box: Download this day as PDF](day-01-mon-2-nov-2026.pdf){ .md-button }

## Before you start: the big picture

A silicon photonic chip carries light in tiny "wires" of glass-like material called waveguides. These are only about half a micrometre wide. An optical fibre, which brings light to the chip, has a core about 20 times wider. So a basic problem is: how do you get light from the fibre into the chip, and back out again?

One popular answer is the **grating coupler**. It is a row of small ridges ("teeth") etched into the top of the waveguide. Light moving along the waveguide hits each tooth, and each tooth scatters a little light upward. If the spacing of the teeth is chosen well, all those little scattered waves add up in one direction, making a beam that leaves the chip at a chosen angle. A fibre held above the chip at that angle catches it. The same works in reverse: light from the fibre goes down into the waveguide.

An everyday picture: think of a marching band walking past a row of evenly spaced drummers. Each drummer hits the drum when the band passes. Because the drummers are evenly spaced and the band moves at a fixed speed, the sounds reach a listener in step only from one particular direction. This section works out *which direction*. The answer is one simple rule, the **Bragg condition**, that links the tooth spacing, the colour (wavelength) of light, and the exit angle.

## Background you need

**Light is a wave.** Light is a wiggle in electric and magnetic fields that travels through space. Like a water wave, it has crests and troughs.

**Wavelength ($\lambda$).** The distance from one crest to the next. Telecom light used in silicon photonics usually has a wavelength near 1550 nm (1.55 micrometres) in vacuum. We write the vacuum wavelength as $\lambda_0$. (The source sometimes writes just $\lambda$ for the same thing.)

**Refractive index ($n$).** Light travels slower in materials than in vacuum. The refractive index says how much slower: speed $= c/n$. Air has $n \approx 1$. Silicon dioxide (glass, "oxide") has $n \approx 1.44$. Silicon has $n \approx 3.5$. Because the light's frequency does not change, a slower wave has crests packed closer together: the wavelength inside a material is $\lambda_0 / n$.

**Phase.** Where in its up-and-down cycle a wave is at a given place and time. One full cycle is $2\pi$ radians of phase.

**Wavenumber ($k$).** How much phase a wave gains per unit length travelled: $k = 2\pi/\lambda$. In vacuum (or air), $k_0 = 2\pi/\lambda_0$. In a material with index $n$, $k = n k_0 = 2\pi n/\lambda_0$. A bigger $k$ means more crests per metre.

**Wave vector.** A wave also has a direction. The **wave vector** is an arrow pointing the way the wave travels, with length $k$. Like any arrow, it can be split into parts along the $x$ and $z$ axes. If the wave travels at angle $\theta$ from the vertical $z$ axis, its horizontal part is $k_x = k \sin\theta$.

**Waveguide and effective index ($n_{eff}$).** A **waveguide** traps light inside a high-index strip (silicon) surrounded by lower-index material (oxide or air), by total internal reflection: light hitting the boundary at a shallow angle bounces back in. The trapped light pattern is called a **mode**. Part of the mode sits in the silicon and part leaks a little into the surroundings, so the light "feels" an average index somewhere between the two. This average is the **effective index** $n_{eff}$. For a silicon waveguide it is typically between about 1.5 and 3.

**Propagation constant ($\beta$).** The wavenumber of the guided mode along the waveguide: $\beta = n_{eff} k_0$. It is just "$k$" for the guided wave.

**Interference.** When two waves meet, they add. If crest meets crest, they make a bigger wave (**constructive interference**). If crest meets trough, they cancel (**destructive interference**).

**Huygens–Fresnel principle.** Every point that a wave reaches can be treated as a tiny new source sending out little circular waves (**wavelets**). The wave you see further on is the sum of all these wavelets.

**Diffraction and diffraction orders.** When a wave hits a regular pattern (like grating teeth), the wavelets from each repeat add up strongly only in certain directions. Each such direction is called a **diffraction order**, labelled by a whole number $m = 1, 2, \dots$.

**Momentum view of light.** A wave vector behaves like momentum (physicists literally treat $\hbar k$ as momentum). When a wave scatters off a periodic structure, the structure can "give" or "take" a fixed amount of horizontal momentum. This is the simplest way to understand gratings, and the figures below use it.

**Snell's law.** When light crosses a flat boundary between two materials, the horizontal part of its wave vector stays the same. That gives $n_1 \sin\theta_1 = n_2 \sin\theta_2$.

**Fabry–Pérot cavity.** Two partial mirrors facing each other. Light bounces back and forth between them. The output then goes up and down strongly with wavelength (ripples). On a chip, two reflecting couplers (input and output) can accidentally form one.

> **Key takeaways:**
>
> - Wavenumber $k = 2\pi n/\lambda_0$ counts phase per length; it grows with refractive index.
> - A guided wave has its own wavenumber $\beta = n_{eff} k_0$.
> - Horizontal wave-vector parts are what must "match" at a surface or grating.
> - A grating adds or removes fixed chunks of horizontal wave vector.

## 5.2.2 Theory

> **In one sentence:** A grating coupler sends light out of the chip at the angle where the guided wave's horizontal wavenumber, minus a whole number of "grating wavenumbers", equals the horizontal wavenumber of a free wave in the cladding.

### Why the teeth make a beam (Figure 5.2)

The book explains the grating with the Huygens–Fresnel principle. Each tooth of the grating scatters (diffracts) some of the guided light, so each tooth acts like a small source of new wavelets. These wavelets interfere. In most directions they cancel (destructive). In a few directions they add up (constructive). Those directions are the beams that leave the grating.

**Figure 5.2 — How a grating coupler works (two cases).** (No text rendering of this figure is in the source; this describes what the text says about it.)

- **Case (a): the wavelength inside the grating equals the grating period.** The light's crests inside the grating are spaced exactly one tooth apart. So every tooth scatters in step with every other tooth. The **first-order** beam (drawn in green) goes straight up, perpendicular to the chip. But there is a problem: the **second-order** diffraction (drawn in red) goes straight *back* into the waveguide. That is a reflection.
- **Case (b): the wavelength inside the grating is shorter than the period.** Now the teeth are slightly farther apart than the crests. The first-order beam leaves *tilted* at an angle (green), and there is no second-order reflection back into the waveguide.

```
 (a) Lambda = wavelength in grating   (b) Lambda > wavelength in grating
          ^ out (vertical)                     ^  / out (tilted)
          |                                    | /
  ===|_|_|_|_|_|===>                   ===|__|__|__|__|===>
      <--- back-reflection (2nd order)       (no back-reflection)
```

Why is the back-reflection bad? Light is usually sent in through one grating coupler and out through another. If both reflect a little, the light bounces between them. This forms a Fabry–Pérot cavity, and the measured power wiggles up and down with wavelength ("Fabry–Pérot oscillation"). That spoils measurements.

The fix used in practice: **detune** the grating, meaning choose the period a bit different from the in-grating wavelength, as in case (b). Then the output beam tilts a few degrees from vertical, and the fibre is held at that small angle from the **normal** (the line perpendicular to the chip surface).

### The grating as a 1D structure (Figure 5.3)

The gratings in this section are **one-dimensional periodic structures**: they repeat in one direction only (along the waveguide, called $x$). Such structures are well described by the **Bragg law** (the Bragg condition). Even the **focusing grating couplers** of Section 5.2.3 can be treated as one-dimensional, just with a built-in lens-like curve added.

The setup: the light arriving at the grating is a guided wave in a **slab waveguide** (a flat layer that confines light only up-down; see Section 3.2.2). It travels in the same plane as the grating and hits the teeth head-on (perpendicular to the teeth lines).

**Figure 5.3 — The two "arrows" of a grating coupler.** The picture shows an $x$ axis (along the chip) and a $z$ axis (up, out of the chip). Three arrows lie on the $x$ axis:

- A thick black arrow pointing right (+$x$): the guided wave's wavenumber $\beta = n_{eff}k_0 = 2\pi n_{eff}/\lambda_0$, labelled "waveguide propagation constant".
- A blue arrow pointing left (−$x$), labelled "Grating, m=1": the **grating vector** $K = 2\pi/\Lambda$.
- A longer blue arrow pointing left, labelled "Grating, m=2": twice that, $2K = 2 \cdot 2\pi/\Lambda$.

**Lesson:** think of the guided light as carrying a fixed amount of rightward "momentum" $\beta$. The grating can take away a fixed chunk $K$ (first order) or $2K$ (second order) of it. Whatever horizontal momentum is left decides where the light goes.

The guided wave's propagation constant is

$$\beta = \frac{2 \pi n_{eff}}{\lambda_{0}} \qquad (5.1)$$

- $\lambda_0$: the wavelength of the light in vacuum.
- $n_{eff}$: the effective index of the slab waveguide.
- $2\pi/\lambda_0 = k_0$ is the vacuum wavenumber; multiplying by $n_{eff}$ gives the guided wave's wavenumber.

In words: the guided light gains $2\pi$ of phase every $\lambda_0/n_{eff}$ of distance, i.e. every in-guide wavelength.

The grating repeats every $\Lambda$ (capital lambda), the **grating period** (tooth spacing). Its "wavenumber" is

$$K = \frac{2\pi}{\Lambda}$$

This is built just like a light wavenumber, but from the tooth spacing instead of a light wavelength. **Higher-order** diffraction uses whole-number multiples $m \cdot K$. (A periodic pattern can be broken into a sum of sine waves with periods $\Lambda, \Lambda/2, \Lambda/3, \dots$; these give $K, 2K, 3K, \dots$.)

### The Bragg condition (Figure 5.4)

The general **Bragg condition** is

$$\beta - k_{x} = m \cdot K \qquad (5.2)$$

- $\beta$: horizontal wavenumber of the incoming guided light.
- $k_x$: the horizontal part (along the incident direction, $x$) of the wave vector of the diffracted (outgoing) light.
- $m$: the diffraction order, a whole number.
- $K = 2\pi/\Lambda$: the grating vector.

What it says: horizontal momentum is conserved, except that the grating can absorb exactly $m$ chunks of size $K$. Rearranged: $k_x = \beta - mK$. The outgoing light keeps what is left over. The diffracted light travels in the **cladding** (the material above the grating) with refractive index $n_c$. In the figures the cladding is air.

**Figure 5.4 — Matching momenta and finding the angle.**

- **Panel (a):** the black $\beta$ arrow points right from the origin. From its tip, the blue $K$ arrow ("Grating, m=1") points back left. Where $K$ ends, a red dashed vertical line rises; its $x$ position is $k_x = \beta - mK$. *Lesson:* the leftover horizontal momentum is $\beta - K$.
- **Panel (b):** adds a green half-circle above the $x$ axis, centred at the origin, labelled $n_1 = 1$ (air). Its radius is $k_0 = 2\pi/\lambda_0$, the full wavenumber of light in air. A green arrow goes from the origin to the point where the red dashed line hits the circle. That arrow *is* the outgoing light's wave vector. The angle $\theta$ between it and the vertical $z$ axis is the exit angle, with $\theta = \sin^{-1}(k_x/k_0)$.

```
              z
              ^       green circle: radius k0 (air)
          .---|---.
        /     |  / \      green arrow = outgoing light
       |      |θ/   |     red dashed line at x = kx
  -----+------o-----+-------> x
              |---->|----->       beta (black, to the right)
                    <----         K (blue, back to the left)
```

**Lesson:** the outgoing light must have total wavenumber $k_0$ (it lives on the circle) *and* horizontal part $k_x$ (it lives on the red line). Only one arrow fits both, so only one angle is allowed. Note also: $\beta$ is bigger than $k_0$ (since $n_{eff} > 1$), so without the grating the arrow would land outside the circle, and no light could escape. That is exactly why guided light stays guided, and why the grating is needed: it shortens the horizontal momentum enough to fit inside the circle.

The diffracted light's wavenumber (the circle's radius) is

$$k = \frac{2 \pi n_{c}}{\lambda} \qquad (5.3)$$

Here $n_c$ is the cladding index and $\lambda$ is the vacuum wavelength. In air, $n_c = 1$ and $k = k_0$.

The angle then follows from simple trigonometry, because $k_x$ is the horizontal side of the arrow of length $k$:

$$\sin\theta_{c} = \frac{k_x}{k} = n_{eff}\,\frac{\lambda}{\Lambda} \qquad (5.4)$$

$\theta_c$ is the exit angle in the cladding, measured from the vertical. The first equality ($\sin\theta_c = k_x/k$) is the key step. A note for careful readers: the right-hand side as printed in the source does not follow directly. If you substitute $k_x = \beta - K$ (first order) and $k = 2\pi n_c/\lambda$, you get

$$\sin\theta_c = \frac{\beta - K}{k} = \frac{n_{eff} - \lambda/\Lambda}{n_c}$$

which is exactly the simplified Bragg condition the book gives next:

$$n_{eff} - n_{c} \cdot \sin\theta_{c} = \frac{\lambda}{\Lambda} \qquad (5.5)$$

How to read (5.5), term by term (all terms are "momentum divided by $k_0$"):

- $n_{eff}$: the guided light's horizontal momentum.
- $n_c \sin\theta_c$: the outgoing light's horizontal momentum.
- $\lambda/\Lambda$: the chunk the grating removes (first order).

So: "what you had, minus what you leave with, equals what the grating took."

**Figure 5.5 — Light going up into air and down into the oxide.** The same $x$–$z$ picture, now with two half-circles:

- A green half-circle **above** the axis, labelled $n_1 = 1$ (air), radius $k_0 = 2\pi/\lambda_0$.
- A purple half-circle **below** the axis, labelled $n_2 = n_{SiO_2}$ (the oxide underneath). Physically its radius is $n_{SiO_2} k_0$, which is bigger than the green one because oxide's index (about 1.44) is bigger than air's. (The figure's text labels the purple radius with the $\beta$ formula and "waveguide propagation constant"; read it simply as the larger lower circle.)
- The thick black arrow along $+x$ (the guided wave) and the blue left-pointing arrow $K = 2\pi/\Lambda$ ("Grating, m=1").
- One red dashed vertical line at $x = k_x = \beta - mK$. It crosses both circles. A green arrow goes from the origin up to where the line meets the green circle (light going up into air). A purple arrow goes down to where the line meets the purple circle (light going down into the oxide/substrate).

**Lesson:** the grating sends light both up *and* down, with the same horizontal momentum $k_x$. Because the lower circle is larger, the same horizontal distance $k_x$ is a smaller fraction of its radius. So the downward beam is closer to vertical than the upward beam.

### Angle in air, and diffraction into the substrate

Because the cladding might not be air (for example, the chip may be covered in oxide), the light may leave the cladding and then cross into air. Snell's law says the horizontal momentum $n \sin\theta$ stays the same across flat boundaries. So $n_c \sin\theta_c = \sin\theta_{air}$, and (5.5) becomes

$$n_{eff} - \sin\theta_{air} = \frac{\lambda}{\Lambda} \qquad (5.6)$$

$\theta_{air}$ is the angle of the beam in air, which is what you set your fibre to. Nice point: the cladding index drops out. The air angle depends only on $n_{eff}$, $\lambda$ and $\Lambda$.

**Worked example (illustrative numbers, not from the book).** Take $\lambda = 1550$ nm and suppose $n_{eff} = 2.8$ in the grating.

- For a perfectly vertical beam ($\theta_{air} = 0$), (5.6) gives $\Lambda = \lambda/n_{eff} = 1550/2.8 \approx 554$ nm. This is case (a) of Figure 5.2: period equals in-grating wavelength, and you get the unwanted back-reflection.
- Detune to $\Lambda = 630$ nm. Then $\lambda/\Lambda \approx 2.46$, so $\sin\theta_{air} \approx 2.8 - 2.46 = 0.34$, and $\theta_{air} \approx 20^\circ$. This is case (b): a tilted beam, no back-reflection.
- Downward into oxide ($n \approx 1.44$): $\sin\theta_{ox} \approx 0.34/1.44 \approx 0.24$, so $\theta_{ox} \approx 14^\circ$, closer to vertical than the 20° in air, as Figure 5.5 shows.
- Check of the back-reflection idea: in case (a), $K = \beta$, so the second order gives $k_x = \beta - 2K = -\beta$. That is a guided wave with the same size momentum going backwards, i.e. a reflection into the waveguide.

Finally, the book notes that light diffracted into the substrate (Figure 5.5) travels at a smaller angle from the surface normal in the oxide than the light in air does. This downward light is usually lost, which is one reason real grating couplers are not 100% efficient.

> **Key takeaways:**
>
> - Each grating tooth scatters light; the scattered wavelets add up only in certain directions (Huygens–Fresnel).
> - Bragg condition: $\beta - k_x = mK$; the grating removes whole chunks $K = 2\pi/\Lambda$ of horizontal momentum.
> - Exit angle in air: $n_{eff} - \sin\theta_{air} = \lambda/\Lambda$; it depends on wavelength, so a grating coupler works best over a limited wavelength range.
> - If $\Lambda$ equals the in-grating wavelength, light leaves vertically but the second order reflects back, which causes Fabry–Pérot ripples; so gratings are detuned and the fibre is tilted a little.
> - Light also goes down into the oxide, at an angle closer to vertical than in air.

## Glossary

| Term | Plain meaning |
|---|---|
| Back-reflection | Light sent backwards into the waveguide by the grating (here, by the second diffraction order). |
| Bragg condition (Bragg law) | The rule $\beta - k_x = mK$ that picks the direction where scattered waves from a periodic structure add up. |
| Cladding | The material above (or around) the waveguide core; index $n_c$. Often air or oxide. |
| Constructive / destructive interference | Waves adding up (crest on crest) / cancelling (crest on trough). |
| Detuning | Choosing the grating period slightly away from the in-grating wavelength so the beam tilts and back-reflection is avoided. |
| Diffraction | Spreading and redirection of a wave by an obstacle or a periodic pattern. |
| Diffraction order ($m$) | Whole-number label of each direction where a grating's scattered waves add up. |
| Effective index ($n_{eff}$) | The "average" refractive index that a guided mode feels. |
| Fabry–Pérot oscillation | Ripples in transmitted power versus wavelength caused by light bouncing between two reflectors. |
| Focusing grating coupler | A grating coupler with curved teeth that also focuses the light (Section 5.2.3). |
| Grating coupler | A row of etched teeth on a waveguide that couples light between the chip and a fibre above it. |
| Grating period ($\Lambda$) | Distance from one tooth to the next. |
| Grating vector ($K$) | $2\pi/\Lambda$; the chunk of horizontal momentum the grating can add or remove. |
| Huygens–Fresnel principle | Every point on a wave acts as a source of new little waves; their sum gives the wave further on. |
| Mode | A stable light pattern that travels along a waveguide without changing shape. |
| Normal | The direction perpendicular to a surface. |
| Oxide ($SiO_2$) | Silicon dioxide, glass; index about 1.44. Lies under the silicon layer. |
| Phase | Position within a wave's cycle; one cycle is $2\pi$. |
| Propagation constant ($\beta$) | Wavenumber of a guided mode along the waveguide, $n_{eff} \cdot 2\pi/\lambda_0$. |
| Refractive index ($n$) | How many times slower light is in a material than in vacuum. |
| Slab waveguide | A flat layer that traps light only in the up-down direction. |
| Snell's law | $n_1 \sin\theta_1 = n_2 \sin\theta_2$ at a flat boundary; horizontal momentum is kept. |
| Substrate | The base of the chip below the oxide. |
| Wavelength ($\lambda$, $\lambda_0$) | Crest-to-crest distance; $\lambda_0$ is in vacuum. |
| Wavenumber ($k$, $k_0$) | Phase gained per unit length, $2\pi n/\lambda_0$; $k_0$ is the vacuum value. |
| Wave vector | An arrow along the wave's direction with length equal to its wavenumber. |

## Check yourself

1. Why can't guided light leave a smooth waveguide on its own?

   *Answer:* Its horizontal wavenumber $\beta = n_{eff}k_0$ is larger than the full wavenumber of light in the cladding ($n_c k_0$), so no outgoing direction can match it. The grating has to remove some horizontal momentum first.

2. What does $K = 2\pi/\Lambda$ represent?

   *Answer:* The grating vector: the fixed chunk of horizontal wavenumber that a grating of period $\Lambda$ can give or take (multiples $mK$ for higher orders).

3. Write the Bragg condition and say what each term means.

   *Answer:* $\beta - k_x = mK$. Incoming horizontal momentum minus outgoing horizontal momentum equals $m$ chunks of grating momentum.

4. If the period equals the wavelength inside the grating, where does light go?

   *Answer:* The first order goes straight up (vertical). The second order goes straight back into the waveguide (a reflection).

5. Why is that back-reflection a problem, and how is it avoided?

   *Answer:* Reflections at the input and output couplers form a Fabry–Pérot cavity, giving ripples in the measured spectrum. It is avoided by detuning the grating so the beam tilts, and tilting the fibre slightly from the normal.

6. Using (5.6), with $n_{eff} = 2.8$, $\lambda = 1550$ nm, $\Lambda = 630$ nm, what is the angle in air?

   *Answer:* $\sin\theta_{air} = 2.8 - 1550/630 \approx 0.34$, so $\theta_{air} \approx 20^\circ$.

7. If the wavelength increases a bit while everything else stays fixed, which way does the beam angle move?

   *Answer:* $\lambda/\Lambda$ grows, so $\sin\theta_{air} = n_{eff} - \lambda/\Lambda$ shrinks (ignoring the small change of $n_{eff}$ with wavelength): the beam moves closer to vertical.

8. Why is the beam into the oxide closer to vertical than the beam into air?

   *Answer:* Both have the same horizontal wavenumber $k_x$, but the oxide's total wavenumber ($1.44\,k_0$) is larger, so $\sin\theta = k_x/k$ is smaller.

9. Why does the cladding index drop out of equation (5.6)?

   *Answer:* Snell's law keeps $n\sin\theta$ fixed across flat boundaries, so $n_c\sin\theta_c = \sin\theta_{air}$; the air angle depends only on $n_{eff}$, $\lambda$ and $\Lambda$.
