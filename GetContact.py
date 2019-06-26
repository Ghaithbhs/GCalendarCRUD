from __future__ import print_function
import gdata.data
import gdata.contacts.client
import gdata.contacts.data

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.google.com/m8/feeds/contacts/{smartbox@focus-corporation.com}/full']


def main():

    # Get inputs
    """print("What's the name of the event?")

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
    #looking for contacts:
    """"""Retrieves a list of contacts and displays name and primary email.""""""
    feed = self.gd_client.GetContacts()
    self.PrintPaginatedFeed(feed, self.PrintContactsFeed)"""

    gd_client = gdata.contacts.client.ContactsClient()
    feed = gd_client.GetContacts()
    for i, entry in enumerate(feed.entry):
        print
        '\n%s %s' % (i + 1, entry.name.full_name.text)
        if entry.content:
            print
            '    %s' % (entry.content.text)
            # Display the primary email address for the contact.
        for email in entry.email:
            if email.primary and email.primary == 'true':
                print
                '    %s' % (email.address)
        # Show the contact groups that this contact is a member of.
        for group in entry.group_membership_info:
            print
            '    Member of group: %s' % (group.href)
        # Display extended properties.
        for extended_property in entry.extended_property:
            if extended_property.value:
                value = extended_property.value
            else:
                value = extended_property.GetXmlBlob()
            print
            '    Extended Property - %s: %s' % (extended_property.name, value)


if __name__ == '__main__':
    main()
