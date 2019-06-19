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
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    #print("What's the name of the event you want t delete?")
    n = 'NGh0Z3BtbTFobWFrNzQ0cjBrYmtkY29kYXIgZXVndTlrYW4xZGRpMXBtaTZzazNpYjWoNmdAZw'
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

    creds = get_credentials()
    http = creds.authorize(httplib2.Http())
    calendar_service = discovery.build('calendar', 'v3', http=http)
    event = calendar_service.events().insert(calendarId='primary',
                                             body=event).execute()
    eventId = event.get('id')
    # Get event by name
    ''' Event{eid=k5r2meajcb92kgbf3olu74hs4g_20190619T160000Z*, 
    organizer=ghaithbhs095@gmail.com, 
    participant=ghaithbhs095@gmail.com, 
    actor=ghaithbhs095@gmail.com, 
    summary=testing notification, 
    status=CONFIRMED, seq=0, 
    startTime=2019-06-19T17:00:00Z, 
    endTime=2019-06-20T01:00:00Z, 
    firstStart=20190618T170000, 
    rdata=RRULE:FREQ=DAILY;COUNT=2}
    event = service.events().get(calendarId='primary', eventId=eventId).execute()
    print(event['summary'])'''


if __name__ == '__main__':
    main()
