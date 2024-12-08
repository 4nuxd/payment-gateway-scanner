# 🛡️ Payment Gateway Scanner 🚀  

A Python-based tool to scan websites for **payment gateways**, **CAPTCHA**, **Cloudflare protection**, **GraphQL**, **e-commerce platforms**, and **card support**. Ideal for researchers and enthusiasts exploring payment system integrations! 🌐  

---
## 📋 Example Output  

```plaintext
███╗   ██╗ ██████╗  ██████╗ ██████╗   A Payment Gateway  Scanner
████╗  ██║██╔═══██╗██╔═══██╗██╔══██╗  Version: v 2.0.0
██╔██╗ ██║██║   ██║██║   ██║██████╔╝  Author: Noob Pirate Aka Blionrie
██║╚██╗██║██║   ██║██║   ██║██╔══██╗  Note: Every Action Has a Consequence
██║ ╚████║╚██████╔╝╚██████╔╝██████╔╝  Join: https://t.me/piratexnetwork
╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═════╝   Bored..? : http://bit.ly/3MTMHyU
___________________________________________________________________________

Enter the website URL: https://example.com  
Scanning: 100%|█████████████████████████████████████████████████████████████████

Scan completed!  
URL: https://example.com  
Payment Gateways: Stripe, PayPal  
Captcha: True  
Cloudflare: False  
GraphQL: True  
Platforms: WooCommerce  
Card Support: Visa, MasterCard  
```  
---

## ⚙️ Features  

- 🏦 **Detect Payment Gateways**: Stripe, PayPal, Razorpay, and more!  
- 🔒 **CAPTCHA Detection**: Supports reCAPTCHA, hCAPTCHA, and others.  
- ☁️ **Cloudflare Protection Check**: Identifies Cloudflare-protected sites.  
- 📊 **GraphQL Support**: Scans for GraphQL integration.  
- 🛍️ **E-Commerce Platforms**: Detects WooCommerce, Shopify, Magento, etc.  
- 💳 **Card Support**: Finds supported card types (Visa, MasterCard, etc.).  
- 📑 **Multi-Page Scanning**: Extends scans to related pages .
- 🔎 **Progress Tracking**: Visualize progress with a dynamic progress bar.  

---

## 🛠️ Installation  

### **Dependencies**  
Ensure you have Python 3.7+ installed. Install the required libraries using:  
```bash
pip install -r requirements.txt
```  

### **Required Libraries**  
- `requests` 🌐  
- `bs4` (BeautifulSoup) 🍜  
- `re` (Built-in) 🧩  
- `tqdm` 📊  
- `colorama` 🌈  

---

## 🚀 How to Use  

1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/payment-gateway-scanner.git
   cd payment-gateway-scanner
   ```  

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

3. Run the script:  
   ```bash
   python scanner.py
   ```  

4. Enter the website URL when prompted:  
   ```plaintext
   Enter the website URL: https://example.com
   ```  

5. Wait for the scan to complete, and review the consolidated results!  

---

## 📚 Notes  

1. **Use Responsibly**: Ensure you have permission before scanning any website.  
2. **Legal Disclaimer**: The author is not responsible for any misuse of this tool.  

---

## 👩‍💻 Author  

**Noob Pirate Aka Blionrie**  
- 🏴‍☠️ [Telegram](https://t.me/noobpirate)  
- 🌟 Bored..? Check this out: [Click Here](http://bit.ly/3MTMHyU)  
