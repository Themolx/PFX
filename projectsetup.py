import nuke
import nukescripts

def setup_2k_dcp_project():
    root = nuke.root()
    format_knob = root['format']
    
    desired_width = 2048
    desired_height = 1080
    desired_pixel_aspect = 1.0
    desired_name = "2K_DCP"
    
    existing_format = None
    for format in nuke.formats():
        if (format.width() == desired_width and
            format.height() == desired_height and
            format.pixelAspect() == desired_pixel_aspect and
            format.name() == desired_name):
            existing_format = format
            break
    
    if existing_format:
        print(f"2K DCP format already exists. Setting project to use it.")
        format_knob.setValue(desired_name)
    else:
        print(f"2K DCP format not found. Creating and setting it.")
        try:
            new_format = f"{desired_width} {desired_height} {desired_pixel_aspect} {desired_name}"
            nuke.addFormat(new_format)
            format_knob.setValue(desired_name)
        except RuntimeError as e:
            print(f"Error creating new format: {e}")
            print("Attempting to set format using existing method...")
            format_knob.fromScript(f"{desired_width} {desired_height} {desired_pixel_aspect}")
    
    root['lock_range'].setValue(True)
    
    current_format = format_knob.value()
    print(f"\nProject Format:")
    print(f"Name: {current_format.name()}")
    print(f"Resolution: {current_format.width()}x{current_format.height()}")
    print(f"Pixel Aspect Ratio: {current_format.pixelAspect()}")
    print(f"Lock Range: {root['lock_range'].value()}")

def set_viewer_process_rec709_aces():
    viewer_process = "Rec.709 (ACES)"
    viewers_updated = 0
    errors = []

    viewer_nodes = nuke.allNodes('Viewer')
    if not viewer_nodes:
        print("No Viewer nodes found. Creating a new Viewer node.")
        new_viewer = nuke.createNode('Viewer')
        viewer_nodes.append(new_viewer)

    for node in viewer_nodes:
        try:
            if 'viewerProcess' in node.knobs():
                node['viewerProcess'].setValue(viewer_process)
                viewers_updated += 1
            else:
                errors.append(f"Node {node.name()} does not have a viewerProcess knob.")
            
            if 'monitorOutOutputTransform' in node.knobs():
                node['monitorOutOutputTransform'].setValue(viewer_process)
            else:
                errors.append(f"Node {node.name()} does not have a monitorOutOutputTransform knob.")
        
        except Exception as e:
            errors.append(f"Error setting {viewer_process} for {node.name()}: {str(e)}")
    
    print(f"\nViewer Process Update Results:")
    print(f"Successfully updated {viewers_updated} Viewer node(s) to {viewer_process}")
    
    if errors:
        print("\nErrors encountered:")
        for error in errors:
            print(f"- {error}")
    else:
        print("No errors encountered.")

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
    
    print("\nFlipbook LUT set to Rec.709 (ACES)")

def comprehensive_setup():
    print("Starting comprehensive Nuke project setup...")
    setup_2k_dcp_project()
    set_viewer_process_rec709_aces()
    set_default_flipbook_lut()
    print("\nComprehensive setup complete!")

if __name__ == "__main__":
    comprehensive_setup()