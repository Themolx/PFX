# Reduce Noise Node Finder and Backdrop Creator
#
# This script finds all Reduce Noise v5 nodes in the Nuke script,
# places a red backdrop under each one, and reports the total number found.

import nuke

def find_reduce_noise_nodes():
    reduce_noise_nodes = []
    for node in nuke.allNodes():
        if node.Class() == "OFXcom.absoft.neatvideo5_v5":
            reduce_noise_nodes.append(node)
    return reduce_noise_nodes

def create_backdrop(node, color):
    backdrop = nuke.nodes.BackdropNode()
    backdrop['label'].setValue(node.name())
    backdrop['note_font_size'].setValue(42)
    backdrop['tile_color'].setValue(color)
    
    # Set backdrop size and position
    bdX = node.xpos() - 50
    bdY = node.ypos() - 50
    bdW = node.screenWidth() + 100
    bdH = node.screenHeight() + 100
    
    backdrop.setXYpos(bdX, bdY)
    backdrop['bdwidth'].setValue(bdW)
    backdrop['bdheight'].setValue(bdH)
    backdrop['z_order'].setValue(1)
    
    return backdrop

def highlight_reduce_noise_nodes_with_backdrops():
    reduce_noise_nodes = find_reduce_noise_nodes()
    red_color = int(0xFF0000FF)
    
    for node in reduce_noise_nodes:
        create_backdrop(node, red_color)
    
    nuke.message(f"Found and highlighted {len(reduce_noise_nodes)} Reduce Noise v5 nodes.")

if __name__ == "__main__":
    highlight_reduce_noise_nodes_with_backdrops()