from emailsender_v1 import gmail_send_message as sender
import random

# Viestin otsikko
subject = open("subject.txt", "r", encoding="utf-8").read()
content = open("content.txt", "r", encoding="utf-8").read()

class Recipient:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.target_name = ""
        self.target_email = ""

#TODO
def main():
    participants = []

    print(r"""
      .-""-.
     /,..___\
    () {_____}      SECRET SANTA
      (/-@-@-\)
      {`-=^=-'}     2022
      {  `-'  } 
       {     }
        `---'

        """)

    number_of_participants = int(input("Kuinka monta osallistujaa?\n"))
    print()
    gift_price = input("Lahjan hinta?\n")
    print()

    while True:
        for i in range(number_of_participants):
            print("Vastaanottaja {}/{}".format(i+1, number_of_participants))
            name = input("Anna vastaanottajan nimi:\n")
            email = input("Anna vastaanottajan sähköpostiosoite:\n")
            participants.append(Recipient(name, email))
            print()
        print("Ilmoitit {} osallistujaa seuraavin yhteystiedoin:".format(len(participants)))
        for participant in participants:
            print("{0:20s}{1:20s}".format(participant.name, participant.email))
        print()
        ready = input("Onko osallistujien yhteystiedot oikein? [k/e]\n")
        if ready == "k":
            print()
            break
        participants.clear()

    # Shuffle the list to get a random order
    random.shuffle(participants)
     
     # Define a target person for every participant
    for i in range(len(participants)):
        if i < len(participants)-1:
            participants[i].target_name = participants[i+1].name
            participants[i].target_email = participants[i+1].email
        else:
            participants[i].target_name = participants[0].name
            participants[i].target_email = participants[0].email

    # Testiprintti jaosta --> lähetä mailit tässä, tai miksei jo tossa aiemmassa. Näillä määrillä ihan sama kuinka monta silmukkaa pyöräyttää.
    count = 1
    for participant in participants:
        print("Lähetetään viestiä {}/{}...".format(count, len(participants)))
        count += 1
        if sender(participant.email, subject, content.format(participant.name, participant.target_name, gift_price)) is not None:
            print("Lähetetty")
        else:
            print("Lähetys epäonnistui. :/")
    print()
    print("Kaikki viestit lähetetty! Mukavaa joulun odotusta!")
    print()

if __name__ == '__main__':
    main()