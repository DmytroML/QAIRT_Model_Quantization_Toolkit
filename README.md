# Setup environment
## 1. Create and activate a new virtual environment
py -3.10 -m venv ".venv"
& ".venv\Scripts\Activate.ps1"
## 2. Update all dependencies by running the following commands in Powershell:
python -m pip install --upgrade pip
## 3. Install next python lib:
pip install ultralytics==8.4.58
            onnx==1.21.0

            




pip freeze > requirements.txt
