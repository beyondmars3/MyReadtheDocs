# mysql
1. 官方文档： https://dev.mysql.com/doc/refman/5.7/en/
2. 中文： https://www.mysqlzh.com/

## mysqlbinlog
1. MySQL主从复制：MySQL Replication在Master端开启binlog，Master把它的二进制日志传递给slaves来达到
master-slave数据一致的目的。
2. 自然就是数据恢复了，通过使用mysqlbinlog工具来使恢复数据。
   
## 事务隔离级别
1. 未提交读（脏读）
2. 默认是 可重复读
3. 事务隔离级别，实现原理是
4. mvcc 多版本控制 事务开始的时候做一个快照，每一行记录会有多个版本

## 事务特征
1. 事务是 一组操作抽象的逻辑单元
2. 特征是 acid。 原子性，隔离性，一致性，持久性
   
## 锁
1. 共享锁S 可以并发的读，但不能并发写 select ... lock in share mode:
2. 排他锁 select ... for update
3. 间隙锁
4. 是么时候加锁，insert、delete和update都是会加排它锁(Exclusive Locks)的，而select只有显式声明才会加锁

## 三大范式
1. 表的字段单一属性，不可以再拆分
2. 确保表中的每列都和主键相关
3. 每列都与主键有直接关系，不存在传递依赖，非主键字段不能相互依赖
   
## 索引 
1. 参考 https://tech.meituan.com/2014/06/30/mysql-index.html
2. 真实的情况是，3层的b+树可以表示上百万的数据，如果上百万的数据查找只需要三次IO，性能提高将是巨大的，如果没有索引，每个数据项都要发生一次IO，那么总共需要百万次的IO，显然成本非常非常高. 
3. 建索引的几大原则： 
```
    1. 最左前缀匹配原则. mysql会一直向右匹配直到遇到范围查询(>、<、between、like)就停止匹配
    2. 尽量选择区分度高的列作为索引
    3. 索引列不能参与计算
```
4. explain 查询优化神器 rows是核心指标

## 一致性非锁定读和一致性锁定读


## 死锁产生和解决
1. 相互等待锁的释放
2. 加锁顺序不一致