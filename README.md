🎬 AWS Movie Timetable Web Application
This project demonstrates how to deploy a simple movie management web app (add/delete/view) using AWS resources including EC2, S3, and RDS (PostgreSQL). It showcases both backend and frontend deployment.

✅ Project Overview
Frontend: Static webpage (HTML/CSS) hosted on AWS S3.

Backend: Python Flask API running on AWS EC2 (public IP: http://54.255.135.111).

Database: PostgreSQL hosted on AWS RDS.

📦 Folder Structure
pgsql
Copy
Edit
movie-app/
├── backend/
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   └── index.html

🚀 Deployment Steps
Step 1: Set up EC2 Instance
Configure the security group:

Allow ports: 22, 80, 443, 8000, 5432, and all traffic between EC2 ↔ RDS.

SSH into EC2:

<pre> ```ssh -i "C:\your_key_2_ec2.pem" ubuntu@<EC2_Public_IP> ``` </pre>

Step 2: Install Dependencies on EC2


<pre> ```sudo apt update 
sudo apt install python3 python3-pip postgresql-client -y
pip3 install flask psycopg2-binary``` </pre>

Step 3: Connect to PostgreSQL RDS

<pre> ```psql -h <RDS_End_Point> -U postgres -d itemsdb ``` </pre>

Example: psql -h eldor-2t.ct6ei6agkus4.ap-south-1.rds.amazonaws.com -U postgres -d itemsdb

Step 4: Create and Populate Table

<pre> ``` CREATE TABLE tbl_movies (
  id INT PRIMARY KEY,
  title TEXT,
  year INT,
  distributor TEXT,
  domestic_sales BIGINT,
  worldwide_sales BIGINT,
  genre TEXT
); ``` </pre>

-- Sample Insert
<pre> ```INSERT INTO tbl_movies VALUES
(0, 'Avatar', 2009, 'Twentieth Century Fox', 785221649, 2923706026, 'Action, Adventure, Fantasy, Sci-Fi');
Step 5: Upload HTML to S3 ``` </pre>
Go to your S3 bucket

Enable static website hosting

Upload index.html

Set public read permissions

Step 6: Run Flask App on EC2

<pre> ``` python3 app.py ``` </pre>

App should be accessible at: http://54.255.135.111


9. Frontend (S3 Hosting)
Upload your index.html (with Add and Delete buttons) to an S3 bucket.

Make it public or enable static website hosting.

🌐 Deployed Resources
Frontend (S3 URL): <pre> ```http://<your-s3-bucket>.s3-website-<region>.amazonaws.com``` </pre>

Backend (EC2 Public IP): <pre> ```http://<EC2_Public_IP>/movies``` </pre>

Database (RDS): itemsdb on <pre> ```diyor-3t.ct6ei6agkus4.ap-south-1.rds.amazonaws.com``` </pre>
