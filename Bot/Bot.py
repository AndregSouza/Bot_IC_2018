# Example 1: sets up service wrapper, sends initial message, and
# receives response.

import watson_developer_cloud

# Set up Assistant service.
service = watson_developer_cloud.AssistantV1(
  username = 'c5c98610-f036-4f05-a2b6-681cb2f5a45d', # replace with service username
  password = 'PTx0jXlZUv8S', # replace with service password
  version = '2018-02-16'
)
workspace_id = '1ee08fda-2edb-4fd4-98d2-07290313c5dc' # replace with workspace ID

# Start conversation with empty message.
response = service.message(
  workspace_id = workspace_id,
  input = {
    'text': ''
  }
)

# Print the output from dialog, if any. Assumes a single text response.
if response.result['output']:
  print(response.result['output']['text'][0])
