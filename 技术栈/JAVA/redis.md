# Redis集群主要有三种模式
    主从复制模式（Master-Slave）、哨兵模式（Sentinel）和Cluster模式。
    主从复制模式：适用于数据备份和读写分离场景，配置简单，但在主节点故障时需要手动切换。
    哨兵模式：在主从复制的基础上实现自动故障转移，提高高可用性，适用于高可用性要求较高的场景。
    Cluster模式：通过数据分片和负载均衡实现大规模数据存储和高性能，适用于大规模数据存储和高性能要求场景。