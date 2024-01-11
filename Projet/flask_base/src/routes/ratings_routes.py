from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
import requests
from src.models.songs import Song
import src.routes.songs as song_routes

ratings_app = Blueprint('ratings_app', __name__)

BASE_URL = 'https://ratings-foxtrot.edu.forestier.re'

# Routes for operations on ratings

@ratings_app.route('/songs/<song_id>/ratings', methods=['GET'])
def get_song_ratings(song_id):
    """
    ---
    get:
      description: Get ratings for a specific song
      parameters:
        - in: path
          name: song_id
          required: true
          type: string
          description: ID of the song to get ratings for
      responses:
        '200':
          description: Successful response with song ratings
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
            application/yaml:
              schema:
                type: array
                items:
                  type: object
        '404':
          description: Song not found
          content:
            application/json:
              schema: 
                type: object
                properties:
                  error:
                    type: string
            application/yaml:
              schema:
                type: object
                properties:
                  error:
                    type: string
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema: 
                type: object
                properties:
                  error:
                    type: string
            application/yaml:
              schema:
                type: object
                properties:
                  error:
                    type: string
    """
    ratings_url = f'{BASE_URL}/songs/{song_id}/ratings'

    song = song_routes.get_song(song_id)  
    if song is None:
        return jsonify({'error': 'Song not found'}), 404
    try:
        response = requests.get(ratings_url)
        if response.status_code == 200:
            ratings_data = response.json()
            return jsonify(ratings_data)
        else:
            return jsonify({'error': 'Failed to fetch ratings'}), response.status_code

    except requests.RequestException as e:
        return jsonify({'error': f'Request Exception: {str(e)}'}), 500

@ratings_app.route('/songs/<song_id>/ratings', methods=['POST'])
@login_required
def add_song_rating(song_id):
    """
    ---
    post:
      description: Add a rating for a specific song
      parameters:
        - in: path
          name: song_id
          required: true
          type: string
          description: ID of the song to add a rating for
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                user_id:
                  type: integer
                  description: ID of the user adding the rating
                rating_value:
                  type: number
                  description: Value of the rating
      responses:
        '201':
          description: Successful response with the newly added rating
          content:
            application/json:
              schema: 
                type: object
            application/yaml:
              schema: 
                type: object
        '401':
          description: Unauthorized
          content:
            application/json:
              schema: 
                type: object
                properties:
                  error:
                    type: string
            application/yaml:
              schema: 
                type: object
                properties:
                  error:
                    type: string
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema: 
                type: object
                properties:
                  error:
                    type: string
            application/yaml:
              schema: 
                type: object
                properties:
                  error:
                    type: string
    """
    ratings_url = f'{BASE_URL}/songs/{song_id}/ratings'

    try:
        data = request.json
        
        response = requests.post(ratings_url, json=data)
        if response.status_code == 201:  # 201 for Created
            new_rating = response.json()
            return jsonify(new_rating), 201
        else:
            return jsonify({'error': 'Failed to add rating'}), response.status_code

    except requests.RequestException as e:
        return jsonify({'error': f'Request Exception: {str(e)}'}), 500

@ratings_app.route('/songs/<song_id>/ratings/<rating_id>', methods=['GET'])
def get_specific_rating(song_id, rating_id):
    """
    ---
    get:
      description: Get a specific rating for a song
      parameters:
        - in: path
          name: song_id
          required: true
          type: string
          description: ID of the song
        - in: path
          name: rating_id
          required: true
          type: string
          description: ID of the rating to retrieve
      responses:
        '200':
          description: Successful response with the specific rating
          content:
            application/json:
              schema: 
                type: object
            application/yaml:
              schema: 
                type: object
        '404':
          description: Rating not found
          content:
            application/json:
              schema: 
                type: object
                properties:
                  error:
                    type: string
            application/yaml:
              schema: 
                type: object
                properties:
                  error:
                    type: string
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema: 
                type: object
                properties:
                  error:
                    type: string
            application/yaml:
              schema: 
                type: object
                properties:
                  error:
                    type: string
    """
    rating_url = f'{BASE_URL}/songs/{song_id}/ratings/{rating_id}'

    try:
        response = requests.get(rating_url)
        if response.status_code == 200:
            rating_data = response.json()
            return jsonify(rating_data)
        else:
            return jsonify({'error': 'Failed to fetch rating'}), response.status_code

    except requests.RequestException as e:
        return jsonify({'error': f'Request Exception: {str(e)}'}), 500

