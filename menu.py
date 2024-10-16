# Import the script modules

import nuke
import projectsetup
import maskcheckergrade
import maskcheckerpremult
import sequenceloader
import AppenderLoader
import LoadLightningRender
import LightShuffler
import ReduceNoiseBackdrop
import NewDenoiseComp


import nukescripts


# Create the Custom Tools menu
toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("MTScripts", icon="Difference.png")

# Add menu items with correct function calls
m.addCommand("Setup 2K DCP Project", projectsetup.comprehensive_setup, icon="Viewer.png")
m.addCommand("Load Lightning Render", LoadLightningRender.find_latest_renders, icon="ColorAdd.png")

m.addCommand("Shuffle LightGroup renders",LightShuffler.split_light_channels, icon="DirectLight.png")

m.addCommand("Mask Checker Grade", maskcheckergrade.mask_channel_splitter_with_grade_series, icon="Shuffle.png")
m.addCommand("Mask Checker Premult", maskcheckerpremult.mask_channel_splitter_with_individual_premults_and_hero_dot, icon="Shuffle.png")
m.addCommand("MultiSequence Loader", sequenceloader.load_sequence_and_create_contact_sheet, icon="Read.png")
m.addCommand("Appender Loader", AppenderLoader.load_sequence_and_create_append_clip, icon="Camera.png")
m.addCommand("Reduce Noise Backdrops",ReduceNoiseBackdrop.highlight_reduce_noise_nodes_with_backdrops, icon="CopyBBox.png")
m.addCommand("NewDenoiseComp",NewDenoiseComp.main, icon="Assert.png")




# Wind integration (if needed)
try:
    import wind
    nuke.menu('Nuke').addCommand('Wind/Show Wind', wind.show, 'ctrl+w')
except ImportError:
    print("Wind module not found. Wind integration skipped.")

#nastaveni flipbooku

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




print("Uz to bude")
nuke.tprint("Loaded scripts made by Martin Tomek")


