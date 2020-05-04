# elasticsearch-scroll-and-dump
A simple python script to scroll over an index and dump it to a file. 

This relies on the [Elasticsearch Python libraries](https://pypi.org/project/elasticsearch/), which can be installed using `pip install elasticsearch`. 

For a version of this code that does not require additional libraries (and that therefore doesn't take advantage of built-in error handling, connection pooling, etc.), see:
[Elasticsearch scroll and dump without dependencies](https://github.com/alexander-marquardt/elasticsearch-scroll-and-dump-without-dependencies). 
