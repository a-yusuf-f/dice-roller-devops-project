# 🎲 Dice Roller DevOps Project

## 🚀 Overview

This project is a simple web-based Dice Roller application built with Flask and deployed on a virtual machine using Terraform and libvirt.

It demonstrates a full DevOps workflow from local development to infrastructure deployment and remote access.

---

## 🌍 Live Deployment

This application is deployed on AWS EC2 and is publicly accessible.

Example:
http://52.56.134.55:5000

---

## 🧩 Tech Stack
- Python
- Flask
- Terraform (VM provisioning)
- libvirt (local virtualization)
- SSH (port forwarding)

---

## ⚙️ Features
- Roll dice using commands (e.g. "roll persuasion")
- Applies skill modifiers
- Web-based interface using Flask
- Runs on a virtual machine

---

## 🧠 What I Learned

- How to deploy applications to AWS EC2  
- Difference between private and public networking  
- Managing SSH keys and secure access  
- Configuring security groups to allow traffic  
- Debugging real-world infrastructure issues  
- Transitioning from local development to cloud deployment  

---

## 🏗️ Architecture

### Local Setup
WSL (Ubuntu)
   ↓
libvirt VM
   ↓
Flask App
   ↓
SSH Tunnel → Browser

### Cloud Setup (AWS)
Terraform
   ↓
AWS EC2 Instance
   ↓
Flask App
   ↓
Public IP → Browser 🌍

---

## 🔧 How to Run

### 1. Clone the repo
git clone https://github.com/a-yusuf-f/dice-roller-devops-project.git

cd dice-roller-devops-project


### 2. Install dependencies
pip install flask


### 3. Run the app
python app.py


### 4. Open in browser
http://localhost:5000

---

## 🔮 Future Improvements

- Automate deployment using Ansible  
- Use Nginx and port 80 for production setup  
- Add domain name and HTTPS  
- Implement voice input using AWS services  

---
