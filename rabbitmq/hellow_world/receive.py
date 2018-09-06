#-*-coding:utf-8-*-
import pika


def callback(ch,method,properties,body):
    print(body)


if __name__=="__main__":
    #认证信息
    credentials=pika.PlainCredentials("admin","admin")
    #创建连接
    connection=pika.BlockingConnection(pika.ConnectionParameters( "58.87.97.238", 5672, "/", credentials))
    #创建管道
    channel=connection.channel()
    #声明队列
    channel.queue_declare(queue="queue")
    #接收消息
    channel.basic_consume(callback,queue="queue",no_ack=True)
    # 等待数据并运行回调
    channel.start_consuming()