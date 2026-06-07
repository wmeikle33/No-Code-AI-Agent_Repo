import win32com.client as win32

def send_outlook_email(to_address, subject, body, attachment_path=None):
    # Connect to Outlook
    outlook = win32.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0) # 0 = Mail Item
    
    # Configure Email Fields
    mail.To = to_address
    mail.Subject = subject
    mail.Body = body  # Use mail.HTMLBody for HTML formatted text
    
    # Optional: Attach a file
    if attachment_path:
        mail.Attachments.Add(attachment_path)
    
    # Send or Preview
    # mail.Display() # Uncomment to preview the email before sending
    mail.Send()

def read_inbox_emails(limit=5):
    outlook = win32.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # 6 refers to Inbox
    messages = inbox.Items
    
    # Sort messages by received time (newest first)
    messages.Sort("[ReceivedTime]", True)
    
    for i, message in enumerate(messages):
        if i >= limit:
            break
        print(f"Subject: {message.Subject}")
        print(f"Sender: {message.SenderName}")
        print(f"Received: {message.ReceivedTime}")
        print(f"Body snippet: {message.Body[:100]}\n")
