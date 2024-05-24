from flask import Flask, request, jsonify
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

handler = RotatingFileHandler('events.log', maxBytes=10000, backupCount=3)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)

@app.route('/log', methods=['POST'])
def log_event():
    data = request.get_json()    
    if not data:
        return jsonify({"error": "Invalid input, JSON required"}), 400    
    
    if 'user' not in data or 'action' not in data or 'time' not in data:
        return jsonify({"error": "JSON must contain user, action, and time"}), 400    
    
    user = data['user']
    action = data['action']
    timestamp = data['time']    
    
    log_message = f"User: {user},\n Action: {action},\n Time: {timestamp}\n"
    app.logger.info(log_message)    
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True)