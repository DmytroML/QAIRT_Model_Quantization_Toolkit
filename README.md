## Deployment Pipeline

<p align="center">
  <img src="docs/ChatGPT Image.png" width="400">
</p>

# QAIRT Model Quantization Toolkit

A practical toolkit and step-by-step guide for quantizing ONNX models
for Qualcomm® AI Runtime (QAIRT) and deploying them on Qualcomm NPUs.

Supported:
- ONNX models
- INT8 quantization
- Per-channel quantization
- Windows
- Linux +-
- QCS6490

## Features

- ONNX model quantization
- INT8 deployment pipeline
- Calibration dataset generation
- QAIRT SDK integration
- QNN conversion support
- Windows and Linux support
- Qualcomm NPU deployment

## Tested Platforms

| Platform | Status |
|-----------|---------|
| QCS6490 | ✅ |
| Windows 11 | ✅ |

## Quick Start
### 1. Download QAIRT SDK
```bash
wget https://softwarecenter.qualcomm.com/api/download/software/sdks/Qualcomm_AI_Runtime_Community/All/2.47.0.260601/v2.47.0.260601.zip
```
[Install Qualcomm SDK](https://docs.qualcomm.com/doc/80-63442-10/topic/windows_setup.html#step-1-install-qualcomm-ai-engine-direct-aka-the-qnn-sdk)

### 2. Install dependencies

```bash
pip install -r requirements.txt
```
### 3. Run quantization

```bash
.venv\Scripts\Activate.ps1

Unblock-File ./v2.47.0.260601/qairt/2.47.0.260601/bin/envsetup.ps1
./v2.47.0.260601/qairt/2.47.0.260601/bin/envsetup.ps1

python.exe main.py --default
```
## Example Output

Original model size:
12.4 MB

Quantized model size:
3.3 MB

Reduction:
73%

Backend:
HTP (NPU)

Precision:
INT8

## FAQ

### ERROR: WindowsFileIO couldn't open libcdsprpc.dll

Windows host cannot access DSP libraries.
DSP execution is available only on supported Qualcomm devices.

### Why is INT4 not available?

Current QAIRT public releases primarily target INT8 deployment.


## Setup environment
```bash
py -3.10 -m venv ".venv"
& ".venv\Scripts\Activate.ps1"
```
```bash
python -m pip install --upgrade pip
```
```bash
pip install ultralytics==8.4.58
            onnx==1.21.0
            onnxruntime==1.23.2
            qairt-visualizer==0.8.0 
            tflite==2.18.0
```
```bash
Unblock-File ./v2.47.0.260601/qairt/2.47.0.260601/bin/envsetup.ps1
./v2.47.0.260601/qairt/2.47.0.260601/bin/envsetup.ps1
```
you should get something like:
```bash
[INFO] QAIRT_SDK_ROOT: C:\**********\Qualcomm QAIRT SDK MODEL QUANTISATION\v2.47.0.260601\qairt\2.47.0.260601
[INFO] QAIRT SDK environment setup complete
```

```bash
Unblock-File "${QAIRT_SDK_ROOT}/bin/check-windows-dependency.ps1"
& "${QAIRT_SDK_ROOT}/bin/check-windows-dependency.ps1"
```
When you have installed all the necessary dependencies, the script will say “All Done”.
```bash
Unblock-File "${QAIRT_SDK_ROOT}/bin/envcheck.ps1"
& "${QAIRT_SDK_ROOT}/bin/envcheck.ps1" -m
```
Update all dependencies by running the following commands in Powershell:
```bash
python "$env:QAIRT_SDK_ROOT\bin\check-python-dependency"
```
Coppy next Qualcomm SDK lib from ./Qualcomm QAIRT SDK MODEL QUANTISATION/v2.47.0.260601/qairt/2.47.0.260601/lib/python to ./src
```bash
./v2.47.0.260601/qairt/2.47.0.260601/lib/python/qairt -> ./src/qairt
./v2.47.0.260601/qairt/2.47.0.260601/lib/python/qti -> ./src/qti
```
For testing......
```bash
.venv\Scripts\Activate.ps1

Unblock-File ./v2.47.0.260601/qairt/2.47.0.260601/bin/envsetup.ps1
./v2.47.0.260601/qairt/2.47.0.260601/bin/envsetup.ps1

python.exe main.py --default
```

pip freeze > requirements.txt
