# yomamabot/fb_yomamabot/views.py
import requests  # Importing requests directly
import json 
from django.views import generic
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from pprint import pprint


# # Create your views here.

# # class YoMamaBotView(generic.View):

# #     def get(self, request, *args, **kwargs):

# #         return HttpResponse("Hello World!")

# jokes = {

#          'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",

#                     """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],

#          'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",

#                     """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],

#          'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",

#                     """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""]

#          }
# def post_facebook_message(fbid, recevied_message):
#     # Remove all punctuations, lower case the text and split it based on space
#     tokens = re.sub(r"[^a-zA-Z0-9\s]",' ',recevied_message).lower().split()
#     joke_text = ''
#     for token in tokens:
#         if token in jokes:
#             joke_text = random.choice(jokes[token])
#             break
#     if not joke_text:
#         joke_text = "I didn't understand! Send 'stupid', 'fat', 'dumb' for a Yo Mama joke!"
#     post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=<page-access-token>'
#     response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":joke_text}})
#     status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
#     pprint(status.json())

#     user_details_url = "https://graph.facebook.com/v2.6/%s"%fbid
#     user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':'<page-access-token>'}
#     user_details = requests.get(user_details_url, user_details_params).json()
#     joke_text = 'Yo '+user_details['first_name']+'..!' + joke_text


#     post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=<page-access-token>'
#     response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":recevied_message}})
#     status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
#     pprint(status.json())
# # yomamabot/fb_yomamabot/views.py

# class YoMamaBotView(generic.View):

#     def get(self, request, *args, **kwargs):

#         if self.request.GET['hub.verify_token'] == '2318934571':

#             return HttpResponse(self.request.GET['hub.challenge'])

#         else:

#             return HttpResponse('Error, invalid token')
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return generic.View.dispatch(self, request, *args, **kwargs)

#     # Post function to handle Facebook messages
#     def post(self, request, *args, **kwargs):
#         # Converts the text payload into a python dictionary
#         incoming_message = json.loads(self.request.body.decode('utf-8'))
#         # Facebook recommends going through every entry since they might send
#         # multiple messages in a single call during high load
#         for entry in incoming_message['entry']:
#             for message in entry['messaging']:
#                 # Check to make sure the received call is a message call
#                 # This might be delivery, optin, postback for other events
#                 # if 'message' in message:
#                 #     # Print the message to the terminal
#                 #     pprint(message)
#                 if 'message' in message:
#                     # Print the message to the terminal
#                     pprint(message)
#                     # Assuming the sender only sends text. Non-text messages like stickers, audio, pictures
#                     # are sent as attachments and must be handled accordingly.
#                     post_facebook_message(message['sender']['id'], message['message']['text'])
#         return HttpResponse()
    
# from django.http import HttpResponse, JsonResponse
# import json
# import requests

# PAGE_ACCESS_TOKEN = 'YOUR_PAGE_ACCESS_TOKEN'

# def home(request):
#     return HttpResponse("Welcome to the homepage!")

# def webhook(request):
#     if request.method == 'GET':
#         if request.GET.get('hub.verify_token') == 'YOUR_VERIFY_TOKEN':
#             return JsonResponse(request.GET.get('hub.challenge'), safe=False)
#         return JsonResponse('Error, invalid token', status=403)

#     if request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         for entry in data['entry']:
#             for messaging_event in entry['messaging']:
#                 if messaging_event.get('message'):
#                     sender_id = messaging_event['sender']['id']
#                     message_text = messaging_event['message']['text']
#                     send_button_message(sender_id, message_text)
#         return JsonResponse({"status": "ok"}, status=200)

