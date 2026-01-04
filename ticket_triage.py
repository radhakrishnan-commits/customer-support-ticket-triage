import pandas as pd

# Load the collected dataset
data = pd.read_csv("customer_tickets.csv")

def analyze_ticket(message):
    message = message.lower()

    # Identify issue type, priority, and response time
    if ("error" in message or "crash" in message or
        "failed" in message or "not opening" in message):
        issue_type = "Technical Issue"
        priority = "High"
        response_time = "1 Hour"

    elif ("payment" in message or "refund" in message or
          "money" in message or "deducted" in message):
        issue_type = "Billing Issue"
        priority = "Medium"
        response_time = "4 Hours"

    else:
        issue_type = "General Query"
        priority = "Low"
        response_time = "24 Hours"

    return issue_type, priority, response_time


print("\nCustomer Support Ticket Triage System")
print("=" * 50)

# Process each ticket from dataset
for index, row in data.iterrows():
    issue, priority, time = analyze_ticket(row["Message"])

    print("Ticket ID:", row["Ticket_ID"])
    print("Customer Message:", row["Message"])
    print("Issue Type:", issue)
    print("Priority:", priority)
    print("Expected Response Time:", time)
    print("-" * 50)
