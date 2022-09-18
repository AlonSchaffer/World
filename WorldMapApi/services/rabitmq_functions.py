import pika
#Parameters
HOST = 'localhost'
EXCHANGE_NAME = 'worldapidata'
QUAUE_NAME = 'worldapiquaue'
ROUTE_KEY = 'time-zones'

try:
    #Connect to RabitMq
    rabit_connection = pika.BlockingConnection(pika.ConnectionParameters(HOST))
    channel = rabit_connection.channel()
except Exception as e:
    print('Error in connecting to Rabitmq\n' + str(e))
    exit()

try:
    #Declare Exchange for the world api
    channel.exchange_declare(exchange = EXCHANGE_NAME,
                        exchange_type ='fanout')

    #Declare Quaue for the world api
    channel.queue_declare(queue = QUAUE_NAME)

    #Bind them togather    
    channel.queue_bind(exchange = EXCHANGE_NAME,
                queue= QUAUE_NAME,
                routing_key = ROUTE_KEY
                )
except Exception as e:
    print('Error At rabitmq script: ' + str(e))
    exit()

def send_message_to_quaue(message_body):
    try:
        channel.basic_publish(exchange = EXCHANGE_NAME,
                    body = message_body,
                    routing_key = ROUTE_KEY
                    )
    except Exception as e:
        print('Error in send_message_to_quaue function: ' + str(e))
        exit()
