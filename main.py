from src.import_to_onnx import get_onnx_models
import argparse

def main(args):
    print("options:\
            \n\t-h, --help            show this help message and exit")

    print(args.model_name)
    print(args.imgsz)
    
    #get = get_onnx_models('yolo11s', 640)
    #get.export_model()
    #get.modify_onnx()
    #get.check_results()    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process....."
    )
    parser.add_argument("--imgsz", type=int, default=640, help="input image dimensions")
    parser.add_argument("--model_name", type=str, default="yolo11n", help="Name of the model to use from ultralytics repository")
    parser.add_argument(
                        "--thresholds",
                        type=str,
                        nargs='+',
                        default=[0.25, 0.5, 0.75]
                        , help="input image dimensions"
                    )

    args = parser.parse_args()

    main(args)