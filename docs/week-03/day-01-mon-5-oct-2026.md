# Week 3 · Day 1 — Monday 5 Oct 2026

*Simple-English study version of Chrostowski & Hochberg §4.2 (Y-branch)*

[:material-file-pdf-box: Download this day as PDF](day-01-mon-5-oct-2026.pdf){ .md-button }

## Before you start: the big picture

On a silicon photonic chip, light travels along tiny "wires" made of glass-like silicon, called waveguides. Very often you need to take the light in one waveguide and share it between two waveguides. Or you need to bring the light from two waveguides back into one. The simplest part that does this is the **Y-branch**. It looks like the letter Y lying on its side: one road in, two roads out.

Think of a water pipe that forks into two pipes. Water coming in from the single pipe is shared equally between the two. That part is easy. The surprise comes when you run it backwards. If you push water into only one of the two branches, you might expect all of it to come out of the single pipe. With light, that is **not** what happens. Only half comes out. This packet explains why. The answer comes from the wave nature of light: light has a phase, and waves can add up or cancel out.

This matters a lot because the Y-branch is a building block of the **Mach-Zehnder interferometer** (next section, §4.3). That device splits light, sends it down two paths, and joins it again. It is used to build switches, modulators (which put data onto light) and sensors. To understand those, you first need to understand what a Y-branch does in both directions.

## Background you need

### Light is a wave with an amplitude and a phase

Light is a wave of electric and magnetic fields that wiggle as the light moves. At any point we can describe the wave by its **electric field**, written $E$. The field has a size (the **amplitude**: how big the wiggle is) and a **phase** (where in its up-and-down cycle the wiggle is at that moment). A full cycle is $360^\circ$, or $2\pi$ radians.

### Intensity is the field squared

What a detector actually measures is the **intensity** $I$ (power per area) or the **power** $P$. It is not the field itself. Intensity goes as the square of the field:

$$
I \propto |E|^2
$$

The symbol $\propto$ means "is proportional to". The bars $|\cdot|$ mean "size of", ignoring the phase. So if you double the field, you get four times the intensity. And if you want half the intensity, you need the field to shrink by a factor of $\sqrt{2} \approx 1.414$, because $(1/\sqrt{2})^2 = 1/2$.

### Interference: waves add as fields, not as powers

When two waves meet, their **fields** add, and the phase matters:

- **In phase** (crests line up, phase difference 0): fields add up. Two fields of size $a$ give $2a$, so intensity $4a^2$. This is **constructive interference**.
- **Out of phase** (crest meets trough, phase difference $\pi$ or $180^\circ$): fields cancel. $a - a = 0$, so intensity 0. This is **destructive interference**.

Energy is never lost. When light cancels in one place, the energy goes somewhere else.

### Coherent vs. incoherent light

Two beams are **coherent** if their phases are locked together in a fixed relation (for example, both came from the same laser). Then they interfere in a steady way. Two beams are **incoherent** if their phase difference drifts randomly (for example, two separate lasers). Then the interference averages out over time, and on average you just add powers.

### Waveguides and modes

A **waveguide** is a strip of material with a high **refractive index** (silicon, about 3.5) surrounded by lower-index material (glass, about 1.44). Light bends back into the strip at the walls and stays trapped inside, like light in an optical fiber.

Light can only travel in a waveguide in certain fixed patterns across its width. Each pattern is called a **mode**. A mode keeps its shape as it travels.

- The **fundamental mode** (first-order mode) is a single bump: brightest in the middle, fading to the edges. Its field has the same sign everywhere.
- The **second-order mode** has two bumps with opposite signs: the left half points "up" while the right half points "down". It is antisymmetric.
- **Radiation modes** are not trapped at all. They are light that leaks out of the waveguide and flies away into the surroundings. This is lost light.

```
 fundamental mode        second-order mode
       __                  __
      /  \                /  \
 ____/    \____      ____/    \      ____
                              \    /
                               \__/
   (symmetric)          (antisymmetric: + then -)
```

A narrow single-mode waveguide can only carry the fundamental mode. Any light that "wants" to be in the second-order shape cannot stay guided there, so it radiates away and is lost.

### Ports

