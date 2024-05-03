Flink Mac本地安装、运行
https://blog.csdn.net/smile0198/article/details/114011350
brew install apache-flink

MacOS安装Apache Flink
https://iyichen.xyz/2020/12/mac-install-apache-flink/


# brew install apache-flink

    ......
    Pruned 0 symbolic links and 6 directories from /usr/local
    ==> Caveats
    ==> jenkins-lts
    Note: When using launchctl the port will be 8080.

    To start jenkins-lts now and restart at login:
    brew services start jenkins-lts
    Or, if you don't want/need a background service you can just run:
    /usr/local/opt/openjdk/bin/java -Dmail.smtp.starttls.enable\=true -jar /usr/local/opt/jenkins-lts/libexec/jenkins.war --httpListenAddress\=127.0.0.1 --httpPort\=8080


# flink --version
    Version: 1.19.0, Commit ID: eaffd22
# brew info apache-flink
    ==> apache-flink: stable 1.19.0 (bottled), HEAD
    Scalable batch and stream data processing
    https://flink.apache.org/
    Installed
    /usr/local/Cellar/apache-flink/1.19.0 (171 files, 500.4MB) *
    Poured from bottle using the formulae.brew.sh API on 2024-05-02 at 19:29:52
    From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/a/apache-flink.rb
    License: Apache-2.0
    ==> Dependencies
    Required: openjdk@11 ✔
    ==> Options
    --HEAD
        Install HEAD version
    ==> Analytics
    install: 316 (30 days), 1,049 (90 days), 3,606 (365 days)
    install-on-request: 316 (30 days), 1,049 (90 days), 3,606 (365 days)
    build-error: 0 (30 days)





# cd /usr/local/Cellar/apache-flink/1.19.0
# start-cluster
    /usr/local/Cellar/apache-flink/1.19.0/libexec/bin/start-cluster.sh
    ./libexec/bin/start-cluster.sh
    Starting cluster.
    Starting standalonesession daemon on host 7RP-OFFB-Lhqer.local.
    Starting taskexecutor daemon on host 7RP-OFFB-Lhqer.local.

# 访问地址
http://localhost:8081/

# nc -lk 9999

# run 
/usr/local/Cellar/apache-flink/1.19.0/libexec/bin/flink run /Users/lhqer/MY/2024/idea/flink01/target/flink01-1.0-SNAPSHOT.jar
./libexec/bin/flink run   /Users/lhqer/MY/2024/idea/flink01/target/flink01-1.0-SNAPSHOT.jar

# RuntimeException
Caused by: java.lang.RuntimeException: Record has Long.MIN_VALUE timestamp (= no timestamp marker). Is the time characteristic set to 'ProcessingTime', or did you forget to call 'DataStream.assignTimestampsAndWatermarks(...)'?
查看代码是使用 ProcessingTime还是 EventTime进行业务处理， 如果是使用的事件时间进行处理的业务，则应该指定相应的事件时间和watermark

.window(TumblingEventTimeWindows.of(Time.seconds(8))) //添加滚动窗口 ，采用事件时间进行处理
.window(SlidingProcessingTimeWindows.of(Time.seconds(10),Time.seconds(5))) //添加滑动窗口，采用处理时间进行处理
# run
./libexec/bin/flink run   /Users/lhqer/MY/2024/idea/flink01/target/flink01-1.0-SNAPSHOT.jar
Job has been submitted with JobID ba4f5f3d5fd1cc414ec6a51c2e19c970

# tail
cd /usr/local/Cellar/apache-flink/1.19.0
ls ./libexec/log/
tail -100f libexec/log/flink-lhqer-taskexecutor-0-lhqer.out
tail -100f ./libexec/log/flink-lhqer-taskexecutor-0-7RP-OFFB-Lhqer.local.out



# WindowWordCount
```java
package org.example.flink;

import org.apache.flink.api.common.functions.FlatMapFunction;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.windowing.assigners.SlidingProcessingTimeWindows;
import org.apache.flink.streaming.api.windowing.assigners.TumblingEventTimeWindows;
import org.apache.flink.streaming.api.windowing.time.Time;
import org.apache.flink.util.Collector;


public class WindowWordCount {

    public static void main(String[] args) throws Exception {

        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        DataStream<Tuple2<String, Integer>> dataStream = env
                .socketTextStream("localhost", 9999)
                .flatMap(new Splitter())
                .keyBy(0)
                .window(SlidingProcessingTimeWindows.of(Time.seconds(10),Time.seconds(5))) //添加滑动窗口，采用处理时间进行处理
//                .timeWindow(Time.seconds(5))

                .sum(1);

        dataStream.print();

        env.execute("Window WordCount");
    }

    public static class Splitter implements FlatMapFunction<String, Tuple2<String, Integer>> {
        @Override
        public void flatMap(String sentence, Collector<Tuple2<String, Integer>> out) throws Exception {
            for (String word: sentence.split(" ")) {
                out.collect(new Tuple2<String, Integer>(word, 1));
            }
        }
    }
}
```

