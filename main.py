#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "DA485359-6DCE-4084-812F-91326DACA28A",
  "name": "Reliving",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631297418482,
  "passages": [
    {
      "name": "Room",
      "tags": "",
      "id": "1",
      "text": "This is your room. It's blandly decorated and you have a computer for gaming built on your desk.Your mind is scattered and you feel extremely stressed. What would you like to do?\n\n\n[[Gym->Gym]]\n[[PC->Desk]]\n[[Lunch->Restaurant]]\n[[Lay in Bed->Bed2]]",
      "links": [
        {
          "linkText": "Gym",
          "passageName": "Gym",
          "original": "[[Gym->Gym]]"
        },
        {
          "linkText": "PC",
          "passageName": "Desk",
          "original": "[[PC->Desk]]"
        },
        {
          "linkText": "Lunch",
          "passageName": "Restaurant",
          "original": "[[Lunch->Restaurant]]"
        },
        {
          "linkText": "Lay in Bed",
          "passageName": "Bed2",
          "original": "[[Lay in Bed->Bed2]]"
        }
      ],
      "hooks": [],
      "cleanText": "This is your room. It's blandly decorated and you have a computer for gaming built on your desk.Your mind is scattered and you feel extremely stressed. What would you like to do?"
    },
    {
      "name": "Gym",
      "tags": "",
      "id": "2",
      "score":10,
      "text": "You decided to get out of the house for once and go to the gym to get into shape and clear your mind. You feel as if your mind is a little less scattered and free. What would you like to do next?\n\n\n[[Lunch->Restaurant]]\n[[Room->Room 2]]",
      "links": [
        {
          "linkText": "Lunch",
          "passageName": "Restaurant",
          "original": "[[Lunch->Restaurant]]"
        },
        {
          "linkText": "Room",
          "passageName": "Room 2",
          "original": "[[Room->Room 2]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to get out of the house for once and go to the gym to get into shape and clear your mind. You feel as if your mind is a little less scattered and free. What would you like to do next?"
    },
    {
      "name": "Desk",
      "tags": "",
      "id": "3",
      "text": "You decided to play some video games on your computer. You see some of your friends in a voice chat. Would you like to join them and play together or play alone?\n\n\n[[Alone->Alone]]\n[[Together->Voice call]]",
      "links": [
        {
          "linkText": "Alone",
          "passageName": "Alone",
          "original": "[[Alone->Alone]]"
        },
        {
          "linkText": "Together",
          "passageName": "Voice call",
          "original": "[[Together->Voice call]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to play some video games on your computer. You see some of your friends in a voice chat. Would you like to join them and play together or play alone?"
    },
    {
      "name": "Restaurant",
      "tags": "",
      "id": "4",
      "score":10,
      "text": "You decide to make plans with one of your childhood friends to go out and eat. The two of you go to a dine-in restaurant and order your food. The two of you are having a fun conversation and you decide to tell them about what's going on in your life. You feel a weight lifted off your shoulders as you begin to share all the stresses and problems with them. They console you and recommend coming to them again if you need someone to talk to. After lunch, you still have most of the day. What would you life to do?\n\n\n[[Gym->Gym]] \n[[Room->Room 2]]\n[[Therapy->Therapist]]",
      "links": [
        {
          "linkText": "Gym",
          "passageName": "Gym",
          "original": "[[Gym->Gym]]"
        },
        {
          "linkText": "Room",
          "passageName": "Room 2",
          "original": "[[Room->Room 2]]"
        },
        {
          "linkText": "Therapy",
          "passageName": "Therapist",
          "original": "[[Therapy->Therapist]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide to make plans with one of your childhood friends to go out and eat. The two of you go to a dine-in restaurant and order your food. The two of you are having a fun conversation and you decide to tell them about what's going on in your life. You feel a weight lifted off your shoulders as you begin to share all the stresses and problems with them. They console you and recommend coming to them again if you need someone to talk to. After lunch, you still have most of the day. What would you life to do?"
    },
    {
      "name": "Room 2",
      "tags": "",
      "id": "5",
      "text": "You're back in your room. You feel better after getting out of the house for the first time in a few weeks. You feel a little tired after being out though. What would you like to do?\n\n[[Sleep->Bed]]\n[[PC->Desk]]\n[[Lunch->Restaurant]]",
      "links": [
        {
          "linkText": "Sleep",
          "passageName": "Bed",
          "original": "[[Sleep->Bed]]"
        },
        {
          "linkText": "PC",
          "passageName": "Desk",
          "original": "[[PC->Desk]]"
        },
        {
          "linkText": "Lunch",
          "passageName": "Restaurant",
          "original": "[[Lunch->Restaurant]]"
        }
      ],
      "hooks": [],
      "cleanText": "You're back in your room. You feel better after getting out of the house for the first time in a few weeks. You feel a little tired after being out though. What would you like to do?"
    },
    {
      "name": "Bed",
      "tags": "",
      "id": "6",
      "text": "You decided to take a nap and wake up a few hours later with most of the day still ahead of you. You feel different from when you normally sleep. You feel healthier and more rested and have the will to do more. What would you like to do?\n\n\n[[Play Video Games->Desk]]\n[[Go to Therapy->Therapist]]",
      "links": [
        {
          "linkText": "Play Video Games",
          "passageName": "Desk",
          "original": "[[Play Video Games->Desk]]"
        },
        {
          "linkText": "Go to Therapy",
          "passageName": "Therapist",
          "original": "[[Go to Therapy->Therapist]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to take a nap and wake up a few hours later with most of the day still ahead of you. You feel different from when you normally sleep. You feel healthier and more rested and have the will to do more. What would you like to do?"
    },
    {
      "name": "Alone",
      "tags": "",
      "id": "7",
      "score":-10,
      "text": "You decided to play games by yourself. You begin to zone out and start thinking about all of your struggles and become more stressed. You feel more tired and depressed than before. What would you like to do?\n\n\n[[Play more->Alone2]]\n[[Lie down->Bed2]]\n[[Gym->Gym]]\n[[Therapy->Therapist]]\n[[Lunch->Restaurant]]",
      "links": [
        {
          "linkText": "Play more",
          "passageName": "Alone2",
          "original": "[[Play more->Alone2]]"
        },
        {
          "linkText": "Lie down",
          "passageName": "Bed2",
          "original": "[[Lie down->Bed2]]"
        },
        {
          "linkText": "Gym",
          "passageName": "Gym",
          "original": "[[Gym->Gym]]"
        },
        {
          "linkText": "Therapy",
          "passageName": "Therapist",
          "original": "[[Therapy->Therapist]]"
        },
        {
          "linkText": "Lunch",
          "passageName": "Restaurant",
          "original": "[[Lunch->Restaurant]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to play games by yourself. You begin to zone out and start thinking about all of your struggles and become more stressed. You feel more tired and depressed than before. What would you like to do?"
    },
    {
      "name": "Voice call",
      "tags": "",
      "id": "8",
      "score":10,
      "text": "You decide to play some games with your friends and join the voice call. They greet you and invite you to join them on one of your favorite games. You all play together and you have fun. You feel your spirits lifted a bit and feel like you're having genuine fun. After a couple hours, you all are just talking in the vc and they ask how you're doing. What would you like to do?\n\n\n[[Lie->Deceit2]]\n[[Be honest->Honesty2]]",
      "links": [
        {
          "linkText": "Lie",
          "passageName": "Deceit2",
          "original": "[[Lie->Deceit2]]"
        },
        {
          "linkText": "Be honest",
          "passageName": "Honesty2",
          "original": "[[Be honest->Honesty2]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide to play some games with your friends and join the voice call. They greet you and invite you to join them on one of your favorite games. You all play together and you have fun. You feel your spirits lifted a bit and feel like you're having genuine fun. After a couple hours, you all are just talking in the vc and they ask how you're doing. What would you like to do?"
    },
    {
      "name": "Alone2",
      "tags": "",
      "id": "9",
      "score":-5,
      "text": "Your mind continues to wonder and your being to trail into a path of despair and hopelessness. You shut off the game and contemplate your life choices, thinking about the people you've lost and the mistakes you've made.\n\n\n[[Continue->Bad Ending]]\n[[Call parents->Phone Call]]",
      "links": [
        {
          "linkText": "Continue",
          "passageName": "Bad Ending",
          "original": "[[Continue->Bad Ending]]"
        },
        {
          "linkText": "Call parents",
          "passageName": "Phone Call",
          "original": "[[Call parents->Phone Call]]"
        }
      ],
      "hooks": [],
      "cleanText": "Your mind continues to wonder and your being to trail into a path of despair and hopelessness. You shut off the game and contemplate your life choices, thinking about the people you've lost and the mistakes you've made."
    },
    {
      "name": "Bed2",
      "tags": "",
      "id": "10",
      "score":-5,
      "text": "You lay on your bed and begin thinking more and more about how life is not worth living. You being falling even more into a path of despair and hopelessness. Your motivation decreases further. What will you do?\n\n\n[[Call Parents->Phone Call]]\n[[Nothing->Alone2]]\n[[Gym->Gym]]\n[[Lunch->Restaurant]]",
      "links": [
        {
          "linkText": "Call Parents",
          "passageName": "Phone Call",
          "original": "[[Call Parents->Phone Call]]"
        },
        {
          "linkText": "Nothing",
          "passageName": "Alone2",
          "original": "[[Nothing->Alone2]]"
        },
        {
          "linkText": "Gym",
          "passageName": "Gym",
          "original": "[[Gym->Gym]]"
        },
        {
          "linkText": "Lunch",
          "passageName": "Restaurant",
          "original": "[[Lunch->Restaurant]]"
        }
      ],
      "hooks": [],
      "cleanText": "You lay on your bed and begin thinking more and more about how life is not worth living. You being falling even more into a path of despair and hopelessness. Your motivation decreases further. What will you do?"
    },
    {
      "name": "Therapist",
      "tags": "",
      "id": "11",
      "score":20,
      "text": "You decided to go see a therapist that was mentioned by a friend of yours a few months ago when they talked about their mental health being poor. You visit them and are nervous. The therapist is friendly and begins introducing themselves and the two of you begin talking. The therapist then asks what's going on that brings you to their office. You being being honest with the therapist and they make a quick diagnosis and decide to prescribe you with some medication and you feel much better. You go and pick up the meds and bring them back to your room. You debate whether or not to stick with the meds or if their pointless. What would you like to do?\n\n\n[[Stick with the meds-> Therapy ending]]\n[[Not stick with the meds->Bad Ending2]]",
      "links": [
        {
          "linkText": "Stick with the meds",
          "passageName": "Therapy ending",
          "original": "[[Stick with the meds-> Therapy ending]]"
        },
        {
          "linkText": "Not stick with the meds",
          "passageName": "Bad Ending2",
          "original": "[[Not stick with the meds->Bad Ending2]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to go see a therapist that was mentioned by a friend of yours a few months ago when they talked about their mental health being poor. You visit them and are nervous. The therapist is friendly and begins introducing themselves and the two of you begin talking. The therapist then asks what's going on that brings you to their office. You being being honest with the therapist and they make a quick diagnosis and decide to prescribe you with some medication and you feel much better. You go and pick up the meds and bring them back to your room. You debate whether or not to stick with the meds or if their pointless. What would you like to do?"
    },
    {
      "name": "Bad Ending",
      "tags": "",
      "id": "12",
      "score":-100,
      "text": "You've ended your life after so long of feeling hopeless, in despair, and feeling like there is no point to anything. If you feel this way or depressed in another manner or notice someone else has been behaving this way, please don't hesitate to call family, friends, a trusted person, or the national suicide prevention hotline. Remember that there are plenty of opportunities to get help and that you need to grasp them when you can.\n\n\n[[Play again->Room]]",
      "links": [
        {
          "linkText": "Play again",
          "passageName": "Room",
          "original": "[[Play again->Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "You've ended your life after so long of feeling hopeless, in despair, and feeling like there is no point to anything. If you feel this way or depressed in another manner or notice someone else has been behaving this way, please don't hesitate to call family, friends, a trusted person, or the national suicide prevention hotline. Remember that there are plenty of opportunities to get help and that you need to grasp them when you can."
    },
    {
      "name": "Phone Call",
      "tags": "",
      "id": "13",
      "score":20,
      "text": "You call your parents for the first time in over 2 months. Your father answers and you begin making small talk with him about how life has been with him and your mother. After he finishes talking about how life has been with them, he asks you the same questions. What do you do?\n\n\n[[Hide your pain and lie->Deceit]]\n[[Be honest and say things are not okay->Honesty]]",
      "links": [
        {
          "linkText": "Hide your pain and lie",
          "passageName": "Deceit",
          "original": "[[Hide your pain and lie->Deceit]]"
        },
        {
          "linkText": "Be honest and say things are not okay",
          "passageName": "Honesty",
          "original": "[[Be honest and say things are not okay->Honesty]]"
        }
      ],
      "hooks": [],
      "cleanText": "You call your parents for the first time in over 2 months. Your father answers and you begin making small talk with him about how life has been with him and your mother. After he finishes talking about how life has been with them, he asks you the same questions. What do you do?"
    },
    {
      "name": "Deceit",
      "tags": "",
      "id": "14",
      "score":-10,
      "text": "You lie to your father and explain that life is going great. He seems happy for you and you feel the weight on your shoulders get heavier as you keep lying to him. Though, you decide to keep up the facade. After a couple hours of conversation, you both say goodbye and hang up the phone. You become extremely overwhelmed with sudden grief and hopelessness.\n\n\n[[Continue->Bad Ending]]",
      "links": [
        {
          "linkText": "Continue",
          "passageName": "Bad Ending",
          "original": "[[Continue->Bad Ending]]"
        }
      ],
      "hooks": [],
      "cleanText": "You lie to your father and explain that life is going great. He seems happy for you and you feel the weight on your shoulders get heavier as you keep lying to him. Though, you decide to keep up the facade. After a couple hours of conversation, you both say goodbye and hang up the phone. You become extremely overwhelmed with sudden grief and hopelessness."
    },
    {
      "name": "Honesty",
      "tags": "",
      "id": "15",
      "score":10,
      "text": "You decide to be completely honest with your father. You explain all the stresses and challenges that life has thrown at you ever since you began to live on your own a year ago. He sits quietly and listens as for the first time, you begin to rant about your problems. After you finish you feel a massive weight lifted off your shoulders as you are in tears. He reminds you that he loves you, and recommends that you see a therapist urgently and that he will come visit you weekly on his days off work.\n\n\n[[Continue->Phone Call Ending]]",
      "links": [
        {
          "linkText": "Continue",
          "passageName": "Phone Call Ending",
          "original": "[[Continue->Phone Call Ending]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide to be completely honest with your father. You explain all the stresses and challenges that life has thrown at you ever since you began to live on your own a year ago. He sits quietly and listens as for the first time, you begin to rant about your problems. After you finish you feel a massive weight lifted off your shoulders as you are in tears. He reminds you that he loves you, and recommends that you see a therapist urgently and that he will come visit you weekly on his days off work."
    },
    {
      "name": "Phone Call Ending",
      "tags": "",
      "id": "16",
      "score":100,
      "text": "You take your fathers advice and visit a therapist. They prescribe you medication and weekly sessions. Your father begins to visit you weekly and checks in on your to make sure you're doing okay. The stresses begin to lift and you feel like you're alive again. Sometimes, as much as we hate it, talking is what we need to do. Please don't hesitate to talk to a trusted person and let them know what's going on in your life. People do care about you, as much as the world seems like it doesn't.\n\n\n[[Play Again->Room]]",
      "links": [
        {
          "linkText": "Play Again",
          "passageName": "Room",
          "original": "[[Play Again->Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "You take your fathers advice and visit a therapist. They prescribe you medication and weekly sessions. Your father begins to visit you weekly and checks in on your to make sure you're doing okay. The stresses begin to lift and you feel like you're alive again. Sometimes, as much as we hate it, talking is what we need to do. Please don't hesitate to talk to a trusted person and let them know what's going on in your life. People do care about you, as much as the world seems like it doesn't."
    },
    {
      "name": "Honesty2",
      "tags": "",
      "id": "17",
      "score":20,
      "text": "You decide to be honest with them and tell them that things haven't been going well for a while. You go on a rant and they being giving you advice on what you should do. They recommend getting out of the house and going to see a therapist or call family. You feel a weight lifted off your shoulders. After the conversation, the call ends as everyone has stuff to do. What would you like to do?\n\n\n[[Continue Playing games alone->Alone]]\n[[Gym->Gym]]\n[[Therapy->Therapist]]\n[[Lunch->Restaurant]]\n[[Call your parents->Phone Call]]\n[[Lie down and think->Bed2]]",
      "links": [
        {
          "linkText": "Continue Playing games alone",
          "passageName": "Alone",
          "original": "[[Continue Playing games alone->Alone]]"
        },
        {
          "linkText": "Gym",
          "passageName": "Gym",
          "original": "[[Gym->Gym]]"
        },
        {
          "linkText": "Therapy",
          "passageName": "Therapist",
          "original": "[[Therapy->Therapist]]"
        },
        {
          "linkText": "Lunch",
          "passageName": "Restaurant",
          "original": "[[Lunch->Restaurant]]"
        },
        {
          "linkText": "Call your parents",
          "passageName": "Phone Call",
          "original": "[[Call your parents->Phone Call]]"
        },
        {
          "linkText": "Lie down and think",
          "passageName": "Bed2",
          "original": "[[Lie down and think->Bed2]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide to be honest with them and tell them that things haven't been going well for a while. You go on a rant and they being giving you advice on what you should do. They recommend getting out of the house and going to see a therapist or call family. You feel a weight lifted off your shoulders. After the conversation, the call ends as everyone has stuff to do. What would you like to do?"
    },
    {
      "name": "Deceit2",
      "tags": "",
      "id": "18",
      "score":-10,
      "text": "You lie to your friends and begin to tell them that life is going great. You feel guilt as you keep on lying to them about what's happening in life and avoid answering any questions about problems. After a bit, the voice call ends. What would you like to do?\n\n\n[[Lie down->Bed2]]\n[[Think->Alone2]]\n[[Continue playing games alone->Alone]]",
      "links": [
        {
          "linkText": "Lie down",
          "passageName": "Bed2",
          "original": "[[Lie down->Bed2]]"
        },
        {
          "linkText": "Think",
          "passageName": "Alone2",
          "original": "[[Think->Alone2]]"
        },
        {
          "linkText": "Continue playing games alone",
          "passageName": "Alone",
          "original": "[[Continue playing games alone->Alone]]"
        }
      ],
      "hooks": [],
      "cleanText": "You lie to your friends and begin to tell them that life is going great. You feel guilt as you keep on lying to them about what's happening in life and avoid answering any questions about problems. After a bit, the voice call ends. What would you like to do?"
    },
    {
      "name": " Therapy ending",
      "tags": "",
      "id": "19",
      "score":100,
      "text": "You decide to stick the medication and see how it will work in the long run. A few months go by and you feel healthier as you've been going out more, taking the medication and listening to the therapist's advice. Remember that going to therapy isn't something that should be embarassing. They are there to help you, and everyone needs someone to help them at some point in their life, but different people need different people to help them.\n\n\n[[Play again->Room]]",
      "links": [
        {
          "linkText": "Play again",
          "passageName": "Room",
          "original": "[[Play again->Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide to stick the medication and see how it will work in the long run. A few months go by and you feel healthier as you've been going out more, taking the medication and listening to the therapist's advice. Remember that going to therapy isn't something that should be embarassing. They are there to help you, and everyone needs someone to help them at some point in their life, but different people need different people to help them."
    },
    {
      "name": "Bad Ending2",
      "tags": "",
      "id": "20",
      "score":-100,
      "text": "You decided that the medication isn't worth using and fall deep into despair. As much as you felt better after getting the weights off your shoulder by talking to the therapist, you begin to argue that they don't know you, and that they don't know what it feels like. You argue yourself down a train of thought that results in you overdosing on your new medication. It feels sometimes that people don't know what you're going through or don't know what it's like, but it's important to remember that different people have different struggles. The thing that's in common is that everyone struggles. Don't dismiss help or advice from others with logic that they don't understand or don't know what they're talking about. Take the advice they give you and live it to the fullest.\n\n\n[[Play again->Room]]",
      "links": [
        {
          "linkText": "Play again",
          "passageName": "Room",
          "original": "[[Play again->Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided that the medication isn't worth using and fall deep into despair. As much as you felt better after getting the weights off your shoulder by talking to the therapist, you begin to argue that they don't know you, and that they don't know what it feels like. You argue yourself down a train of thought that results in you overdosing on your new medication. It feels sometimes that people don't know what you're going through or don't know what it's like, but it's important to remember that different people have different struggles. The thing that's in common is that everyone struggles. Don't dismiss help or advice from others with logic that they don't understand or don't know what they're talking about. Take the advice they give you and live it to the fullest."
    }
  ]
}


# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
		#print("Moves: " + str(moves) + ", Score: " + str(score))
		print("Moves: {}, Score: {}".format(moves, score))
		print("You are at the " + str(current_location["name"]))
		print(current_location["cleanText"] + "\n")

def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"].upper() == response:
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label


# ----------------------------------------------------------------

location_label = "Room"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break
	moves = moves + 1
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if "score" in current_location:
		score = score + current_location["score"]
	render(current_location, score, moves)
	response = get_input()

  
print("Thanks for playing!")