A **port** is an entry or exit point of a device. A Y-branch looks like it has three ports: one on the single side and two on the split side.

### Decibels (dB)

Engineers measure loss in **decibels**:

$$
\text{Loss (dB)} = 10 \log_{10}\left(\frac{P_\text{out}}{P_\text{in}}\right)
$$

$P_\text{out}/P_\text{in}$ is the fraction of power that makes it through. Some handy values:

| Fraction of power kept | dB |
|---|---|
| 100% (1) | 0 dB |
| about 93% | −0.3 dB |
| 50% (1/2) | about −3.01 dB |
| 1% | −20 dB |
| 0.0001% ($10^{-7}$) | −70 dB |

Read it this way: every −3 dB halves the power, every −10 dB divides it by 10. The sign convention varies. The plots in the book show negative numbers; the text speaks of a "loss of 3 dB". Same thing.

**Insertion loss** is how much power you lose by putting the device in the path. **Excess loss** is the extra loss beyond what an ideal device would have. For a perfect 50/50 splitter, each output is ideally at −3 dB. If a real output is at −3.25 dB, the excess loss is about 0.25 dB.

### Simulation tools: FDTD and GDS

**FDTD** (finite-difference time-domain) is a computer method that solves Maxwell's equations (the basic laws of light) on a fine grid, step by step in time. You watch the light wave move through your structure, as in a movie. **3D FDTD** is accurate but slow. **2.5D FDTD** (in Lumerical this is called varFDTD) squashes the 3D problem into an approximate 2D one. It is much faster and usually good enough for planar devices.

**GDS** is the standard file format for chip layouts: the top-down drawing of shapes that will be etched into the silicon.

A **genetic algorithm** is an optimization method inspired by evolution. You make many candidate designs, keep the best ones, "mutate" and mix them, and repeat. Over many rounds the designs get better.

> **Key takeaways:**
>
> - Detectors measure intensity, which goes as field squared: $I \propto |E|^2$.
> - Fields add with their phases: in phase they reinforce, out of phase they cancel.
> - A waveguide carries light in fixed patterns called modes; a narrow guide keeps only the fundamental mode, and other light radiates away.
> - −3 dB means half the power is lost.

## 4.2 Y-branch

> **In one sentence:** A Y-branch splits light 50/50 from one waveguide into two, but used backwards it is *not* a lossless combiner — it acts as a 50/50 beam-splitter in that direction too, so what comes out depends on the phases of the inputs.

### What the device does

A Y-branch has two jobs:

- As a **splitter**: light from one waveguide is shared equally into two waveguides.
- As a **combiner**: light from two waveguides is merged into one waveguide.

**Figure 4.21 — Y-branch splitter/combiner (layout file `YBranch_Compact.gds`).** This is a top-down view of the actual shape drawn for fabrication, shown on a grid with a 1 µm scale bar. A straight input waveguide comes in from the left. It then widens into a smooth, rounded, symmetric "bulb" (a **taper**, a region where the width changes gradually). From this bulb, two curved arms leave to the right: one curves up, one curves down. In the middle, between the two arms, there is a small teardrop-shaped notch (a gap with no silicon). The lesson: the whole device is only a few micrometers long, and its exact outline is not a simple "Y". The widths along the device were carefully shaped by computer optimization so that light splits with very little loss.

```
                    ___________  output 1
                   /
 input ===========(  < notch
                   \___________  output 2
       |--- a few µm ---|
```

### The splitter: the easy direction

Start with input light of intensity $I_i$ and electric field $E_i$. The device shares it equally, so each output gets half the intensity:

$$
I_1 = I_2 = \frac{I_i}{2}
$$

Here $I_1$ and $I_2$ are the intensities in the two output arms. What about the fields? Since $I \propto |E|^2$, halving the intensity means dividing the field by $\sqrt{2}$:

$$
E_1 = E_2 = \frac{E_i}{\sqrt{2}}
$$

Check: $|E_1|^2 = |E_i|^2/2$. Add the two outputs: $|E_i|^2/2 + |E_i|^2/2 = |E_i|^2$. All the power is accounted for. Good.

