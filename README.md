# BMI Calculator

A simple desktop BMI (Body Mass Index) calculator built with Python and Tkinter. Enter your weight and height to instantly calculate your BMI and see your health category.

---

## Features

- Clean and simple GUI window (350×350)
- Accepts weight in **kilograms** and height in **meters**
- Calculates BMI using the standard formula
- Displays the BMI value rounded to 2 decimal places
- Shows the corresponding health category

---

## BMI Categories

| BMI Range      | Category     |
|----------------|--------------|
| Less than 18.5 | Underweight  |
| 18.5 – 24.9    | Normal       |
| 25.0 – 29.9    | Overweight   |
| 30.0 and above | Obese        |

---

## Requirements

- Python 3.x
- `tkinter` (included with standard Python installations)

> No additional packages need to be installed.

---

## Usage

```bash
python BMI_notepad.py
```

1. Enter your **weight** in kilograms (e.g., `70`)
2. Enter your **height** in meters (e.g., `1.75`)
3. Click the **Calculate** button
4. Your BMI score and health category will be displayed below

---

## BMI Formula

```
BMI = Weight (kg) / Height (m)²
```

**Example:**
- Weight: 70 kg
- Height: 1.75 m
- BMI = 70 / (1.75²) = **22.86 → Normal**

---

## Screenshot

```
┌─────────────────────────┐
│      BMI Calculator     │
│                         │
│  Enter Weight (kg): [  ]│
│  Enter Height (m):  [  ]│
│                         │
│       [Calculate]       │
│                         │
│   BMI = 22.86           │
│   Normal                │
└─────────────────────────┘
```

---

## License

This project is open source and free to use.
