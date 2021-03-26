import argparse

parser = argparse.ArgumentParser(description='Example with long option names')

# Where to find data
parser.add_argument('--data_path', default=None)
parser.add_argument('--vocab_path', default=None)

# Important settings
parser.add_argument('--mode', default='train',  choices=['train', 'eval', 'decode'])
parser.add_argument('--single_pass', default=False)
parser.add_argument('--decode_after', default=0)
parser.add_argument('--decode_from', default='train')

# Where to save output
parser.add_argument('--log_root', default='')
parser.add_argument('--exp_name', default='')

# batcher parameter, for consistent results, set all these parameters to 1
parser.add_argument('--example_queue_threads', default=4)
parser.add_argument('--batch_queue_threads', default=2)
parser.add_argument('--bucketing_cache_size', default=100)

print(parser.parse_args())

if __name__ == "__main__":
    parser.parse_args()
    #parser.print_help()