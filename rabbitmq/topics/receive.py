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
    #定义转换器 topic用于匹配
    channel.exchange_declare(exchange="topic_message",exchange_type="topic")
    #定义队列
    result=channel.queue_declare(exclusive=True)
    queue_name=result.method.queue
    #绑定转换器和队列 *匹配一个单词  #匹配一个或多个单词
    routing_key=["type.*"]
    for item in routing_key:
        channel.queue_bind(exchange="topic_message",queue=queue_name,routing_key=item)
    #接收消息
    channel.basic_consume(callback,queue=queue_name,no_ack=True)
    #等待结果执行回调
    channel.start_consuming()