# ===== URL TRACKER FOR COLAB NGROK LINKS =====
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import json
import os

app = Flask(__name__)
CORS(app)  # Allow all origins

# Store current backend info
current_backend = {
    "url": "",
    "last_updated": "",
    "status": "offline",
    "model": "Qwen2.5-VL-7B-Instruct",
    "uptime": 0
}

# Store last 5 URLs for backup
url_history = []

@app.route('/')
def home():
    return jsonify({
        "service": "Colab URL Tracker",
        "endpoints": {
            "GET /url": "Get current Colab URL",
            "POST /url": "Update Colab URL",
            "GET /status": "Check if Colab is online",
            "GET /history": "Get recent URLs"
        }
    })

@app.route('/url', methods=['GET'])
def get_url():
    """Frontend calls this to get Colab's current URL"""
    if current_backend["url"]:
        return jsonify({
            "success": True,
            "backend": current_backend
        })
    else:
        return jsonify({
            "success": False,
            "error": "No active backend found",
            "backend": current_backend
        })

@app.route('/url', methods=['POST'])
def set_url():
    """Colab calls this when it starts"""
    try:
        data = request.get_json()
        
        if not data or 'url' not in data:
            return jsonify({"success": False, "error": "No URL provided"}), 400
        
        new_url = data['url'].strip().rstrip('/')
        
        # Validate URL
        if not new_url.startswith(('http://', 'https://')):
            return jsonify({"success": False, "error": "Invalid URL format"}), 400
        
        # Add to history
        if current_backend["url"] and current_backend["url"] != new_url:
            url_history.append({
                "url": current_backend["url"],
                "last_used": current_backend["last_updated"]
            })
            # Keep only last 5
            if len(url_history) > 5:
                url_history.pop(0)
        
        # Update current
        current_backend["url"] = new_url
        current_backend["last_updated"] = datetime.now().isoformat()
        current_backend["status"] = "online"
        
        print(f"✅ [{datetime.now().strftime('%H:%M:%S')}] URL Updated: {new_url}")
        
        return jsonify({
            "success": True,
            "message": "URL registered successfully",
            "backend": current_backend
        })
        
    except Exception as e:
        print(f"❌ Error in set_url: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/status', methods=['GET'])
def status():
    """Check if Colab is currently online"""
    return jsonify({
        "success": True,
        "online": current_backend["status"] == "online",
        "last_updated": current_backend["last_updated"],
        "model": current_backend["model"]
    })

@app.route('/history', methods=['GET'])
def get_history():
    """Get recent URLs (for backup)"""
    return jsonify({
        "success": True,
        "current": current_backend,
        "history": url_history
    })

@app.route('/health', methods=['GET'])
def health():
    """Health check for the tracker itself"""
    return jsonify({
        "status": "healthy",
        "service": "Colab URL Tracker",
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"🚀 URL Tracker starting on port {port}...")
    app.run(host='0.0.0.0', port=port)
