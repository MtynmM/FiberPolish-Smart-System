# FiberPolish Smart System

A touch-friendly Python HMI for controlling a fiber-optic polishing machine on Raspberry Pi 5 with a 7-inch touchscreen.

> **Project context:** This repository is the GitHub snapshot of an internship project developed at Quantum Center. The deployed/prototyped system was developed around Raspberry Pi hardware owned by the center. The repository is preserved as a portfolio snapshot and is not intended to claim production-ready industrial safety certification.

## Architecture

The application follows a lightweight **Model–View–Presenter (MVP)** structure:

- **Model:** hardware-facing control classes for the light, Lissa motor and polishing/column motors.
- **View:** the `ttkbootstrap` touchscreen GUI and its control panels.
- **Presenter:** connects GUI events to the corresponding model and keeps interaction logic out of the view.

## Features in this repository

- Touch-friendly control panels
- Light brightness control
- Lissa motor ON/OFF control
- Polishing pad speed and direction control
- Column up/down control
- Stopwatch and countdown UI
- Drawer-style navigation
- Full-screen/kiosk-oriented UI
- Raspberry Pi GPIO integration through `gpiozero`

Some UI sections are intentionally kept as prototype/in-progress elements because the original hardware environment is no longer available to the author.

## Project structure

```text
src/
├── main.py
├── model/
│   ├── column_model.py
│   ├── light_model.py
│   ├── lissa_model.py
│   └── pad_model.py
├── presenter/
│   ├── column_presenter.py
│   ├── light_presenter.py
│   ├── lissa_presenter.py
│   └── pad_presenter.py
└── view/
    ├── main_view.py
    └── panels/
        ├── control_panel.py
        └── timer_panel.py
```

## Installation

### Requirements

- Python 3.10+
- Raspberry Pi 5 for real GPIO/hardware operation
- 7-inch touchscreen (recommended for the intended HMI layout)

Clone the repository:

```bash
git clone https://github.com/matin-mohamadi/FiberPolish-Smart-System.git
cd FiberPolish-Smart-System
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running

The current source uses project-local imports, so run the entry point from the `src` directory:

```bash
cd src
python main.py
```

This application expects Raspberry Pi GPIO hardware for the hardware-facing models. Running it on a normal laptop without the required GPIO environment is not expected to reproduce the full system behavior.

## Hardware mapping

The GPIO mapping currently defined in `src/main.py` is:

| Function | GPIO |
|---|---:|
| Light | 18 |
| Lissa motor | 26 |
| Pad PWM | 12 |
| Pad CW | 13 |
| Pad CCW | 6 |
| Column enable/PWM | 19 |
| Column direction | 5 |

**Safety:** This software controls physical hardware. The repository should be treated as an internship/prototype codebase, not as certified industrial safety software. Hardware behavior must be independently verified before any real-machine deployment.

## Status

The original internship work is complete. The repository is maintained as a portfolio snapshot rather than as an actively developed product.
