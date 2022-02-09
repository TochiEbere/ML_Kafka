import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Parses args to CNN pipeline", 
        allow_abbrev=False)

    parser.add_argument('--image_path', type=str,
                        help='Full path to image')
    
    parser.add_argument('--labels', type=str,
                        help='Json file of labels')

    parser.add_argument('--model_path', type=str,
                        help='Full path to CNN model')

    parser.add_argument('--target_size', type=int,
                        default=28,
                        help='Dimension to which input image will be resized')  
    
    parser.add_argument('--data_source', type=str,
                        default='fashion_mnist',
                        help='Either fashion_mnist or custom')
    
    args = parser.parse_args()
    return args

