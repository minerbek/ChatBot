from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

import json
import pickle

class ActionWeather(Action):
    def name(self):
        return 'action_doctor'

    def run(self, dispatcher, tracker, domain):

        loc = tracker.get_slot('department')
        aaa = tracker.current_slot_values()
        response = '#' + json.dumps(aaa) + '#'

        if loc == 'algoloji':
            response = "Prof. Dr. Öznur Öken"

        elif loc == 'beyin sinir ve cerrahisi':
            response = "1- Doç. Dr. Gülşah Bademci\n2- Doç. Dr. Suat CANBAY"

        elif loc == 'çocuk hematoloji':
            response = "Prof. Dr. Hatice Emel Özyürek"

        elif loc == 'çocuk nefrolojisi':
            response = "Prof. Dr. Süleyman Kalman"

        elif loc == 'çocuk sağlığı ve hastalıkları':
            response = "1- Prof. Dr. Musa Kazım Çağlar\n2- Prof. Dr. Süleyman Kalman\n3- Prof. Dr. Hatice Emel Özyürek\n4- Yar. Doç. Dr. Pakize Elif Alkış\n5- Uzm. Dr. Mustafa Yücel Kızıltan\n6- Uzm. Dr. Gökalp Başbozkurt\n7- Uzm. Dr. Hafsa Uçur\n8- Uzm. Dr. Hüsniye Altan\n 9- Uzm. Dr. Sarkhan Elbayıyev\n 10- Uzm. Dr. Shahın Guliyev"

        elif loc == 'dermatoloji':
            response = "1- Uzm. Dr. Aylin Gözübüyükoğulları\n2- Uzm. Dr. Yeşim Akpınar Kara"

        elif loc == 'diyet polikinliği':
            response = "1- Uzm. Dyt. Gaye Başkurt\n2- Dyt. Deniz Özdemir\n3- Dyt. Halime Besler"

        elif loc == 'endokrinoloji':
            response = "Prof. Dr. Serdar Güler"

        elif loc == 'enfeksiyon hastalıkları':
            response = "Uzm. Dr. Mine Işık Arıgün"

        elif loc == 'fizik tedavi ve rehabilitasyon':
            response = "1- Prof. Dr. Öznur Öken\n2- Uzm. Dr. Beril Özturan"

        elif loc == 'gastroenteroloji':
            response = "1- Doç. Dr. Reskan Altun\n2- Doç. Dr. Yasemin Özderin Özin"

        elif loc == 'genel cerrahi':
            response = "1- Prof. Dr. Mehmet Mahir Özmen\n2- Yar. Doç. Dr. Cem Emir Güldoğan\n3- Yar. Doç. Dr. Emre Gündoğdu"

        elif loc == 'gögüs hastalıkları':
            response = "Prof. Dr. Uğur Gönüllü"

        elif loc == 'göz hastalıkları':
            response = "Op. Dr. Samim Özdeş"

        elif loc == 'hematoloji polikinliği':
            response = "Prof. Dr. Oral Nevruz"

        elif loc == 'iç hastalıkları':
            response = "1- Doç. Dr. Beril Akman\n2- Uzm. Dr. Sercan Cansaran\n3- Uzm. Dr. Sevgi Karabuğa\n4- Yar. Doç. Dr. Gökhan Celbek"

        elif loc == 'kadın hastalıkları ve doğum':
            response = "1- Yar. Doç. Dr. Müberra Namlı Kalem\n2- Yar. Doç. Dr. Coşkun Şimşir\n3- Prof. Dr. Ali Ergün\n4- Doç. Dr. Korhan Kahraman\n5- Doç. Dr. Turgut Var\n6- Doç. Dr. Türkan Örnek Gülpınar\n7- Op. Dr. Aslı Yücetürk\n8- Op. Dr. Ebru Yüce\n9- Prof. Dr. Timur Gürgan"

        elif loc == 'kalp ve damar cerrahisi':
            response = "1- Prof. Dr. Erol Şener\n2- Yar. Doç. Dr. Emre Boysan\n2- Yar. Doç. Renda Cırcı"

        elif loc == 'kardiyoloji':
            response = "1- Prof. Dr. Erdoğan İlkay\n2- Doç. Dr. Alper Canbay\n3- Uzm. Dr. Çiğdem Koca Tarı\n4- Uzm. Dr. Erol Kalender"

        elif loc == 'KBB hastalıkları':
            response = "1- Prof. Dr. Ali Altuntaş\n2- Prof. Dr. Serdar Karahatay\n3- Yar. Doç Dr. Canset Aydın"

        elif loc == 'nefroloji':
            response = "Doç. Dr. Beril Akman"

        elif loc == 'nöroloji':
            response = "1- Prof. Dr. Mehmet Zülküf Önal\n2- Yar. Doç. Dr. Akçay Övünç Ozon"

        elif loc == 'ortopedi ve travmatoloji':
            response = "1- Yar. Doç. Dr. Uğur Gönç\n2- Op. Dr. Mesut Atabek\n3- Prof. Dr. levent Çelebi"

        elif loc == 'plastik cerrahi':
            response = "1- Op. Dr. Ergin Işık\n2- Op. Dr. Serdar Düzgün"

        elif loc == 'psikiyatri':
            response = "Prof. Dr. Ali Bozkurt"

        elif loc == 'psikolog':
            response = "Psk. Ezgi Kılınç"

        elif loc == 'romatoloji':
            response = "Doç. Dr. Orhan Küçükşahin"

        elif loc == 'tıbbi onkoloji':
            response = ["Prof. Dr. Fikret Arpacı", "Doç. Dr. Gökhan Erdem"]

        elif loc == 'üroloji':
            response = "Müsait doktor bulunmamaktadır..."

        #response = "abc\n\nasd"

        dispatcher.utter_message(response)
        return [SlotSet('doctor', response)]

