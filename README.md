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
├── database/
│   ├── schema.sql
│   └── data_import.sql
├── README.md
🚀 Deployment Steps
Step 1: Set up EC2 Instance
Configure the security group:

Allow ports: 22, 80, 443, 8000, 5432, and all traffic between EC2 ↔ RDS.

SSH into EC2:

bash
Copy
Edit
ssh -i "C:\your_key_2_ec2.pem" ubuntu@<EC2_Public_IP>
Step 2: Install Dependencies on EC2
bash
Copy
Edit
sudo apt update
sudo apt install python3 python3-pip postgresql-client -y
pip3 install flask psycopg2-binary
Step 3: Connect to PostgreSQL RDS
bash
Copy
Edit
psql -h <RDS_End_Point> -U postgres -d itemsdb
Example: psql -h eldor-2t.ct6ei6agkus4.ap-south-1.rds.amazonaws.com -U postgres -d itemsdb

Step 4: Create and Populate Table
sql
Copy
Edit
CREATE TABLE tbl_movies (
  id INT PRIMARY KEY,
  title TEXT,
  year INT,
  distributor TEXT,
  domestic_sales BIGINT,
  worldwide_sales BIGINT,
  genre TEXT
);

-- Sample Insert
INSERT INTO tbl_movies VALUES
(0, 'Avatar', 2009, 'Twentieth Century Fox', 785221649, 2923706026, 'Action, Adventure, Fantasy, Sci-Fi');
Step 5: Upload HTML to S3
Go to your S3 bucket

Enable static website hosting

Upload index.html

Set public read permissions

Step 6: Run Flask App on EC2
bash
Copy
Edit
python3 app.py
App should be accessible at: http://54.255.135.111
