# 🎲 Dice Roller DevOps Project

## 🚀 Overview
This project is a simple web-based Dice Roller application inspired by Dungeons & Dragons mechanics.

It was built as part of a DevOps learning journey to understand how applications are deployed from local environments to virtual machines, and eventually to the cloud.

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

## 🚀 Next Steps
- Automate deployment with Ansible
- Deploy to AWS EC2
- Add voice input functionality
