# Setup environment
## 1. Create and activate a new virtual environment
```bash
py -3.10 -m venv ".venv"
& ".venv\Scripts\Activate.ps1"
```
## 2. Update all dependencies by running the following commands in Powershell:
```bash
python -m pip install --upgrade pip
```
## 3. Install next python lib:
```bash
pip install ultralytics==8.4.58
            onnx==1.21.0
            onnxruntime==1.23.2
            qairt-visualizer==0.8.0 
            tflite==2.18.0
```
## 4. [Install Qualcomm SDK](https://docs.qualcomm.com/doc/80-63442-10/topic/windows_setup.html#step-1-install-qualcomm-ai-engine-direct-aka-the-qnn-sdk) to curent .venv
### 4.1. [Download the Qualcomm SDK](https://softwarecenter.qualcomm.com/catalog/item/Qualcomm_AI_Runtime_Community?osArch=Any&osType=All&version=2.47.0.260601) and unzip 
### 4.2. Setup the environment using the below commands:
```bash
Unblock-File ./v2.47.0.260601/qairt/2.47.0.260601/bin/envsetup.ps1
./v2.47.0.260601/qairt/2.47.0.260601/bin/envsetup.ps1
```
you should get something like:
```bash
[INFO] QAIRT_SDK_ROOT: C:\**********\Qualcomm QAIRT SDK MODEL QUANTISATION\v2.47.0.260601\qairt\2.47.0.260601
[INFO] QAIRT SDK environment setup complete
```
### 4.3. Run Unblock-File "${QAIRT_SDK_ROOT}/bin/check-windows-dependency.ps1"
### 4.4. Run & "${QAIRT_SDK_ROOT}/bin/check-windows-dependency.ps1"
When you have installed all the necessary dependencies, the script will say “All Done”.
### 4.5. Run Unblock-File "${QAIRT_SDK_ROOT}/bin/envcheck.ps1"
### 4.6. Run & "${QAIRT_SDK_ROOT}/bin/envcheck.ps1" -m
## 5. Step 2: Install QNN SDK dependencies
### 5.1. Update all dependencies by running the following commands in Powershell:
```bash
python "$env:QAIRT_SDK_ROOT\bin\check-python-dependency"
```
### 5.2. Coppy next Qualcomm SDK lib from ./Qualcomm QAIRT SDK MODEL QUANTISATION/v2.47.0.260601/qairt/2.47.0.260601/lib/python to ./src
```bash
./v2.47.0.260601/qairt/2.47.0.260601/lib/python/qairt -> ./src/qairt
./v2.47.0.260601/qairt/2.47.0.260601/lib/python/qti -> ./src/qti
```
## 6. RUN
For testing......
```bash
.venv\Scripts\Activate.ps1

Unblock-File ./v2.47.0.260601/qairt/2.47.0.260601/bin/envsetup.ps1
./v2.47.0.260601/qairt/2.47.0.260601/bin/envsetup.ps1

python.exe main.py --default
```

pip freeze > requirements.txt
