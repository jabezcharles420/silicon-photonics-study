# Week 7 · Day 2 — Tuesday 3 Nov 2026

*Simple-English study version of Chrostowski & Hochberg §10.1–10.2 (Process design kit and mask layout), plus a preview of Chapter 11.*

[:material-file-pdf-box: Download this day as PDF](day-02-tue-3-nov-2026.pdf){ .md-button }

## Before you start: the big picture

Imagine you want a custom bookshelf made by a carpentry shop. The shop has a catalogue: the wood thicknesses they stock, the cuts their machines can make, the smallest hole they can drill, and a set of ready-made parts (hinges, shelves, brackets). You draw your design using only those parts and within those limits. Then you check your drawing twice: once to make sure the shop *can* build it, and once to make sure the drawing really is the bookshelf you meant to design. Only then do you send it off.

Building a silicon photonic chip works the same way. A **foundry** (a chip factory) offers a fixed manufacturing recipe. It gives designers a **process design kit (PDK)**: the catalogue, the rules, and the ready-made parts. The designer draws a **schematic** (a wiring diagram of which parts connect to which), simulates it, turns it into a **layout** (the exact shapes that will be printed on the chip), and then runs two checks: **design rule checking (DRC)** — "can the factory make this?" — and **layout versus schematic (LVS)** — "is this what I meant?".

Section 10.1 walks through this whole flow using a free, teaching-oriented kit called the **Generic Silicon Photonics (GSiP) PDK**, with a small example: a two-channel optical transmitter. Section 10.2 then talks about practical ways to arrange many test devices on a chip, either quickly or in a space-saving way. Space on a chip costs real money, so packing devices cleverly matters. The packet ends with the first paragraph of Chapter 11, which is about how manufacturing is never perfect.

## Background you need

### Light as a wave, and wavelength

Light is a wave of electric and magnetic fields. The distance between two wave crests is the **wavelength**, written $\lambda$ (Greek "lambda"). Silicon photonics mostly uses infrared light with $\lambda \approx 1550$ nm (nanometres; 1 nm = $10^{-9}$ m), the same wavelength used in long-distance fibre-optic internet cables. Silicon is transparent at this wavelength, so light can travel through it. You will see "1550" inside part names such as `GC_TE1550_20`.

Useful units: 1 mm = 1000 µm (micrometres, "microns"), and 1 µm = 1000 nm. A human hair is about 50–100 µm wide. Most photonic devices in this packet are a few µm to a few hundred µm in size.

### Refractive index and waveguides

The **refractive index** $n$ of a material tells how much slower light travels in it than in vacuum: speed $= c/n$, where $c$ is the speed of light in vacuum. Silicon has $n \approx 3.5$; silicon dioxide (glass, "oxide") has $n \approx 1.44$. (You will see `n_cladd = 1.44` in one figure — that is the index of the oxide **cladding**, the material around the silicon.)

When light inside a high-index material hits a boundary with a low-index material at a shallow angle, it bounces back completely. This is **total internal reflection**. A thin strip of silicon surrounded by oxide therefore traps light and guides it along, like water in a pipe. This strip is a **waveguide**. Typical silicon waveguides here are 500 nm wide (`wg_width = 0.5`, in µm) and 220 nm tall.

Two common shapes:

- **Strip waveguide**: a rectangular bar of silicon, fully etched on both sides. Confines light tightly, so it can bend sharply.
- **Rib waveguide**: a bar sitting on a thinner sheet ("slab") of silicon, because the etch did not go all the way down. Light is less tightly held, but the slab lets electrical current reach the waveguide, which modulators need.

```
   Strip waveguide          Rib waveguide
      ______                   ______
     |  Si  |            _____|  Si  |_____
     |______|           |___________________|  <- thin slab
   ~~~~~ oxide ~~~~~       ~~~~~ oxide ~~~~~
```

### Modes and polarization (TE and TM)

A waveguide does not carry light in any random pattern. Only certain stable field patterns, called **modes**, travel without changing shape. A **single-mode** waveguide carries only one pattern (simple, predictable). A **multi-mode** waveguide is wider and carries several.

Light's electric field points in a particular direction; this is its **polarization**. In a flat chip waveguide we name two families: **TE** (transverse electric — the electric field lies mostly sideways, parallel to the chip surface) and **TM** (transverse magnetic — the electric field points mostly up/down). They behave differently: in 220 nm thick silicon, the TM mode is held less tightly, so it leaks out of bends more easily and needs larger bend radii.

### Loss and decibels (dB)

Light power gets weaker as it travels or passes through parts. Engineers measure this in **decibels (dB)**:

$$
\text{Loss (dB)} = -10 \log_{10}\left(\frac{P_\text{out}}{P_\text{in}}\right)
$$

Here $P_\text{in}$ is the power going in and $P_\text{out}$ is the power coming out. The logarithm turns multiplication into addition, so losses of parts in a row simply add. Rules of thumb: 3 dB means half the power is lost; 10 dB means only 1/10 remains; 0.1 dB means about 2.3% is lost.

Waveguide **propagation loss** is quoted per length, in **dB/cm**. For example, 0.27 dB/cm over 10 cm gives 2.7 dB total, so about $10^{-0.27} \approx 0.54$ (54%) of the light survives. **Insertion loss** is the total loss a component adds when you put it in the light's path.

### Bends: two ways to lose light

When a waveguide bends, light can be lost in two ways:

- **Radiation loss**: in a too-tight bend, the outer part of the light "cannot keep up" and leaks out of the waveguide, like a car skidding off a sharp curve.
- **Mode-mismatch loss**: the light's pattern in a curved waveguide is shifted outward compared with a straight one. Where a straight section suddenly meets a curved one, the patterns do not line up perfectly, and some light is scattered at the junction. Changing the curvature gradually ("adiabatically") avoids this sudden jump.

**Adiabatic** here just means "changing slowly enough that the light smoothly adjusts and nothing is lost".

### Interference, rings and modulators

When two light waves meet, they add. If crests meet crests, the light gets brighter (**constructive interference**); if crests meet troughs, they cancel (**destructive interference**). The relative position of crests is called **phase**.

A **ring resonator** is a waveguide loop next to a straight "bus" waveguide. Light at certain wavelengths fits a whole number of times around the loop, builds up, and is pulled out of the bus. So the ring acts as a wavelength filter. A **racetrack** is a ring stretched with straight sections, giving a longer coupling region. The narrow space between ring and bus is the **gap**; the straight coupling length is $L_c$.

A **modulator** encodes data onto light by switching it on and off (or changing it) very fast. In a **ring modulator**, the ring contains a **pn junction** (explained next). Applying voltage changes the number of free charges in the silicon, which slightly changes its refractive index, which shifts the ring's resonant wavelength. Light at a fixed wavelength is then passed or blocked, carrying the electrical data onto the light.

### Doping, pn junctions, and concentrations

Pure silicon conducts electricity poorly. **Doping** means deliberately adding a tiny amount of other atoms. **N-type** doping adds atoms that donate extra free **electrons** (negative carriers). **P-type** doping adds atoms that create **holes** — missing electrons that act like positive carriers. Doping is done by **ion implantation**: firing the atoms into the silicon through a patterned mask.

A **pn junction** is where p-type meets n-type. Applying a voltage pushes carriers in or pulls them out of the junction region. This is what ring modulators and many detectors use.

Doping strength is a **concentration**, in atoms per cubic centimetre (cm$^{-3}$). Silicon has about $5 \times 10^{22}$ atoms per cm$^3$. So $5 \times 10^{17}$ cm$^{-3}$ means about one dopant per 100,000 silicon atoms: light doping, used where light travels (dopants absorb light, so you want few). The "++" levels, around $10^{20}$ cm$^{-3}$, are a thousand times heavier and make the silicon conduct almost like a metal. They are used only where metal wires touch the silicon, away from the light.

### Germanium detectors

Silicon does not absorb 1550 nm light, so it cannot detect it. **Germanium (Ge)** does absorb it. A small block of germanium grown on the silicon turns light into electrical current (a **photodetector**).

### Getting light on and off the chip

Light usually comes from an **optical fibre** (a hair-thin glass thread). A **grating coupler** is a patch of shallow grooves etched into silicon. The grooves scatter light upward out of the chip (or catch light coming down from a fibre held above the chip, at an angle such as 20°). An **edge coupler** instead brings light in through the polished side of the chip. A **fibre array** is a row of fibres held at a fixed spacing, so you can couple many grating couplers at once.

A **bond pad** (or **probe pad**) is a square of metal where an electrical wire is bonded or a probe needle touches down. **GS probe pads** are a pair: **G**round and **S**ignal, used with high-frequency probes.

### How a chip is made, very briefly

A silicon photonic chip starts from a **silicon-on-insulator (SOI)** wafer: a thin top layer of silicon (e.g. 220 nm) sitting on a layer of oxide (the **buried oxide**, BOX, e.g. 2 µm), sitting on a thick silicon base. Patterns are made by **lithography**: a light-sensitive coating is exposed through a **mask** (a stencil), developed, and then the uncovered silicon is **etched** (removed) to some depth. Each step (each etch, each doping, each metal layer) needs its own mask. **Deposition** adds material (e.g. metal or germanium). **CMP (chemical mechanical polishing)** grinds the wafer surface flat between steps.

### Electronic design automation (EDA) vocabulary

Chip design borrowed a mature toolset from electronics, called **EDA** (electronic design automation). Key words:

