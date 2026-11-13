# Calibration of differential pressure sensors (MOLONARI)

## Folder contents

- `test_pressure_sensor_.xlsx`: manual measurements for the linear calibration (11 points, constant temperature) and the least-squares line fit.
- `calib.py`: thermal model of the sensor and pressure correction as a function of temperature (see [Temperature correction](#temperature-correction)).
- `AtmoCONTROL_command_generation.ipynb`: the thermostatic chamber only accepts temperature ramps. This program decomposes any signal into ramps.
- `AtmoCONTROL_userguide.md`: user guide for the thermostatic chamber.


## Introduction

Every pressure sensor is unique and depends on temperature: for the same differential pressure, two sensors can output different voltages, and the voltage of a single sensor varies with its temperature (up to 50% for the same pressure).

The calibration must therefore make it possible to recover the difference in water height between the two columns, and hence the differential pressure, from the voltage $U$ and the temperature $T$:

$$U = f(\Delta H, T) \quad \rightarrow \quad \Delta H = f(U, T)$$

The ideal model is $U = \alpha \Delta H$. It must be corrected for temperature. The manufacturer suggests:

$$U_{corr} = U_{mes} + (T_0 - T)\frac{\partial U_{mes}}{\partial T}$$

where the linear relation between $U$ and $\Delta H$ is established at a constant temperature $T_0$.

We therefore split the calibration into two steps:

1. **Constant temperature, variable $\Delta H$**: manual measurements, adding water to one of the two tubes. This gives the linear characteristic of the sensor.
2. **Constant $\Delta H$, variable temperature**: automated tests in the climate chamber. We quantify the effect of temperature on the voltage, then correct it with `calib.py`.

## Equipment

- Differential pressure sensor (Honeywell 26PC series) connected to two water-filled tubes.
- 4-channel HOBO datalogger: pressure sensor voltage and temperature probes (HOBO TMC6-HD).
- Memmert climate chamber controlled with AtmoCONTROL.

## Step 1: linear calibration at constant temperature

### Protocol

The setup (photo below) makes it possible to fix the water height in each of the two tubes. For each point:

1. set the water heights $H_1$ (tube 1) and $H_2$ (tube 2), in cm;
2. compute $\Delta H = H_2 - H_1$;
3. read the voltage $V$ given by the datalogger once the value has stabilized.

The measurement was repeated **11 times**, with height differences ranging from −4.9 cm to +7.3 cm. The temperature must remain constant.

![Measurement setup](</differential pressure sensor/calibration/pictures/setup_sampling.jpg> "Measurement setup at room temperature")

### Measurements

| $H_1$ (cm) | $H_2$ (cm) | $\Delta H = H_2 - H_1$ (cm) | $V$ (V) |
|---|---|---|---|
| 4.9 | 0 | −4.9 | 1.514 |
| 4.9 | 4.4 | −0.5 | 1.648 |
| 4.9 | 5 | 0.1 | 1.659 |
| 4.1 | 4.4 | 0.3 | 1.666 |
| 1.7 | 4.4 | 2.7 | 1.733 |
| 5.5 | 8.8 | 3.3 | 1.724 |
| 5.3 | 10.4 | 5.1 | 1.762 |
| 4.9 | 10.4 | 5.5 | 1.771 |
| 1.7 | 8.8 | 7.1 | 1.812 |
| 3.1 | 10.4 | 7.3 | 1.814 |
| 0.6 | 7.9 | 7.3 | 1.813 |

### Least-squares regression

We look for $\Delta H = m\,V + c$ with $x_i = V_i$, $y_i = \Delta H_i$ and $n = 11$:

$$m = \frac{n\sum x_i y_i - \sum x_i \sum y_i}{n\sum x_i^2 - \left(\sum x_i\right)^2}, \qquad c = \frac{\sum y_i - m\sum x_i}{n}$$

We obtain:

$$\boxed{\Delta H = 42.43663\,V - 69.9479 \ \text{(cm)}}$$

The differential pressure follows (water, $\rho = 998\ \text{kg/m}^3$, $g = 9.81\ \text{m/s}^2$):

$$\Delta P = \rho\, g\, \Delta H = 998 \times 9.81 \times \frac{\Delta H}{100} \ \text{(Pa)}$$

that is, about 97.9 Pa per cm of water.

### Reading the results

- Sensitivity: about 23.6 mV per cm of water, with $\Delta H = 0$ for $V \approx 1.648$ V.
- Quality of the fit: $R^2 \approx 0.985$, root-mean-square error of about 0.46 cm (about 45 Pa), maximum error of about 0.9 cm. Points 5 and 6 are not in the expected order (1.733 V for 2.7 cm, then 1.724 V for 3.3 cm), which shows the measurement noise (manual reading of the heights, sensor stabilization).
- This line gives the **difference** in pressure between the two tubes. To obtain the water pressure, the reference pressure must still be added.

## Step 2: effect of temperature

### Observation

At constant $\Delta H$, the sensor voltage varies when the temperature changes. If the line from step 1 is applied without correction, this variation is wrongly interpreted as a pressure variation. It could come from the components (resistors) inside the sensor; this is a hypothesis, not verified.

In addition, the sensor does not follow the chamber temperature immediately: the box that holds it and the water introduce a thermal delay. The temperature that matters is that of the sensor, not that of the chamber.

### Climate chamber tests

The sensor is placed in a box inside the chamber. Two temperature probes are recorded by the HOBO:

- an **external** probe, inside the chamber but outside the box (imposed temperature);
- an **internal** probe, inside the box of the pressure sensor.

The setpoints are sent as ramps (AtmoCONTROL, see `AtmoCONTROL_userguide.md`). Tests carried out:

| Test | Setpoints |
|---|---|
| 1 h | 20, 19, 17, 15, 12, 11, 10, 11, 12, 15, 17, 19, 20 °C, 5 min per step |
| 1 h 40 min, no water in the tubes | temperature variation in the chamber (21 Oct 2026) |
| 5 h, constant $\Delta H = 2.9$ cm | 20 → 10 °C then back to 20 °C, one point every 15 min (20; 19.76; 19.05; 17.94; 16.55; 15; 13.45; 12.06; 10.95; 10.24; 10), linear between points (26 Oct 2026) |

The 5 h test (`test_5h_calibration.xlsx`, HOBO at 1 Hz) is the basis for `calib.py`.

## Temperature correction

`calib.py` corrects the pressure in three stages. The calibration file is a `DataFrame` containing the columns `Température externe` (external temperature), `Température interne` (internal temperature) and `Pression` (pressure). The `Pression` column is the pressure computed from the voltage using the line from step 1. Since the test is run at constant real pressure, any variation of this column comes from temperature.

### 1. Thermal model (`apprendre_modele_thermique`)

The internal temperature is modeled as a **first-order discrete-time low-pass filter** (recursive exponential average) of the external temperature:

$$T_i[n] = a\,T_i[n-1] + (1-a)\,\bigl(b + g\,T_e[n-1]\bigr)$$

- $a \in [0\,;\,1[$: memory of the filter. The time constant is $\tau = -\Delta t / \ln a$ ($\Delta t = 1$ s for the HOBO at 1 Hz).
- $g$: static gain between external and internal temperature.
- $b$: offset.

The three parameters are obtained by least squares (`scipy.optimize.least_squares`) by minimizing the one-step prediction error, $T_i[n] - \hat{T}_i[n]$, on the real measurements. The bounds impose $0 \le a \le 0.99999$, with $(a, b, g) = (0.9\,;\,0\,;\,1)$ as the starting point. The measurements must be regularly spaced.

### 2. Thermal sensitivity of the pressure (`apprendre_modele_pression`)

We first simulate $T_i$ with the previous model from $T_e$, starting from the true initial internal temperature. We then regress the pressure on this estimated internal temperature:

$$P = c + k\,T_{i,est}$$

$k$ (Pa/°C) is the thermal sensitivity of the sensor, and $T_{ref}$ is the mean of $T_{i,est}$ during the calibration.

### 3. Correction of the measured pressure (`corriger_pression`)

On field data, $T_i$ is estimated **from the external temperature only**, then:

$$P_{corr} = P - k\,\bigl(T_i - T_{ref}\bigr)$$

This is the manufacturer's formula transposed to pressure: $T_0$ becomes $T_{ref}$, and the sensor temperature is not measured but estimated by the filter, which removes the need for an internal probe in real conditions.

### Usage

```python
import pandas as pd
from calib import corriger_pression

# columns: 'Température externe', 'Température interne', 'Pression'
calibration = pd.read_excel("test_5h_calibration.xlsx")

# P_field and Te_field: vectors of the same size, regularly sampled
P_corr = corriger_pression(calibration, P_field, Te_field, temperature_initiale=None)
```

If `temperature_initiale` is `None`, the first internal temperature is taken equal to $b + g\,T_e[0]$. If the real sensor temperature at the start of the series is known, it is better to provide it.

### Results of the 5 h test

| Parameter | Value |
|---|---|
| $a$ | *to be completed* |
| $\tau$ (s) | *to be completed* |
| $g$ | *to be completed* |
| $b$ | *to be completed* |
| $k$ (Pa/°C) | *to be completed* |
| $T_{ref}$ (°C) | *to be completed* |
| Deviation before correction (Pa, peak to peak) | *to be completed* |
| Deviation after correction (Pa, peak to peak) | *to be completed* |

*(Add the plot of the pressure before and after correction here.)*

## Calibration of the temperature sensors (Arduino)

The Arduino temperature channels are NTC thermistors (HOBO TMC6-HD) mounted in a voltage divider; they only provide a **voltage**. They are calibrated against the HOBO datalogger, taken as the reference.

A least-squares fit of an exponential law between the normalized voltage ("Last number normalized") and the real temperature, on 1116 records (30 Oct 2026, `RECORDS_corrige.xlsx`):

$$T = 146.133\, e^{-1.1428\,V}$$

A degree-4 polynomial fit (Excel trendline) was tried first. The exponential law was kept: it is a simple empirical fit, valid over the temperature range of the test. The physical β model of the thermistor, $\frac{1}{T} = \frac{1}{T_0} + \frac{1}{\beta}\ln\frac{R}{R_0}$, was not used for the final calibration; it would be preferable for extrapolating outside this range.


## Registering the calibration in the data repository

Once the sensor is calibrated, the results must be added to the `MOLO-data-light` repository:

1. Go to `MOLO-data-light/calibration/` and create a new file for this sensor
   (*naming convention: to be completed*).
2. Put the calibration measurements in this file: the table from
   [Step 1](#step-1-linear-calibration-at-constant-temperature)
   ($H_1$, $H_2$, $\Delta H$, $V$).
3. Open `lab/lab.json` and update the entry of this sensor using the values
   from this README:
   - the linear calibration of step 1, $\Delta H = m\,V + c$ (*fields to be completed*);
   - the thermal parameters $a$, $b$, $g$, $k$, $T_{ref}$ from the
     [5 h test](#results-of-the-5-h-test), if `lab.json` has fields for them.
4. Commit and push.

If the sensor is recalibrated, update both the file in `calibration/` and `lab/lab.json`, so the two stay consistent.


## Problems encountered

### Connectivity

Some HOBO channels give erratic, unusable pressure measurements. This may come from defects in the jack connectors.

### Long-term voltage drift

Some sensors see their voltage slowly decrease (about 5 mV/min), for example sensor XXV. After a 36 h test with a sinusoidal temperature setpoint, the voltage decreases continuously while the temperature goes up and down. The problem depends neither on the HOBO, nor on the channel used, nor on air bubbles (the voltage goes back up on a new channel, then drops again). The probable cause is electronic or related to the battery.

### Accuracy of the manual calibration

The deviation of about 0.46 cm (RMS) around the line (step 1) limits the accuracy in pressure. Possible improvements: reading the heights more precisely, letting the sensor stabilize longer, measuring more points.

## History: conduction model (2025)

In previous years, thermal conduction was modeled with a phase shift $\phi = a\,\frac{\partial T}{\partial t} + b$, then in 2025 with a second-order low-pass filter without oscillations:

$$H(p) = \frac{1}{(1 + \tau_1 p)(1 + \tau_2 p)}$$

For sensor XV: $\tau_1 = 377.91$ s and $\tau_2 = 922.88$ s (MSE = 0.01 on a sine). `calib.py` uses a simpler first-order version, with a single memory parameter $a$ and a gain $g$.