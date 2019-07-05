i = 1
max = 10
attendees = ['blabla@blabla'] * max
# first attendee
print('attendees :')
a = input()
if a != '':
    attendees[0] = a
else:
    print('no attendees added')
# other attendees to add less then max
while i != max:
    a = input()
    if a == '':
        break
    else:
        attendees[i] = a
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
