## Generated Story 0
        * greet
            - utter_greet
        * appointment{"appointment": "appointment"}
            - utter_ask_location
        * location{"location": "ANKARA"}
            - utter_ask_department
        * department{"department": "child nephrology"}
            - slot{"department": "child nephrology"}
            - action_doctor
            - slot{"department": "child nephrology"}
            - utter_ask_date
        * date{"date": "next sunday"}
            - utter_ask_doctor

        * inform{"doctor": "Prof. Dr. Öznur Öken"}
            -utter_ask_tc
        * goodbye
            - utter_goodbye
