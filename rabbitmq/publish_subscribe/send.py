#-*-coding:utf-8-*-
import pika

if __name__=="__main__":
    #验证信息
    credentials=pika.PlainCredentials("admin","admin")
    #创建连接
    connection=pika.BlockingConnection(pika.ConnectionParameters("58.87.97.238", 5672, "/",credentials))
    #创建管道
    channel=connection.channel()
    #定义转换器
    channel.exchange_declare(exchange="log",exchange_type="fanout")
    #发送消息
    channel.basic_publish(exchange="log",routing_key="",body="发送和订阅模式")
    #关闭连接
    connection.close()