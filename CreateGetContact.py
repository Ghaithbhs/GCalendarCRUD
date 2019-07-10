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

# Go to the Google API Console, open your application's
# credentials page, and copy the client ID and client secret.
# Then paste them into the following code.
FLOW = OAuth2WebServerFlow(
    client_id='361001423406-meqq5djv2vf54fhd0ect7163ugkpssmm.apps.googleusercontent.com',
    client_secret='pioORdrpsd-cFemxkETi08yM',
    scope='https://www.googleapis.com/auth/contacts.readonly',
    user_agent='Focus Smart Box')


def main():

    # CREDENTIALS FOR GOOGLE CALENDAR API
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

    # CREDENTIALS FOR GOOGLE PEOPLE API
    # If the Credentials don't exist or are invalid, run through the
    # installed application flow. The Storage object will ensure that,
    # if successful, the good Credentials will get written back to a
    # file.
    storage = Storage('info.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid is True:
        credentials = tools.run_flow(FLOW, storage)

    # Create an httplib2.Http object to handle our HTTP requests and
    # authorize it with our good Credentials.
    http = httplib2.Http()
    http = credentials.authorize(http)

    # Build a service object for interacting with the API. To get an API key for
    # your application, visit the Google API Console
    # and look at your application's credentials page.
    people_service = build(serviceName='people', version='v1', http=http)
    results = people_service.people().connections().list(
        resourceName='people/me',
        pageSize=10,
        personFields='emailAddresses,names').execute()
    connections = results.get('connections', [])

    # Get inputs
    print("What's the name of the event?")
    n = input()
    print('what the day of the event')
    d = input()
    print("month: ")
    m = input()
    print('year : ')
    y = input()
    print('Meeting Room : ')
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
    i = 1
    atto = []
    noms = []
    found = False
    al = 0
    for person in connections:
        emailAddresses = person.get('emailAddresses', [])
        names = person.get('names', [])
        atto.append(emailAddresses[0].get('value'))
        noms.append(names[0].get('displayName'))
    attendees = ['blabla@blabla'] * maxattendees
    # first attendee
    print('attendees :')
    a = input()
    if a != '':
        while (al != len(noms)) & (found is False):
            if noms[al] == a:
                attendees[0] = a
                al = al + 1
                found = True
            else:
                print('name not found')
    else:
        print('no attendees added')
    # other attendees to add less then max
    while i != maxattendees:
        a = input()
        if a == '':
            break
        else:
            attendees[i] = a
            i = i + 1
    # until this stage we have a list of attendees + blanks filled with blabla@blabla.om
    #print(attendees)
    l = len(attendees)
    #print(l)
    # in this part we are going to get the attendees without the blanks
    t = 0
    att = []
    while t != l:
        if attendees[t] != 'blabla@blabla':
            att.append(attendees[t])
            t = t + 1
        else:
            t = t + 1
    l2 = len(att)

    attendee = []
    for r in range(l2):
        email = {'email': att[r]}
        attendee.append(email)
    attendee.append(mr)

    #Add an event
    event = {
        'summary': n,
        'location': r,
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
        'attendees': attendee,
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    '''s = 0
    for s in range(l2):
        query = {**event, **attendee[s]}'''
    event = service.events().insert(calendarId='primary', sendNotifications=True, body=event).execute()
    print
    'Event created: %s' % (event.get('htmlLink'))


if __name__ == '__main__':
    main()
