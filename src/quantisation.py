import qairt
from qairt.api.converter.converter_config import CalibrationConfig
from qairt.api.compiler.config_util import HtpGraphConfig


model_name = "yolo11n_split"
soc_details = "chipset:QCS6490"

class processing_model():
    def __init__(self,calibrate_dataset, model_name=model_name, soc_details=soc_details):

        self.model_name = f"{model_name}"
        self.soc_details = soc_details
        self.calibration_config = CalibrationConfig(dataset= calibrate_dataset
                                        ,per_channel_quantization=True
                                        ,batch_size=1 
                                        ,weights_precision=8 
                                        ,num_of_samples=512 
                                        ,act_precision=8 
                                        ,bias_precision=8)
        # Step 5: Compile the model for HTP backend
        print("Compiling the model for HTP backend...")

        self.htp_graph_config = HtpGraphConfig(name=self.model_name,
                                                vtcm_size_in_mb=0)
        # Compile the model for a particular SOC  
        self.compile_config =  qairt.CompileConfig(backend="HTP"
                                            , soc_details=self.soc_details
                                            ,graph_custom_configs=[self.htp_graph_config]
                                            )  
        #print("======================================================================================")
        #print("calibration config....................................................................")
        #print(self.calibration_config)
        #print("htp_graph_config config...............................................................")
        #print(self.htp_graph_config)       
        #print("compile_config config.................................................................")
        #print(self.compile_config)    
        #print("======================================================================================")

    def convert_model(self) -> qairt.Model:
        print("Converting the onnx model to a QAIRT model using calibration data...")

        converted_model: qairt.Model = qairt.convert(
                        f"./models/{self.model_name}.onnx",
                        calibration_config=self.calibration_config,
                        backend="HTP" )
        print("======================================================================================")
        print("Model conversion complete!")
        print(f"Converted model input tensors: {converted_model.input_tensors}")
        print(f"Converted model output tensors: {converted_model.output_tensors}")
        print(f"Converted model name: {converted_model.name}")
        converted_model.save(f"./models/{self.model_name}_w8a8.dlc")
        print("======================================================================================")
        return converted_model



    def compiled_model(self,converted_model: qairt.Model) -> qairt.CompiledModel:
        print("Converting the onnx model to a QAIRT model using calibration data...")

        compiled_model: qairt.CompiledModel = qairt.compile(converted_model
                                                            ,config=self.compile_config                                       
                                                            
                                                            )
        print("======================================================================================")
        print("Model compilation complete!")
        print(f"compiled_model input tensors: {compiled_model.input_tensors}")
        print(f"compiled_model output tensors: {compiled_model.output_tensors}")
        compiled_model.save(f"./models/{self.model_name}.bin")
        print("======================================================================================")


#processing_model= processing_model('calibration_data.txt', model_name="yolo11n_split")
##converted_model = processing_model.convert_model()
#processing_model.compiled_model(converted_model)