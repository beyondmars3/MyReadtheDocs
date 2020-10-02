# kafka

## ack
1. 生产者发送消息的时候，确保发送消息不丢失
2. 0: Producer 不等待 Broker 的 ACK
3. 1: Partition 的 Leader 落盘成功后返回 ACK
4. -1: Partition 的 Leader 和 Follower 全部落盘成功后才返回 ACK

## Follower Leader
1. 每个分区都有若干个副本，一个 Leader 和若干个 Follower。
2. 生产者发送数据的对象，以及消费者消费数据的对象，都是 Leader

## ISR
1. 和 Leader 保持同步的 Follower 集合。
2. 当 ISR 集合中的 Follower 完成数据的同步之后，Leader 就会给 Follower 发送 ACK。

如果 Follower 长时间未向 Leader 同步数据，则该 Follower 将被踢出 ISR 集合，该时间阈值由 replica.lag.time.max.ms 参数设定。Leader 发生故障后，就会从 ISR 中选举出新的 Leader。


## Exactly Once 语义
1. 
