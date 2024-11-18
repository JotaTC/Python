import paho.mqtt.client as mqtt
import threading
#configura o mqtt para funções
usuario = "Username"
senha = "123455"
broker = "mqtt.eclipseprojects.io"
topico = "test_topic1"

#decodificar mensagens recebidas
def on_message(client, userdata, msg):
    mensagem = msg.payload.decode()
    if not mensagem.startswith(f"{usuario}: "):  #impede que o nome do proprio usuário apareca
        print(f"\n{mensagem}")

#configura o envio de mensagens(pub)
pub = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
pub.username_pw_set(usuario, senha)
pub.connect(broker, 1883)

#cofigura o recebimento de mensagens(sub)
sub = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
sub.username_pw_set(usuario, senha)
sub.connect(broker, 1883)
sub.subscribe(topico)
sub.on_message = on_message

#inicio a parte de envio de mensagens
def sub_loop_start():
    sub_loop_start()

def pub_loop_start():
    while True:
        mensagem = input()
        mensagem_formatada = f"{usuario}: {mensagem}"
        pub.publish(topico, mensagem_formatada)
sub.loop_start()

print("Digite suas mensagens:")

#Uso do threding para fazer execução de diversos comando simultaneamente

pub_thread = threading.Thread(target=pub_loop_start())
pub_thread.daemon = True
pub_thread.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Encerrando...")
    sub.loop_stop()
    pub.disconnect()
    sub.disconnect()
#encerra o envio de mensagens
