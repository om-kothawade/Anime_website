from app import app
import os
if __name__ == '__main__':
    # Run on all IP addresses and default port (8000 for Versal)
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8000)), debug=False)
