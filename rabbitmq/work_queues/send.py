# -*-coding:utf-8-*-
import pika

if __name__ == "__main__":
    # 认证信息
    credentials = pika.PlainCredentials("admin", "admin")
    # 创建连接
    connection = pika.BlockingConnection(pika.ConnectionParameters("58.87.97.238", 5672, "/", credentials))
    # 创建管道
    channel = connection.channel()
    # 声明队列 durable:持久的
    channel.queue_declare(queue="work_queues",durable=True)
    # 发送信息
    channel.basic_publish(exchange="", routing_key="work_queues", body="竞争者模式1",
                          properties=pika.BasicProperties(
                              delivery_mode=2 #设置属性传递类型为2,使消息持久
                          ))
    # 关闭连接
    connection.close()
