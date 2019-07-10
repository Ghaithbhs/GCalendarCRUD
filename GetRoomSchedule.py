from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly' +
          'https://www.googleapis.com/auth/admin.directory.resource.calendar.readonly']


def main():
    # Get Credentials
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

    # Call the Calendar API
    print('Meeting Room : ')
    r = input()
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
    elif r == "Ksour Meeting Room":
        room = "focus-corporation.com_@resource.calendar.google.com"
    elif r == "Medeina Meeting Room":
        room = "focus-corporation.com_@resource.calendar.google.com"
    elif r == "Thyna Meeting Room":
        room = "focus-corporation.com_@resource.calendar.google.com"
    # until this stage we have the name of the meeting room in a variable called room
    # next part is to get the id an the calendar of that room
    # Request :
    '''R = {
        "timeMin": datetime,
        "timeMax": datetime,
        "timeZone": 'America/Los_Angeles',
        "items": [
            {
                "id": string
            }
        ]
    }'''
    #now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the schedule of the meeting room')
    events_result = service.events().list(calendarId='focus-corporation.com_3436373433373035363932',
                                          maxResults=1, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('event not found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'], event['location'])
        eventid = event['id']
        print(event['id'])
        print(eventid)


if __name__ == '__main__':
    main()
