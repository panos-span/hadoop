#!/bin/bash
i=0
while :
do
	hadoop jar ../../../../usr/lib/hadoop-mapreduce/hadoop-streaming.jar -file centers.txt -file ./mapper.py -mapper ./mapper.py -file ./reducer.py -reducer ./reducer.py -input /testMapReduce/dataset -output /testMapReduce/mapreduce-output$i
	rm -f centers.txt
	hadoop fs -copyToLocal /testMapReduce/mapreduce-output$i/part-00000 centers.txt
	seeiftrue=`cat centers.txt | grep "Converged"`
	if [ $seeiftrue = 1 ]
	then
		rm centroids.txt
		hadoop fs -copyToLocal /testMapReduce/mapreduce-output$i/part-00000 centers.txt
		break
	else
		rm centroids.txt
		hadoop fs -copyToLocal /testMapReduce/mapreduce-output$i/part-00000 centers.txt
	fi
	i=$((i+1))
done