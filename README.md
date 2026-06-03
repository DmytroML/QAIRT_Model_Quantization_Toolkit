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
## 
download (https://softwarecenter.qualcomm.com/catalog/item/Qualcomm_AI_Runtime_Community?osArch=Any&osType=All&version=2.47.0.260601)

[text] by default did use https://ultralytics.com/assets/coco128.zip dataset      




pip freeze > requirements.txt