**Worked example:** 1 mW goes in. Each arm gets 0.5 mW. If the input field has size 1 (in some unit), each output field has size $1/\sqrt{2} \approx 0.707$.

### Why it is not really a "three-port" device

The key idea of this section: **you cannot think of the Y-branch as just three ports.** It *looks* like one input and two outputs. But light does not just care about which waveguide it is in; it cares about which **mode** it is in.

Look at the single-waveguide side. Near the junction, this waveguide region can hold (at least) two patterns:

1. the fundamental mode (one symmetric bump), and
2. either the second-order mode (antisymmetric, + and −) or, if the waveguide is too narrow to guide it, radiation modes (light leaking away).

On the two-arm side there are also two "channels": arm 1 and arm 2. So the honest picture is **two modes in, two modes out**. It is a 2-by-2 system, just like a 50/50 glass **beam-splitter** in a lab, which has two inputs and two outputs.

How do the arm patterns match up with the modes? Imagine both arms carrying light of equal size:

- If the two arms are **in phase** (+, +), together they look like one symmetric bump. That matches the **fundamental mode**.
- If they are **out of phase** (+, −), together they look like the antisymmetric pattern. That matches the **second-order mode**.

```
 arms in phase  (+,+)   -->  fundamental mode   (kept, guided)
 arms out of phase (+,-) -->  2nd-order mode     (lost if guide is single-mode)
```

The output waveguide is usually single-mode. So only the fundamental mode survives. Anything that ends up in the second-order pattern radiates away.

### The combiner: the surprising direction

Now send light into just **one** arm, with intensity $I_1$ and field $E_1$. Light in one arm alone is *half* "both arms in phase" and *half* "both arms out of phase". (Mathematically: the pattern $(1, 0)$ equals $\tfrac{1}{2}(1,1) + \tfrac{1}{2}(1,-1)$.) So the same 50/50 rule applies: the light splits equally between the fundamental mode and the second-order (or radiation) mode.

Only the fundamental-mode half comes out of the combined port:

$$
I_i = \frac{I_1}{2}, \qquad E_i = \frac{E_1}{\sqrt{2}}
$$

Here $I_i$ and $E_i$ are now the intensity and field at the single (combined) port. The other half is lost as radiation.

**Worked example:** 1 mW into one arm only, nothing in the other. Only 0.5 mW comes out of the single port. The other 0.5 mW leaks into the chip around the device.

So the Y-branch behaves like a 50/50 beam-splitter **in both directions**.

### Two important consequences

1. **You cannot add up two incoherent beams with a Y-branch.** Suppose you have two separate lasers, 1 mW each, and you hope to combine them into 2 mW in one waveguide. It does not work. Their phase difference wanders randomly. On average, each beam behaves like the "one input only" case: half of each gets through. You get about 1 mW out, the same as you started with in one arm. You cannot squeeze more power into a single mode this way.
2. **If light is in only one input port, the output is cut to half.** This is a 3 dB loss, and it is built in. It is not a flaw of fabrication; it is physics.

What *does* work is combining two **coherent** beams with the right phase. That is what the simulations below show.

### Real Y-branches: not perfect

Real Y-branches do not split exactly 50/50, and they lose some extra light (the **excess loss**). Their shape has to be tuned. The book's design was optimized with FDTD simulations plus a genetic algorithm. The algorithm changed the width of the Y-branch at several points along its length and kept the designs with the least loss. The result was an **insertion loss below 0.3 dB** (that is, less than about 7% of the light lost beyond the ideal split). The final shape is the one in Figure 4.21.

### How the simulations are done (Listing 4.12)

The book gives a Lumerical script, Listing 4.12 (the code itself is not in this packet). It can run in either 2.5D or 3D FDTD. In words, it does this:

1. **Load the layout:** read the Y-branch shape from the GDS file.
2. **Set up the simulation:** materials, simulation region, light source (a waveguide mode) and monitors (virtual detectors).
3. **Run four cases:**
   - splitter: light into the single port;
   - combiner, one input only;
   - combiner, two inputs **in phase**;
   - combiner, two inputs **out of phase**.
