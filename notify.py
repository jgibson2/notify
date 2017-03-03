from twilio.rest import TwilioRestClient
import argparse
import subprocess

ACCOUNT_SID = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
AUTH_TOK = 'bcXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
PHONE_TO = '+1XXXXXXXXXX'
PHONE_FROM = '+1XXXXXXXXXX'


client = TwilioRestClient(ACCOUNT_SID, AUTH_TOK)

parser = argparse.ArgumentParser(description='Run a job and notify when finished.')
parser.add_argument('-c', '--command', action='store', help='Command to run (place in quotes)', required=True)
parser.add_argument('-q', '--quiet', action='store_true', help='Do not send text message')
parser.add_argument('-m', '--message', action='store', help='Message to send')

args = parser.parse_args()

subprocess.check_call(args.command, shell=True)
if not args.quiet:
    client.messages.create(
        to=PHONE_TO,
        from_=PHONE_FROM,
        body='Job done: %s' % args.message,
    )
