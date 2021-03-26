from absl import app
from absl import flags

FLAGS = flags.FLAGS

class Seq2Seq(object):
    def main(self, unused_argv):
        print(unused_argv)
        
def main(unused_argv):
  seq2seq = Seq2Seq()
  seq2seq.main(unused_argv)

if __name__ == '__main__':
  app.run()