4. **Measure the output:** for the combiner cases, a **mode-expansion monitor** computes a **mode overlap integral**. This asks: "How much of the output light has the exact shape of the fundamental mode?" Only that part counts as useful output.
5. **Output:** field-profile pictures, insertion loss versus wavelength, and movies of light moving through the device. The movies help you *see* where light is lost.

Inputs: the GDS file and simulation settings. Outputs: field maps, loss spectra, movies.

### Case 1: the splitter

**Figure 4.22 — Y-branch as a splitter.** (a) Field profile: a colour map of light intensity seen from above, about 16 µm long ($x$ from −3 to 13 µm) and 8 µm tall ($y$ from −4 to 4 µm). Blue is dark, red/yellow is bright. Light enters from the left in a single waveguide at $y = 0$. Near $x \approx 2$–3 µm it spreads out in the junction and then separates cleanly into two bright arms, one going up-right and one going down-right. Little light leaks out. (b) Insertion loss into one output arm versus wavelength from 1.5 to 1.6 µm (1500–1600 nm, the main telecom band). The curve is very flat. It goes from about −3.29 dB at 1.5 µm, up to about −3.24 dB near 1.545 µm, and to about −3.26 dB at 1.6 µm.

How to read the numbers: an ideal split gives −3.01 dB per arm. The simulation gives about −3.25 dB. So the excess loss is about 0.25 dB, which fits the "below 0.3 dB" claim. The variation across the whole 100 nm band is only about 0.05 dB, so the device works over a wide range of wavelengths. Lesson: the light splits evenly, with insertion loss slightly over 3 dB. The 3 dB is the expected 50%; the small extra is the non-ideal device.

### Case 2: combiner with light in one input only

**Figure 4.23 — Y-branch as a combiner with a single input.** (a) Field profile on the same kind of map. Light comes into one arm and passes through the junction into the single waveguide. In the single waveguide and the transition region, you can see ripples or fringes along the direction of travel. These come from two modes travelling together and beating against each other: the fundamental mode and the **second-order TE mode** are both excited. (TE means "transverse electric", the usual polarization in these chips: the electric field points sideways, in the plane of the chip.) (b) Insertion loss, counting only the power in the fundamental mode, versus wavelength. It runs from about −3.28 dB at 1.5 µm, to about −3.225 dB near 1.545–1.55 µm, to about −3.248 dB at 1.6 µm.

Lesson: exactly as the theory predicts, only about half the light (loss slightly over 3 dB) ends up in the useful fundamental mode. The other half is in the second-order mode and will be lost. The loss is measured with mode overlap integrals, not just total power, because the second-order light is not useful.

### Case 3: combiner with two in-phase inputs

Now feed light into **both** arms, with equal size and **the same phase**, from the same (coherent) source. In the single waveguide, the two halves add up into the symmetric fundamental mode. This is constructive interference. Ideally, close to 100% of the input power ends up in the output waveguide. Whatever is missing is the **excess loss** of the device.

**Figure 4.24 — Y-branch as a combiner with two in-phase inputs.** (a) Field profile: light in both symmetric arms (reaching about $y \approx \pm 2.5$ µm at the far end) merges at the junction (around $x \approx 2$ µm) into one bright beam in the single waveguide. (b) Insertion loss versus wavelength, now on a very different scale: about −0.265 dB at 1.5 µm, best value about −0.215 dB near 1.545 µm, and about −0.238 dB at 1.6 µm.

