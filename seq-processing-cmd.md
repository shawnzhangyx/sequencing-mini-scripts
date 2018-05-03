#bamtoBigWig
bamCoverage --bam input.bam --outFileFormat bigwig --outFileName output.rpkm.bw --binSize 25 --numberOfProcessors 4 --normalizeUsingRPKM
