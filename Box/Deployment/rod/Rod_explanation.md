# Probe rod

The rod is driven into the riverbed and carries the temperature probes at different depths. It is 3D printed in a single piece, with clips that hold each probe and keep it away from the body of the rod.

## Contents

1. [Files](#files)
2. [Design](#design)
3. [Changes from last year's model](#changes-from-last-years-model)
4. [Printing](#printing)
5. [Mounting the probes](#mounting-the-probes)
6. [Field validation](#field-validation)

---

## Files

| Part | Modify (Onshape) | Print (STL) |
|---|---|---|
| Probe rod | [Open in Onshape](https://cad.onshape.com/documents/2f37f9a7a72e3b844bc26cf5/w/325063e0cb311e8a45c4c956/e/2f46907a06a0c7d93dc3eaa5) | [TO BE COMPLETED: file name] |

> 💡 To modify the model without changing the original, make a copy of the document in Onshape (*Make a copy*).

---

## Design

| Feature | Role |
|---|---|
| **Single-piece body** | Sturdier than a rod assembled from several parts, and nothing to assemble |
| **Hooks / clips** | Hold each probe away from the rod, so that the rod does not influence the temperature measurement |
| **Cable groove** | Guides the probe cables along the rod |
| **Positioning holes** | The tip of each probe sits slightly inside a hole, which keeps it at the right place |
| **Probe protectors** | Shield the probes from friction against the soil when the rod is driven in or pulled out |

The rod is also connected to the box by a tube: take care of this tube when handling the rod.

---

## Changes from last year's model

We started from last year's rod and made the following changes:

1. **Single piece**: the rod is now printed in one piece instead of several.
2. **Hooks added** to keep the probes as far as possible from the rod.
3. **Cable groove reduced by 0.5 mm**, so that the cables are held firmly.
4. **Clip contact surface increased**: the small clips of the first version printed badly or broke.
5. **Holes added** to position the tips of the probes more accurately.
6. **Probe protection reinforced**, so that the probes are not torn off when the rod is inserted into the ground.

> ℹ️ The first hooks were tested on a flat surface. Since the rod is round, their dimensions had to be adjusted and the part reprinted. Always test clips on the real geometry.

---

## Printing

| Setting | Value |
|---|---|
| Material | [TO BE COMPLETED: PLA?] |
| Orientation | [TO BE COMPLETED] |
| Supports | [TO BE COMPLETED] |
| Infill | [TO BE COMPLETED] |
| Print time | [TO BE COMPLETED] |

After printing, check that:
- no clip is broken or poorly printed;
- the cable groove is clean along its whole length;
- the positioning holes are not blocked.

---

## Mounting the probes

1. Lay each probe cable in the groove.
2. Clip the probe into its hook, at the planned depth.
3. Push the tip of the probe slightly into its positioning hole.
4. Check that each probe is behind its protector and that no cable sticks out.

---

## Field validation

<img src="photos/field_test.png" alt="Rod driven into the ground during the field test" width="280">

The rod was tested in the garden of the Mines.

**Procedure:**
1. Make a pilot hole with a **crowbar** and a **sledgehammer**.
2. Drive the rod into the hole, vertically, with the probes clipped on.
3. Pull the rod out vertically, without twisting it.
4. Check the probes and clips after insertion and after removal.

**Result:** ✅ no element came loose, neither during insertion nor during removal. **The design is validated** and this rod is kept for the final system.