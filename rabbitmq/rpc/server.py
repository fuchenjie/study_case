#-*-coding:utf-8-*-
import pika


def on_request(ch,method,properties,body):
    body="数据已加工"
    ch.basic_publish(exchange="",
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(correlation_id=properties.correlation_id),
                     body=str(body))
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(body)


#远程调用
if __name__=="__main__":
    #验证信息
    credentials=pika.PlainCredentials("admin","admin")
    #创建连接
    connection=pika.BlockingConnection(pika.ConnectionParameters("58.87.97.238", 5672, "/",credentials))
    #创建管道
    channel=connection.channel()
    #定义队列
    channel.queue_declare(queue="rpc_queue")
    #设置每次获取一条信息
    channel.basic_qos(prefetch_count=1)
    #发送消息
    channel.basic_consume(on_request,queue="rpc_queue",no_ack=False)
    channel.start_consuming()
