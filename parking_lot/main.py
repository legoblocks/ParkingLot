import argparse
import yaml
from coordinates_generator import CoordinatesGenerator
from motion_detector import MotionDetector
from colors import *
import logging


def main():
    logging.basicConfig(level=logging.INFO)

    args = parse_args()

    image_file = args.image_file
    data_generate_file = args.data_generate_file
    data_file = args.data_file
    video_file = args.video_file
    start_frame = args.start_frame

    # generate coordinate based data map.
    if image_file is not None and args.data_generate_file:
        with open(data_generate_file, "w+") as points:
            generator = CoordinatesGenerator(image_file, points, COLOR_RED)
            generator.generate()

    # read from coordinate data map
    if data_file is not None and video_file is not None:
        with open(data_file, "r") as data:
            #points = yaml.load(data)
            points = yaml.safe_load(data)
            detector = MotionDetector(video_file, points, int(start_frame))
            detector.detect_motion()


def parse_args():
    parser = argparse.ArgumentParser(description='Generates Coordinates File')

    parser.add_argument("--image",
                        dest="image_file",
                        required=False,
                        help="Image file to generate coordinates on")

    parser.add_argument("--video_file",
                        dest="video_file",
                        #required=True,
                        help="Video file to detect motion on")

    parser.add_argument("--data_generate_file",
                        dest="data_generate_file",
                        #required=True,
                        help="Data file to be used with OpenCV")

    parser.add_argument("--data_file",
                        dest="data_file",
                        #required=True,
                        help="Data file to be used with OpenCV")

    parser.add_argument("--start-frame",
                        dest="start_frame",
                        #required=False,
                        default=1,
                        help="Starting frame on the video")

    return parser.parse_args()


if __name__ == '__main__':
    main()
