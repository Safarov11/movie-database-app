from flask import Flask, jsonify, request
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database configuration
DB_HOST = '********.ct6ei6agkus4.ap-south-1.rds.amazonaws.com'
DB_NAME = 'itemsdb'
DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_PORT = '5432'

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )

# Get all movies
@app.route('/movies', methods=['GET'])
def get_movies():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, year, distributor, domestic_sales, worldwide_sales, genre FROM tbl_diyor_movies")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{
        'id': row[0], 'title': row[1], 'year': row[2],
        'distributor': row[3], 'domestic_sales': row[4],
        'worldwide_sales': row[5], 'genre': row[6]
    } for row in rows])

# Add a new movie
@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO tbl_diyor_movies (id, title, year, distributor, domestic_sales, worldwide_sales, genre)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (data['id'], data['title'], data['year'], data['distributor'],
          data['domestic_sales'], data['worldwide_sales'], data['genre']))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Movie added successfully'})

# Delete movie by ID
@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tbl_diyor_movies WHERE id = %s", (movie_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Movie deleted successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
