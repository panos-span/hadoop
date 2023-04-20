$i = 0
while ($true)
{
    hadoop jar C:\hadoop\share\hadoop\tools\lib\hadoop-streaming-3.3.0.jar -file centers.txt -file ./mapper.py -mapper ./mapper.py -file ./reducer.py -reducer ./reducer.py -input /input/data.txt -output "/testMapReduce/mapreduce-output$i"
    Remove-Item centers.txt
    hadoop fs -copyToLocal "/testMapReduce/mapreduce-output$i/part-00000" centers.txt
    $seeiftrue = Select-String -Path centers.txt -Pattern "Converged"
    Remove-Item centers.txt
    hadoop fs -copyToLocal "/testMapReduce/mapreduce-output$i/part-00000" centers.txt
    if ($seeiftrue)
    {
        break
    }
    $i++
}