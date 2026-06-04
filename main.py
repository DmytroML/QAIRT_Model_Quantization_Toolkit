from src.import_to_onnx import get_onnx_models
import src.procesing_data as procesing_data
import argparse
import v2.47.0.260601


def main(args):
    print("options:\
            \n\t-h, --help            show this help message and exit")
    get = get_onnx_models(args.model_name, args.imgsz)

    if args.default:
        print(args.model_name)
        print(args.imgsz)
        print(args.default)  # True   
        
        get.import_model()
        get.modify_onnx()
        get.check_results()   
        procesing_data.get_calibration_data(args.imgsz).process() 

    if 'import' in args.import_mode:
        print('import....')
        get.import_model()
    if 'modify' in args.import_mode:
        print('modify....')
        get.modify_onnx()
    if 'check' in args.import_mode:
        print('check....')
        get.check_results()
    if 'check' in args.import_mode:
        print('check....')
        get.check_results()
    if 'getROW' in args.import_mode:
        print('getROW....')
        procesing_data.get_calibration_data(args.imgsz).process() 



    #print(args.import_mode)  # ['import', 'modify', 'check']

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process....."
    )
    parser.add_argument("--imgsz", type=int, default=640, help="input image dimensions")
    parser.add_argument("--model_name", type=str, default="yolo11n", help="Name of the model to use from ultralytics repository")
    parser.add_argument("--default", action="store_true", help="Enable default mode") 
    parser.add_argument(
                        "--import_mode",
                        type=str,
                        nargs='+',
                        default=[None]
                        , help="input model settinds: import, modify, check, getROW"
                    )
    args = parser.parse_args()

    main(args)
