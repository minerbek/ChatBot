from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.dispatcher import Button, Element, Dispatcher
import json
import pickle

class ActionWeather(Action):
    def name(self):
        return 'action_doctor'

    def run(self, dispatcher, tracker, domain):

        loc = tracker.get_slot('department')
        #response = tracker.current_slot_values()
        # response = '#' + json.dumps(aaa) + '#'

        if loc == 'algology':
            #response = "Prof. Dr. Öznur Öken"
            buttons = [
                Button(title="Prof. Dr. Öznur Öken", payload="/Dr1")
            ]

        elif loc == 'brain and neurosurgery':
            #response = "1- Doç. Dr. Gülşah Bademci\n2- Doç. Dr. Suat CANBAY"
            buttons = [
                Button(title="Doç. Dr. Gülşah Bademci", payload="/btn1"),
                Button(title="Doç. Dr. Suat CANBAY", payload="/btn2")
            ]

        elif loc == 'child hematology':
            #response = "Prof. Dr. Hatice Emel Özyürek"
            buttons = [
                Button(title="Prof. Dr. Hatice Emel Özyürek", payload="/btn1")
            ]

        elif loc == 'child nephrology':
            #response = "Prof. Dr. Süleyman Kalman"
            buttons = [
                Button(title="Prof. Dr. Süleyman Kalman", payload="/btn1")
            ]

        elif loc == 'child health and illness':
            #response = "1- Prof. Dr. Musa Kazım Çağlar\n2- Prof. Dr. Süleyman Kalman\n3- Prof. Dr. Hatice Emel Özyürek\n4- Yar. Doç. Dr. Pakize Elif Alkış\n5- Uzm. Dr. Mustafa Yücel Kızıltan\n6- Uzm. Dr. Gökalp Başbozkurt\n7- Uzm. Dr. Hafsa Uçur\n8- Uzm. Dr. Hüsniye Altan\n 9- Uzm. Dr. Sarkhan Elbayıyev\n 10- Uzm. Dr. Shahın Guliyev"
            buttons = [
                Button(title="Prof. Dr. Musa Kazım Çağlar", payload="/btn1"),
                Button(title="Prof. Dr. Süleyman Kalman", payload="/btn2"),
                Button(title="Prof. Dr. Hatice Emel Özyürek", payload="/btn3"),
                Button(title="Yar. Doç. Dr. Pakize Elif Alkışn", payload="/btn4"),
                Button(title="Uzm. Dr. Mustafa Yücel Kızıltan", payload="/btn5"),
                Button(title="Uzm. Dr. Gökalp Başbozkurt", payload="/btn6"),
                Button(title="Uzm. Dr. Hafsa Uçur", payload="/btn7"),
                Button(title="Uzm. Dr. Hüsniye Altan", payload="/btn8"),
                Button(title="Uzm. Dr. Sarkhan Elbayıyev", payload="/btn9"),
                Button(title="Uzm. Dr. Shahın Guliyev", payload="/btn10")
            ]
        elif loc == 'dermatology':
            #response = "1- Uzm. Dr. Aylin Gözübüyükoğulları\n2- Uzm. Dr. Yeşim Akpınar Kara"
            buttons = [
                Button(title="Uzm. Dr. Aylin Gözübüyükoğulları", payload="/Dr1"),
                Button(title="Uzm. Dr. Yeşim Akpınar Kara", payload="/Dr2")
            ]
        elif loc == 'diet policlinic':
            #response = "1- Uzm. Dyt. Gaye Başkurt\n2- Dyt. Deniz Özdemir\n3- Dyt. Halime Besler"
            buttons = [
                Button(title="Uzm. Dyt. Gaye Başkurt", payload="/Dr1"),
                Button(title="Dyt. Deniz Özdemir", payload="/Dr2"),
                Button(title="Dyt. Halime Besler", payload="/Dr3")
            ]

        elif loc == 'endocrinology':
            #response = "Prof. Dr. Serdar Güler"
            buttons = [
                Button(title="Prof. Dr. Serdar Güler", payload="/Dr1")
            ]

        elif loc == 'infectious diseases':
            #response = "Uzm. Dr. Mine Işık Arıgün"
            buttons = [
                Button(title="Uzm. Dr. Mine Işık Arıgün", payload="/Dr1")
            ]

        elif loc == 'physical therapy and rehabilitation':
            #response = "1- Prof. Dr. Öznur Öken\n2- Uzm. Dr. Beril Özturan"
            buttons = [
                Button(title="Prof. Dr. Öznur Öken", payload="/Dr1"),
                Button(title="Uzm. Dr. Beril Özturan", payload="/Dr2")
            ]

        elif loc == 'gastroenterology':
            #response = "1- Doç. Dr. Reskan Altun\n2- Doç. Dr. Yasemin Özderin Özin"
            buttons = [
                Button(title="Doç. Dr. Reskan Altun", payload="/Dr1"),
                Button(title="Doç. Dr. Yasemin Özderin Özin", payload="/Dr2")
            ]

        elif loc == 'general surgery':
            #response = "1- Prof. Dr. Mehmet Mahir Özmen\n2- Yar. Doç. Dr. Cem Emir Güldoğan\n3- Yar. Doç. Dr. Emre Gündoğdu"
            buttons = [
                Button(title="Prof. Dr. Mehmet Mahir Özmen", payload="/Dr1"),
                Button(title="Yar. Doç. Dr. Cem Emir Güldoğan", payload="/Dr2"),
                Button(title="Yar. Doç. Dr. Emre Gündoğdu", payload="/Dr3")
            ]

        elif loc == 'chest diseases':
            #response = "Prof. Dr. Uğur Gönüllü"
            buttons = [
                Button(title="Prof. Dr. Uğur Gönüllü", payload="/Dr1")
            ]


        elif loc == 'eye diseases':
            #response = "Op. Dr. Samim Özdeş"
            buttons = [
                Button(title="Op. Dr. Samim Özdeş", payload="/Dr1")
            ]

        elif loc == 'hematology policlinic':
            #response = "Prof. Dr. Oral Nevruz"
            buttons = [
                Button(title="Prof. Dr. Oral Nevruz", payload="/Dr1")
            ]

        elif loc == 'internal diseases':
            #response = "1- Doç. Dr. Beril Akman\n2- Uzm. Dr. Sercan Cansaran\n3- Uzm. Dr. Sevgi Karabuğa\n4- Yar. Doç. Dr. Gökhan Celbek"
            buttons = [
                Button(title="Doç. Dr. Beril Akman", payload="/Dr1"),
                Button(title="Uzm. Dr. Sercan Cansaran", payload="/Dr2"),
                Button(title="Uzm. Dr. Sevgi Karabuğa", payload="/Dr3"),
                Button(title="Yar. Doç. Dr. Gökhan Celbek", payload="/Dr4")
            ]

        elif loc == 'gynecology and Obstetrics':
            #response = "1- Yar. Doç. Dr. Müberra Namlı Kalem\n2- Yar. Doç. Dr. Coşkun Şimşir\n3- Prof. Dr. Ali Ergün\n4- Doç. Dr. Korhan Kahraman\n5- Doç. Dr. Turgut Var\n6- Doç. Dr. Türkan Örnek Gülpınar\n7- Op. Dr. Aslı Yücetürk\n8- Op. Dr. Ebru Yüce\n9- Prof. Dr. Timur Gürgan"
            buttons = [
                Button(title="Yar. Doç. Dr. Müberra Namlı Kalem", payload="/Dr1"),
                Button(title="Yar. Doç. Dr. Coşkun Şimşir", payload="/Dr2"),
                Button(title="Prof. Dr. Ali Ergün", payload="/Dr3"),
                Button(title="Doç. Dr. Korhan Kahraman", payload="/Dr4"),
                Button(title="Doç. Dr. Turgut Var", payload="/Dr5"),
                Button(title="Doç. Dr. Türkan Örnek Gülpınar", payload="/Dr6"),
                Button(title="Op. Dr. Aslı Yücetürk", payload="/Dr7"),
                Button(title="Op. Dr. Ebru Yüce", payload="/Dr8"),
                Button(title="Prof. Dr. Timur Gürgan", payload="/Dr9")
            ]

        elif loc == 'cardiac surgery':
            #response = "1- Prof. Dr. Erol Şener\n2- Yar. Doç. Dr. Emre Boysan\n2- Yar. Doç. Renda Cırcı"
            buttons = [
                Button(title="Prof. Dr. Erol Şener", payload="/Dr1"),
                Button(title="Yar. Doç. Dr. Emre Boysan", payload="/Dr2"),
                Button(title="Yar. Doç. Renda Cırcı", payload="/Dr3")
            ]

        elif loc == 'cardiology':
            #response = "1- Prof. Dr. Erdoğan İlkay\n2- Doç. Dr. Alper Canbay\n3- Uzm. Dr. Çiğdem Koca Tarı\n4- Uzm. Dr. Erol Kalender"
            buttons = [
                Button(title="Prof. Dr. Erdoğan İlkay", payload="/Dr1"),
                Button(title="Doç. Dr. Alper Canbay", payload="/Dr2"),
                Button(title="Uzm. Dr. Çiğdem Koca Tarı", payload="/Dr3"),
                Button(title="Uzm. Dr. Erol Kalender", payload="/Dr4")
            ]

        elif loc == 'ENT diseases':
            #response = "1- Prof. Dr. Ali Altuntaş\n2- Prof. Dr. Serdar Karahatay\n3- Yar. Doç Dr. Canset Aydın"
            buttons = [
                Button(title="Prof. Dr. Ali Altuntaş", payload="/Dr1"),
                Button(title="Prof. Dr. Serdar Karahatay", payload="/Dr2"),
                Button(title="Yar. Doç Dr. Canset Aydın", payload="/Dr3")
            ]

        elif loc == 'nephrology':
            #response = "Doç. Dr. Beril Akman"
            buttons = [
                Button(title="Doç. Dr. Beril Akman", payload="/Dr1")
            ]

        elif loc == 'neurology':
            #response = "1- Prof. Dr. Mehmet Zülküf Önal\n2- Yar. Doç. Dr. Akçay Övünç Ozon"
            buttons = [
                Button(title="Prof. Dr. Mehmet Zülküf Önal", payload="/Dr1"),
                Button(title="Yar. Doç. Dr. Akçay Övünç Ozon", payload="/Dr2")
            ]

        elif loc == 'orthopedics and traumatology':
            #response = "1- Yar. Doç. Dr. Uğur Gönç\n2- Op. Dr. Mesut Atabek\n3- Prof. Dr. levent Çelebi"
            buttons = [
                Button(title="Yar. Doç. Dr. Uğur Gönç", payload="/Dr1"),
                Button(title="Op. Dr. Mesut Atabek", payload="/Dr2"),
                Button(title="Prof. Dr. levent Çelebi", payload="/Dr3")

            ]

        elif loc == 'plastic surgery':
            #response = "1- Op. Dr. Ergin Işık\n2- Op. Dr. Serdar Düzgün"
            buttons = [
                Button(title="Op. Dr. Ergin Işık", payload="/Dr1"),
                Button(title="Op. Dr. Serdar Düzgün", payload="/Dr2")

            ]

        elif loc == 'psychiatry':
            #response = "Prof. Dr. Ali Bozkurt"
            buttons = [
                Button(title="Prof. Dr. Ali Bozkurt", payload="/Dr1")

            ]

        elif loc == 'psychologist':
            #response = "Psk. Ezgi Kılınç"
            buttons = [
                Button(title="Psk. Ezgi Kılınç", payload="/Dr1")

            ]

        elif loc == 'rheumatology':
            #response = "Doç. Dr. Orhan Küçükşahin"
            buttons = [
                Button(title="Doç. Dr. Orhan Küçükşahin", payload="/Dr1")

            ]


        elif loc == 'medical oncology':
            #response = ["Prof. Dr. Fikret Arpacı", "Doç. Dr. Gökhan Erdem"]
            buttons = [
                Button(title="Prof. Dr. Fikret Arpacı", payload="/Dr1"),
                Button(title="Doç. Dr. Gökhan Erdem", payload="/Dr2")

            ]

        elif loc == 'urology':
            response = "Müsait doktor bulunmamaktadır..."

        #response = "abc\n\nasd"

        response=""
        # buttons = [
        #     Button(title="Btn1", payload="/btn1"),
        #     Button(title="Btn2", payload="/btn2")
        # ]
        dispatcher.utter_button_message("my message", buttons)
        return [SlotSet('doctor', response)]
