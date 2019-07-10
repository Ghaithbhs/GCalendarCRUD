from __future__ import print_function
import httplib2
from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
#from oauth2client.tools import run
from oauth2client import tools

FLOW = OAuth2WebServerFlow(
    client_id='361001423406-meqq5djv2vf54fhd0ect7163ugkpssmm.apps.googleusercontent.com',
    client_secret='pioORdrpsd-cFemxkETi08yM',
    scope='https://www.googleapis.com/auth/contacts.readonly',
    user_agent='Focus Smart Box')

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

i = 1
max = 10
f = 0
found = False
found = False
attendees = ['blabla@blabla'] * max
atto = []
noms = []
# get all contacts in a list
for person in connections:
    emailAddresses = person.get('emailAddresses', [])
    names = person.get('names', [])
    atto.append(emailAddresses[0].get('value'))
    noms.append(names[0].get('displayName'))
print(atto)
print(noms)
p = len(noms)
print(p)
g = 0
# first attendee
print('attendees :')
a = input()
if a != '':
    while (g != p) & (found is False):
        if noms[g] == a:
            attendees[0] = atto[g]
            g = g + 1
            found = True
        else:
            print('contact not found')
            g = g + 1
else:
    print('no attendees added')
# other attendees to add less then max
while i != max:
    a = input()
    if a == '':
        break
    else:
        while (f != len(noms)) | (found is False):
            if noms[f] == a:
                attendees[i] = atto[f]
                found = True
            f = f + 1
    i = i + 1
# until this stage we have a list of attendees + blanks filled with blabla@blabla.om
print(attendees)
l = len(attendees)
print(l)
# in this part we are going to get the attendees without the blanks
m = 0
att = []
while m != l:
    if attendees[m] != 'blabla@blabla':
        att.append(attendees[m])
        m = m+1
    else:
        m = m+1
l2 = len(att)
print(att)
print(l2)

attendee = []
for r in range(l2):
    email = {'email': att[r]}
    attendee.append(email)
room = {'email': 'room'}
attendee.append(room)
event = {
        'summary': 'test',
        'location': 'test',
        #'resource': 'focus-corporation.com_3436373433373035363932@resource.calendar.google.com',
        'description': 'A chance to hear more about Google\'s developer products.',
        'start': {
            'dateTime': 'T9:00:00-01:00',
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': 'T17:00:00-01:00',
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=2'
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
        'attendees': attendee,
    }
print(event)
