# Setup environment
## 1. Create and activate a new virtual environment
py -3.10 -m venv ".venv"
& ".venv\Scripts\Activate.ps1"
## 2. Update all dependencies by running the following commands in Powershell:
python -m pip install --upgrade pip
## 3. Install next python lib:
pip install ultralytics==8.4.58
            onnx==1.21.0
            onnxruntime==1.23.2
## 4. [Install Qualcomm SDK](https://docs.qualcomm.com/doc/80-63442-10/topic/windows_setup.html#step-1-install-qualcomm-ai-engine-direct-aka-the-qnn-sdk) to curent .venv
### 4.1. [Download the Qualcomm SDK](https://softwarecenter.qualcomm.com/catalog/item/Qualcomm_AI_Runtime_Community?osArch=Any&osType=All&version=2.47.0.260601) 
or press in your command line 
```bash
wget https://softwarecenter.qualcomm.com/api/download/software/sdks/Qualcomm_AI_Runtime_Community/All/2.47.0.260601/v2.47.0.260601.zip
### 4.2. 

wget https://softwarecenter.qualcomm.com/api/download/software/sdks/Qualcomm_AI_Runtime_Community/All/2.47.0.260601/v2.47.0.260601.zip


[text] by default did use https://ultralytics.com/assets/coco128.zip dataset      



## Qualcomm SDK Installation

### Qualcomm Software Center

1. Sign in to Qualcomm Developer Portal.
2. Open Qualcomm Software Center.
3. Download SDK packages available for your board.
4. Install required components.

pip freeze > requirements.txt
