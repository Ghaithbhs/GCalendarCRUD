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
        listeofattendees = event['attendees']
        #print(event['id'])
        #print(eventid)
    print('what do you want to update? Summery - Start Date/Time - End Date/Time - Location - Attendees - Meeting Room?')
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
            room = "focus-corporation.com_3636383930383831343637@resource.calendar.google.com"
        elif r == "Medeina Meeting Room":
            room = "focus-corporation.com_3538333137333939363039@resource.calendar.google.com"
        elif r == "Thyna Meeting Room":
            room = "focus-corporation.com_38333135333134383939@resource.calendar.google.com"

        listofroomsadress = ['focus-corporation.com_3436373433373035363932@resource.calendar.google.com',
                             'focus-corporation.com_3132323634363237333835@resource.calendar.google.com',
                             'focus-corporation.com_3335353934333838383834@resource.calendar.google.com',
                             'focus-corporation.com_3335343331353831343533@resource.calendar.google.com',
                             'focus-corporation.com_3436383331343336343130@resource.calendar.google.com',
                             'focus-corporation.com_36323631393136363531@resource.calendar.google.com',
                             'focus-corporation.com_3935343631343936373336@resource.calendar.google.com',
                             'focus-corporation.com_3739333735323735393039@resource.calendar.google.com',
                             'focus-corporation.com_3132343934363632383933@resource.calendar.google.com',
                             'focus-corporation.com_3636383930383831343637@resource.calendar.google.com',
                             'focus-corporation.com_3538333137333939363039@resource.calendar.google.com',
                             'focus-corporation.com_38333135333134383939@resource.calendar.google.com']
        listofroomsnames = ['Midoun meeting room', 'Aiguilles Meeting Room', 'Barrouta Meeting Room',
                            'Kantaoui Meeting Room', 'Gorges Meeting Room', 'Ichkeul Meeting Room',
                            'Khemir Meeting Room', 'Tamaghza Meeting Room', 'Friguia Meeting Room',
                            'Ksour Meeting Room', 'Medeina Meeting Room', 'Thyna Meeting Room']
        o = 0
        p = 0
        t = 0
        y = 0
        attendemail = []
        # meetingroom = []
        attendname = []
        finallist = []
        #mr = {'email': room}
        # meetingroom.append(mr)
        # event['attendees'] = meetingroom
        attend = event['attendees']
        l = len(attend)
        while o != l:
            attendemail.append(attend[o]['email'])
            attendname.append(attend[0].get('displayName'))
            o = o + 1
        while p != len(attendemail):
            while t != len(listofroomsadress):
                if attendemail[p] == listofroomsadress[t]:
                    attendemail[p] = room
                    attendname[p] == r
                t = t + 1
            p = p + 1
        while y != len(attendemail):
            mr = {'email': attendemail[y]}
            finallist.append(mr)
            y = y + 1

        event['attendees'] = finallist
        event['location'] = r
        updated_event = service.events().update(calendarId='primary', eventId=eventid, body=event).execute()
        #updated_event = service.events().insert(calendarId='primary', eventId=eventid, body=event).execute()
    # updating the attendees
    elif u == 'Attendees':
        # Getting the all ready invited attendees
        invitedattendees = event['attendees']
        invitedattendemail = []
        invitedattendname = []
        finallist = []
        o = 0
        l = len(invitedattendees)
        while o != l:
            invitedattendemail.append(invitedattendees[o]['email'])
            invitedattendname.append(invitedattendees[o].get('displayName'))
            o = o + 1
        # at this stage we have 3 lists
        # 1) invitedattend[] which is what we get from the google calendar
        # 2) invitedattendname[]the list of names of each attendee
        # 3) invitedattendemail[] the list of emails of each attendee

        # Now we have to figure out the number of attendees that we can add no more then the capacity of the room
        maxattendees = 10
        if event['location'] == 'Friguia Meeting Room':
            maxattendees = 15
        print('how many attendees would like to add ?')
        at = int(input())
        na = maxattendees - at
        if na <= 0:
            print('you can\'t add attendees')
        elif na < at:
            print('you can only add ', na, ' attendees')
        else:
            na = at
        # Getting the Attendees from input
        attemail = []
        noms = []
        f = 0
        i = 1
        g = 0
        found = False
        found2 = False
        # get all contacts in a list
        for person in connections:
            emailAddresses = person.get('emailAddresses', [])
            names = person.get('names', [])
            attemail.append(emailAddresses[0].get('value'))
            noms.append(names[0].get('displayName'))
        print(noms)
        p = len(noms)
        # Int a list of attendees and it's length is the maximum number of attendees according to the room chosen befor
        attendees = ['blabla@blabla'] * na
        # first attendee
        print('attendees :')
        a = input()
        # looking for the contact in contact list
        if a != '':
            while (g != p) & (found is False):
                # if the name in the input matches the a name in the list we add the email of that person to the attendees
                # list which will be treated later to delete the examples 'blabla@blabla.com'
                if noms[g] == a:
                    attendees[0] = attemail[g]
                    g = g + 1
                    found = True
                else:
                    g = g + 1
            if found is False:
                print('contact not found try again please')
        else:
            print('no attendees added')
        # other attendees to add less then max number of attendees
        while i != na:
            a = input()
            if a == '':
                break
            else:
                while (f != p) | (found2 is False):
                    if noms[f] == a:
                        attendees[i] = attemail[f]
                        found2 = True
                    f = f + 1
            i = i + 1
        # until this stage we have a list of attendees + blanks filled with blabla@blabla.om
        # print(attendees)
        l = len(attendees)
        # print(l)
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
        print(att)
        # print(l2)
        w = 0
        attendemail = []

        while w != len(attendees):
            print(attendees[w])
            attendemail.append(attendees[w])
            w = w + 1
            # attendname.append(attendees[0].get('displayName'))
        attendee = []
        print(attendemail)
        for s in range(len(invitedattendemail)):
            email = {'email': invitedattendemail[s]}
            attendee.append(email)
        print(attendee)
        for r in range(len(attendemail)):
            email = {'email': attendemail[r]}
            attendee.append(email)
        print(attendee)
        event['attendees'] = attendee

        updated_event = service.events().update(calendarId='primary', eventId=eventid, body=event).execute()
    elif u == 'Start Date/Time':
        start = event['start'].get('dateTime', event['start'].get('date'))
        print('Your event starts at ', start)
        print('what\'s the new start date of the event? yyyy-mm-ddT00:00:00')
        nsd = input()
        event['start'] = nsd
        updated_event = service.events().update(calendarId='primary', eventId=eventid, body=event).execute()
    elif u == 'End':
        end = event['end'].get('dateTime', event['start'].get('date'))
        print('Your event ends at ', end)
        print('what\'s the new end date of the event? yyyy-mm-ddT00:00:00')
        ned = input()
        nedt = ned.get('dateTime')
        event['end'] = nedt + '+01:00'
        updated_event = service.events().update(calendarId='primary', eventId=eventid, body=event).execute()


if __name__ == '__main__':
    main()
