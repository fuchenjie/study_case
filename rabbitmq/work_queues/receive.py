#-*-coding:utf-8-*-
import pika


def callback(ch,method,properties,body):
    print(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)



if __name__=="__main__":
    #认证信息
    credentials=pika.PlainCredentials("admin","admin")
    #创建连接
    connection=pika.BlockingConnection(pika.ConnectionParameters("58.87.97.238", 5672, "/",credentials))
    #创建管道
    channel=connection.channel()
    #声明队列
    channel.queue_declare(queue="work_queues",durable=True)
    #限制一次接收一个
    channel.basic_qos(prefetch_count=1)
    #接收信息
    channel.basic_consume(callback,queue="work_queues",no_ack=False)
    #等待数据并运行回调
    channel.start_consuming()
