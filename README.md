# 🎲 Dice Roller DevOps Project

## 🚀 Overview

This project is a simple web-based Dice Roller application built with Flask and deployed on a virtual machine using Terraform and libvirt.

It demonstrates a full DevOps workflow from local development to infrastructure deployment and remote access.

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
- How to convert a CLI script into a web application
- How to deploy applications onto a VM
- Networking between host and VM (SSH tunneling)
- Debugging infrastructure issues (disk space, networking, ports)

---

## 🏗️ Architecture

Local Machine (WSL)

   ↓ SSH Tunnel
   
Virtual Machine (libvirt)

   ↓
   
Flask Web Application

   ↓
   
Browser Access (localhost:8080)

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
- Deploy application to AWS EC2  
- Replace SSH tunneling with public access  
- Add voice input functionality  

---

## 🚀 Next Steps
- Automate deployment with Ansible
- Deploy to AWS EC2
- Add voice input functionality
