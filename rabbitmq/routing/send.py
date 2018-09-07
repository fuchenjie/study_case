#-*-coding:utf-8-*-
import pika


if __name__=="__main__":
    #验证信息
    credentials=pika.PlainCredentials("admin","admin")
    #创建连接
    connection=pika.BlockingConnection(pika.ConnectionParameters("58.87.97.238", 5672, "/",credentials))
    #创建管道
    channel=connection.channel()
    #定义转换器 direct topic主题类型 headers  fanout
    channel.exchange_declare(exchange="direct_message",exchange_type="direct")
    #发送消息
    channel.basic_publish(exchange="direct_message",routing_key="type2",body="有选择的接收消息")
    #关闭连接
    connection.close()