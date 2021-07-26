
from threading import Thread, Condition
import time
import random

queue = []
MAX_NUM = 10
condition = Condition()

class ProducerThread(Thread):
    def run(self):
        numeros = range(10) #Créera la liste [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
        global queue
        while True:
            condition.acquire()
            if len(queue) == MAX_NUM:
                print ("File d'attente pleine, le producteur attend")
                condition.wait()
                print ("Espace dans la file d'attente, le consommateur a notifié le producteur")
            numero = random.choice(numeros) #Sélectionne un nombre aléatoire dans la liste [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
            queue.append(numero) 
            print ("Le producteur a produit quelque chose dans la file d'attente", numero)
            condition.notify()
            condition.release()
            time.sleep(random.random())


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print ("Rien dans la file d'attente, le consommateur attend")
                condition.wait()
                print ("Le producteur a ajouté quelque chose à la file d'attente et a notifié le consommateur.")
            numero = queue.pop(0)
            print ("Le consommateur a consommé quelque chose dans la file d'attente", numero)
            condition.notify()
            condition.release()
            time.sleep(random.random())


ProducerThread().start()
ConsumerThread().start()
