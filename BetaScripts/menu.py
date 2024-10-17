# Import the script modules

import nuke
import AdvancedShuffle
import AdvancedReadNode
import NodeLabeler

import nukescripts

import Dots
import GrabTool



e=nuke.menu('Nuke')

n=e.addMenu('coolDotFromInternet/NodeGraph',icon='NodeGrapf.png')

n.addCommand ('Dots', 'Dots.Dots()', ',')




# Create the Custom Tools menu
toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("MTScripts", icon="Difference.png")

# Add menu items with correct function calls
#m.addCommand("Setup 2K DCP Project", projectsetup.comprehensive_setup, icon="Viewer.png")


