import pysam
import argparse

def parser(): 
  parser = argparse.ArgumentParser(description='Split bam files into pseudo-replicates.')
  parser.add_argument('-i','--input', nargs="+",dest='input',type=str,action='store',
                     default="",required=True,
                    help='input bam files')

  parser.add_argument('-n','--name', nargs="?",dest='name', type=str, action='store',
                     default="NA",
                    help='sample name')

  parser.add_argument('-r','--pseudo-rep', nargs="?",dest='rep', type=int, action='store',
                     default=2,
                    help='pseudo replicate number')

  args = parser.parse_args()
  return args

  
def main():
  args = parser()
  print(args)
  for infile in args.input: 
    with pysam.Samfile( 

if __name__ == "__main__":
  main()
