from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():

    # Get inputs
    print("What's the name of the event?")
    n = input()
    print('what the day of the event')
    d = input()
    print("month: ")
    m = input()
    print('year : ')
    y = input()
    print('attendees : ')
    a = input()
    l = "FOCUS-1ere-Midoune Meeting Room (10)"
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
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

    #Add an event
    event = {
        'summary': n,
        'location': 'Focus',
        #'resource': 'focus-corporation.com_3436373433373035363932@resource.calendar.google.com',
        'description': 'A chance to hear more about Google\'s developer products.',
        'start': {
            'dateTime': y+'-'+m+'-'+d+'T9:00:00-01:00',
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': y+'-'+m+'-'+d+'T17:00:00-01:00',
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=2'
        ],
        'attendees': [
            {'email': a,
             'email': 'focus-corporation.com_3436373433373035363932@resource.calendar.google.com'
             },
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    event = service.events().insert(calendarId='primary', sendNotifications=True, body=event).execute()
    print
    'Event created: %s' % (event.get('htmlLink'))


if __name__ == '__main__':
    main()
