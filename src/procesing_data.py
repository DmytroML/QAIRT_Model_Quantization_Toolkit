from ultralytics.utils.downloads import download
from ultralytics.data.augment import LetterBox
import os
import cv2
import numpy as np
from pathlib import Path

datasets = 'datasets'

class get_calibration_data():
    def __init__(self,imgsz):
        # This automatically downloads and extracts COCO128 into a '../datasets' folder
        self.url = 'https://ultralytics.com/assets/coco128.zip'
        self.imgsz = imgsz
        # This automatically downloads and extracts COCO128 into a '../datasets' folder
        download(self.url, dir=f'./{datasets}/input', unzip=True)
        self.letterbox = LetterBox(new_shape=(imgsz, imgsz), auto=False, scale_fill=False, scaleup=True, stride=32,)
        self.datasets=datasets


    def process(self):

        #python preprocess.py <INPUT PATH> <OUTPUT PATH> 1 0
        if not os.path.exists(f'./{self.datasets}/input'):
            os.makedirs(f'./{self.datasets}/input')
        if not os.path.exists(f'./{self.datasets}/output'):
            os.makedirs(f'./{self.datasets}/output')

        # os.walk returns root path, subfolders, and filenames for every level
        for dirpath, dirnames, filenames in os.walk(f'./{self.datasets}/input'):
            for filename in filenames:
                # Create the full path to the file inside the subfolder
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                    input_path = os.path.join(dirpath, filename)


                    output_path = os.path.join(f'./{self.datasets}', 'output', os.path.splitext(filename)[0] + '.raw')
                    output_path_img = os.path.join(f'./{self.datasets}', 'output', os.path.splitext(filename)[0] + '.jpg')

                    img = self.letterbox(image=cv2.imread(input_path))

                    cv2.imwrite(output_path_img, img)
                    # BGR -> RGB
                    img = img[:, :, ::-1]
                    img = np.transpose(img, (2, 0, 1))

                    img = img / 255
                    numpy_img = np.asarray(img).astype(np.float32)

                    #img = img / 255
                    numpy_img = np.asarray(img).astype(np.float32)
                    #print (numpy_img.shape)
                    numpy_img.tofile(output_path)
                    print(f"\r...Processing {filename}... ", end='')
        self.create_RAW_list()
    
    def create_RAW_list(self):
        target_path = Path(f'./{self.datasets}/output')
        # Extract names of all items
        contents =  [str(item.resolve()) for item in target_path.iterdir() if ".jpg" not in item.name]
        with open(f'./calibration_data.txt', 'w') as f:
                f.write('\n'.join(contents))