- **Schematic**: a diagram of components as symbols, joined by lines showing connections. It shows *what connects to what*, not real sizes or positions.
- **Netlist**: the schematic written as text. Each **net** is one connection (a wire or waveguide) and has a name; each component lists the nets touching its **pins** (also called **ports**, the connection points).
- **SPICE**: a classic circuit simulator from electronics, whose text netlist format is widely copied.
- **Layout**: the actual geometric shapes (polygons) to be printed on each mask layer, at real size.
- **GDS** (GDSII): the standard file format for layouts. Each shape belongs to a numbered **layer**.
- **Cell**: a reusable block of layout (like a stamp). A **PCell** (parameterized cell) is a cell drawn by a script from parameters you choose, e.g. a ring with radius 23 µm or 30 µm.
- **Instance / instantiate**: placing one copy of a cell or symbol into a design.
- **Compact model**: a fast mathematical description of how a component behaves (e.g. its transmission vs wavelength), used in circuit simulation instead of solving full physics.
- **Place and route**: first place the components, then draw the connections (routes) between them.

Tools named in the packet: **Mentor Graphics Pyxis** (schematic and layout editor), **Mentor Graphics Calibre** (DRC/LVS checker), **AMPLE** (Pyxis's scripting language), and **Lumerical INTERCONNECT** (photonic circuit simulator). **FDTD** (finite-difference time-domain) is an accurate but slow simulation that solves the full light-wave equations on a grid.

### WDM and eye diagrams

**Wavelength division multiplexing (WDM)** sends several data channels through one waveguide, each on a different wavelength (colour), like several radio stations sharing the air. A **two-channel WDM transmitter** has two modulators, each tuned to its own wavelength.

An **eye diagram** overlays many short slices of a fast digital signal on top of each other. A wide-open "eye" shape means the ones and zeros are easy to tell apart.

> **Key takeaways:**
>
> - Light is guided in silicon strips (waveguides) surrounded by oxide; 1550 nm is the usual wavelength.
> - Loss is counted in dB (adds up along a path); waveguide loss is in dB/cm.
> - Bends lose light by radiation (too tight) or by mode mismatch (sudden curvature change).
> - Doping makes silicon conduct; pn junctions let voltage change the refractive index (modulators).
> - Chip design uses schematic → netlist → layout (GDS layers) → checks.

## 10.1 Process design kit (PDK)

> **In one sentence:** A PDK is the foundry's "designer's handbook plus parts box plus checking tools", and this section tours a free generic one (GSiP) and its full design flow.

### What a PDK contains

A **process design kit (PDK)** is a set of documents and data files. It describes one manufacturing process at one **semiconductor foundry**, and it gives you everything needed to finish a design for that process. A typical PDK has:

- **Documentation**: technology details (layer thicknesses, materials), instructions for drawing the mask layout, and the **design rules** (what shapes the factory can and cannot make).
- **A library of cells**: ready-made components such as modulators and detectors.
- **Component models and/or measured data**: so you can simulate how each component behaves.
- **Design verification tools**: the scripts that check your design (DRC, LVS).

Real PDKs contain the foundry's secrets (exact recipes, measured performance), so they are usually under a non-disclosure agreement and not public.

### The Generic Silicon Photonics (GSiP) PDK

The authors built the **GSiP PDK** to show how a full silicon photonics design flow works, with no distribution limits. It runs in Mentor Graphics tools (Pyxis for drawing, Calibre for checking) and Lumerical INTERCONNECT (for circuit simulation), and can be downloaded. It is not tied to a real factory, but it can be adapted to one. It also gives a feel for what commercial PDKs offer.

Its pieces, in the order a designer uses them:

1. **Fabrication process parameters and mask layer table** — what the "virtual factory" makes (Tables 10.1 and 10.2 below).
2. **Library** — a small set of components: fibre grating couplers; waveguides, waveguide bends and a splitter; a ring modulator; and an electrical bond pad. Each component comes in three matching views:
    - a **symbol** for drawing schematics (you can also add your own components);
    - a **circuit model** in Lumerical INTERCONNECT, for simulation;
    - a **physical layout**, either a **fixed cell** (one fixed GDS drawing, e.g. the Y-branch splitter) or a **PCell** (drawn by a script from parameters, e.g. the ring modulator).
3. **Schematic capture** — drawing the system as connected symbols. You define the connections (the netlist), name components and ports, and pick PCell parameters.
4. **Circuit simulations** — the schematic is exported as a netlist and loaded into INTERCONNECT. The component models come from the PDK; the connections come from the netlist. You set up a **test-bench** (a simulation set-up) to compute, for example, the optical transmission spectrum (how much light passes at each wavelength) or time-domain behaviour (how the signal looks over time). This shows whether the system works before anything is built.
5. **Schematic-driven layout (SDL)** — before modern EDA tools, designers drew polygons by hand and had to remember what connected to what. In SDL, the components and connections already exist from the schematic. They are imported and placed (automatically or semi-automatically), the required connections are shown on screen as guide lines, and the designer then routes the metal wires and optical waveguides, interactively or automatically. This is "place and route".
6. **Waveguide routing** — routing electrical wires is highly automated in electronics tools. Photonics needs extra care: smooth bends instead of sharp corners, different waveguide types, wide low-loss waveguides for long runs, and waveguide crossings.
7. **Design rule checking (DRC)** — checks the layout against foundry rules: minimum feature size, minimum spacing, inclusion and exclusion rules. The GSiP kit has basic rules for typical minimum sizes. DRC is about one question: *can the factory reliably make this?*
8. **Layout versus schematic (LVS)** — DRC does not notice if your circuit is *wrong*, only if it is *unmanufacturable*. LVS reads the layout, recognises the components and connections in it, builds a netlist from the drawing, and compares it with the schematic's netlist. It catches:
    - **net errors**: broken waveguides or metal wires, unconnected optical or electrical ports, accidental crossings of connections;
    - **component errors**: missing components, the wrong component placed, wrong PCell parameters (e.g. a ring with the wrong radius).
9. **Tiling** — foundries require that the patterns on each layer cover a roughly even fraction of the area (a **density rule**). To meet it, small dummy squares (**tiles**) are added to empty areas, mostly on the silicon and metal layers. Two reasons: (a) **CMP** polishing removes material faster where there is less of it, so uneven density makes the wafer surface uneven; (b) etching works most consistently when the etched fraction is as uniform as possible, which reduces variation in the finished devices. The GSiP kit does not include a tiling script, because tiling scripts are written in a proprietary language.
10. **Sub-system design example and tutorial** — a complete two-channel WDM optical transmitter using ring modulators. It includes the schematic, circuit simulations (optical spectra and eye diagrams), schematic-driven layout, DRC, LVS, and **post-layout extraction** (reading real waveguide lengths back from the layout into the simulation).
11. **Electronic/photonic co-design** — the kit has both a generic photonic technology and a generic electronic (CMOS) technology, so two separate chips (one optical, one electronic) can be designed together. The tools pass data between the electrical and optical simulations. For example:
    - design a CMOS **modulator driver** circuit, simulate it, and feed its output voltage waveform into the modulator simulation;
    - at the receiver, the light reaching the detector becomes a **photocurrent**, which is fed into a **trans-impedance amplifier (TIA)** — a circuit that turns a small current into a usable voltage.

    This lets you design a complete CMOS → photonics → CMOS link (transmitter and receiver). Either generic kit can be swapped for a real foundry kit, so you can choose different factories for the two chips. The limitation: it is **data exchange**, not **co-simulation**. Each simulator runs, then hands its result to the other. That is fine for one-way signal flow, but not for systems with feedback where optics and electronics must be solved together step by step ("lock-step, self-consistent"), such as a **microwave-photonic opto-electronic oscillator**, where light and electrical signals continuously drive each other in a loop.

**Figure 10.1 — An electrical design in Mentor Graphics: a CML driver schematic.** The figure shows a real electronic circuit drawn in Pyxis, to show that the same tool handles the electronic side of co-design. It is a three-stage **CML (current-mode logic) driver** — a fast amplifier that drives a modulator. Inputs `p_in`/`n_in` are a **differential pair** (the signal is carried as the difference between two wires, which rejects noise). Each stage is a pair of transistors with **inductors** (L1–L8) and resistors as loads. The inductors boost high-frequency response ("inductive peaking"), giving more bandwidth. A bias network on the left sets the currents, and power rails `VDD` (supply) and `VSS` (ground) appear at each stage. The title block shows the design is named `CML_Driver`, created in Pyxis in 2013. **Lesson:** photonic and electronic design live in the same EDA environment, which is what makes co-design possible. You do not need to understand the transistor details for this packet.

**Table 10.1 — GSiP fabrication process parameters.** Read each row as "the factory makes this layer with this thickness/depth or doping level".

| Parameter | Target value | What it means |
|---|---|---|
| Silicon thickness | 220 nm | Height of the top silicon layer = height of waveguides |
| Silicon etch 1 | 60 nm | Shallow etch for grating coupler grooves |
| Silicon etch 2 | 130 nm | Etch for rib waveguides (leaves a 90 nm slab) |
| Buried oxide thickness | 2000 nm | Glass layer under the silicon; keeps light from leaking into the substrate |
| Germanium thickness | 500 nm | Height of the Ge block used in detectors |
| Doping (N) | $5\times10^{17}$ cm$^{-3}$ | Light n-doping, inside the modulator where light travels |
| Doping (P) | $7\times10^{17}$ cm$^{-3}$ | Light p-doping, same purpose |
| Doping (N++) | $5\times10^{20}$ cm$^{-3}$ | Very heavy n-doping, for metal contacts |
| Doping (P++) | $1.9\times10^{20}$ cm$^{-3}$ | Very heavy p-doping, for metal contacts |

Notice the jump of about 1000× between light and "++" doping. Light doping is a compromise: enough carriers to change the index quickly, but not so many that they absorb the light. Heavy doping is used only near metal contacts, away from the light, to make a good low-resistance electrical connection.

> **Key takeaways:**
>
> - A PDK = documentation + rules + component library (symbol, model, layout) + verification tools.
> - The flow is: schematic → simulate → schematic-driven layout → route → DRC → LVS → (tiling) → send to factory.
> - DRC asks "can it be built?"; LVS asks "is it what I designed?".
> - GSiP also supports electronic/photonic co-design by exchanging data between simulators, but not true lock-step co-simulation.

### 10.1.1 Fabrication process parameters

> **In one sentence:** The kit uses the industry-standard 220 nm silicon layer, with a few etch depths each chosen for a particular job, a numbered list of mask layers, and a set of geometric rules.

#### Silicon thickness and etch

Different groups use different top-silicon thicknesses: 3 µm (e.g. Kotura), 300 nm (e.g. Luxtera), 260 nm (e.g. NRC), and 220 nm (e.g. IMEC, LETI, OpSIS, IME). Thicker silicon gives bigger, more forgiving waveguides; thinner silicon gives tiny, tightly confined waveguides that bend sharply. The GSiP kit uses the common 220 nm standard (Table 10.1).

With 220 nm silicon, several **etch depths** (how deep you cut into the silicon) are useful:

1. **Grating coupler etch**: a shallow etch of 60 nm (OpSIS) to 70 nm (IMEC) works best for grating couplers. Shallow grooves scatter light gently, so the light leaves over a patch about the size of the fibre's light spot.
2. **Rib waveguide etch**: a separate etch can make rib waveguides. Its depth is a **compromise**:
    - a *deeper* etch (thinner slab) holds the light more tightly, so **bends lose less light**;
    - a *shallower* etch (thicker slab) leaves more silicon for current to flow through, so the pn-junction modulator has **lower electrical resistance** (which makes it faster).

    GSiP's 130 nm etch leaves a 90 nm slab.

#### GDS layer map

Table 10.2 (shown in §10.1.2 below) lists every mask layer of the generic technology. They cover: etch and deposition for silicon and germanium, implants (doping) for electrically active devices, and metal layers. Extra "miscellaneous" layers are not printed as material; they help the software (checking, labelling, floorplanning).

#### Design rules

Design rules set limits on the geometry: minimum feature sizes, spacings, and so on. They are described in §10.1.6.

> **Key takeaways:**
>
> - 220 nm silicon is the most common platform; GSiP uses it.
> - Each etch depth serves a purpose: ~60–70 nm for gratings, a deeper partial etch for rib waveguides.
> - Rib etch depth trades bend loss (wants deep) against modulator resistance (wants shallow).

### 10.1.2 Library

> **In one sentence:** The library holds the building blocks, each with a schematic symbol and a matching (often parameterized) layout, such as a ring modulator whose radius, gap and doping offsets you can set.

Figure 10.2 shows schematic symbols from the library. A good example is the **parameterized double-bus racetrack modulator**. "Double-bus" means it has two straight waveguides next to the ring (one on each side); it can also be set up as a **point-coupled** ring (a plain circle touching the bus at one point). Its layout was shown earlier in the book (Figure 6.10). Its parameters are:

- **radius** of the ring;
- **directional coupler gap and length** — the spacing between ring and bus, and the length of the straight side-by-side section ($L_c$);
- **waveguide width**;
- dimensions of the **doped regions** (where the N, P, N++, P++ implants go);
- **pn-junction offset** — how far the p/n boundary sits from the centre of the waveguide.

Each parameter changes the behaviour: the radius sets which wavelengths resonate; the gap and $L_c$ set how strongly light couples in and out; the doping layout sets speed and loss.

**Figure 10.2 — Schematic symbols for library components.** Four symbols:

- **(a) Fibre grating coupler** `GC_TE1550_20`: a grey block (the grating) with a fibre line coming in at an angle. Port `opt_fiber` is the fibre side; `opt_wg` connects to the on-chip waveguide. The name encodes "Grating Coupler, TE polarization, 1550 nm, 20° fibre angle".
- **(b) Bond pad** `BondPad`: a red square with two ports, `off_chip` (to the outside world) and `on_chip` (to the circuit).
- **(c) Y-branch** `YBranch_R15_Open5_W500`: a Y-shaped splitter with input `opt_a1` and two outputs `opt_b1`, `opt_b2`. It splits light 50/50 (or combines two inputs). The name records its design values (the W500 likely refers to 500 nm waveguides).
- **(d) Ring modulator** `RingModulator` (instance `XRM3`): a circle over a straight bus waveguide with optical ports, plus three electrical pins `anode1`, `cathode`, `anode2` (the anode is the p-side, the cathode the n-side of the junction). Its parameter list: `r=23` (radius, µm), `Lc=10` (coupler length, µm), `wg_width=0.5` (µm), `gap=0.2` (µm), `dis_nn`, `dis_pp`, `dis_nnn`, `dis_ppp` = 1 (distances setting where the doped regions sit, µm), and `pn_offset=0` (junction centred in the waveguide).

**Lesson:** every component has a short symbol with named ports, and parameterized components carry their parameter values right on the schematic.

**Table 10.2 — GSiP GDS layer map.** Every shape in a GDS file sits on a numbered layer. This table says what each number means. Read the "GDS #" column as the number the software uses; the description says what will be made on the chip.

| Name | Description | GDS # |
|---|---|---|
| **Materials and etches** | | |
| Si | Full-thickness silicon; for waveguides and active devices | 1 |
| SiEtch1 | Silicon shallow etch; defines grating couplers | 2 |
| SiEtch2 | Silicon shallow etch; defines rib waveguides | 3 |
| SiEtch3 | Silicon deep etch; trench for edge coupling or cleaving | 4 |
| Ge | Germanium growth for detectors | 5 |
| OxEtch | Oxide etch; opens access down to the silicon waveguides | 6 |
| **Implants** | | |
| N | Doping (N) | 20 |
| P | Doping (P) | 21 |
| N+ | Doping (N+) | 22 |
| P+ | Doping (P+) | 23 |
| Npp | Doping (N++) | 24 |
| Ppp | Doping (P++) | 25 |
| GeN | Germanium N doping; for Ge detectors | 26 |
| GeP | Germanium P doping; for Ge detectors | 27 |
| Defect1 | Silicon defects; for ion-implanted defect-mediated detectors | 28 |
| **Metals** | | |
| VC | Contact via between N++/P++ silicon and Metal 1 | 40 |
| M1 | Metal 1, for wiring | 41 |
| V1 | Via 1, above Metal 1 | 42 |
| M2 | Metal 2, for wiring | 43 |
| VL | Last via, connecting M1 (or M2) to the last metal | 44 |
| ML | Last metal, for wiring and probe/bond pads | 45 |
| MLOpen | Opening above the last metal, so probes can touch it | 46 |
| **Miscellaneous** | | |
| M1KO | Tiling keep-out for M1 | 60 |
| M2KO | Tiling keep-out for M2 | 61 |
| MLKO | Tiling keep-out for ML | 62 |
| SiKO | Tiling keep-out for Si | 63 |
| fp | Design outline; for error checking and floorplanning | 63 (as printed; likely a typo for 64) |
| Dicing | Dicing lanes (where the wafer is sawn into chips) | 65 |
| Text | Text comments, not printed; used for automated measurements | 66 |
| DRCex | Exclusion layer: DRC is skipped inside it | 67 |
| devrec | LVS: device recognition layer | 68 |
| pinrec | LVS: pin recognition layer | 69 |
| fbrtgt | LVS: fibre target pin layer | 81 |
| bndtgt | LVS: electrical bond target pin layer | 82 |

How to make sense of it:

- **Materials and etches** (1–6) shape the silicon and germanium. SiEtch3 is a deep trench, used to make a clean chip edge for edge couplers or for **cleaving** (snapping the chip along a line).
- **Implants** (20–28) add dopants. The "+" levels sit between light and "++". **Defect-mediated detectors** use deliberately damaged silicon (by implanting ions) so that it absorbs some 1550 nm light, as an alternative to germanium.
- **Metals** (40–46) build the wiring stack: a **via** is a vertical plug connecting one layer to the one above. The path is: heavily doped silicon → VC → M1 → V1 → M2 → VL → ML (top metal, where pads are).
- **Miscellaneous** layers are instructions to software, not materials. **Keep-out** (KO) layers forbid tiling in an area — important near waveguides, because dummy tiles next to a waveguide would disturb the light. **devrec**, **pinrec**, **fbrtgt**, **bndtgt** help LVS find devices and pins (see §10.1.7).

> **Key takeaways:**
>
> - Library components carry parameters (e.g. ring radius, gap, coupler length, doping positions).
> - Each component has a symbol with named optical and electrical ports.
> - The GDS layer map assigns a number to every mask (etch, implant, metal) and to helper layers for checking and tiling.

### 10.1.3 Schematic capture

> **In one sentence:** You draw the system as connected symbols, label the chip's inputs and outputs, insert "pwg" waveguide placeholders to track lengths, and let the tool check the drawing.

Figure 10.3 shows the schematic of the example: a **two-channel optical transmitter**. You pick components from a symbol selector or by searching the library, then draw wires between them — both optical connections (waveguides) and electrical ones. The chip's interface (bond pads and grating couplers) is defined by naming each pin's net and adding input/output ports.

**Figure 10.3 — Schematic for the example system.** Reading left to right:

- Four grating couplers `X_GC1`–`X_GC4` (type `GC_TM1550_20`, a TM-polarization coupler) connect to external optical ports: `opt_ina` and `opt_inb` (two light inputs), `opt_test`, and `opt_output`.
- Two Y-branches (`XYJ_1`, `XYJ_2`, joined by the net `WG_MID`) combine the two input lights into one waveguide and also tap a copy to the test port.
- The combined light passes two **ring modulators in series**, `XRM1` then `XRM2`. Each ring is tuned to a different wavelength, so each one modulates only "its" channel. That is what makes it a 2-channel WDM transmitter.
- Each ring is wired to two bond pads: `XBP_1`/`XBP_2` (external pins `ch1a`, `ch1b`) for ring 1, and `XBP_3`/`XBP_4` (`ch2a`, `ch2b`) for ring 2. These carry the electrical data signals.
- Waveguide segments `PWG1`–`PWG7` are the "pwg" placeholders described below.

**Lesson:** a schematic shows the *logic* of the system — light flows from inputs, through combiners, past two modulators, to the output, while electrical drive comes down from pads — without any real geometry.

```
 ina --GC1--\                                    ch1a ch1b   ch2a ch2b
             Y--WG_MID--Y--> ring XRM1 ----> ring XRM2 ----> GC3 -- output
 inb --GC2--/           \
                          --> GC4 -- test
```

(The sketch is simplified; the exact Y-branch wiring is in Listing 10.1.)

Next, the schematic is updated by inserting **"pwg" waveguide devices** between components. A pwg is a placeholder that stands for "the waveguide that will connect these two parts". It serves three purposes:

- it lets the tool **track the total length** of each routed waveguide once the layout exists (light loss and delay depend on length);
- the layout tool uses it for **waveguide routing** and later for **post-layout extraction**;
- you can use it to set **routing constraints** (e.g. "this waveguide must be shorter than X") or give an **initial length estimate** for early simulations.

Finally, the schematic is checked and saved. Optical signals are drawn in a different colour from electrical ones. Rule checks make sure optical connections are **point-to-point** (one output to exactly one input — unlike an electrical wire, a waveguide cannot just branch; you need a splitter component) and run only between optical pins.

> **Key takeaways:**
>
> - The example is a 2-channel WDM transmitter: two inputs combined, two rings in series, one output, four electrical pads.
> - "pwg" devices represent waveguides so their real lengths can later be fed back into simulation.
> - The schematic checker enforces that optical links are point-to-point between optical pins.

### 10.1.4 Circuit export

> **In one sentence:** The schematic is written out as a SPICE-style text netlist (plus symbol positions) so the circuit simulator can rebuild and simulate exactly the same circuit.

Pyxis exports a **netlist** of the schematic (Listing 10.1). The format follows SPICE. How to read it:

- `.subckt WDM2 OPT_OUTPUT OPT_INB OPT_INA OPT_TEST CH2B CH2A CH1B CH1A` — the whole design is wrapped as one **sub-circuit** named `WDM2`, with its external terminals (4 optical, 4 electrical) listed. `.ends WDM2` closes it.
- Each following line is one component, in the form: **unique label**, then **the nets it connects to** (in the order of its ports), then **the library component name**, then any **parameters**.

For example:

```
XRM1 PWG5 PWG7 N$22 N$22 N$20 RingModulator r=23 w=0.5 gap=0.2 Lc=10
```

reads: "Component `XRM1` is a `RingModulator`. Its optical ports connect to nets `PWG5` (in) and `PWG7` (out). Its electrical pins anode1, anode2 both connect to net `N$22`, and the cathode to net `N$20`. Radius 23 µm, waveguide width 0.5 µm, gap 0.2 µm, coupler length 10 µm." `N$22` is an automatically named internal net — here it is the wire from bond pad `XBP_1` (line `XBP_1 CH1A N$22 BondPad`). `XRM2` is the same but with **r = 30 µm**, so it resonates at a different wavelength — the second channel. Two other example lines: `X_GC1 OPT_INA PWG2 GC_TM1550_20` (grating coupler from the external input to waveguide net PWG2) and `XYJ_2 WG_MID PWG2 PWG3 YBranch_R15_Open5_W500` (Y-branch joining PWG2 and PWG3 into WG_MID).

Only PCells such as `RingModulator` carry extra parameter values at the end of their line (the book's example: `r = 30`). Fixed cells such as the Y-branch, bond pad and grating coupler need none.

The key design idea: the **library component name** (e.g. `YBranch_R15_Open5_W500`) is the same everywhere — symbol, simulation model, and layout. That single shared name is what ties the three views together.

For simulation, the netlist is imported into Lumerical INTERCONNECT. So that the circuit looks the same on screen there, the **instance positions** are also exported (Listing 10.2). Each line gives: the component type, its label, an x and y position on the schematic sheet, a rotation angle (0 or 90 degrees), and a true/false flag (likely whether the symbol is mirrored). For example `RingModulator XRM1 -1.25 0.25 0 @false`. Ports are listed as `portin` (inputs `opt_ina`, `opt_inb`), `portout` (`opt_test`, `opt_output`) and `portbi` (bidirectional electrical ports `ch1a`…`ch2b`, rotated 90°). These positions only affect the drawing, not the physics.

This first netlist does **not** include the pwg waveguides. They can be included in the export if you want the simulation to account for waveguide lengths.

> **Key takeaways:**
>
> - The netlist is SPICE-style text: label, connected nets, component name, parameters.
> - One shared component name links symbol, simulation model and layout.
> - Ring XRM1 (r = 23 µm) and XRM2 (r = 30 µm) differ in radius, so they handle different wavelengths.
> - Positions are exported only so the simulator's schematic looks the same.

### 10.1.5 Schematic-driven layout

> **In one sentence:** The tool places the schematic's components into the layout for you, you arrange them with testing in mind, draw rough routes, and a "Make PWGs" function turns those rough routes into real waveguides with smooth low-loss bends, S-bends, low-loss wide sections and crossings.

#### Placing the components

A new layout is created from the schematic's connectivity. Schematic and layout are open side by side. The **"AutoInst"** function places the schematic components into the layout semi-automatically, usually in groups (first all modulators, then all pads, then all grating couplers). AutoInst tries to keep the same relative positions and orientations as in the schematic. Then **alignment tools** line up waveguide ports exactly horizontally or vertically. Why? If two ports are perfectly in line, a straight waveguide joins them; if they are slightly offset, you need an **S-bend**, which costs space and adds a little loss. The result is Figure 10.4.

This is also the moment to think about **testing** ("design for test", covered in Section 12.3 of the book). The most critical choice is where the optical inputs/outputs sit relative to the electrical pads, because fibres and electrical probes are physical objects that must both reach the chip without colliding. (Listing 10.3, shown later, is related: it is the netlist after the layout's real waveguide lengths are extracted.)

**Figure 10.4 — Layout before routing.** A top view of the chip drawing. On the left, four grating couplers in a column (`opt_test`, `opt_ina`, `opt_inb`, `opt_output`), each in a dashed bounding box. In the middle, the two racetrack ring modulators (the second one larger, since it has the larger radius), drawn with coloured layers for silicon, doping and metal. Along the top, four large pad areas `ch1a`, `ch1b`, `ch2a`, `ch2b`. Thin lines (called **flylines** or "rat's nest" lines in EDA) show which ports *should* be connected, straight from point to point, ignoring geometry. **Lesson:** at this stage the parts are placed and the required connections are known, but no real wires or waveguides exist yet.

#### Routing

Next, the designer routes electrical and optical connections with Pyxis's **"IRoute"** interactive routing tool. It creates **path objects** (lines with a width) for both kinds of connection. At first, the optical routes have sharp 90° corners, just like metal wires (Figure 10.5).

**Figure 10.5 — Layout after routing.** Same chip, now with real connections. Cyan lines are optical routes from the grating couplers to the rings and from the rings to the output. Magenta lines are metal tracks from the four top pads (`ch1a/b`, `ch2a/b`) down to each ring's electrical contacts. Ports are now labelled `test`, `ina`, `inb`, `output`. **Lesson:** after routing, everything is connected — but the optical paths still have sharp corners, which light cannot follow well. That is fixed next.

#### Turning routes into real waveguides: "Make PWGs"

The **"Make PWGs"** function converts the rough optical paths into proper waveguides. It handles four things.

**1. Waveguide bends.** A metal wire can turn a sharp 90° corner (Figure 10.6a) — electrons follow the metal. Light cannot: at a sharp corner most of it would scatter away. So optical waveguides need **smooth bends**, either:

- a **radial bend**: a quarter circle with constant radius (Figure 10.6b); or
- an **adiabatic bend**, whose curvature changes gradually, such as a **Bézier curve** (Figure 10.6c).

The right choice depends on what you need (insertion loss, **back-reflections** — light bouncing back toward the source), the waveguide type, the wavelength, and the polarization (TM modes need larger bend radii, because they are less tightly confined). The PDK lets the designer choose the radius and the bend type (radial or Bézier), for each waveguide type (strip or rib).

**Figure 10.6 — Possible 90° bends.** Three blue shapes turning from horizontal to vertical: (a) an L-shaped sharp corner, fine for metal routing; (b) a quarter-circle arc, with constant curvature, its centreline dashed; (c) an adiabatic Bézier bend, which starts almost straight, curves most strongly near the middle, and straightens out again. **Lesson:** light needs smooth turns, and turns whose curvature changes gradually are even better.

```
 (a) metal corner     (b) circular arc       (c) adiabatic Bezier
   ______              ____                  ___
  |                   /                     /         curvature: 0 at ends,
  |                  |                     |          largest in the middle
  |                  |                     |
```

**What is a Bézier curve?** It is a smooth curve defined by a few **control points**. A cubic Bézier curve uses four points $P_0, P_1, P_2, P_3$:

$$
B(t) = (1-t)^3 P_0 + 3(1-t)^2 t \, P_1 + 3(1-t) t^2 \, P_2 + t^3 P_3, \quad 0 \le t \le 1
$$

Here $t$ runs from 0 (start) to 1 (end), and $B(t)$ is the point on the curve. The curve starts at $P_0$ heading toward $P_1$, and ends at $P_3$ arriving from the direction of $P_2$. It does not pass through $P_1$ and $P_2$; they "pull" the curve toward them, like magnets. The weights $(1-t)^3$, $3(1-t)^2 t$, etc. always add to 1, so each point on the curve is a weighted average of the control points. For a 90° bend, $P_0$ and $P_3$ are the start and end, $P_1$ lies straight ahead of the start, and $P_2$ lies straight back from the end. Moving $P_1$ and $P_2$ changes the shape. The book's single **Bézier parameter** controls this placement, so one number sweeps through a family of bend shapes.

Why does this help? Recall **mode-mismatch loss**: at a straight-to-arc junction, the curvature jumps suddenly from zero to $1/R$, and the light's pattern has to jump too. A Bézier bend starts with zero curvature (matching the straight waveguide), increases it gradually, then decreases it back to zero. The light pattern can follow smoothly, so less light is scattered.

**Figure 10.7 — Bézier bend paths, L = 3 µm.** A plot of six bend shapes, all starting at (0, 0) heading right and ending at (3, 3) heading up (units µm; $L$ = 3 µm is the size of the bend), for Bézier parameter = 0, 0.1, 0.2, 0.3, 0.4, 0.45. With parameter 0, the path hugs the x-axis for a long time (y ≈ 0.1 at x = 2.5) and then turns very sharply near the corner at (3, 0) — it stays nearly straight, then crams most of the turning into a small region. As the parameter grows, the curve spreads the turn more evenly (at x = 2.5, y ≈ 0.4, 0.8, 1.1, 1.5, 1.8 for 0.1 to 0.45). At 0.45, the shape is approximately a normal circular arc. **Lesson:** one number tunes the bend from "nearly an arc" to "very non-uniform curvature", with the same start and end points.

**Figure 10.8 — Simulated loss of Bézier bends (3D FDTD), L = 3 µm and L = 5 µm.** The horizontal axis is the Bézier parameter (0 to 0.5). The vertical axis is the bend loss on a logarithmic scale ($10^{-3}$ to $10^{0}$). Both curves are for TE light at 1550 nm in strip waveguides. Both are **U-shaped**:

| Bend size $L$ | Loss at parameter 0 | Best parameter | Loss at best | Loss at 0.45 (≈ arc) |
|---|---|---|---|---|
| 3 µm | ≈ 0.4–0.5 | ≈ 0.3 | ≈ 0.012 | ≈ 0.04 |
| 5 µm | ≈ 0.04 | ≈ 0.2 | ≈ 0.002 | ≈ 0.02 |

Read the table row by row: start at parameter 0 (very uneven curvature, so the tightest part of the turn is too tight and leaks light), go down to an optimum, then rise again toward the plain arc (0.45), where the sudden curvature jump at the ends causes mode mismatch. The best Bézier bend has about 3× (3 µm) to 10× (5 µm) lower loss than the arc of the same size. A bigger bend (5 µm) is always better than a smaller one (3 µm), because its curvature is gentler everywhere. The caption notes that parameter 0.45 is approximately a conventional constant-radius arc. **Lesson:** there is a sweet spot — vary curvature gradually, but not so unevenly that one part of the bend becomes too tight.

The text explains: as described in Section 3.3 of the book, for TE light in strip waveguides, **mode-mismatch loss dominates** bend loss. Varying curvature continuously reduces it, so an adiabatic Bézier 90° bend can have lower insertion loss than a constant-radius arc. These bends were simulated (TE, 1550 nm, strip waveguide) with the 3D FDTD method of Section 3.3.1. The Bézier parameter sweeps from a constant radius (0.45) to a "natural" Bézier curve. (The source text writes "Bézier = 0.45" for both ends of this range — clearly a typo; from the figures, 0.45 is the arc and smaller values are the more strongly Bézier-shaped curves.) Figure 10.8 shows much lower losses for the Bézier bends.

How good is this in practice? The **best 5 µm Bézier bend performs like a 20 µm-radius circular bend**, and the **best 3 µm Bézier bend performs like a 6 µm-radius circular bend** (compare Figure 3.28a of the book). So for the same allowed loss, Bézier bends are much more compact — a 5 µm bend instead of 20 µm saves a lot of area when there are hundreds of bends. The designer must pick the parameter to suit how the waveguide is used.

Important exception: for **TM polarization**, adiabatic bends help little. TM light is weakly confined, so its main bend loss is **radiation** (leaking out), not mode mismatch. Smoothing the curvature does not stop leakage; only a larger radius does.

**2. S-bends.** An **S-bend** smoothly joins two straight waveguides that are parallel but offset sideways (like a lane change on a highway). "Make PWGs" can insert them automatically when needed.

**3. Automated augmented waveguides.** For long optical routes, you want lower loss. Narrow strip waveguides lose light mainly by **scattering from sidewall roughness**: the etched sides are never perfectly smooth, and the narrower the waveguide, the more light touches the sides. A **wide waveguide** keeps most of the light away from the sidewalls and loses much less. So the trick is: use narrow **strip** waveguides in the **bends** (where tight confinement is needed), and switch to **wide rib** waveguides for the **long straight runs**, joined by gradual **tapers** (slowly changing width, so the light adjusts without loss). Reported numbers:

| Wide waveguide | Width | Loss | Source |
|---|---|---|---|
| Single-mode | 700 nm | 0.27 dB/cm | Bogaerts & Selvaraja |
| Multi-mode, passive-only process | 3 µm | 0.026 dB/cm | Li et al. |
| Multi-mode, full-flow process | 3 µm | 0.75 dB/cm | Li et al. |
| IME full-flow, measured | 3 µm rib, 5 µm slab | < 0.06 dB/cm | IME-fabricated devices |

A **passive** process makes only waveguides (no doping or metal); a **full-flow** process includes all steps (doping, metal, germanium), and extra steps can add loss (e.g. 0.75 vs 0.026 dB/cm for the same design). Even so, the IME full-flow 3 µm rib achieved below 0.06 dB/cm. Worked example: a 1 cm route at 0.06 dB/cm loses 0.06 dB — about 1.4% of the light. That is tiny.

Why can a multi-mode (3 µm) waveguide be used? Because the light enters it through a slow taper in its fundamental mode and travels straight; without sharp disturbances, it stays in that one mode. The bends, where higher modes would be excited, are done in the narrow single-mode strip.

The PDK can apply this augmentation automatically. Its parameters: a **length threshold** (only straight sections longer than this get widened, since short sections are not worth the taper overhead), the **taper length**, and the **wide waveguide width**. Figure 10.9 shows the result.

**Figure 10.9 — Layout with optical paths converted into waveguides.** The same chip as Figure 10.5, but the cyan optical routes are now real waveguides with curved bends. Small rectangles along the straight input section are visible (most likely the tapers into and out of a widened section, or small taps/monitors — the book points to this figure when discussing augmentation). The long route to the `output` coupler and the connections between couplers and rings are visible; pads `ch1a/b` connect to the first ring and `ch2a/b` to the second. **Lesson:** "Make PWGs" turns a sketchy route into a manufacturable, low-loss optical path.

**4. Waveguide crossings.** Unlike electrons in wires, photons in two crossing waveguides pass through each other without interacting. Two metal wires that cross would short-circuit, so electronics needs several wiring layers stacked with insulation between them. Photonics can cross waveguides in a **single layer**, which keeps fabrication simple — good, because building multi-layer photonic circuits is hard. (The source text says crossings mean fabrication "does require multi-layer routing"; from context it means "does *not* require".) A plain intersection would still scatter some light, so special **low-loss, low-cross-talk crossings** have been designed and built (typically by widening the waveguide at the crossing so the light passes the junction as a narrow beam). They are used in routing and even inside devices such as ring resonators. The designer adds crossings by hand, like any other component.

#### Post-layout extraction

**Listing 10.3 — Netlist after extracting waveguide lengths.** This is Listing 10.1 again, but now each pwg waveguide appears as a component with its real length taken from the layout. For example:

```
X_PWG4 PWG4 PWG4_PWG pwg wg_length=727.516 wg_width=0.5
```

means "a 727.5 µm long, 0.5 µm wide waveguide between nets PWG4 and PWG4_PWG". The listed lengths (µm) are: PWG5 36.95, WG_MID 36.95, PWG4 727.516 (the long run to the output coupler), PWG3 96.279, PWG2 96.279, PWG1 314.716, PWG7 121.25. The other components are rewired to the new "_PWG" nets so the waveguides sit between them. Re-simulating with these lengths gives a more realistic prediction (extra loss and delay). Note that PWG2 and PWG3, the two input arms, have identical lengths (96.279 µm), which keeps the two inputs balanced.

> **Key takeaways:**
>
> - AutoInst places components; alignment avoids unnecessary S-bends; placement must consider how fibres and probes will reach the chip.
> - Routes start with sharp corners and are converted to real waveguides by "Make PWGs".
> - Bézier (adiabatic) bends cut mode-mismatch loss for TE light: a 5 µm Bézier bend ≈ a 20 µm arc; a 3 µm one ≈ a 6 µm arc. They don't help TM (radiation-limited).
> - Long routes switch to wide rib waveguides (down to < 0.06 dB/cm) via tapers; photons can cross in one layer using special crossings.
> - Post-layout extraction feeds real waveguide lengths back into simulation.

### 10.1.6 Design rule checking

> **In one sentence:** DRC automatically checks every shape against the foundry's geometric limits (size, spacing, inclusion, density), either live while you draw or on the whole chip before sign-off.

Why rules at all? Lithography and etching are not perfect. A line that is too thin may not print, or may break; two shapes too close together may merge; a contact via that is not fully inside the silicon below it may miss. The foundry knows its limits from experience and writes them as rules. Following them gives a design that **yields** well (most chips come out working).

There are three main rule types (Figure 10.10):

- **Minimum feature size (width)**: no shape may be narrower than a set value.
- **Minimum spacing**: two shapes on the same layer may not be closer than a set value.
- **Minimum inclusion (enclosure)**: a shape on one layer must sit inside a shape on another layer with a set margin, e.g. a contact via must be inside the silicon, not hanging over the edge.

Other rules also matter, such as **density rules** (the minimum/maximum fraction of area covered on a layer — see tiling in §10.1). (The source sentence listing additional rules is cut off after "density rules".)

**Figure 10.10 — Types of DRC rules.** Three small drawings: (a) one blue silicon rectangle with an arrow across its width labelled "min" — the width must be at least the minimum; (b) two silicon rectangles with an arrow across the gap labelled "min" — the gap must be at least the minimum; (c) an orange "VC" (contact via) box drawn inside a larger silicon area, with a "min" arrow — the via must meet a minimum size and be properly enclosed in the silicon. **Lesson:** most DRC rules are just distances measured inside a shape, between shapes, or between layers.

```
 (a) width        (b) spacing          (c) inclusion
 |<-min->|       ____ |<min>| ____     ____________
 [  Si   ]      [ Si ]       [ Si ]   | [VC]   Si  |
                                       |____________|
```

**Listing 10.4 — Example Calibre DRC rules.** Two rules for the silicon layer:

```
Si.Width {
@ Si layer: Width, minimum: 0.2
OUTSIDE ( INT Si < 0.2 REGION) DRCex
}
```

How to read it: `INT Si < 0.2` measures the *interior* distance across every silicon shape and flags places narrower than 0.2 µm (200 nm). `OUTSIDE ... DRCex` keeps only errors that lie outside the `DRCex` layer. The `@` line is the message shown to the user. The second rule, `Si.Space`, is the same with `EXT` (the *exterior* distance between separate shapes): silicon shapes must be at least 200 nm apart.

So in this kit, both **minimum silicon width and minimum silicon spacing are 200 nm**. The **DRCex** exclusion layer lets a designer switch the rules off in a marked area — useful for special experimental structures where you knowingly break a rule (at your own risk). A real foundry's rule file can have **hundreds** of rules.

**Figure 10.11 — Interactive DRC.** Two screenshots of the layout editor. (a) The designer has drawn a curved waveguide too close to a rectangular block; a red outline marks the problem area with the message "Min. Space 0.100". (b) The designer moves the shape; the red flag disappears. **Lesson:** errors can be caught and fixed the moment they are made. (This screenshot uses a 0.100 µm spacing rule, a different value from the 0.2 µm example in Listing 10.4.)

The checker has **two modes**:

1. **Interactive**: while you draw, the tool checks the part of the layout you are editing and viewing, and marks errors on screen right away (Figure 10.11). It only checks this small region, so it is fast.
2. **Sign-off verification**: the full layout is exported and checked completely. Errors are reported as a list and shown graphically. "Sign-off" means this is the final check before the design is sent to the foundry.

> **Key takeaways:**
>
> - The three basic rule types: minimum width, minimum spacing, minimum inclusion; plus density rules.
> - In GSiP, silicon width and spacing must each be ≥ 200 nm; a DRCex layer can exempt special regions.
> - DRC runs interactively (local, instant) and as a full sign-off check.

### 10.1.7 Layout versus schematic

> **In one sentence:** LVS reads the drawn shapes, recognises which devices they are and how they connect, writes a netlist from the layout, and compares it with the schematic's netlist to catch wiring and component mistakes.

Steps of LVS:

1. **Parse** the layout file.
2. **Extract devices**: find known devices (ring modulator, grating coupler, etc.) among the shapes.
3. **Find connectivity**: work out which device pins are joined by waveguides or metal.
4. **Write a netlist** from the layout.
5. **Compare** it with the original schematic netlist and report differences.

Recognising devices from raw polygons is hard, so the PDK uses **recognition layers** (from Table 10.2) to help:

- **devrec** (device recognition): a polygon marking the outline of each device, plus a text label naming it (e.g. "RingModulator").
- **pinrec** (pin recognition): marks the position and name of each pin, both electrical (e.g. `anode1`, `anode2`, `cathode`) and optical (e.g. `opt_a2`, `opt_b2`).

The tool then applies **logical operations** (like "find all Si shapes inside this devrec outline") to find each device's geometry, and makes **measurements** to extract its parameters (e.g. the gap in a directional coupler, or a ring's radius). Further operations trace connections between components. Because the parameters are measured, LVS can catch a ring drawn with the wrong radius, not just a missing ring.

**Listing 10.5 — LVS netlist extracted from the layout.** How to read it:

- The first blocks (`.SUBCKT RingModulator opt_a2 opt_b2 anode1 anode2 cathode` … `.ENDS`) are empty "black box" definitions. They only declare which pins each device type has: the ring modulator (2 optical + 3 electrical pins), the Y-branch (3 optical), the bond pad (`off_chip`, `on_chip`), and two grating coupler types (TM and TE, each with `opt_fiber` and `opt_wg`).
- The main block `.SUBCKT wdm2tx_routed ch1a ch1b ch2a ch2b opt_output opt_inb opt_ina opt_test` is the routed chip. The line `** N=71 EP=8 IP=0 FDC=12` is a summary from the tool: 71 nets, 8 external pins, 12 devices found.
- Each device line looks like `X0 4 7 56 56 57 RingModulator $X=288250 $Y=79700 $D=0`: device X0, connected to nets numbered 4, 7, 56, 56, 57, is a RingModulator, located at coordinates $X$, $Y$ (in layout database units, likely nanometres, so about (288 µm, 80 µm)), with `$D` an internal device-type index.
- The 12 devices found: 2 ring modulators (X0, X1), 2 Y-branches (X2, X3), 4 bond pads (X4–X7, all at the same $Y$ = 237000, i.e. in a row at the top), and 4 grating couplers (X8–X11, all at $X$ = −1700, i.e. in a column at the left edge).

Nets now have numbers instead of names, but the *structure* — which pins connect together — can be matched with the schematic. For example, ring X0's anodes share net 56, which goes to bond pad X4 on `ch1a`, exactly as XRM1's anodes share `N$22` to `XBP_1` on `CH1A` in Listing 10.1. If the two netlists match, the layout is correct; if not, LVS reports exactly what differs.

> **Key takeaways:**
>
> - LVS = extract devices + extract connections from the layout → netlist → compare with schematic.
> - devrec and pinrec layers mark device outlines/names and pin locations/names to make extraction reliable.
> - Measured parameters (gap, radius) let LVS catch wrong-parameter errors, not just missing parts.

## 10.2 Mask layout

> **In one sentence:** This section gives practical advice on drawing component layouts and arranging many test devices on a chip, either quickly (simple tiling) or compactly (shared waveguide bundles).

A **mask layout** is the full set of shapes, on all layers, that will be turned into the masks used in fabrication. The section discusses how to generate it in practice.

### 10.2.1 Components

> **In one sentence:** Simple components can be drawn by hand; complex ones are drawn by scripts as parameterized cells, so a designer just fills in a few numbers.

To build circuit layouts as in §10.1.5, you need a library of component layouts. There are two ways to make them:

- **Manual layout**: drawing basic shapes (polygons) by hand. Good for simple geometry, such as the edge couplers of the book's Figure 5.6 (essentially a tapered strip).
- **Scripted layout**: a program computes the shapes from parameters. Necessary for complex structures like **focusing grating couplers** (curved grooves, each at a precisely calculated position) or ring resonators (curves, doping regions, contacts all depending on the radius).

In Pyxis, parameterized components are written in the **AMPLE** scripting language. (An example grating coupler script is in the book's §5.2.3.) When the designer places one of these components, a dialog appears to choose its parameters (Figure 10.12).

**Figure 10.12 — Parameterized cell layouts.** Two dialog windows:

- **(a) Grating coupler**: parameters `Si_thickness = 0.22` (µm), `etch_depth = 0.07` (70 nm), `ff = 0.5` (**fill factor**: the fraction of each grating period that is left unetched, here half), incident angle `20` (degrees, the fibre tilt), `n_cladd = 1.44` (cladding index), `pl = TE` (polarization), `wg_width = 0.5` (µm), `wl = 1.55` (wavelength, µm). Below that are placement attributes (position Origin X = 27.25, Origin Y = 2.25, rotation 0, scale 1, flip none, area 1.28k µm²). Notice the script takes *physical* inputs (wavelength, angle, thicknesses, index) and computes the grating geometry itself — the designer does not draw grooves.
- **(b) Adiabatic 2×2 splitter**: a 3 dB coupler (splits light 50/50 between two outputs) made by slowly changing two waveguides' widths. Parameters: `wg1_width = 0.4`, `wg2_width = 0.6`, `wg_3dB_width = 0.5` (µm, label truncated), `l_coupler = 100` (µm, coupling length), `l_taper = 30` (µm), `wg_gap = 2` (µm), `coupler_gap = 0.2` (µm), `etch = SiEtch2` (rib), `layer = Si`. The dialog here is "Add array", which can place a grid of copies (Array Columns/Rows set to 0 here).

**Lesson:** PCells turn complex, error-prone geometry into a short form of physical and geometric numbers.

> **Key takeaways:**
>
> - Hand-draw simple parts; script complex ones as PCells.
> - PCells take inputs such as wavelength, angle, etch depth, widths, gaps and lengths, and generate the shapes.

### 10.2.2 Layout for electrical and optical testing

> **In one sentence:** A test device needs electrical probe pads and a pair of grating couplers placed far enough apart (about 1 mm) for the probe and the fibre array to fit, which sets its size (about 2.8 mm × 0.4 mm).

Figure 10.13a shows a single device ready for testing. It has **GS probe pads** (ground and signal) for electrical testing. Its waveguide runs to a distant **pair of grating couplers** — one input, one output — which are reached by a fibre array (Figure 10.13b). Figure 10.14 shows the whole test cell.

**Figure 10.13 — (a) Single device to be tested; (b) a pair of grating couplers.** (a) Two large hatched square pads at the top (GS pads), a long rectangular device between/below them, and magenta metal lines connecting them; a 50 µm scale bar shows the pads are tens of µm across. (b) Two grating couplers side by side at the bottom, each with a tapered region, whose waveguides bend and join into one route heading up toward the device; again a 50 µm scale bar. **Lesson:** each device has an electrical end (pads) and an optical end (a coupler pair), connected by waveguide.

**Figure 10.14 — Complete test cell.** A long, thin layout: electrical pads on the far left, grating couplers on the far right, joined by a long horizontal waveguide; a 200 µm scale bar. The caption: total size of the largest device is about **2.8 mm × 0.4 mm = 1.1 mm²**. Two things set this size:

1. the size of the device itself, or of the fibre array — here this sets the **height** (0.4 mm);
2. the **minimum separation between the optical and electrical probes**, plus their holders and mechanics — here this sets the **width** (2.8 mm).

**Lesson:** test equipment, not the device, often decides how much chip area a test structure needs.

The key choice is the **spacing between electrical and optical probes**. It depends on the actual test set-up. For the set-ups in the book's Section 12.2, **1 mm** is enough. (More "design for test" advice is in Section 12.3.)

> **Key takeaways:**
>
> - A test cell = GS electrical pads + device + waveguide to an input/output grating coupler pair.
> - Probe-to-fibre clearance (about 1 mm here) makes test cells large: about 2.8 mm × 0.4 mm ≈ 1.1 mm².

### 10.2.3 Approaches for fast GDS layout

> **In one sentence:** The quickest way is to draw each device separately and place them side by side ("tiling"), which is easy but wastes space.

The fastest method is to **tile** the devices: draw each one separately, then merge them side by side into one GDS file. This is ideal when time is short and you need many devices over a large area. (Note: this "tiling" means arranging devices, not the density-fill tiling of §10.1.)

You can save some space by **varying the dimensions** (e.g. making shorter devices shorter rather than all the same length) and **arranging them in L-shapes** so they nest together.

> **Key takeaways:**
>
> - Simple side-by-side tiling is fast but area-hungry.
> - Varying device lengths and using L-shaped arrangements recovers some space.

### 10.2.4 Approaches for space-efficient GDS layout

> **In one sentence:** By routing all devices to a shared, tightly packed bundle of waveguides and a compact array of grating couplers, 26 devices fit in 1.8 mm² instead of 20.7 mm² — 11.5× smaller.

To save space, the designer arranges devices and routes waveguides to minimise "white" (unused) space. This makes the waveguide routing more complex, so it is usually done by writing a script that generates the routing waveguides.

Saving space saves money (chip area is paid for), but there are **risks**:

- **Optical cross-talk**: light can leak between waveguides that run close together (directional coupling, Section 4.1.7 of the book). Waveguides must be far enough apart. For strip waveguides, **3 µm** separation is considered safe, giving negligible cross-talk over the distances on a chip. If unsure, decide what cross-talk you can tolerate and simulate the pair as a directional coupler. A second kind of cross-talk is between **grating couplers**: they must be far enough apart that light from one fibre does not enter the neighbouring coupler. With **single-mode fibres** (small light spot, about 10 µm) this rarely matters. With **multi-mode fibres** (large core), the coupler spacing should exceed the core size, e.g. **> 50 µm**.
- **Electrical cross-talk**: fast electrical signals in neighbouring devices can couple into each other. Careful **microwave design** is needed to prevent this and to suppress **microwave resonances** (unwanted standing waves in the metal structures) that could cause ripples or oscillations in the frequency response.
- **Measurement challenges**: unexpected practical problems may appear — for example, the optical and mechanical set-up may limit how close the fibres can get to the electrical probes.

#### Worked example: packing 26 devices

In a typical design cycle you make many versions of one device, each with a slightly different parameter. In this example, 26 devices were packed together. The method:

1. **Build a dense array of fibre-array optical probe pads** (grating couplers), with routing waveguides running *between* the couplers (Figure 10.15).
2. This can be extended to **16 pairs** of couplers, with all waveguides running between them to form a **waveguide bundle** — a tight group of parallel waveguides — that the devices connect to (Figure 10.16). The design used **3 µm centre-to-centre waveguide spacing**, enough to avoid cross-talk.
3. If more than 16 devices are needed, extra waveguides are routed **around the outside** of the couplers (Figure 10.17).
4. **Connect the devices to the bundle** (Figure 10.18). The left-most device connects to the left-most couplers, so that each device's electrical probe area is far enough from the couplers in use.
5. The final layout (Figure 10.19) has 26 devices on the right and 26 coupler pairs on the left.

**Figure 10.15 — Coupler array with routing between couplers.** Eight grating couplers in two rows of four; waveguides enter from the right and turn with 90° bends into each coupler, passing through the space between the rows. Scale bar 50 µm. **Lesson:** the gaps between couplers, normally wasted, can carry waveguides.

**Figure 10.16 — Sixteen coupler pairs feeding a bundle.** 32 couplers in two rows of 16. Each coupler's waveguide runs right; top-row waveguides bend down and bottom-row ones bend up, merging into one dense horizontal bundle between the rows. Scale bar 100 µm. **Lesson:** all optical I/O is collected into one compact bus that devices can tap.

**Figure 10.17 — Extra waveguides routed outside the couplers.** Two rows of four couplers with a dense bundle of roughly 20–25 parallel waveguides running through the middle; additional waveguides loop around the outside of the coupler rows. Estimated from the 50 µm scale: couplers about 25 µm square, about 100 µm apart, rows about 150 µm apart, bundle about 125 µm wide. **Lesson:** when the space between couplers is full, routing can continue around the outside.

**Figure 10.18 — Devices connected to the bundle.** Couplers on the left, the bundle running across with smooth 90° bends, and four device units (with large hatched pads) on the right, each tapping into the bundle. Scale bar 50 µm. **Lesson:** devices are placed in order so the closest-in device uses the farthest-out couplers, keeping optical probes and electrical probes well separated.

**Figure 10.19 — Full 26-device layout.** On the left, 26 pairs of grating couplers (52 squares) in two rows; in the middle, the routing bundle fans out in a funnel shape; on the right, 26 devices in a row. Scale bar 500 µm. Total area **4.7 mm × 0.4 mm = 1.8 mm²**. If laid out side by side without this approach: **20.7 mm²**. Compression factor:

$$
\frac{20.7 \text{ mm}^2}{1.8 \text{ mm}^2} \approx 11.5
$$

**Lesson:** sharing one compact optical I/O block among many devices shrinks the chip area by an order of magnitude.

Why such a big saving? In simple tiling, each device carries its own ~1 mm gap between probes and fibres, so every device costs about 0.8 mm² (20.7 mm² / 26 ≈ 0.8 mm²). In the bundle approach, that clearance is paid once for the whole group, and the waveguides squeeze into 3 µm-pitch bundles. Per device, the area is about $1.8 / 26 \approx 0.07$ mm².

> **Key takeaways:**
>
> - Dense layouts save money but risk optical cross-talk (keep strip waveguides ~3 µm apart; couplers > 50 µm apart for multi-mode fibre), electrical cross-talk, and test difficulties.
> - Route waveguides between and around a grating-coupler array to form a shared bundle; connect devices in order to keep probes apart.
> - 26 devices: 1.8 mm² instead of 20.7 mm², an 11.5× reduction.

## Looking ahead: Chapter 11 — Fabrication (opening paragraph)

> **In one sentence:** Real chips never come out exactly as drawn — silicon thickness and feature widths vary — and the next chapter is about designing with that in mind.

The packet ends with the start of Chapter 11. Its main points:

- **Manufacturing variability** affects silicon photonic circuits. The two dominant variations are **silicon thickness** (the 220 nm is never exactly 220 nm) and **feature size** (a 500 nm waveguide may come out a bit wider or narrower).
- These variations occur **from wafer to wafer** and also **within a single chip**.
- **Smoothing by lithography** matters too: sharp corners in the drawing come out rounded on the chip, because the printing process cannot reproduce perfectly sharp details.
- The chapter discusses how to include these variations in design, and shows measured results from on-chip test structures to illustrate how non-uniform manufacturing is.

Why it matters: devices like ring resonators are very sensitive. A few nanometres of width or thickness change shifts the resonance wavelength noticeably. So the clean design flow of this packet must be combined with an understanding of what the factory actually delivers.

> **Key takeaways:**
>
> - Thickness and width variation are the main manufacturing imperfections, across wafers and within chips.
> - Lithography rounds off sharp features.
> - Good design accounts for these variations.

## Glossary

| Term | Plain meaning |
|---|---|
| 3 dB coupler | A splitter that sends half the light to each of two outputs |
| Adiabatic | Changing slowly enough that light adjusts smoothly with no loss |
| AMPLE | Scripting language of the Pyxis tool, used to write PCells |
| Anode / cathode | The p-side / n-side electrical terminal of a pn junction |
| AutoInst | Pyxis function that places schematic components into the layout automatically |
| Back-reflection | Light bouncing back toward where it came from |
| Bézier curve | A smooth curve shaped by control points; used for low-loss bends |
| Bond pad / probe pad | Metal square where a wire is bonded or a probe needle touches |
| Buried oxide (BOX) | Glass layer under the top silicon in an SOI wafer |
| Calibre | Mentor Graphics tool for DRC and LVS checks |
| Cell / PCell | Reusable layout block / one drawn by a script from parameters |
| Cladding | Low-index material surrounding a waveguide core |
| CML driver | Fast current-mode-logic amplifier that drives a modulator |
| CMOS | The standard technology for making electronic chips |
| CMP | Chemical mechanical polishing: grinding the wafer flat |
| Co-design / co-simulation | Designing optics and electronics together / solving them together in lock-step |
| Compact model | Fast mathematical description of a component's behaviour |
| Cross-talk | Unwanted leakage of signal from one path into a neighbour |
| dB, dB/cm | Logarithmic loss unit; loss per centimetre of waveguide |
| Defect-mediated detector | Detector using deliberately damaged silicon to absorb light |
| Density rule | Rule on what fraction of an area a layer must cover |
| Design rules | Foundry's geometric limits (min width, spacing, inclusion...) |
| devrec / pinrec | Helper layers marking device outlines and pin positions for LVS |
| Dicing lane | Strip where the wafer is sawn into separate chips |
| Directional coupler | Two waveguides close together that exchange light |
| Doping (N, P, ++) | Adding atoms to silicon to make it conduct; "++" means very heavy |
| DRC | Design rule checking: can the factory build this layout? |
| DRCex | Layer marking areas where DRC is skipped |
| EDA | Electronic design automation: chip design software |
| Edge coupler | Couples light in through the chip's side edge |
| Etch depth | How deep silicon is cut away |
| Eye diagram | Overlay of signal slices; open eye = clean data |
| FDTD | Accurate full-wave light simulation on a grid in time |
| Fibre array | Row of optical fibres at fixed spacing |
| Fill factor (ff) | Fraction of each grating period left unetched |
| Fixed cell | Layout block with one fixed drawing |
| Flyline | Straight guide line showing a connection still to be routed |
| Foundry | Factory that makes chips for outside designers |
| Full-flow process | Process with all steps (doping, metal, Ge), not just waveguides |
| GDS (GDSII) | Standard layout file format with numbered layers |
| Germanium (Ge) | Material that absorbs 1550 nm light; used in detectors |
| Grating coupler | Etched grooves that couple light between chip and fibre above |
| GS pads | Ground-Signal probe pad pair for high-speed electrical testing |
| GSiP PDK | Generic Silicon Photonics PDK, a free teaching kit |
| Insertion loss | Total loss a component adds to the light path |
| Instance | One placed copy of a component |
| INTERCONNECT | Lumerical's photonic circuit simulator |
| IRoute | Pyxis interactive routing tool |
| Ion implantation | Firing dopant atoms into silicon through a mask |
| Keep-out (KO) layer | Marks areas where tiling is not allowed |
| Layout | The actual shapes on each mask layer, at real size |
| Lithography | Printing patterns onto the wafer using light and masks |
| LVS | Layout versus schematic: is the layout the circuit I designed? |
| Make PWGs | Function turning rough optical routes into real waveguides |
| Mask | Stencil defining where one process step acts |
| Mode | A stable light pattern that travels unchanged in a waveguide |
| Mode-mismatch loss | Loss where waveguide shape changes suddenly and light patterns don't match |
| Modulator | Device that puts data onto light |
| Net / netlist | One connection / text list of all components and connections |
| Passive process | Process making only waveguides, no active parts |
| Photodetector | Turns light into electrical current |
| Place and route | Placing components, then drawing connections |
| pn junction | Boundary between p-type and n-type silicon |
| Polarization (TE/TM) | Direction of light's electric field: sideways (TE) or vertical (TM) |
| Port / pin | Connection point of a component |
| Post-layout extraction | Reading real lengths/values from the layout back into simulation |
| pwg | Placeholder component for a routed waveguide, tracks its length |
| Pyxis | Mentor Graphics schematic and layout editor |
| Process design kit (PDK) | Foundry's documentation, rules, library and checking tools |
| Racetrack | Ring resonator stretched with straight sections |
| Radial bend | Bend shaped as a circular arc of constant radius |
| Radiation loss | Light leaking out of a too-tight bend |
| Refractive index | How much slower light is in a material than in vacuum |
| Rib waveguide | Partially etched waveguide sitting on a thin slab |
| Ring resonator | Waveguide loop that selects certain wavelengths |
| S-bend | Smooth sideways jog between two offset parallel waveguides |
| Schematic | Diagram of components and connections (no real geometry) |
| Schematic-driven layout (SDL) | Layout built from the schematic's parts and connections |
| Sign-off verification | Final full-chip check before sending to the factory |
| Single-mode / multi-mode | Carries one light pattern / several |
| SOI | Silicon-on-insulator wafer: thin silicon on oxide |
| SPICE | Classic circuit simulator; its netlist format is widely used |
| Strip waveguide | Fully etched rectangular silicon waveguide |
| Subcircuit (.subckt) | A named block in a SPICE netlist with its own terminals |
| Taper | Section where waveguide width changes gradually |
| Test-bench | Simulation set-up that applies inputs and measures outputs |
| Tiling (density fill) | Adding dummy squares to meet density rules |
| Tiling (device) | Placing separately drawn devices side by side |
| Trans-impedance amplifier (TIA) | Circuit turning small photocurrent into a voltage |
| Via | Vertical metal plug joining two layers |
| Waveguide | Light-guiding strip, like a pipe for light |
| Waveguide bundle | Group of closely spaced parallel waveguides |
| Waveguide crossing | Junction where two waveguides cross in the same layer |
| WDM | Wavelength division multiplexing: several channels on different colours |
| Yield | Fraction of fabricated chips that work |
| Y-branch | Y-shaped splitter/combiner |

## Check yourself

1. **What four kinds of things does a PDK typically contain?**

    *Answer:* Documentation (technology details, layout instructions, design rules); a library of cells; component models and/or measured data; and design verification tools (DRC, LVS).

2. **What is the difference between DRC and LVS?**

    *Answer:* DRC checks whether the layout obeys the foundry's geometric rules, so it can be manufactured. LVS checks whether the layout's devices and connections match the schematic, so it is the intended circuit. A layout can pass DRC and still be wrong (e.g. a broken waveguide or a ring with the wrong radius).

3. **Why does the rib-waveguide etch depth have to be a compromise?**

    *Answer:* A deeper etch holds light more tightly and reduces bend loss; a shallower etch leaves a thicker slab and lowers the electrical resistance of pn-junction modulators. You cannot have both fully.

4. **In the line `XRM2 PWG7 PWG4 N$28 N$28 N$30 RingModulator r=30 w=0.5 gap=0.2 Lc=10`, what is XRM2 and why does its radius differ from XRM1's (23 µm)?**

    *Answer:* XRM2 is a ring modulator connected to optical nets PWG7 and PWG4 and electrical nets `N$28` (both anodes) and `N$30` (cathode), with radius 30 µm, width 0.5 µm, gap 0.2 µm and coupler length 10 µm. A different radius gives a different resonant wavelength, so each ring modulates its own WDM channel.

5. **Why can an adiabatic Bézier bend have lower loss than a circular arc of the same size, and why doesn't this help TM light?**

    *Answer:* For TE light in strip waveguides, bend loss is mostly mode mismatch at the sudden curvature change where straight meets arc. A Bézier bend starts and ends with zero curvature and changes gradually, so the light adjusts smoothly. TM light's bend loss is mostly radiation (leakage), which smoothing does not fix; only a larger radius helps.

6. **Using Figure 10.8, roughly how much better is the best 5 µm Bézier bend than a 5 µm arc, and what circular bend is it equivalent to?**

    *Answer:* About 10× lower loss (≈ 0.002 vs ≈ 0.02 on the plot), and it performs like a 20 µm-radius circular bend.

7. **A route is 2 cm long. Compare the loss with a 0.27 dB/cm single-mode wide waveguide and a < 0.06 dB/cm 3 µm rib waveguide.**

    *Answer:* 0.27 × 2 = 0.54 dB (about 12% of the light lost) versus less than 0.06 × 2 = 0.12 dB (under about 3% lost). The wide multi-mode rib is much better for long runs.

8. **Why can photonic circuits route in a single layer when electronic circuits need multiple wiring layers?**

    *Answer:* Light beams in crossing waveguides pass through each other without interacting, so a well-designed crossing works in one layer. Crossing metal wires would short-circuit, so electronics needs stacked, insulated metal layers.

9. **What sets the 2.8 mm × 0.4 mm size of the test cell in Figure 10.14?**

    *Answer:* The height is set by the device (or fibre array) size; the width is set by the minimum distance between the optical fibres and the electrical probes plus their mechanics (about 1 mm is needed for the set-ups in the book).

10. **How does the waveguide-bundle approach achieve an 11.5× area reduction, and what spacing keeps the bundle free of cross-talk?**

    *Answer:* Instead of each device having its own couplers and its own probe clearance (20.7 mm² for 26 devices), all 26 devices share one compact coupler array and a tightly packed bundle of waveguides (1.8 mm²); 20.7 / 1.8 ≈ 11.5. A 3 µm centre-to-centre spacing between strip waveguides keeps cross-talk negligible.
