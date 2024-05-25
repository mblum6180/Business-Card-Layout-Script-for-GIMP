# Business Card Layout Script for GIMP

This repository contains a Python-Fu script for GIMP that automatically layouts business cards on a custom-sized page. The script allows users to define the number of rows, columns, and spacing between cards, facilitating easy creation of ready-to-print business card sheets.

## Installation

To use this script, you need to have GIMP installed on your computer. This script is compatible with GIMP 2.10 and newer versions. Follow these steps to install the script:

1. Download the `layout_business_cards.py` file from this repository.
2. Locate your GIMP scripts folder, which is typically found at one of the following paths depending on your operating system:
   - Windows: `C:\Program Files\GIMP 2\share\gimp\2.0\scripts\`
   - macOS: `~/Library/Application Support/GIMP/2.10/scripts/`
   - Linux: `~/.config/GIMP/2.10/scripts/`
3. Place the downloaded script file into the scripts folder.
4. Restart GIMP. After restarting, the script should be accessible via `File -> Create -> Layout Business Cards`.

## Usage

To use the script:
1. Open GIMP and load the image you want to use as the business card.
2. Navigate to `File -> Create -> Layout Business Cards`.
3. In the dialog box that appears, enter the number of rows, columns, and the spacing in pixels between the cards.
4. Click OK to generate the layout.

The script will create a new image containing your business cards laid out according to the specified parameters.

## Contributing

Contributions to this script are welcome. If you have suggestions for improvements or have found a bug, please open an issue or submit a pull request.

## License

This script is provided under the MIT License. See the LICENSE file in this repository for more information.

---

For more information on Python-Fu scripts for GIMP, refer to the [official GIMP Python-Fu documentation](https://www.gimp.org/docs/python/).
