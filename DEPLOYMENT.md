# Ubuntu EC2 Deployment Guide (Flask + SQLite + Nginx + Gunicorn)

This guide provides step-by-step instructions to deploy this Flask & SQLite web application to an AWS EC2 Ubuntu instance.

---

## 1. AWS EC2 Setup

1. **Launch an EC2 Instance**:
   - OS: Ubuntu 22.04 LTS or 24.04 LTS.
   - Instance Type: `t2.micro` or `t3.micro` (Free tier eligible).
   - Key Pair: Download `.pem` file (e.g. `my-key.pem`).

2. **Configure Security Group Rules (Inbound Rules)**:
   - **SSH**: Port 22 (Your IP or Anywhere)
   - **HTTP**: Port 80 (Anywhere `0.0.0.0/0`)
   - **HTTPS**: Port 443 (Anywhere `0.0.0.0/0`)

3. **Connect via SSH**:
   ```bash
   ssh -i /path/to/my-key.pem ubuntu@<YOUR_EC2_PUBLIC_IP>
   ```

---

## 2. Server Preparation

Run the following commands on your Ubuntu server:

```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install Python3, pip, venv, Nginx, and Git
sudo apt install -y python3-pip python3-venv nginx git
```

---

## 3. Clone & Setup Project

```bash
# Navigate to home directory or web directory
cd /var/www

# Give permissions to current user (or clone into ~ and link)
sudo chown -R ubuntu:ubuntu /var/www

# Clone repository (or upload project files)
git clone <YOUR_GIT_REPOSITORY_URL> vaii
cd vaii

# Create virtual environment and activate it
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 4. SQLite Database & Uploads Permissions

SQLite needs write permissions on both `vaii.db` **and** the directory containing it (`/var/www/vaii`), as well as the upload directory (`static/uploads/users`):

```bash
# Ensure upload folder exists
mkdir -p static/uploads/users

# Change ownership to www-data (Nginx/Gunicorn user) or give write permissions
sudo chown -R www-data:www-data /var/www/vaii
sudo chmod -R 775 /var/www/vaii
```

---

## 5. Systemd Service Configuration (Gunicorn)

Create a systemd service file so Flask runs as a background service and starts automatically on boot:

```bash
sudo nano /etc/systemd/system/vaii.service
```

Paste the following configuration:

```ini
[Unit]
Description=Gunicorn instance to serve Vaii Flask Application
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/vaii
Environment="PATH=/var/www/vaii/venv/bin"
Environment="SECRET_KEY=vaii_secure_store_session_secret_key_2026"
ExecStart=/var/www/vaii/venv/bin/gunicorn --workers 3 --bind unix:vaii.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
```

Save and exit (`Ctrl + O`, `Enter`, `Ctrl + X`).

Start and enable the service:

```bash
sudo systemctl daemon-reload
sudo systemctl start vaii
sudo systemctl enable vaii

# Check status
sudo systemctl status vaii
```

---

## 6. Nginx Reverse Proxy Setup

Configure Nginx to pass incoming HTTP traffic on port 80 to the Gunicorn Unix socket (`vaii.sock`):

```bash
sudo nano /etc/nginx/sites-available/vaii
```

Paste the following configuration (replace `<YOUR_EC2_PUBLIC_IP_OR_DOMAIN>`):

```nginx
server {
    listen 80;
    server_name <YOUR_EC2_PUBLIC_IP_OR_DOMAIN>;

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/vaii/vaii.sock;
    }

    # Serve static assets directly for better performance
    location /static/ {
        alias /var/www/vaii/static/;
        expires 30d;
    }
}
```

Enable the configuration and restart Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/vaii /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

---

## 7. Optional: Enable SSL / HTTPS (Let's Encrypt)

If you have a domain name pointing to your EC2 IP:

```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

---

## Summary of Useful Commands

| Action | Command |
| --- | --- |
| Check Gunicorn Service Status | `sudo systemctl status vaii` |
| Restart Gunicorn App | `sudo systemctl restart vaii` |
| View Gunicorn App Logs | `sudo journalctl -u vaii -f` |
| Restart Nginx | `sudo systemctl restart nginx` |
| Test Nginx Configuration | `sudo nginx -t` |