# def send_button_message(recipient_id, message_text):
#     url = "https://graph.facebook.com/v11.0/me/messages"
#     headers = {
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "recipient": {
#             "id": recipient_id
#         },
#         "message": {
#             "attachment": {
#                 "type": "template",
#                 "payload": {
#                     "template_type": "button",
#                     "text": f"Thanks for your message: {message_text}! What would you like to do next?",
#                     "buttons": [
#                         {
#                             "type": "postback",
#                             "title": "Option 1",
#                             "payload": "OPTION_1"
#                         },
#                         {
#                             "type": "postback",
#                             "title": "Option 2",
#                             "payload": "OPTION_2"
#                         },
#                         {
#                             "type": "web_url",
#                             "url": "https://www.example.com",
#                             "title": "Visit Website"
#                         }
#                     ]
#                 }
#             }
#         }
#     }
#     params = {
#         "access_token": PAGE_ACCESS_TOKEN
#     }
#     response = requests.post(url, params=params, headers=headers, json=payload)
#     print(response.json())
 

#  import json
# import random
# import re
# import requests
# from pprint import pprint
# from django.http import HttpResponse
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from django.views import generic




# # Example message dictionary for random responses
# message = {
    
#      'hello': ['Hello!', 'Hi there!', 'Greetings!'],
   
# }

# PAGE_ACCESS_TOKEN = 'EAAOMWCjlT3EBO4YV21FAudVf3FwKvupFoh9nwvBeMztBKvrL0FBXx57V0MBloc4619ZBMywS0vEFcTlRZCRfyWhXQRmEztZBXK2gduSb5jVK6lyy4aSXLJdiQyw878YTq1T4gUGtxQKKIuVTwjunIQCrLgoc52DlVFHkiZC0E81ZCNVj9bNyZCY0ohfdOMgLMeFzznxBXilAZDZD'

# def post_facebook_message(fbid, received_message):
#     tokens = received_message
#     # tokens = re.sub(r"[^a-zA-Z0-9\s]", ' ', received_message).lower().split()
#     messenger_text = ''
#     for token in tokens:
#         if token in message:
#             messenger_text = random.choice(message[token])
#             break
#     if not messenger_text:
#        messenger_text = "Hi! Welcome to this page"

#     # Constructing the button template message
#                             "35_14_starting_template": {
#                             "messaging_type": "RESPONSE",
#                             "message": {
#                             "text": "Welcome to Fetech test, Would you like to continue?",
#                             "quick_replies": [
#                             {
#                                 "content_type": "text",
#                                 "title": "Yes",
#                                 "payload": "35_14_Yes"
#                             },
#                             {
#                                 "content_type": "text",
#                                 "title": "No",
#                                 "payload": "35_14_No"
#                             }
#                             ]
#                         }
#                         },

#                         "35_14_Yes":{
#                         "messaging_type": "RESPONSE",
#                         "message": {
#                             "text": "Hi, You filled out a form for enquiry, would you like to continue with the enquiries?",
#                             "quick_replies": [
#                             {
#                                 "content_type": "text",
#                                 "title": "Yes",
#                                 "payload": "35_14_dndnode_3"
#                             },
#                             {
#                                 "content_type": "text",
#                                 "title": "No",
#                                 "payload": "35_14_dndnode_4"
#                             }
#                             ]
#                         }
#                         },

#                         "35_14_No":{
#                         "messaging_type": "RESPONSE",
#                         "message": {
#                             "text": "Thanks"
#                         }
#                         },

#                         "35_14_dndnode_3":{
#                         "messaging_type": "RESPONSE",
#                         "message": {
#                             "text": "Great, We need to cover some formalities before we continue, Do you like to continue?",
#                             "quick_replies": [
#                             {
#                                 "content_type": "text",
#                                 "title": "Yes",
#                                 "payload": "35_14_dndnode_5"
#                             },
#                             {
#                                 "content_type": "text",
#                                 "title": "No",
#                                 "payload": "35_14_dndnode_6"
#                             }
#                             ]
#                         }
#                         },

#                         "35_14_dndnode_4":{
#                         "messaging_type": "RESPONSE",
#                         "message": {
#                             "text": "Do you like to purchase any other course?",
#                             "quick_replies": [
#                             {
#                                 "content_type": "text",
#                                 "title": "Yes",
#                                 "payload": "35_14_dndnode_9"
#                             },
#                             {
#                                 "content_type": "text",
#                                 "title": "No",
#                                 "payload": "35_14_dndnode_10"
#                             }
#                             ]
#                         }
#                         },

#                         "35_14_dndnode_5":{
#                         "messaging_type": "RESPONSE",
#                         "message": {
#                             "text": "Can we give you a callback now?",
#                             "quick_replies": [
#                             {
#                                 "content_type": "text",
#                                 "title": "Yes",
#                                 "payload": "35_14_dndnode_7"
#                             },
#                             {
#                                 "content_type": "text",
#                                 "title": "No",
#                                 "payload": "35_14_dndnode_8"
#                             }
#                             ]
#                         }
#                         },


#                         "35_14_dndnode_6":{
#                         "messaging_type": "RESPONSE",
#                         "message": {
#                             "text": "Thanks"
#                         }
#                         },

#                         "35_14_dndnode_7":{
#                         "messaging_type": "RESPONSE",
#                         "message": {
#                             "text": "Thanks"
#                         }
#                         },

#                         "35_14_dndnode_8":{
#                         "messaging_type": "RESPONSE",
#                         "message": {
#                             "text": "Thanks"
#                         }
#                         },


#                         "35_14_dndnode_9":{
#                         "messaging_type": "RESPONSE",
#                         "message": {
#                             "text": "Great, We need to cover some formalities before we continue, Do you like to continue?",
#                             "quick_replies": [
#                             {
#                                 "content_type": "text",
#                                 "title": "Yes",
#                                 "payload": "35_14_dndnode_5"
#                             },
#                             {
#                                 "content_type": "text",
#                                 "title": "No",
#                                 "payload": "35_14_dndnode_6"
#                             }
#                             ]
#                         }
#                         },

#                         "35_14_dndnode_10":{
#                         "messaging_type": "RESPONSE",
#                         "message": {
#                             "text": "Do you have any other queries?",
#                             "quick_replies": [
#                             {
#                                 "content_type": "text",
#                                 "title": "Yes",
#                                 "payload": "35_14_dndnode_11"
#                             },
#                             {
#                                 "content_type": "text",
#                                 "title": "No",
#                                 "payload": "35_14_dndnode_12"
#                             }
#                             ]
#                         }
#                         },

#                         "35_14_dndnode_11":{
#                         "messaging_type": "RESPONSE",
#                         "message": {
#                             "text": "Can we give you a callback now?",
#                             "quick_replies": [
#                             {
#                                 "content_type": "text",
#                                 "title": "Yes",
#                                 "payload": "35_14_dndnode_7"
#                             },
#                             {
#                                 "content_type": "text",
#                                 "title": "No",
#                                 "payload": "35_14_dndnode_8"
#                             }
#                             ]
#                         }
#                         },

#                         "35_14_dndnode_12":{
#                         "messaging_type": "RESPONSE",
#                         "message": {
#                             "text": "Thanks"
#                         }
#                         }

 
   

# post_message_url = f'https://graph.facebook.com/v2.6/me/messages?access_token={PAGE_ACCESS_TOKEN}'
# status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=json.dumps(response_msg))
# pprint(status.json())



# class MessengerWebhook(generic.View):
#     def get(self, request, *args, **kwargs):
#         verify_token = self.request.GET.get('hub.verify_token', None)
#         if verify_token == '123456':
#             return HttpResponse(self.request.GET.get('hub.challenge', ''))
#         else:
#             return HttpResponse('Error, invalid token')

#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return generic.View.dispatch(self, request, *args, **kwargs)

#     # Post function to handle Facebook messages
#     def post(self, request, *args, **kwargs):
#         incoming_message = json.loads(self.request.body.decode('utf-8'))
#         for entry in incoming_message['entry']:
#             for message in entry['messaging']:
#                 if 'message' in message:
#                     pprint(message)
#                     post_facebook_message(message['sender']['id'], message['message']['text'])
#         return HttpResponse()
    


# #4..
# def post_facebook_message(fbid, received_message):
#     response_msg = {
#         "35_14_starting_template": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "attachment": {
#                     "type": "template",
#                     "payload": {
#                         "template_type": "button",
#                         "text": "Welcome to Fetech test, Would you like to continue?",
#                         "buttons": [
#                             {
#                                 "type": "postback",
#                                 "title": "Yes",
#                                 "payload": "35_14_Yes"
#                             },
#                             {
#                                 "type": "postback",
#                                 "title": "No",
#                                 "payload": "35_14_No"
#                             }
#                         ]
#                     }
#                 }
#             }
#         },
#         "35_14_Yes": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "attachment": {
#                     "type": "template",
#                     "payload": {
#                         "template_type": "button",
#                         "text": "Hi, You filled out a form for enquiry, would you like to continue with the enquiries?",
#                         "buttons": [
#                             {
#                                 "type": "postback",
#                                 "title": "Yes",
#                                 "payload": "35_14_dndnode_3"
#                             },
#                             {
#                                 "type": "postback",
#                                 "title": "No",
#                                 "payload": "35_14_dndnode_4"
#                             }
#                         ]
#                     }
#                 }
#             }
#         },
#         "35_14_No": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "text": "Thanks"
#             }
#         },
#         "35_14_dndnode_3": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "attachment": {
#                     "type": "template",
#                     "payload": {
#                         "template_type": "button",
#                         "text": "Great, We need to cover some formalities before we continue, Do you like to continue?",
#                         "buttons": [
#                             {
#                                 "type": "postback",
#                                 "title": "Yes",
#                                 "payload": "35_14_dndnode_5"
#                             },
#                             {
#                                 "type": "postback",
#                                 "title": "No",
#                                 "payload": "35_14_dndnode_6"
#                             }
#                         ]
#                     }
#                 }
#             }
#         },
#         "35_14_dndnode_4": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "text": "Do you like to purchase any other course?"
#             }
#         },
#         "35_14_dndnode_5": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "attachment": {
#                     "type": "template",
#                     "payload": {
#                         "template_type": "button",
#                         "text": "Can we give you a callback now?",
#                         "buttons": [
#                             {
#                                 "type": "postback",
#                                 "title": "Yes",
#                                 "payload": "35_14_dndnode_7"
#                             },
#                             {
#                                 "type": "postback",
#                                 "title": "No",
#                                 "payload": "35_14_dndnode_8"
#                             }
#                         ]
#                     }
#                 }
#             }
#         },
#         "35_14_dndnode_6": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "text": "Thanks"
#             }
#         },
#         "35_14_dndnode_7": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "text": "Thanks"
#             }
#         },
#         "35_14_dndnode_8": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "text": "Thanks"
#             }
#         },
#         "35_14_dndnode_9": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "attachment": {
#                     "type": "template",
#                     "payload": {
#                         "template_type": "button",
#                         "text": "Great, We need to cover some formalities before we continue, Do you like to continue?",
#                         "buttons": [
#                             {
#                                 "type": "postback",
#                                 "title": "Yes",
#                                 "payload": "35_14_dndnode_5"
#                             },
#                             {
#                                 "type": "postback",
#                                 "title": "No",
#                                 "payload": "35_14_dndnode_6"
#                             }
#                         ]
#                     }
#                 }
#             }
#         },
#         "35_14_dndnode_10": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "attachment": {
#                     "type": "template",
#                     "payload": {
#                         "template_type": "button",
#                         "text": "Do you have any other queries?",
#                         "buttons": [
#                             {
#                                 "type": "postback",
#                                 "title": "Yes",
#                                 "payload": "35_14_dndnode_11"
#                             },
#                             {
#                                 "type": "postback",
#                                 "title": "No",
#                                 "payload": "35_14_dndnode_12"
#                             }
#                         ]
#                     }
#                 }
#             }
#         },
#         "35_14_dndnode_11": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "attachment": {
#                     "type": "template",
#                     "payload": {
#                         "template_type": "button",
#                         "text": "Can we give you a callback now?",
#                         "buttons": [
#                             {
#                                 "type": "postback",
#                                 "title": "Yes",
#                                 "payload": "35_14_dndnode_7"
#                             },
#                             {
#                                 "type": "postback",
#                                 "title": "No",
#                                 "payload": "35_14_dndnode_8"
#                             }
#                         ]
#                     }
#                 }
#             }
#         },
#         "35_14_dndnode_12": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "text": "Thanks"
#             }
#         }
#     }

#     # Determine which response message to send based on received_message
#     payload = response_msg.get(received_message, response_msg["35_14_starting_template"])

#     post_message_url = f'https://graph.facebook.com/v2.6/me/messages?access_token={PAGE_ACCESS_TOKEN}'
#     headers = {"Content-Type": "application/json"}

#     # Send the message to Facebook Messenger API
#     response = requests.post(post_message_url, headers=headers, data=json.dumps(payload))
#     pprint(response.json())

#     def post_facebook_message(fbid, received_message):
#     response_msg = {
#         "35_14_starting_template": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "attachment": {
#                     "type": "template",
#                     "payload": {
#                         "template_type": "button",
#                         "text": "Welcome to Fetech test, Would you like to continue?",
#                         "buttons": [
#                             {
#                                 "type": "postback",
#                                 "title": "Yes",
#                                 "payload": "35_14_Yes"
#                             },
#                             {
#                                 "type": "postback",
#                                 "title": "No",
#                                 "payload": "35_14_No"
#                             }
#                         ]
#                     }
#                 }
#             }
#         },
#         "35_14_Yes": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "attachment": {
#                     "type": "template",
#                     "payload": {
#                         "template_type": "button",
#                         "text": "Hi, You filled out a form for enquiry, would you like to continue with the enquiries?",
#                         "buttons": [
#                             {
#                                 "type": "postback",
#                                 "title": "Yes",
#                                 "payload": "35_14_dndnode_3"
#                             },
#                             {
#                                 "type": "postback",
#                                 "title": "No",
#                                 "payload": "35_14_dndnode_4"
#                             }
#                         ]
#                     }
#                 }
#             }
#         },
#         "35_14_No": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "text": "Thanks"
#             }
#         },
#         "35_14_dndnode_3": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "attachment": {
#                     "type": "template",
#                     "payload": {
#                         "template_type": "button",
#                         "text": "Great, We need to cover some formalities before we continue, Do you like to continue?",
#                         "buttons": [
#                             {
#                                 "type": "postback",
#                                 "title": "Yes",
#                                 "payload": "35_14_dndnode_5"
#                             },
#                             {
#                                 "type": "postback",
#                                 "title": "No",
#                                 "payload": "35_14_dndnode_6"
#                             }
#                         ]
#                     }
#                 }
#             }
#         },
#         "35_14_dndnode_4": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "text": "Do you like to purchase any other course?"
#             }
#         },
#         "35_14_dndnode_5": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "attachment": {
#                     "type": "template",
#                     "payload": {
#                         "template_type": "button",
#                         "text": "Can we give you a callback now?",
#                         "buttons": [
#                             {
#                                 "type": "postback",
#                                 "title": "Yes",
#                                 "payload": "35_14_dndnode_7"
#                             },
#                             {
#                                 "type": "postback",
#                                 "title": "No",
#                                 "payload": "35_14_dndnode_8"
#                             }
#                         ]
#                     }
#                 }
#             }
#         },
#         "35_14_dndnode_6": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "text": "Thanks"
#             }
#         },
#         "35_14_dndnode_7": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "text": "Thanks"
#             }
#         },
#         "35_14_dndnode_8": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "text": "Thanks"
#             }
#         },
#         "35_14_dndnode_9": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "attachment": {
#                     "type": "template",
#                     "payload": {
#                         "template_type": "button",
#                         "text": "Great, We need to cover some formalities before we continue, Do you like to continue?",
#                         "buttons": [
#                             {
#                                 "type": "postback",
#                                 "title": "Yes",
#                                 "payload": "35_14_dndnode_5"
#                             },
#                             {
#                                 "type": "postback",
#                                 "title": "No",
#                                 "payload": "35_14_dndnode_6"
#                             }
#                         ]
#                     }
#                 }
#             }
#         },
#         "35_14_dndnode_10": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "attachment": {
#                     "type": "template",
#                     "payload": {
#                         "template_type": "button",
#                         "text": "Do you have any other queries?",
#                         "buttons": [
#                             {
#                                 "type": "postback",
#                                 "title": "Yes",
#                                 "payload": "35_14_dndnode_11"
#                             },
#                             {
#                                 "type": "postback",
#                                 "title": "No",
#                                 "payload": "35_14_dndnode_12"
#                             }
#                         ]
#                     }
#                 }
#             }
#         },
#         "35_14_dndnode_11": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "attachment": {
#                     "type": "template",
#                     "payload": {
#                         "template_type": "button",
#                         "text": "Can we give you a callback now?",
#                         "buttons": [
#                             {
#                                 "type": "postback",
#                                 "title": "Yes",
#                                 "payload": "35_14_dndnode_7"
#                             },
#                             {
#                                 "type": "postback",
#                                 "title": "No",
#                                 "payload": "35_14_dndnode_8"
#                             }
#                         ]
#                     }
#                 }
#             }
#         },
#         "35_14_dndnode_12": {
#             "recipient": {"id": fbid},
#             "message": {
#                 "text": "Thanks"
#             }
#         }
#     }

#     # Determine which response message to send based on received_message
#     payload = response_msg.get(received_message, response_msg["35_14_starting_template"])

#     post_message_url = f'https://graph.facebook.com/v2.6/me/messages?access_token={PAGE_ACCESS_TOKEN}'
#     headers = {"Content-Type": "application/json"}

#     # Send the message to Facebook Messenger API
#     response = requests.post(post_message_url, headers=headers, data=json.dumps(payload))
#     pprint(response.json())


#     ##5.
PAGE_ACCESS_TOKEN = 'EAAOMWCjlT3EBO3XaA5LDcOhtRqaSndqX6EgPwT5tirWNGHVv6jpPzZBg68aEl9govfYobVRNmJXJCzgFpnex8oTbPPWkEW2WZC7PgKyw3UGvXgSpOmXL6SZCKL1cjzzYMLtS1XgVzQDZBxwDfnPUEUcIRSuwYI5aCy1lzWbBXy0ZCtLBsdxO8IAZA3AJN8kgrKPtXXzMSk1wZDZD' 

def post_facebook_message(fbid, received_message):
    response_msg = {
        "35_14_starting_template": {
            "recipient": {"id": fbid},
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "button",
                        "text": "Welcome to the Student Survey! Would you like to participate?",
                        "buttons": [
                            {
                                "type": "postback",
                                "title": "Yes",
                                "payload": "35_14_Yes"
                            },
                            {
                                "type": "postback",
                                "title": "No",
                                "payload": "35_14_No"
                            }
                        ]
                    }
                }
            }
        },
        "35_14_Yes": {
            "recipient": {"id": fbid},
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "button",
                        "text": "How satisfied are you with your current course?",
                        "buttons": [
                            {
                                "type": "postback",
                                "title": "Very Satisfied",
                                "payload": "35_14_dndnode_3"
                            },
                            {
                                "type": "postback",
                                "title": "Satisfied",
                                "payload": "35_14_dndnode_3"
                            }
                        ]
                    }
                }
            }
        },
        "35_14_No": {
            "recipient": {"id": fbid},
            "message": {
                "text": "Thank you for participating in our survey!"
            }
        },
        "35_14_dndnode_3": {
            "recipient": {"id": fbid},
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "button",
                        "text":"How would you rate your instructor?",
                        "buttons": [
                            {
                                "type": "postback",
                                "title": "Good",
                                "payload": "35_14_dndnode_5"
                            },
                            {
                                "type": "postback",
                                "title": "poor",
                                "payload": "35_14_dndnode_6"
                            }
                        ]
                    }
                }
            }
        },
        "35_14_dndnode_5": {
            "recipient": {"id": fbid},
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "button",
                        "text": "Are you interested in enrolling in more courses in the future?",
                        "buttons": [
                            {
                                "type": "postback",
                                "title": "Yes",
                                "payload": "35_14_dndnode_7"
                            },
                            {
                                "type": "postback",
                                "title": "No",
                                "payload": "35_14_dndnode_8"
                            }
                        ]
                    }
                }
            }
        },
        "35_14_dndnode_6": {
            "recipient": {"id": fbid},
            "message": {
                "text": "Thank you for participating in our survey!"
            }
        },
        "35_14_dndnode_7": {
            "recipient": {"id": fbid},
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "button",
                        "text": "Which topics are you interested in?",
                        "buttons": [
                            {
                                "type": "postback",
                                "title": "Science",
                                "payload": "35_14_dndnode_8"
                            },
                            {
                                "type": "postback",
                                "title": "arts",
                                "payload": "35_14_dndnode_8"
                            }
                        ]
                    }
                }
            }
        },
        "35_14_dndnode_8":{
            "recipient": {"id": fbid},
            "message": {
                "text": "Thank you for participating in our survey!"
            }
        }
    }

    # Determine which response message to send based on received_message
    payload = response_msg.get(received_message, response_msg["35_14_starting_template"])

    post_message_url = f'https://graph.facebook.com/v2.6/me/messages?access_token={PAGE_ACCESS_TOKEN}'
    headers = {"Content-Type": "application/json"}

    # Send the message to Facebook Messenger API
    response = requests.post(post_message_url, headers=headers, data=json.dumps(payload))
    pprint(response.json())

class MessengerWebhook(generic.View):
    def get(self, request, *args, **kwargs):
        verify_token = self.request.GET.get('hub.verify_token', None)
        if verify_token == '123456':
            return HttpResponse(self.request.GET.get('hub.challenge', ''))
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message and 'text' in message['message']:
                    pprint(message)
                    post_facebook_message(message['sender']['id'], message['message']['text'])
                elif 'postback' in message and 'payload' in message['postback']:
                    pprint(message)
                    post_facebook_message(message['sender']['id'], message['postback']['payload'])
        return HttpResponse()