import pika


class RabbitPublisher:
    queue_name = "sales_data"

    def queue_message(self, message: str):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=self.queue_name)
        channel.basic_publish(exchange="",
                              routing_key=self.queue_name,
                              body=message)
        connection.close()


RabbitPublisher().queue_message("HELLO, RABBIT")
