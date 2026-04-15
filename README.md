# 🎲 Dice Roller DevOps Project

> A voice-enabled web application deployed on AWS, showcasing a full DevOps workflow from local development to cloud infrastructure.

---

## 🌍 Live Demo

👉 http://52.56.134.55

🎤 **Voice Feature**
- Click the **Speak** button  
- Say: `"roll persuasion"`  
- Get an instant dice result  

> ⚠️ Best experienced in Google Chrome (for voice support)

---

## 📸 Demo

![App Screenshot](images/screenshot1.png)
![App Screenshot](images/screenshot2.png)

---

## 🚀 Overview

This project is a web-based Dice Roller inspired by Dungeons & Dragons mechanics.

It demonstrates an end-to-end DevOps workflow:
- Local development  
- Virtual machine deployment  
- Cloud migration to AWS  
- Reverse proxy configuration  
- Voice-enabled frontend interaction  

---

## 🧩 Tech Stack

- Python  
- Flask  
- Terraform  
- libvirt (local virtualization)  
- AWS EC2  
- Nginx (reverse proxy)  
- JavaScript (Web Speech API)  

---

## ⚙️ Features

- 🎲 Dice rolling system with modifiers  
- 🌐 Web-based interface (Flask)  
- ☁️ Deployed on AWS EC2  
- 🔁 Reverse proxy using Nginx  
- 🎤 Voice command support (browser-based)  

---

## 🏗️ Architecture

### 🖥️ Local Setup
WSL (Ubuntu)  
↓  
libvirt VM  
↓  
Flask App  
↓  
SSH Tunnel → Browser  

---

### ☁️ Cloud Setup (AWS)
Terraform  
↓  
AWS EC2 Instance  
↓  
Nginx (Port 80)  
↓  
Flask App (Port 5000)  
↓  
Public Internet 🌍  

---

## 🔧 How to Run

### 🖥️ Run Locally

```bash
git clone https://github.com/a-yusuf-f/dice-roller-devops-project.git
cd dice-roller-devops-project

python3 -m venv venv
source venv/bin/activate

pip install flask
python app.py
```

Open in browser:

```
http://localhost:5000
```

---

### ☁️ Run on AWS (Production Setup)

#### 1. Provision Infrastructure

```bash
terraform init
terraform apply
```

---

#### 2. Connect to EC2

```bash
ssh -i ~/dice-key.pem ubuntu@<your-public-ip>
```

---

#### 3. Install Dependencies

```bash
sudo apt update
sudo apt install -y python3-pip python3-venv git nginx
```

---

#### 4. Clone the Repository

```bash
git clone https://github.com/a-yusuf-f/dice-roller-devops-project.git
cd dice-roller-devops-project
```

---

#### 5. Set Up Python Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
```

---

#### 6. Run the Application

```bash
python app.py
```

---

#### 7. Configure Nginx (Reverse Proxy)

```bash
sudo nano /etc/nginx/sites-available/default
```

Replace:

```nginx
location / {
    try_files $uri $uri/ =404;
}
```

With:

```nginx
location / {
    proxy_pass http://127.0.0.1:5000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

Restart Nginx:

```bash
sudo systemctl restart nginx
```

---

#### 8. Access the Application

```
http://<your-public-ip>
```

---

> 💡 Nginx listens on port 80 and forwards traffic to Flask running on port 5000.

---

## 🧠 What I Learned

- Deploying applications to AWS EC2  
- Managing SSH access and key pairs securely  
- Understanding public vs private networking  
- Configuring security groups and ports  
- Using Nginx as a reverse proxy  
- Debugging real-world infrastructure issues  
- Transitioning from local environments to cloud systems  

---

## 🔮 Future Improvements

- 🔒 Add HTTPS (SSL with Let’s Encrypt)  
- ⚙️ Automate deployment using Ansible  
- 🌐 Add a custom domain name  
- 🎙️ Integrate AWS voice services (Transcribe/Polly)  

---

## 💼 Author

**Yusuf A.**  
Aspiring DevOps / Cloud Engineer  

---

## ⭐ If you found this useful

Feel free to star the repo or connect with me!
