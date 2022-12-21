argv = commandArgs(trailing=T)
if (length(argv)<3) {
  exit("Rscript [prog] [fai file] [peak file] [out file]")
  }

genome = argv[1]
peak = argv[2]
out = argv[3]


chrom = read.table(genome,stringsAsFactors=F)
## currently support human or mouse. 
chrom = chrom[which(chrom$V1 %in% paste0("chr",c(1:22,"X"))),]

#N = 10

pos = 0
for (i in 1:nrow(chrom)){ 
  chrom$V3[i] = pos
  pos = pos+ chrom$V2[i]
  }

lists = read.table(peak)
widths = lists$V3-lists$V2

#for (w in widths ){

rand = runif(length(widths),min=0,max=chrom[nrow(chrom),3])

find_chr = function(num){
  tail(which(chrom$V3< num),1)
  }

idx = sapply(1:length(rand), function(x){ find_chr(rand[x])})

chr = chrom[idx,1]
start = floor(rand - chrom[idx,3])
end = start + widths


write.table(data.frame(chr,start,end),out,row.names=F,
  col.names=F, sep='\t',quote=F)

