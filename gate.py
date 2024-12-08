import requests
from bs4 import BeautifulSoup
import re
from tqdm import tqdm
from colorama import *

# Initialize colorama
init(autoreset=True)

# Color definitions
merah = Fore.LIGHTRED_EX
putih = Fore.LIGHTWHITE_EX
hijau = Fore.LIGHTGREEN_EX
kuning = Fore.LIGHTYELLOW_EX
biru = Fore.LIGHTBLUE_EX
reset = Style.RESET_ALL

# Main function for the app banner
def main():
    banner = f"""
{putih}███╗   ██╗ ██████╗  ██████╗ ██████╗   {putih}A Payment Gateway {hijau} Scanner 
████╗  ██║██╔═══██╗██╔═══██╗██╔══██╗  {hijau}Version: {putih}v 1.0.0
██╔██╗ ██║██║   ██║██║   ██║██████╔╝  {putih}Author: {hijau}Noob Pirate Aka Blionrie
██║╚██╗██║██║   ██║██║   ██║██╔══██╗  {hijau}Note: {putih}Every Action Has a Consequence
██║ ╚████║╚██████╔╝╚██████╔╝██████╔╝  {putih}Join: {hijau}https://t.me/piratexcrew
╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═════╝   {hijau}Bored..? : {putih}http://bit.ly/3MTMHyU
___________________________________________________________________________
    {reset}"""
    print(banner)

# Call main() to display the banner at the beginning
main()

# Function to scan a single page
def scan_page(url):
    result = {
        "payment_gateways": set(),
        "captcha": False,
        "cloudflare": False,
        "graphql": False,
        "platforms": set(),
        "card_support": set(),
    }
    try:
        # Fetch page content
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        html_content = response.text

        # Check for Cloudflare
        result["cloudflare"] = "cloudflare" in response.headers.get("server", "").lower()

        # Detect payment gateways
        gateway_keywords = ["stripe", "paypal", "paytm", "razorpay", "square"]
        for keyword in gateway_keywords:
            if keyword in html_content.lower():
                result["payment_gateways"].add(keyword.capitalize())

        # Check for CAPTCHA
        captcha_patterns = [
            r"g-recaptcha",
            r"data-sitekey",
            r"captcha",
            r"hcaptcha",
            r"protected by cloudflare",
        ]
        if any(re.search(pattern, html_content, re.IGNORECASE) for pattern in captcha_patterns):
            result["captcha"] = True

        # Check for GraphQL
        result["graphql"] = "graphql" in html_content.lower()

        # Detect platform
        platform_keywords = {
            "woocommerce": "WooCommerce",
            "shopify": "Shopify",
            "magento": "Magento",
            "bigcommerce": "BigCommerce",
        }
        for keyword, name in platform_keywords.items():
            if keyword in html_content.lower():
                result["platforms"].add(name)

        # Detect card support
        card_keywords = ["visa", "mastercard", "amex", "discover", "diners", "jcb"]
        for card in card_keywords:
            if card in html_content.lower():
                result["card_support"].add(card.capitalize())

    except requests.exceptions.RequestException:
        pass  # Ignore errors and continue
    return result


# Main function to scan homepage and related pages
def scan_site(base_url):

    # Ensure URL has proper protocol
    if not base_url.startswith("http://") and not base_url.startswith("https://"):
        base_url = "http://" + base_url

    # Define extended list of related pages
    related_pages = [
        "/", "/checkout", "/buynow", "/cart", "/payment", "/order", 
        "/purchase", "/subscribe", "/confirm", "/billing", "/pay", 
        "/transactions", "/order-summary", "/complete"
    ]

    # Initialize aggregated results
    aggregated_results = {
        "payment_gateways": set(),
        "captcha": False,
        "cloudflare": False,
        "graphql": False,
        "platforms": set(),
        "card_support": set(),
    }

    # Scan all related pages
    with tqdm(total=len(related_pages), desc="Scanning", unit="page", ncols=80, bar_format="{l_bar}{bar}") as pbar:
        for page in related_pages:
            full_url = base_url.rstrip("/") + page
            page_results = scan_page(full_url)

            # Aggregate results
            aggregated_results["payment_gateways"].update(page_results["payment_gateways"])
            aggregated_results["captcha"] = aggregated_results["captcha"] or page_results["captcha"]
            aggregated_results["cloudflare"] = aggregated_results["cloudflare"] or page_results["cloudflare"]
            aggregated_results["graphql"] = aggregated_results["graphql"] or page_results["graphql"]
            aggregated_results["platforms"].update(page_results["platforms"])
            aggregated_results["card_support"].update(page_results["card_support"])

            pbar.update(1)

    # Display consolidated results
    print("\n\nScan completed!\n")
    print(f"URL: {base_url}")
    print(f"Payment Gateways: {', '.join(sorted(aggregated_results['payment_gateways'])) if aggregated_results['payment_gateways'] else 'None found'}")
    print(f"Captcha: {aggregated_results['captcha']}")
    print(f"Cloudflare: {aggregated_results['cloudflare']}")
    print(f"GraphQL: {aggregated_results['graphql']}")
    print(f"Platforms: {', '.join(sorted(aggregated_results['platforms'])) if aggregated_results['platforms'] else 'Unknown'}")
    print(f"Card Support: {', '.join(sorted(aggregated_results['card_support'])) if aggregated_results['card_support'] else 'None found'}")


# Entry point
if __name__ == "__main__":
    input_url = input("Enter the website URL: ")
    scan_site(input_url)
