#filter reads with low mapping quality
samtools view -@ 4 -F 1804 -q 10 -b input.bam > output.bam
#remove PCR duplicates 
java -Xmx12G -XX:ParallelGCThreads=3 -jar picard.jar TMP_DIR=tmp INPUT=input.bam OUTPUT=output.bam METRICS_FILE=qc.txt VALIDATION_STRINGENCY=LENIENT ASSUME_SORTED=true REMOVE_DUPLICATES=True
#bamtoBigWig
bamCoverage --bam input.bam --outFileFormat bigwig --outFileName output.rpkm.bw --binSize 25 --numberOfProcessors 4 --normalizeUsingRPKM
