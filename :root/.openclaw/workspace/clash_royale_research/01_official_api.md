# Clash Royale Official API Research

## Base URL
```
https://api.clashroyale.com/v1
```

## Authentication
- Register at https://developer.clashroyale.com
- IP-allowlist required
- Browser requests blocked (CORS)

## Rate Limits
- Not officially published
- ~10-30 requests/sec estimated
- HTTP 429 on rate limit

## Key Endpoints

### Players
- `GET /players/{tag}` - Profile data
- `GET /players/{tag}/battlelog` - Recent battles (25 max)
- `GET /players/{tag}/upcomingchests` - Chest cycle

### Clans
- `GET /clans/{tag}` - Clan info
- `GET /clans` - Search with filters
- `GET /clans/{tag}/members` - Member list
- `GET /clans/{tag}/warlog` - War history

### Cards
- `GET /cards` - All cards with stats

## SDKs
Python: `pip install clashroyale`

## Example (Python)
```python
import clashroyale
client = clashroyale.official_api.Client(token="YOUR_TOKEN")
player = client.get_player("#PLAYER_TAG")
print(player.trophies)
```
