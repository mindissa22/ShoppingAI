import os
from dotenv import load_dotenv
from aipolabs import ACI
import json

# Step 1: Load environment variables from the .env file
load_dotenv()

# Step 2: Get API Key and Account Owner ID from environment variables
ACI_API_KEY = os.getenv("ACI_API_KEY")
LINKED_ACCOUNT_OWNER_ID = os.getenv("LINKED_ACCOUNT_OWNER_ID")

# Step 3: Log the API Key and Account Owner ID to ensure they are loaded correctly
print(f"Using API Key: {ACI_API_KEY}")
print(f"Account Owner ID: {LINKED_ACCOUNT_OWNER_ID}")

# Step 4: Initialize ACI client
aci = ACI(api_key=ACI_API_KEY)

# Step 5: Get the function definition for FIRECRAWL__SEARCH
function_definition = aci.functions.get_definition("FIRECRAWL__SEARCH")

# Step 6: Prepare the parameters (for example, a search query)
params = {
    "body": {
        "query": "light blue polo shirt under £30 site:h&m.com",  # Search query
        "limit": 5  # Limit the number of search results to 5
    }
}

# Step 7: Execute the function with the prepared parameters
result = aci.functions.execute(
    function_definition["function"]["name"],  # FIRECRAWL__SEARCH
    params,  # Pass the parameters (query and limit)
    linked_account_owner_id=LINKED_ACCOUNT_OWNER_ID
)

# Step 8: Print the result from the function call
print(f"Function call result: {result}")

