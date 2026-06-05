import qairt
from qairt.api.converter.converter_config import CalibrationConfig



model_name = "yolo11n"


class get_model():
    def __init__(self,calibrate_dataset):
        self.calibration_config = CalibrationConfig(dataset= calibrate_dataset,
                                       per_channel_quantization=True,
                                       batch_size=1, 
                                       weights_precision=8 
                                       )
        print("calibration config...")
        print(self.calibration_config)
    
    def convert_model(self):
        print("Converting the onnx model to a QAIRT model using calibration data...")

        converted_model: qairt.Model = qairt.convert(
                        f"./models/{model_name}_split.onnx",
                        calibration_config=self.calibration_config,
                        #output_path=f"./models/{model_name}_f32.dlc"
                        backend="HTP" )



get_model= get_model('calibration_data.txt')
get_model.convert_model()