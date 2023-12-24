> ⚠️ **Work in Progress & Frequent Crashes**  
> 
> **Attention:** This physics simulation project is a work in progress and may encounter frequent crashes or unexpected behavior. Please exercise caution while running the simulation as it's currently unstable. Your patience and feedback are greatly appreciated as we continue to improve its stability and performance.


# Physics Simulation

This is a simple physics simulation program that demonstrates bouncing balls within a tkinter-based graphical user interface.

## Description

The simulation generates multiple balls that bounce around the canvas area. The balls interact with each other upon collision, changing their directions based on the collision angles and applying a bounciness factor. 

## Prerequisites

- Python 3.x

## Installation

1. Clone or download this repository.
2. Install the required Python dependencies using the provided `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the simulation using Python:
    ```bash
    python sim.py
    ```

## Usage

- Upon running the program, the graphical simulation window will open.
- The balls will start bouncing around the canvas.
- The GUI displays the count of balls present in the simulation.
- Each ball collision will trigger the creation of a new ball after a cooldown period.

## Credits

This simulation was created using Python's Tkinter library for the GUI.

