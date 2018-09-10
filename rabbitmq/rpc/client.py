#-*-coding:utf-8-*-
import pika
import uuid


class FibonacciRpcClient(object):
    def __init__(self):
        # 验证信息
        credentials = pika.PlainCredentials("admin", "admin")
        # 创建连接
        self.connection = pika.BlockingConnection(pika.ConnectionParameters("58.87.97.238", 5672, "/", credentials))
        #创建管道
        self.channel=self.connection.channel()
        #定义队里
        result=self.channel.queue_declare(exclusive=True)
        self.callback_queue=result.method.queue
        self.channel.basic_consume(self.on_response,queue=self.callback_queue,no_ack=True)

    def on_response(self,ch,method,props,body):
        if self.corr_id==props.correlation_id:
            self.response=body

    def call(self,n):
        self.response=None
        self.corr_id=str(uuid.uuid4())
        self.channel.basic_publish(
            exchange="",routing_key="rpc_queue",
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
                ),body=str(n))
        while self.response is None:
                self.connection.process_data_events()
        return int(self.response)

if __name__=="__main__":
    fibonacci_rpc = FibonacciRpcClient()
    response=fibonacci_rpc.call(30)
    print(response)