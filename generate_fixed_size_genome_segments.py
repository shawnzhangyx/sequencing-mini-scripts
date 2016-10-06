#### This scripts will take a genome chrom sizes and generate tiling 1k windows along the chromosomes. 
#Usage: python generate_1k_window.py [options] mm10.chrom.sizes output
################
import sys

INTERVAL=1000

def main(argv):
  chrom_file = open(argv[1],'r')
  out_file = open(argv[2],'w')
  chrom_dict = dict()
  for line in chrom_file:
    words = line.strip().split()
    chrom_dict[words[0]] = int(words[1])
    
  # only keep chroms from chr1 to chrY
  std_chr_name = range(1,100)
  std_chr_name.extend(['X','Y'])
  std_chr = ['chr'+str(x) for x in std_chr_name]
  for chr in chrom_dict.keys(): 
    if chr not in std_chr: 
      chrom_dict.pop(chr,None)
  
  print(chrom_dict)
  print(len(chrom_dict))

  for chr in chrom_dict: 
  # write the chromosome 
    for pos in range(1,chrom_dict[chr],INTERVAL):
        out_file.write('\t'.join([chr,str(pos),str(pos-1+INTERVAL)])+'\n')

if __name__ == "__main__":
  main(sys.argv)