@ratings_app.route('/songs/<song_id>/ratings/<rating_id>', methods=['PUT'])
@login_required
def update_rating(song_id, rating_id):
    """
    ---
    put:
      description: Update a specific rating for a song
      parameters:
        - in: path
          name: song_id
          required: true
          type: string
          description: ID of the song
        - in: path
          name: rating_id
          required: true
          type: string
          description: ID of the rating to update
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                user_id:
                  type: integer
                  description: ID of the user updating the rating
                rating_value:
                  type: number
                  description: New value for the rating
      responses:
        '200':
          description: Successful response with the updated rating
          content:
            application/json:
              schema: 
                type: object
            application/yaml:
              schema: 
                type: object
        '401':
          description: Unauthorized
          content:
            application/json:
              schema: 
                type: object
                properties:
                  error:
                    type: string
            application/yaml:
              schema: 
                type: object
                properties:
                  error:
                    type: string
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema: 
                type: object
                properties:
                  error:
                    type: string
            application/yaml:
              schema: 
                type: object
                properties:
                  error:
                    type: string
    """
    rating_url = f'{BASE_URL}/songs/{song_id}/ratings/{rating_id}'
    
    try:          
        data = request.json
        if not(current_user) or current_user.id != data["user_id"]:
            print(current_user) 
            print(data["user_id"])
            return jsonify({'error': 'not authorized'}), 401

        response = requests.put(rating_url, json=data)
        if response.status_code == 200:
            updated_rating = response.json()
            return jsonify(updated_rating)
        else:
            return jsonify({'error': 'Failed to update rating'}), response.status_code

    except requests.RequestException as e:
        return jsonify({'error': f'Request Exception: {str(e)}'}), 500

@ratings_app.route('/songs/<song_id>/ratings/<rating_id>', methods=['DELETE'])
@login_required
def delete_rating(song_id, rating_id):
    """
    ---
    delete:
      description: Delete a specific rating for a song
      parameters:
        - in: path
          name: song_id
          required: true
          type: string
          description: ID of the song
        - in: path
          name: rating_id
          required: true
          type: string
          description: ID of the rating to delete
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                user_id:
                  type: integer
                  description: ID of the user deleting the rating
      responses:
        '204':
          description: Successful response for deleted rating
        '401':
          description: Unauthorized
          content:
            application/json:
              schema: 
                type: object
                properties:
                  error:
                    type: string
            application/yaml:
              schema: 
                type: object
                properties:
                  error:
                    type: string
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema: 
                type: object
                properties:
                  error:
                    type: string
            application/yaml:
              schema: 
                type: object
                properties:
                  error:
                    type: string
    """
    rating_url = f'{BASE_URL}/songs/{song_id}/ratings/{rating_id}'

    try:
        data = request.json
        print(current_user) 
        print(data["user_id"])
        if current_user.id != data["user_id"]:
            print(current_user) 
            print(data["user_id"])
            return jsonify({'error': 'not authorized'}), 401
        response = requests.delete(rating_url)
        if response.status_code == 204:  # 204 for No Content
            return '', 204
        else:
            return jsonify({'error': 'Failed to delete rating'}), response.status_code

    except requests.RequestException as e:
        return jsonify({'error': f'Request Exception: {str(e)}'}), 500
