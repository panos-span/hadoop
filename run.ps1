$i = 0
while ($true) {
    hadoop jar ../../../../usr/lib/hadoop-mapreduce/hadoop-streaming.jar -file centers.txt -file ./mapper.py -mapper ./mapper.py -file ./reducer.py -reducer ./reducer.py -input /testMapReduce/dataset -output "/testMapReduce/mapreduce-output$i"
    Remove-Item centers.txt
    hadoop fs -copyToLocal "/testMapReduce/mapreduce-output$i/part-00000" centers.txt
    $seeiftrue = Select-String -Path centers.txt -Pattern "Converged"
    if ($seeiftrue) {
        Remove-Item centroids.txt
        hadoop fs -copyToLocal "/testMapReduce/mapreduce-output$i/part-00000" centers.txt
        break
    } else {
        Remove-Item centroids.txt
        hadoop fs -copyToLocal "/testMapReduce/mapreduce-output$i/part-00000" centers.txt
    }
    $i++
}