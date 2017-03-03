# notify
Use Twilio API to notify via text when jobs are done.

Be sure to replace the ACCOUNT_SID and AUTH_TOK with your Twilio API key information, which can be obtained from https://www.twilio.com/.

Usage:

  python notify.py -c "COMMAND" [-m "MESSAGE"] [-q]
  
    -c : Command to be run; type exactly as would be input into the shell
    
    -m : Message to be sent
    
    -q : "quiet", don't send a message
