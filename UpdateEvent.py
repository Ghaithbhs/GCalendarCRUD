from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/calendar/v3/calendars/calendarId/events/eventId']

def main():

    # Get inputs
    print('what is the event you want to update')
    e = input()
    print('what do you want to update? ')
    u = input()
    if u == 'name':
        print("What's the new name of the event?")
        n = input()
    elif u == 'date':
        print('what the day of the event')
        d = input()
        print("month: ")
        m = input()
        print('year : ')
        y = input()
    elif u == 'atendees':
        print('attendees : ')
        a = input()
    elif u == 'meeting room':
        print('Meeting Room : ')
        r = input()
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

    # Query
    events_result = service.events().list(calendarId='primary',
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime', q=n).execute()
    events = events_result.get('items', [])

    if not events:
        print('event not found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'], event['location'])
        eventid = event['id']
        print(event['id'])
        print(eventid)

    service.events().delete(calendarId='primary', eventId=eventid).execute()


if __name__ == '__main__':
    main()