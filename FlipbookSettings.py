# Flipbook Default LUT Setter
#
# This script sets the default LUT for the Nuke Flipbook to "Rec.709 (ACES)"
# and ensures this setting is applied when the Flipbook dialog is opened.

import nuke
import nukescripts

def set_default_flipbook_lut():
    """Set the default LUT for Flipbook to "Rec.709 (ACES)" and apply it to the dialog."""
    # Set the default LUT option
    nukescripts.setFlipbookDefaultOption("lut", "Rec.709 (ACES)")

    # Override the flipbook dialog function to ensure our setting is applied
    def custom_flipbook_dialog():
        dialog = nukescripts.FlipbookDialog()
        dialog.setKnob("lut", "Rec.709 (ACES)")
        return dialog

    # Replace the original flipbook dialog function with our custom one
    nukescripts.flipbookDialog = custom_flipbook_dialog

# Call the function to set the default LUT
set_default_flipbook_lut()