# File Corruptor

A simple Python-based file corruptor tool that allows you to introduce various types of corruption into files, creating interesting and often unpredictable results.  This can be used for fun, artistic purposes, or even for testing how applications handle corrupted data.

## Features

*   **Multiple Corruption Engines:** Choose from different corruption methods, including Incrementer, Scrambler, Smoother, and Blender, each producing unique effects.
*   **Customizable Corruption:** Control the start and end bytes of the corruption range, the block size and space, and the amount of change to apply.
*   **User-Friendly Interface:** A simple Tkinter-based graphical user interface makes it easy to select files, configure corruption settings, and apply the corruption.
*   **Image Preview:** Displays a preview of the selected image file (if applicable).
*   **Cross-Platform:** Works on any operating system that supports Python and Tkinter.

## How to Use

1.  **Select File:** Click the "Browse" button to choose the file you want to corrupt.
2.  **Configure Corruption:**
    *   **Start Byte:** The starting byte position for corruption.
    *   **End Byte:** The ending byte position for corruption.
    *   **Block Size:** The number of consecutive bytes to modify in each block.
    *   **Block Space:** The number of bytes to skip between blocks.
    *   **Add Value/Shift Right/Blend Range:** Depending on the selected engine, this value controls how much the bytes are modified.
    *   **Engine:** Select the corruption engine to use:
        *   **Incrementer:** Adds the "Add Value" to each byte.
        *   **Scrambler:** Replaces each byte with a random byte.
        *   **Smoother:** Averages each byte with its previous neighbor.
        *   **Blender:** Adds a random value within the "Blend Range" to each byte.
3.  **Corrupt:** Click the "Corrupt" button to apply the selected corruption settings. A corrupted copy of the original file will be created in the same directory.

## Requirements

*   Python 3.x
*   Tkinter (usually included with Python)
*   PIL (Pillow) library: `pip install Pillow`

## Running the Application

1.  Save the Python code as a `.py` file (e.g., `file_corruptor.py`).
2.  Run the script from your terminal: `python file_corruptor.py`

## Example

(Include a screenshot or GIF of the application in action if possible)

## Notes

*   The corrupted file will be saved with the `_corrupted` suffix.
*   The level of corruption can significantly impact the results. Experiment with different settings to achieve the desired effect.
*   Some file types might be more susceptible to corruption than others.
*   Be careful when corrupting important files! It's always a good idea to work with copies.

## Contributing

(Add contribution guidelines if you plan to accept contributions)

## License

(Licensed by DBS Tools.)