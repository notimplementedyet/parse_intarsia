# Intarsia Machine Knitting Instructions Parser

A tool to parse image files and generate machine knitting instructions for intarsia patterns. It breaks down an image into colored segments and provides row-by-row instructions for knitting.

## Prerequisites

- Python 3.x
- Pillow (Python Imaging Library)

## Setup

Follow these steps to set up a virtual environment and install the necessary dependencies:

1.  **Open your terminal.**
2.  **Navigate to the project directory:**
    ```bash
    cd /home/[PROJECT_PATH]
    ```
3.  **Create a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv .venv
    ```
4.  **Activate the virtual environment:**
    - On **Linux/macOS**:
      ```bash
      source .venv/bin/activate
      ```
    - On **Windows**:
      ```bash
      .venv\Scripts\activate
      ```
5.  **Install the required dependencies:**
    ```bash
    pip install pillow
    ```

## Usage

The script processes an image file and prints instructions for each row. You must provide the path to the image file using the `--file` argument.

### Basic Command

```bash
python3 parse_intarsia_optimized.py --file your_image.jpg
```

### Options

- `--file FILE`: The path to the image file you want to process.
- `--colors COLOR1 COLOR2 ...`: (Optional) Provide names for the colors found in the image. If not provided, colors will be indexed numerically (e.g., "Color 0", "Color 1").

### Example with Named Colors

```bash
python3 parse_intarsia_optimized.py --file vector.jpg --colors Red Blue White
```

### Interactive Knitting

After running the script, it will display information about the image and the colors detected. It will then wait for you to press **ENTER** to display the instructions for each row.

1.  The script starts from the bottom of the image (Row 1).
2.  Instructions will tell you whether to start on the **left** or **right**.
3.  For each segment in the row, it will provide the color and the needle range (e.g., "Color 0, 10 to 20").
4.  Press **ENTER** to proceed to the next row.

## Scripts

- `parse_intarsia_optimized.py`: The recommended version with improved error handling and updated Python syntax.
- `parse_intarsia.py`: The legacy version of the script.
