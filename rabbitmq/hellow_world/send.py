#-*-coding:utf-8-*-
import pika


if __name__=="__main__":
    message="测试消息"
    #认证信息
    credentials=pika.PlainCredentials("admin","admin")
    #创建连接
    connection=pika.BlockingConnection(pika.ConnectionParameters("58.87.97.238",5672,"/",credentials))
    #创建管道
    channel=connection.channel()
    #声明队列
    channel.queue_declare(queue="queue")
    #发送消息
    channel.basic_publish(exchange="",routing_key="queue",body=message)
    #关闭管道
    channel.close()

