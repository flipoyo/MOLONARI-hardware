# MOLONARI – Waterproof sensor box

A 3D-printed box that protects the electronics of a submerged MOLONARI sensor, while letting the temperature probes pass through and exposing the pressure transducer to the water.

This repository contains all the design files (Onshape, STEP, STL) and the instructions to **build, assemble and test** the box from start to finish.

---

## Contents

1. [Bill of materials](#bill-of-materials)
2. [Step-by-step fabrication](#step-by-step-fabrication)
3. [Modifying the box](#modifying-the-box)
4. [Version history](#version-history)

---

## Bill of materials

### Printing
| Item | Details |
|---|---|
| 3D printer | [TO BE COMPLETED] |
| Box filament | PLA and TPU |

### Hardware
| Item | Quantity | Notes |
|---|---|---|
| M5 screws | 6 | Stainless steel recommended (wet environment) |
| M5 nuts | 6 | Inserted into the printed housings |
| 2 kg weights | 2 | Placed in the weight holder |

### Seals
| Item | Proportion |
|---|---|
| BLUESIL RTV 147A silicone | 50% |
| BLUESIL RTV 148A silicone | 50% |
| BLUESIL RTV 147B activator / catalyst | 10% |
| Precision scale, cups, stirring sticks, syringe or pipette | For measuring and pouring |

### Tools
- Power drill (essential for sufficient tightening)
- Allen key / bit matching the screws
- Crowbar and sledgehammer (for installing the rod in the field)

---

## Step-by-step fabrication

| Step | Guide | Estimated time |
|---|---|---|
| 1. Get the files from Onshape. If you wish, you can change the values in the variable table to give the box the dimensions you prefer. | [TO BE COMPLETED: Onshape link] | 1 h |
| 2. Print the box parts, the probe and the molds. Download them as STL files and open them in your printer's software (Bambu Studio, Ultimaker Cura…). Check the dimensions, orient the parts with the holes facing upwards, make sure the material is set to PLA, then slice and print. | STL files | ~2–3 days of printing |
| 3. Cast the silicone seals | [`docs/02_joints.md`](docs/02_joints.md) | 24 h curing |
| 4. Assemble the box with the screws, using a power drill. | [`docs/03_assemblage.md`](docs/03_assemblage.md) | 10 min |
| 5. Test watertightness before deployment | [`docs/04_tests.md`](docs/04_tests.md) | 6 h minimum |

> 💡 Cast the seals **while** the box is printing to save a day.

---

## Modifying the box

The Onshape model is parametric: you change the **variables** (outer dimensions, wall thickness, screw spacing, probe positions…) and all the parts update while staying compatible with each other.

Everything is explained in [`cao/README.md`](cao/README.md).

**Rules to follow:**
- never type a shared dimension in directly: always use the variables;
- if you modify a seal groove, **also modify the matching mold**;
- export the STEP and STL files again, and create a version in Onshape at each step validated by a test.

---

## Version history

| Version | Description | Status |
|---|---|---|
| v1 | Two-part box split along the x axis, barbed fitting split in two | Abandoned: seal housings printed poorly, watertightness could not be tested. File in `cao/archives/v1/` |
| v2 | New architecture: lower sensor part split along the y axis, upper electronics part, separate weight holder | **Current version** |