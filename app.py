"""
app.py
Flask application template for the warm-up assignment


Students need to implement the API endpoints as specified in the assignment.
"""


from flask import Flask, request, jsonify, render_template
from starter_preprocess import TextPreprocessor
import traceback
import requests


app = Flask(__name__)
preprocessor = TextPreprocessor()


@app.route('/')
def home():
    """Render a simple HTML form for URL input"""
    return render_template('index.html')


@app.route('/health')
def health_check():
    """Simple health check endpoint"""
    return jsonify({
        "status": "healthy",
        "message": "Text preprocessing service is running"
    })


@app.route('/api/clean', methods=['POST'])
def clean_text():
    """
    TODO: Implement this endpoint for Part 3

    API endpoint that accepts a URL and returns cleaned text

    Expected JSON input:
        {"url": "https://www.gutenberg.org/files/1342/1342-0.txt"}

    Returns JSON:
        {
            "success": true/false,
            "cleaned_text": "...",
            "statistics": {...},
            "summary": "...",
            "error": "..." (if applicable)
        }
    """
    try:
        # TODO: Get JSON data from request
        data = request.get_json()

        # TODO: Extract URL from the JSON
        url = data.get('url')

        # TODO: Validate URL (should be .txt)
        if not url or not url.endswith('.txt'):
            return jsonify({
                "success": False,
                "cleaned_text": "",
                "statistics": {},
                "summary": "",
                "error": "Please provide a Project URL ending in .txt"
            }), 400

        # TODO: Use preprocessor.fetch_from_url()
        response = requests.get(url)
        response.raise_for_status()
        raw_text = response.text

        # TODO: Clean the text with preprocessor.clean_gutenberg_text()
        cleaned = preprocessor.clean_gutenberg_text(raw_text)

        # TODO: Normalize with preprocessor.normalize_text()
        normalized = preprocessor.normalize_text(cleaned)

        # TODO: Get statistics with preprocessor.get_text_statistics()
        stats = preprocessor.get_text_statistics(normalized)

        # TODO: Create summary with preprocessor.create_summary()
        summary = preprocessor.create_summary(normalized, num_sentences=3)

        # TODO: Return JSON response
        return jsonify({
            "success": True,
            "cleaned_text": normalized,
            "statistics": stats,
            "summary": summary
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Server error: {str(e)}"
        }), 500


@app.route('/api/analyze', methods=['POST'])
def analyze_text():
    """
    TODO: Implement this endpoint for Part 3

    API endpoint that accepts raw text and returns statistics only

    Expected JSON input:
        {"text": "Your raw text here..."}

    Returns JSON:
        {
            "success": true/false,
            "statistics": {...},
            "error": "..." (if applicable)
        }
    """
    try:
        # TODO: Get JSON data from request
        data = request.get_json()

        # TODO: Extract text from the JSON
        text = data.get('text')

        # Error handling
        if not text:
            return jsonify({
                "success": False,
                "statistics": {},
                "error": "No text provided"
            }), 400

        # TODO: Get statistics with preprocessor.get_text_statistics()
        statistics = preprocessor.get_text_statistics(text)

        # TODO: Return JSON response
        return jsonify({
            "success": True,
            "statistics": statistics
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Server error: {str(e)}"
        }), 500


# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": "Endpoint not found"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "success": False,
        "error": "Internal server error"
    }), 500


if __name__ == '__main__':
    print("🚀 Starting Text Preprocessing Web Service...")
    print("📖 Available endpoints:")
    print("   GET  /           - Web interface")
    print("   GET  /health     - Health check")
    print("   POST /api/clean  - Clean text from URL")
    print("   POST /api/analyze - Analyze raw text")
    print()
    print("🌐 Open your browser to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server")

    app.run(debug=True, port=5000, host='0.0.0.0')
