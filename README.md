
Run The following screipts:


*python -m pip install --upgrade pip*

*pip install -r requirements.txt*

Start the ***kafka zookeper*** service in another terminal:

*bin/zookeeper-server-start.sh config/zookeeper.properties*



Start the kafka server with topic "Republic":

*bin/kafka-console-consumer.sh --topic Republicans --bootstrap-server localhost:9092*




***Installing the ELK stack***

Go to the elastic search directory aand in elasticsearch.yml file, 
set:

 **xpack.security.enabled: false** 

and add the statement:

*ingest.geoip.downloader.enabled: false*

Then start the elastic server by: 

 *bin/elasticsearch*

Next Go to ***Kibana*** directory, delete all the lines in **kibana.yml** and add the folloing lines:

*server.name: kibana*

*server.port: 5601*

*server.host: "0.0.0.0"*

*elasticsearch.hosts: [ "http://localhost:9200" ]*

and save

Next go to the **Logstash** directory, go to the **config** folder and add/replace the **logstash.conf** file given in this repository there. 
The logstash.conf given in this repo contains the Logstash configuration for creating a simple log stream for topic "Republicans". Put the topic name to whatever topic is being run by the kafka broker. In this case, its "Republicans" 

Then run the script to start the logstack pipeline:

*bin/logstash -f config/logstash.conf*


Finally run:

*python3 stream_object.py*

This would generate a stream of Twitter Streams along with their sentiments and their sentiment analysis will be visible on the logstack console and would be sent to Kibana via Elastic search

To visualize the sentiment scores of tweets, go to **localhost:5601** 
This would open Kibana's interface and the index that was specified in logstash.conf file would be visible there, select that and you are all set to do vizaualization and analysis. 

The analysis in this case is the Twitter tweets relating to the topic/Keyword "Republicans" and is avalable in **tweet_analysis.pdf** file in this directory. 

Links to Download:
**kafka**: https://kafka.apache.org/downloads

**Elastic Search**: https://www.elastic.co/downloads/elasticsearch

**Logstash**: https://www.elastic.co/cn/downloads/logstash

**Kibana**: https://www.elastic.co/downloads/kibana









