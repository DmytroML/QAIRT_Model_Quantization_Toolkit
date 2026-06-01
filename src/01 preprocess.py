# Copyright (c) 2024 Qualcomm Innovation Center, Inc. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause-Clear

import cv2
import sys
import os
import numpy as np
import argparse
import glob
import os


def letterbox(im, new_shape=(640, 640), color=(114, 114, 114), auto=True, scale_fill=False, scale_up=True, stride=32):
    """
    Resize and pad image while meeting stride-multiple constraints.
    """
    shape = im.shape[:2]  # current shape [height, width]
    if isinstance(new_shape, int):
        new_shape = (new_shape, new_shape)
    
    # Scale ratio (new / old)
    r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
    if not scale_up:  # only scale down, do not scale up (for better val mAP)
        r = min(r, 1.0)
    
    # Compute padding
    ratio = r, r  # width, height ratios
    new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))
    dw, dh = new_shape[1] - new_unpad[0], new_shape[0] - new_unpad[1]  # wh padding
    
    if auto:  # minimum rectangle
        dw, dh = np.mod(dw, stride), np.mod(dh, stride)  # wh padding
    elif scale_fill:  # stretch
        dw, dh = 0.0, 0.0
        new_unpad = (new_shape[1], new_shape[0])
        ratio = new_shape[1] / shape[1], new_shape[0] / shape[0]  # width, height ratios
    
    dw /= 2  # divide padding into 2 sides
    dh /= 2
    
    if shape[::-1] != new_unpad:  # resize
        im = cv2.resize(im, new_unpad, interpolation=cv2.INTER_LINEAR)

    top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
    left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
    im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)  # add border
    return im



def main(input_dir, output_dir, is_nchw, is_uint8):
    #python preprocess.py <INPUT PATH> <OUTPUT PATH> 1 0
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.raw')
            output_path_img = os.path.join(output_dir, os.path.splitext(filename)[0] + '.jpg')
            image = cv2.imread(input_path)
            
            # Keep aspect ratio and resize
            # img = letterbox(image, 320, stride=32, auto=False)
            img = letterbox(image, 640, stride=32, auto=False)
            cv2.imwrite(output_path_img, img)
            # BGR -> RGB
            img = img[:, :, ::-1]

            if is_nchw:
                img = np.transpose(img, (2, 0, 1))
                
            print(f"Processed {filename}: {img.shape}")

            if is_uint8:
                numpy_img = np.asarray(img).astype(np.uint8)               
            else:
                img = img / 255
                numpy_img = np.asarray(img).astype(np.float32)
            #img = img / 255
            numpy_img = np.asarray(img).astype(np.float32)
            print (numpy_img.shape)
            numpy_img.tofile(output_path)



def create_file_list(input_dir, output_filename, ext_pattern, print_out=False, rel_path=False):
    input_dir = os.path.abspath(input_dir)
    output_filename = os.path.abspath(output_filename)
    output_dir = os.path.dirname(output_filename)

    if not os.path.isdir(input_dir):
        raise RuntimeError('input_dir %s is not a directory' % input_dir)

    if not os.path.isdir(output_dir):
        raise RuntimeError('output_filename %s directory does not exist' % output_dir)

    glob_path = os.path.join(input_dir, ext_pattern)
    file_list = glob.glob(glob_path)

    if rel_path:
        file_list = [os.path.relpath(file_path, output_dir) for file_path in file_list]

    if len(file_list) <= 0:
        if print_out: print('No results with %s' % glob_path)
    else:
        with open(output_filename, 'w') as f:
            f.write('\n'.join(file_list))
            if print_out: print('%s created listing %d files.' % (output_filename, len(file_list)))








if __name__ == "__main__":


    input_dir = './coco128/images/'
    output_dir = './RAW1'
    is_nchw = 0
    is_uint8 = 1 #####0 calibrate 1 validate
    main('./coco128/images/train2017','./coco128/RAW',1,0)
    create_file_list('./coco128/RAW', '02_calibrate_dataset_list.txt', '*.raw', print_out=True, rel_path=False)
    #main('./test_input','./test_RAW',1,0)
    #create_file_list('./test_RAW', '02_validate_dataset_list.txt', '*.raw', print_out=True, rel_path=False)