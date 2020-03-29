import requests
import json

webhook_url = 'https://discordapp.com/api/webhooks/{webhook.id}/{webhook.token}'
payload = {'username': 'bot_name', 'avatar_url': '<link_for_image>', 'content': 'hello world'}
requests.post(webhook_url, headers={'Content-Type': 'application/json'}, data=json.dumps(payload))
