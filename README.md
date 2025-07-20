# Firedrill

Train your on-call team with GPT-powered incident simulations.

## Requirements

- Python 3  
- An OpenAI API token with available credits  
- `make` (for setup convenience)

## Getting Started

1. Clone the repo  
2. Ensure you have Python 3 and `make` installed  
3. Copy `.env.example` to `.env` and add your OpenAI API token  
   - Get a token at: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys) 
   - You'll need to load credits onto your token
4. Run `make setup` to install dependencies  
5. Run `make start` to launch the default scenario
6. Run `make start SCENARIO=./scenarios/<insert_scenario_name>.yaml to run an example scenario


Example interactions:

lukerouker@Lukes-MacBook-Air firedrill % make start
Running Firedrill simulation...
source .venv/bin/activate && python ./src/firedrill.py ./scenarios/cache_ttl_misconfig.yaml
🔥 Cache TTL Misconfiguration
ALERT: Customer support has escalated reports of incorrect data showing on the product details page. Users are seeing outdated information, and some edits made through the admin panel are not reflected. You are the primary responder.


>> What would you like to do next? (free text or hint or exit)...
can we load the product details page?
Certainly. When you load the product details page (GET /products/:id), it renders successfully with a 200 OK status. However, the data appears stale compared to what's in the admin panel. What would you like to do next?

>> What would you like to do next? (free text or hint or exit)...
okay, we've got stale data, are we caching that page?
Great question. Yes, the product details page is using a cache layer for product data. What would you like to investigate next?

>> What would you like to do next? (free text or hint or exit)...
let's go see if the caching config has changed recently
Upon reviewing the last deployment, you find that there was a configuration change: the cache TTL was increased from 5 minutes to 12 hours. What would you like to do with this information?

>> What would you like to do next? (free text or hint or exit)...
let's revert that change
Reverting the cache TTL back to 5 minutes is a good step. What would you like to do next to ensure the data is up-to-date for users?

>> What would you like to do next? (free text or hint or exit)...
we should also flush the cache 
🎉 You have successfully resolved the incident!
✅ Resolution:
The cache TTL was reverted to 5 minutes and the cache was flushed. Product data now updates correctly. Issue resolved.

---

lukerouker@Lukes-MacBook-Air firedrill % make start
Running Firedrill simulation...
source .venv/bin/activate && python ./src/firedrill.py ./scenarios/cache_ttl_misconfig.yaml
🔥 Cache TTL Misconfiguration
ALERT: Customer support has escalated reports of incorrect data showing on the product details page. Users are seeing outdated information, and some edits made through the admin panel are not reflected. You are the primary responder.


>> What would you like to do next? (free text or hint or exit)...
can we check if there were any recent changes?
Great idea! Upon reviewing the last deploy, you discover a configuration change: the cache TTL was increased from 5 minutes to 12 hours. What would you like to do next?

>> What would you like to do next? (free text or hint or exit)...
revert that change and flush the cache 
🎉 You have successfully resolved the incident!
✅ Resolution:
The cache TTL was reverted to 5 minutes and the cache was flushed. Product data now updates correctly. Issue resolved.

--- 

lukerouker@Lukes-MacBook-Air firedrill % make start
Running Firedrill simulation...
source .venv/bin/activate && python ./src/firedrill.py ./scenarios/cache_ttl_misconfig.yaml
🔥 I sold that product hours ago!
ALERT: Customer support has escalated reports of incorrect data showing on the product details page. Users are seeing outdated information, and some edits made through the admin panel are not reflected. You are the primary responder.


>> What would you like to do next? (free text or hint or exit)...
can I ask a teammate for help?
Certainly! You can ask a teammate for help. What specific aspect of the incident would you like to ask them about? This will help me simulate their response effectively.

>> What would you like to do next? (free text or hint or exit)...
where should we start looking?
A good starting point would be to investigate the elevated errors on the product details page. You might want to check the logs or recent changes that could have affected the data being displayed. Let me know what you'd like to do next!

>> What would you like to do next? (free text or hint or exit)...
can we check the logs?
Checking the logs is a great idea. Upon reviewing the logs, you find that the product details page (GET /products/:id) renders successfully with a 200 OK status, but the data looks stale compared to what's in the admin panel. What would you like to do next?

>> What would you like to do next? (free text or hint or exit)...
why would the data be stale?
Stale data can often be a result of caching issues. It might be helpful to investigate the cache layer for product data to see if there are any anomalies or recent changes. Would you like to proceed with that?

>> What would you like to do next? (free text or hint or exit)...
is anything wrong with the cache?
Upon checking the cache layer for product data, you find that the data appears present but hasn't updated since 7:00 AM. This suggests that the cache might not be refreshing as expected. What would you like to do next?

>> What would you like to do next? (free text or hint or exit)...
why isn't the cache refreshing?
To understand why the cache isn't refreshing, it would be useful to review any recent changes or deployments that might have affected the cache configuration. Would you like to investigate recent changes?

>> What would you like to do next? (free text or hint or exit)...
look at recent deployments
Reviewing the last deployment reveals a configuration change: the cache TTL (Time-To-Live) was increased from 5 minutes to 12 hours. This change could be causing the stale data issue. How would you like to proceed?

>> What would you like to do next? (free text or hint or exit)...
rollback
🎉 You have successfully resolved the incident!
Resolution:
The cache TTL was reverted to 5 minutes and the cache was flushed. Product data now updates correctly. Issue resolved.
