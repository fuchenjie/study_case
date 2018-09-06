#-*-coding:utf-8-*-
import pika

def callback(ch,method,properties,body):
    print(body)

if __name__=="__main__":
    #验证信息
    credentials=pika.PlainCredentials("admin","admin")
    #创建连接
    connection=pika.BlockingConnection(pika.ConnectionParameters("58.87.97.238", 5672, "/",credentials))
    #创建管道
    channel=connection.channel()
    #定义转换器
    channel.exchange_declare(exchange="log",exchange_type="fanout")
    #定义队列
    result=channel.queue_declare(exclusive=True)
    queue_name=result.method.queue
    #绑定队列和转换器
    channel.queue_bind(exchange="log",queue=queue_name)
    #消费消息
    channel.basic_consume(callback,queue=queue_name,no_ack=True)
    #等待消息并回调
    channel.start_consuming()
