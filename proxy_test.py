import requests

# Proxy configuration
proxies = {
    "http": "socks4://88.24.38.156:8080",
    "https": "socks4://88.24.38.156:8080"
}

# Test URL to check your public IP (this is NOT LinkedIn, just for testing)
url = "http://httpbin.org/ip"

# Make the request with the proxy
try:
    response = requests.get(url, proxies=proxies)
    print("Your public IP when using this proxy is:", response.json())
except Exception as e:
    print("Error connecting with the proxy:", e)
