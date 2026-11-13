# MOLONARI waterproof box

This folder contains everything related to the **MOLONARI sensor box**: its design, how to build it and how to install it in the field.

The box is 3D printed. It protects the sensor's electronics while it is submerged in the river, lets the temperature probes pass through, and puts the pressure transducer in contact with the water.

📷 *[TO BE COMPLETED: photo of the assembled box]*

---

## How this folder is organized

The folder is split into three parts: **building** the box, **deploying** it in the field, and the **tests** that led us to the current version. Each subfolder is self-contained and has its own README.

```
boite/
├── README.md          ← you are here: general overview
├── fabrication/       ← how to BUILD the box
├── tests/             ← prototypes and test parts
└── deploiement/       ← how to INSTALL the box in the field
```

### 📁 `fabrication/`: building the box

For anyone who needs to **produce a box**, from scratch or as a replacement. This folder contains:

- the **design files** (Onshape link, editable STEP files, ready-to-print STL files);
- the **print settings** for the parts and the molds;
- how to **make the seals** from cast silicone (molds, mixing, casting, demolding);
- step-by-step **assembly** of the box;
- the **watertightness test procedures**;
- **lessons learned**: what we tried, what didn't work and why.

➡️ [Go to fabrication](fabrication/README.md)

### 📁 `deploiement/`: installing the box in the field

For anyone who has **a ready box** in its carrying case and needs to install it in the river. This folder contains:

- the **case contents** and preparation before leaving;
- **step-by-step installation** (rod, ballast, submersion) and final checks;
- **retrieval** of the box and **troubleshooting**;
- a printable **deployment sheet**.

➡️ [Go to deployment](deploiement/README.md)

### 📁 `tests/`: our prototypes and test parts

To **understand how we arrived at the current box**, or to **retest a solution** before modifying the box. This folder contains:

- the **previous version of the box** (v1), with the Onshape models of all its parts: complete box, seal molds, calibration plugs, barbed fitting;
- the **test parts**: small printed parts used to validate a solution (closing seal, probe seal…) before printing the complete box.

> ⚠️ These parts are **not meant to be printed to build the box**. For that, go to [`fabrication/`](fabrication/README.md).

➡️ [Go to tests](tests/README.md)

---

## Where to start?

| You want to… | Go to |
|---|---|
| Understand how the box is designed | [Overview](#overview-of-the-box), just below |
| Build a new box | [`fabrication/`](fabrication/README.md) |
| Modify the box (different sensor, different board…) | [`fabrication/`](fabrication/README.md), CAD section |
| Install a box that is already built | [`deploiement/`](deploiement/README.md) |
| Find out why a design choice was made | [`fabrication/`](fabrication/README.md), lessons learned |
| See previous versions or redo a test | [`tests/`](tests/README.md) |

---

## Overview of the box

The box is made of **three parts**:

| Part | Role | Closure |
|---|---|---|
| **Upper part: electronics** | Holds the board, the 6-battery pack and the transmission components. The temperature probes enter through watertight passages. | Screwed lid (M5 screws and nuts) with silicone seal |
| **Lower part: sensor** | Holds the pressure transducer and the cavity where the water comes in. It is split along the y axis so that a continuous, tightly clamped seal can be used. | M5 screws and nuts with silicone seal |
| **Weight holder** | Open box that holds the ballast, in an amount suited to the site. | Draw latches |

The box is used with a **rod**, driven into the riverbed, which carries the temperature probes.

### Main design principles

- **A box in several parts**, to keep the parts simple to print. Each probe passage is made of two half-holes, one on each part, which close around the cable.
- **Cast silicone seals**, made in printed molds. Their hardness is adjusted by mixing two silicones.
- **Metal-on-metal clamping**: the M5 nuts sit in housings in the box and are tightened with a power drill. Tightening matters as much as the seal for watertightness.
- **A parametric model** in Onshape: the main dimensions are variables, so the box can be adapted without redrawing everything.

---

## Current version

| Version | Description | Status |
|---|---|---|
| v1 | Two-part box split along the x axis | Abandoned |
| **v2** | Lower sensor part split along the y axis, upper electronics part, separate weight holder | **Current version** |

Details of the versions and tests can be found in [`fabrication/`](fabrication/README.md).

---

## Contributors

MOLONARI project: [TO BE COMPLETED: school, year, team members' names]