How to read it: −0.22 dB means about 95% of the power gets through. So almost all the light is combined. The 3 dB penalty is gone. This −0.2 to −0.3 dB curve is the excess loss of the device. (The book's text says the excess loss is "plotted in Figure 4.23b", but the excess-loss curve near −0.2 dB is the one in Figure 4.24b; this looks like a slip in the reference.)

Note how this matches the splitter case: about 0.25 dB extra loss in both. Light that runs "backwards" through a splitter, with the right phases, retraces its path.

### Case 4: combiner with two out-of-phase inputs

Finally, feed both arms with equal light but **opposite phase** (180° apart). Now the two halves form the antisymmetric pattern. In the fundamental mode they cancel: destructive interference. Ideally, 0% ends up in the fundamental mode. All the power goes into the second-order TE mode or radiation modes, and is lost from the output waveguide.

**Figure 4.25 — Y-branch as a combiner with two out-of-phase inputs.** (a) Field profile: light is seen in both input arms and in the junction region. Past the junction the light does not form a clean fundamental mode; the pattern shows higher-order-mode excitation (and radiation), as expected. (b) Insertion loss into the fundamental mode versus wavelength. It is U-shaped: about −69.6 dB at 1.5 µm, lowest about −70.7 dB near 1.555 µm, and about −68.9 dB at 1.6 µm.

How to read it: −70 dB means only about $10^{-7}$ of the power, one ten-millionth, is in the fundamental mode. That is essentially zero. The cancellation is almost perfect, because the device is so symmetric.

### Summary of the four cases

| Case | What goes in | Ideal power in output (fundamental mode) | Simulated loss near 1550 nm |
|---|---|---|---|
| Splitter (per arm) | 1 beam into single port | 50% | about −3.25 dB |
| Combiner, one input | light in one arm only | 50% | about −3.23 dB |
| Combiner, in phase | equal coherent beams, same phase | 100% | about −0.22 dB |
| Combiner, out of phase | equal coherent beams, opposite phase | 0% | about −70 dB |

Read each row as: "if I feed the Y-branch like this, how much useful light comes out?" Rows 3 and 4 show that the combiner's output depends completely on the **phase difference** between its inputs. This is the core idea behind interferometers.

### Looking ahead: the Mach-Zehnder interferometer

With this, we can understand the **Mach-Zehnder interferometer (MZI)** of Section 4.3. It is two Y-branches back to back: the first splits light into two arms, and the second combines the arms again. If the light picks up the same phase in both arms, the combiner sees "in phase" and almost all the light comes out. If the arms differ by half a wavelength, it sees "out of phase" and almost nothing comes out. Anything in between gives a partial output. So by changing the phase in one arm (through its length or its refractive index), you control the output.

**Figure 4.26 — Mach-Zehnder interferometer, layout example.** A top-down chip layout with a 40 µm scale bar. A single input waveguide enters on the far left and meets a first Y-branch (the splitter). The top arm goes straight to the right. The bottom arm bends down by 90° with a smooth, rounded bend, then runs to the right in parallel with the top arm. At the far right, the bottom arm bends up by 90° and meets the top arm at a second Y-branch (the combiner). One output waveguide leaves to the far right. The whole device is roughly 560–600 µm long and 120–160 µm tall. Lesson: the MZI is just "split, travel two separate paths, recombine". The two arms here can have different lengths, which gives them different phase. The output brightness then depends on that phase difference.

```
          ________________________________
         /                                \
 in ----<                                  >---- out
         \__                            __/
            |__________________________|
     Y-branch                         Y-branch
     (split)                          (combine)
```

> **Key takeaways:**
>
> - As a splitter, a Y-branch sends half the intensity to each arm: $I_1 = I_2 = I_i/2$, $E_1 = E_2 = E_i/\sqrt{2}$.
> - It is really a 2-input, 2-output system (fundamental mode plus second-order/radiation mode), so it acts as a 50/50 beam-splitter in both directions.
> - With light in only one combiner input, only half reaches the output; you cannot combine incoherent beams to get more power.
> - Coherent in-phase inputs combine almost losslessly (about −0.22 dB); out-of-phase inputs cancel almost completely (about −70 dB).
> - The optimized device has excess loss under 0.3 dB across 1500–1600 nm, and it is the building block of the Mach-Zehnder interferometer.

## Glossary

| Term | Plain meaning |
|---|---|
| 2.5D FDTD | A faster, approximate version of FDTD that turns a flat 3D chip problem into a 2D one. |
| 3D FDTD | Full FDTD simulation in three dimensions; accurate but slow. |
| Amplitude | The size of a wave's wiggle. |
| Beam-splitter (50/50) | A device with two inputs and two outputs that sends half of each input to each output. |
| Coherent | Two beams whose phases are locked together, so they interfere in a steady way. |
| Combiner | A device that merges light from two waveguides into one. |
| Constructive interference | Waves in phase adding up to a bigger wave. |
| Decibel (dB) | A log scale for power ratios: $10\log_{10}(P_\text{out}/P_\text{in})$; −3 dB is half. |
| Destructive interference | Waves out of phase cancelling each other. |
| Electric field ($E$) | The part of a light wave that pushes on charges; its square gives intensity. |
| Excess loss | Loss beyond what an ideal device would have. |
| FDTD | Finite-difference time-domain: a simulation that solves the equations of light step by step on a grid. |
| Fundamental mode | The simplest light pattern in a waveguide: one symmetric bump. |
| GDS | Standard file format for chip layout drawings. |
| Genetic algorithm | An optimization method that "breeds" better designs over many rounds. |
| Incoherent | Beams with random, drifting phase difference; on average their powers just add. |
| Insertion loss | Power lost by putting the device into the light path. |
| Intensity ($I$) | Power per area; what a detector measures; proportional to the field squared. |
| Mach-Zehnder interferometer (MZI) | A split–two paths–recombine device whose output depends on the phase difference between the paths. |
| Mode | A fixed light pattern across a waveguide that keeps its shape as it travels. |
| Mode-expansion monitor | A simulation detector that measures how much light is in each mode. |
| Mode overlap integral | A calculation of how much of a light field matches a given mode's shape. |
| Phase | Where a wave is in its cycle; decides whether waves add or cancel. |
| Port | An entry or exit point of a device. |
| Radiation modes | Light that is not trapped by the waveguide and leaks away (lost). |
| Refractive index | How much a material slows light; high-index cores trap light. |
| Second-order mode | A two-lobed, antisymmetric (+/−) light pattern in a waveguide. |
| Single-mode waveguide | A waveguide narrow enough to guide only the fundamental mode. |
| Splitter | A device that divides light from one waveguide into two. |
| Taper | A region where a waveguide's width changes gradually. |
| TE (transverse electric) | Polarization where the electric field points sideways, in the plane of the chip. |
| Waveguide | A strip of high-index material that traps and guides light. |
| Y-branch | A Y-shaped junction that splits one waveguide into two, or joins two into one. |

## Check yourself

1. A splitter gets 2 mW at its input. What power and what relative field size does each output arm get (ideal device)?

   *Answer:* 1 mW each. The field in each arm is $1/\sqrt{2} \approx 0.707$ times the input field, because intensity goes as field squared.

2. Why is it wrong to think of a Y-branch as a simple three-port device?

   *Answer:* Because the single-waveguide side carries more than one mode (fundamental plus second-order or radiation modes). The device is really two modes in, two modes out, like a 50/50 beam-splitter.

3. You send 1 mW into only one arm of a Y-branch combiner. How much comes out of the single port, and where does the rest go?

   *Answer:* About 0.5 mW (a 3 dB loss). The other half goes into the second-order mode or radiation modes and is lost.

4. Can you combine two separate, unrelated lasers of 1 mW each into 2 mW in one waveguide with a Y-branch? Why?

   *Answer:* No. The beams are incoherent, so on average each one only gets half through; you get about 1 mW in total.

5. What happens with two equal coherent inputs that are in phase? Out of phase?

   *Answer:* In phase: constructive interference, nearly all power goes into the output fundamental mode (simulated about −0.22 dB). Out of phase: destructive interference, almost nothing in the fundamental mode (about −70 dB); the power goes to the second-order mode or radiation.

6. The splitter simulation shows about −3.25 dB per arm. What is the excess loss?

   *Answer:* About 0.25 dB, since an ideal 50/50 split is about −3.01 dB per arm. This matches the "below 0.3 dB" result from the optimization.

7. How was the Y-branch shape optimized?

   *Answer:* With FDTD simulations driven by a genetic algorithm that varied the device widths at several points along its length to minimize insertion loss.

8. Why does the simulation use mode overlap integrals rather than just total power in the output region?

   *Answer:* Because only light in the fundamental mode is useful; light in the second-order mode is still near the waveguide at first but will be lost. The overlap integral picks out just the fundamental-mode part.

9. How does an MZI use Y-branches, and why does its output depend on the arms?

   *Answer:* One Y-branch splits light into two arms and a second recombines it. The combiner's output depends on the phase difference between the arms: in phase gives full output, opposite phase gives almost none.
