#### This scripts will take a genome chrom sizes and generate tiling 1k windows along the chromosomes. 
#Usage: python generate_1k_window.py [options] peakFile outFile
################
import sys

HALF_INTERVAL=500
INTERVAL=HALF_INTERVAL*2
MIN_OVERLAP=0.2

def generate_fixed_size_from_peak(chr,start,end,out_file):
  '''generate fixed size peaks from the center'''
  min_overlap = (start-end)*MIN_OVERLAP
  mid = (start+end)/2
  left = mid-HALF_INTERVAL
  right = mid+HALF_INTERVAL
  # generate the segment covering peak center
  out_file.write('\t'.join([chr,str(left),str(right)])+'\n')
  # generate the segments on the left boundary
  while (left-start)> min_overlap: 
    out_file.write('\t'.join([chr,str(left-INTERVAL),str(left)])+'\n')
    left 


def main(argv):
  peak_file = open(argv[1],'r')
  out_file = open(argv[2],'w')
  chrom_dict = dict()
  for line in peak_file:
    words = line.strip().split()
    chr,start,end = words[0],int(words[1]),int(words[2])
    generate_fixed_size_from_peak(chr,start,end)
    

if __name__ == "__main__":
  main(sys.argv)
