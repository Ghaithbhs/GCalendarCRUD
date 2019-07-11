from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import httplib2
from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
#from oauth2client.tools import run
from oauth2client import tools

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']
FLOW = OAuth2WebServerFlow(
    client_id='361001423406-meqq5djv2vf54fhd0ect7163ugkpssmm.apps.googleusercontent.com',
    client_secret='pioORdrpsd-cFemxkETi08yM',
    scope='https://www.googleapis.com/auth/contacts.readonly',
    user_agent='Focus Smart Box')


def main():
    # Getting the credentials for G.People API
    storage = Storage('info.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid is True:
        credentials = tools.run_flow(FLOW, storage)

    http = httplib2.Http()
    http = credentials.authorize(http)

    people_service = build(serviceName='people', version='v1', http=http)

    results = people_service.people().connections().list(
        resourceName='people/me',
        pageSize=10,
        personFields='emailAddresses,names').execute()
    connections = results.get('connections', [])

    # Getting the credentials for G.Calendar API
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Get inputs
    print("What's the name of the event?")
    n = input()

    l = "FOCUS-1ere-Midoune Meeting Room (10)"
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """

    events_result = service.events().list(calendarId='primary',
                                          maxResults=1, singleEvents=True,
                                          orderBy='startTime', q=n).execute()
    events = events_result.get('items', [])

    if not events:
        print('event not found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
        eventid = event['id']
        #print(event['id'])
        #print(eventid)
    print('what do you want to update? Summery - Start Time - End Time - Location - Attendees - Meeting Room?')
    u = input()
    if u == 'Summery':
        print('what\'s the new summery of the event')
        ns = input()
        event['summary'] = ns
        updated_event = service.events().update(calendarId='primary', eventId=eventid, body=event).execute()
    elif u == 'Location':
        print('what\'s the new location of the event')
        r = input()
        maxattendees = 10
        if r == "Midoun meeting room":
            room = "focus-corporation.com_3436373433373035363932@resource.calendar.google.com"
        elif r == "Aiguilles Meeting Room":
            room = "focus-corporation.com_3132323634363237333835@resource.calendar.google.com"
        elif r == "Barrouta Meeting Room":
            room = "focus-corporation.com_3335353934333838383834@resource.calendar.google.com"
        elif r == "Kantaoui Meeting Room":
            room = "focus-corporation.com_3335343331353831343533@resource.calendar.google.com"
        elif r == "Gorges Meeting Room":
            room = "focus-corporation.com_3436383331343336343130@resource.calendar.google.com"
        elif r == "Ichkeul Meeting Room":
            room = "focus-corporation.com_36323631393136363531@resource.calendar.google.com"
        elif r == "Khemir Meeting Room":
            room = "focus-corporation.com_3935343631343936373336@resource.calendar.google.com"
        elif r == "Tamaghza Meeting Room":
            room = "focus-corporation.com_3739333735323735393039@resource.calendar.google.com"
        elif r == "Friguia Meeting Room":
            room = "focus-corporation.com_3132343934363632383933@resource.calendar.google.com"
            maxattendees = 15
        elif r == "Ksour Meeting Room":
            room = "focus-corporation.com_@resource.calendar.google.com"
        elif r == "Medeina Meeting Room":
            room = "focus-corporation.com_@resource.calendar.google.com"
        elif r == "Thyna Meeting Room":
            room = "focus-corporation.com_@resource.calendar.google.com"

        mr = {'email': room}
        event['location'] = r
        updated_event = service.events().update(calendarId='primary', eventId=eventid, body=event).execute()
    elif u == 'Attendees':
        print('what\'s the new location of the event')
        nl = input()
    elif u == 'Start Time':
        print('what\'s the new location of the event')
        nl = input()
    elif u == 'End Time':
        print('what\'s the new location of the event')
        nl = input()


if __name__ == '__main__':
    main()
