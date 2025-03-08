import re
import tldextract 

url = input("Enter the URL to analyze: ")

def contains_phishing_keywords(url):
    phishing_keywords = ["verify", "secure", "bank", "account", 
                         "update", "password", "confirm", "billing", "support"]
    
    found_keywords = [keyword for keyword in phishing_keywords if keyword in url.lower()]
    if found_keywords:
        print(f"Phishing-related keywords found in URL: {url}\n")
        print(f"Detected Keywords: {', '.join(found_keywords)}\n")
        return True
    return False

def check_url_shorteners(url):
    shorteners = ["bit.ly", "goo.gl", "tinyurl.com", "ow.ly", "t.co"]
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"
    
    if domain in shorteners:
        print(f"URL uses a shortener: {domain}\n")
        return True
    return False

def check_suspicious_subdomains(url):
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"
    subdomain = extracted.subdomain
    
    if subdomain and subdomain not in ["www", ""]:
        print(f"Suspicious subdomain detected: {subdomain}\n")
        return True
    return False

def check_https(url):
    if not url.startswith("https://"):
        print("URL does not use HTTPS, it may be insecure.\n")
        return True
    return False

def analyze_url(url):
    print(f"\nAnalyzing URL: {url}\n")
    
    is_suspicious = any([
        contains_phishing_keywords(url),
        check_url_shorteners(url),
        check_suspicious_subdomains(url),
        check_https(url)
    ])

    if is_suspicious:
        print("This URL is potentially dangerous! Proceed with caution.\n")
    else:
        print("This URL appears to be safe.\n")

URL_pattern = re.compile(r"https?://(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?:/[^\s]*)?")

analyze_url(url)

# URL to Test:
#http://secure-login.bankverify.com/update-password
#https://bit.ly/3xyzabc
#http://paypal.verify-account-support.com
#https://www.github.com
#https://apple.com/home