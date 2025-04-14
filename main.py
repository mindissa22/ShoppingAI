import os
from dotenv import load_dotenv
from aipolabs import ACI

# Load the environment variables from the .env file
load_dotenv()

# Get the values from the environment
LINKED_ACCOUNT_OWNER_ID = os.getenv("LINKED_ACCOUNT_OWNER_ID")
ACI_API_KEY = os.getenv("ACI_API_KEY")

# Ensure both are set, or raise an error
if not LINKED_ACCOUNT_OWNER_ID or not ACI_API_KEY:
    raise ValueError("API Key or Linked Account Owner ID is not set in the environment.")

# Create the ACI client with only the API key
aci = ACI(api_key=ACI_API_KEY)

# Now you can proceed to use the ACI client with your API key and Linked Account Owner ID
print("ACI API Key loaded successfully.")

# Optional: Set the linked_account_owner_id if needed in a different way
# You might need to check the documentation for how to set linked_account_owner_id properly.


