from requests import get

websites = (
    "google.com",
    "netflix.com",
    "https://httpbin.org/status/101",
    "https://httpbin.org/status/304",
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/501"
)

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    
    status = response.status_code
    if status >= 500:
        results[website] = "5xx Server Error"
    elif status >= 400:
        results[website] = "4xx Client Error"
    elif status >= 300:
        results[website] = "3xx Redirection"
    elif status >= 200:
        results[website] = "2xx OK"
    elif status >= 100:
        results[website] = "1xx Informational"
    else:
        results[website] = "Unknown Status"

print(results)
    
