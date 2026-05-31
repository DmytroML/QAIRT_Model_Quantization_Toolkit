# Qualcomm QCS6490 Windows Setup Guide

This repository contains notes, setup instructions, and development resources for working with **Qualcomm Dragonwing™ QCS6490/QCM6490** platforms running **Windows on Arm (WoA)**.

## Overview

The Qualcomm QCS6490 is an edge AI and IoT processor featuring:

* Octa-core Qualcomm Kryo™ CPU
* Qualcomm Adreno™ 643 GPU
* Qualcomm Hexagon™ AI Engine
* Up to 12 TOPS AI performance
* Windows on Arm support
* Linux, Ubuntu, Android, and Windows compatibility

The platform is designed for:

* Edge AI applications
* Computer vision
* Robotics
* Smart cameras
* Industrial IoT
* Human-machine interfaces (HMI)

## Prerequisites

Before starting, ensure you have:

### Hardware

* Qualcomm QCS6490-based development board
* USB cable for flashing/debugging
* Power supply recommended by board vendor
* Windows 11 PC

### Software

* Windows 11 (x64)
* Administrator privileges
* Internet connection
* Qualcomm Software Center account (if required by your board vendor)

## Windows Development Environment Setup

### 1. Install Visual Studio

Download and install:

* Visual Studio 2022
* Desktop Development with C++
* C++ CMake Tools
* Windows SDK
* ARM64 Build Tools

### 2. Install Git

```bash
git --version
```

Download:

https://git-scm.com/

### 3. Install Python

Recommended:

```bash
python --version
```

Download:

https://www.python.org/downloads/

### 4. Install CMake

Verify installation:

```bash
cmake --version
```

Download:

https://cmake.org/download/

## Qualcomm SDK Installation

### Qualcomm Software Center

1. Sign in to Qualcomm Developer Portal.
2. Open Qualcomm Software Center.
3. Download SDK packages available for your board.
4. Install required components.

Typical packages may include:

* Qualcomm AI Engine Direct SDK
* Neural Processing SDK
* Board Support Package (BSP)
* Device drivers
* Platform tools

## Verify ARM64 Toolchain

Open Developer Command Prompt and run:

```cmd
cl
```

Verify ARM64 targets:

```cmd
cmake -A ARM64 ..
```

## AI Development

### ONNX Runtime

Install:

```bash
pip install onnxruntime
```

### OpenCV

Install:

```bash
pip install opencv-python
```

### NumPy

Install:

```bash
pip install numpy
```

## Example Project Structure

```text
project/
│
├── models/
│   └── yolov8n.onnx
│
├── src/
│   ├── main.py
│   └── inference.py
│
├── data/
│
├── requirements.txt
│
└── README.md
```

## Running an Example

```bash
python main.py
```

## Building Native ARM64 Applications

Create build directory:

```bash
mkdir build
cd build
```

Configure:

```bash
cmake .. -A ARM64
```

Build:

```bash
cmake --build . --config Release
```

## Useful Resources

### Qualcomm Documentation

* Qualcomm Developer Documentation
* Qualcomm Software Center
* QCS6490 Platform Documentation

### Development Tools

* Visual Studio 2022
* Windows SDK
* CMake
* Git

## Troubleshooting

### Drivers Not Detected

* Verify board-specific BSP installation.
* Check Device Manager for missing devices.
* Reinstall vendor-provided drivers.

### ARM64 Build Errors

Ensure ARM64 toolchain components are installed:

* MSVC ARM64
* Windows SDK
* CMake support

### SDK Access Issues

Some Qualcomm packages require:

* Qualcomm Developer account
* Approved hardware platform
* Vendor-provided access credentials

## References

* Qualcomm QCS6490 Documentation
* Qualcomm Windows on Arm Documentation
* Microsoft Windows on Arm Documentation

## License

This repository is provided for educational and development purposes.

