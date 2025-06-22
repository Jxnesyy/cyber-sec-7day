cat > day2-self-phish/README.md << 'EOF'
# Day 2: Self-Phishing Lab

### 🎯 Objective
Stand up a local phishing page, send yourself a link via local mail, and capture credentials in **creds.log**.

### 🛠️ Usage
1. **Launch the server**  
   ```bash
   cd day2-self-phish
   ./phish_start.sh
Send the phishing email locally

bash
Copy
Edit
echo -e "Subject: Security Update\n\nPlease login here:\nhttp://82.15.67.125:8080/" \
  | mail -s "Security Update" jxnesyy
Inspect mailbox & captured creds

bash
Copy
Edit
cat mailbox.txt
cat creds.log
📸 Proof
Terminal showing mailbox.txt & creds.log


Phishing page in browser


🚀 Next Steps
Configure a real SMTP relay (e.g., Gmail smarthost) via Exim4

Obfuscate the URL using a shortener to mimic real attacks

Serve over HTTPS with a self-signed certificate
EOF# Day 2: Self-Phishing Lab

### 🎯 Objective
Stand up a local phishing page, send yourself a link via local mail, and capture credentials in creds.log.

### 🛠️ Usage
1. Launch the server:  
   ```bash
   ./phish_start.sh
Send the email:

bash '''
echo -e "Subject: Security Update\n\nPlease login here:\nhttp://82.15.67.125:8080/" \
  | mail -s "Security Update" jxnesyy
Inspect mailbox & creds:


cat mailbox.txt
cat creds.log
📸 Proof



🚀 Next Steps
Configure a real SMTP relay

Obfuscate the URL

Add HTTPS with a self-signed cert
