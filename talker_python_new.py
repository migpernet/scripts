#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker():
    #Iniciar o nó
    rospy.init_node('talker',anonymous=True) 

    #Definir o publisher para o tópico
    chatter_pub = rospy.Publisher('chatter', String, queue_size = 100)
    
    #Defini a taxa de atualização
    rate = rospy.Rate(10)

    #Contador de mensagens
    count = 0
    
    while not rospy.is_shutdown():
        #Criar o texto
        #texto = "Olá mundo! Contagem: " + str(count)
        texto = f'Olá mundo. Contagem: {count}'

        #Mostrar a mensagem no log
        rospy.loginfo(texto)

        #Publicar a mensagem no tópico
        chatter_pub.publish(texto)

        #Pausar
        rate.sleep()

        #Contador
        count+=1

    
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInternalException:
        pass

