# Custom Nuke Tools Documentation

<p align="center">
  <img src="https://github.com/Themolx/PFX/blob/3468a4eb7451d9ecf24509e102c10c59c3d790dc/assets/PFX_Logo.png?raw=true" alt="PFX Logo">
</p>

By Martin Tomek

## Table of Contents
- [Overview](#overview)
- [Tools](#tools)
  - [1. Load Lightning Render](#1-load-lightning-render)
  - [2. Light Shuffler](#2-light-shuffler) 
  - [3. Sequence Loader](#3-sequence-loader)
  - [4. Appender Loader](#4-appender-loader)
  - [5. Reduce Noise Backdrop](#5-reduce-noise-backdrop)
  - [6. New Denoise Comp](#6-new-denoise-comp)
  - [7. Mask Checker - Grade](#7-mask-checker---grade)
  - [8. Mask Checker - Premult](#8-mask-checker---premult)
  - [9. ZDefocus Checker](#9-zdefocus-checker)
  - [10. Cryptomatte Tools](#10-cryptomatte-tools)
- [Project Setup](#project-setup)
  - [Setup 2K DCP Project](#setup-2k-dcp-project)
  - [Viewer Process Rec.709 (ACES)](#viewer-process-rec709-aces) 
  - [Flipbook Default LUT](#flipbook-default-lut)
- [Installation](#installation)
- [Conclusion](#conclusion)

## Overview

This documentation provides an overview of various custom Nuke tools developed to streamline compositing workflows and solve common pipeline challenges. These tools aim to improve efficiency, consistency, and quality control in daily compositing tasks.

## Tools

### 1. Load Lightning Render

- **Problem Solved**: Difficulty in locating and loading the latest lightning render layers
- **Key Features**:
  - Automatic detection of the latest render version
  - Creation of Read nodes for each layer
  - Neat arrangement of nodes
  - Frame range information
  - Support for GUI and non-GUI modes

### 2. Light Shuffler

- **Problem Solved**: Time-consuming manual splitting of light channels
- **Key Features**: 
  - Automatic splitting of light channels from a selected node
  - Creation of Shuffle and Remove nodes for each channel
  - Exclusion of 'lighting' and 'lightning' channels
  - Gray backdrop for generated nodes

### 3. Sequence Loader

- **Problem Solved**: Tedious manual loading of multiple sequences
- **Key Features**:
  - Loading of multiple sequences
  - Creation of Read nodes for each shot
  - Addition of text overlays with dynamic labels
  - Generation of a ContactSheet for easy review
  - Strict loading of denoise renders when selected
  - Smaller, gray backdrop
  - Dimmer colors for each sequence

### 4. Appender Loader

- **Problem Solved**: Difficulty in quickly reviewing multiple shots
- **Key Features**:
  - Loading of multiple sequences
  - Creation of Read nodes for each shot
  - Generation of a single AppendClip node for easy review
  - "Play" button for launching the AppendClip in Flipbook

### 5. Reduce Noise Backdrop

- **Problem Solved**: Difficulty in identifying Reduce Noise v5 nodes
- **Key Features**:
  - Automatic detection of Reduce Noise v5 nodes
  - Placement of a red backdrop under each node
  - Reporting of the total number of nodes found

### 6. New Denoise Comp

- **Problem Solved**: Time-consuming setup of a new denoise comp
- **Key Features**:
  - Automatic import of the latest regular comp file
  - Setup of the 2K DCP project
  - Finding mismatched ZDefocus nodes
  - Checking for white alpha and creating necessary nodes

### 7. Mask Checker - Grade

- **Problem Solved**: Difficulty in verifying mask channels
- **Key Features**:
  - Automatic detection of mask channels from a selected node
  - Creation of Shuffle nodes for each mask channel
  - Application of a Grade node with increased white value
  - Series connection of Grade nodes
  - Output postage stamp for the final result

### 8. Mask Checker - Premult

- **Problem Solved**: Difficulty in checking mask channels with premultiplication
- **Key Features**:
  - Automatic detection of mask channels from a selected node
  - Creation of a "hero" Dot node for the beauty pass
  - Creation of Shuffle and Premult nodes for each mask channel
  - Individual premultiplication of each mask channel with the beauty pass

### 9. ZDefocus Checker

- **Problem Solved**: Inconsistent values in ZDefocus nodes
- **Key Features**:
  - Automatic detection of PxF_ZDefocusHERO nodes
  - Analysis of key knob values (fStop, focalDistance, focalLength, filmBack)
  - Identification of nodes with values differing from the most common value
  - Reporting of mismatched nodes and their values

### 10. Cryptomatte Tools

- **Problem Solved**: Inconsistent Cryptomatte layer settings
- **Key Features**:
  - Automatic detection of the correct Cryptomatte layer based on expressions
  - Locking of the cryptoLayer knob to prevent accidental changes
  - Updating of node labels based on the detected layer

## Project Setup

### Setup 2K DCP Project

- **Problem Solved**: Inconsistent project settings
- **Key Features**:
  - Automatic setup of a 2K DCP project (2048x1080, 1.0 pixel aspect ratio)
  - Creation of the format if it doesn't exist
  - Locking of the frame range

### Viewer Process Rec.709 (ACES)

- **Problem Solved**: Inconsistent color space settings in Viewer nodes
- **Key Features**:
  - Automatic setting of the Viewer Process to Rec.709 (ACES)
  - Application to all existing Viewer nodes
  - Creation of a new Viewer node if none exist

### Flipbook Default LUT

- **Problem Solved**: Inconsistent LUT settings in Flipbook
- **Key Features**:
  - Setting the default LUT for Flipbook to Rec.709 (ACES)
  - Overriding the Flipbook dialog to ensure the setting is applied

## Installation

1. Download the tools package
2. Place the Python scripts in your Nuke plugins directory
3. Add the following line to your `init.py` or `menu.py`:

```python
nuke.pluginAddPath("/path/to/custom_tools")
```

4. Restart Nuke

## Conclusion

These custom Nuke tools provide a comprehensive solution to various compositing challenges, improving efficiency, consistency, and quality control in daily tasks. They automate repetitive processes, ensure consistent settings, and enhance the user experience.

As a Technical Director, I remain committed to refining and expanding this toolkit based on user feedback and evolving production needs. Feel free to reach out with questions, suggestions, or specific workflow challenges that might benefit from similar custom solutions.

