# route.py
import os
from flask import Flask

def create_app():
    app = Flask(name)

    @app.route("/")
    def home():
        return """
        <html>
        <head>
            <title>Dhairya Bots</title>
            <style>
                body {
                    margin: 0;
                    height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    background: linear-gradient(270deg, #0f0c29, #302b63, #24243e);
                    background-size: 600% 600%;
                    animation: gradientShift 12s ease infinite;
                    font-family: Arial, sans-serif;
                }
                @keyframes gradientShift {
                    0% { background-position: 0% 50%; }
                    50% { background-position: 100% 50%; }
                    100% { background-position: 0% 50%; }
                }
                .glow {
                    font-size: 2.5em;
                    color: #fff;
                    text-align: center;
                    text-transform: uppercase;
                    letter-spacing: 5px;
                    animation: neonGlow 2s ease-in-out infinite alternate,
                               moveText 6s linear infinite;
                }
                @keyframes neonGlow {
                    from { text-shadow: 0 0 10px #ff00de, 0 0 20px #ff00de, 0 0 30px #ff00de; }
                    to { text-shadow: 0 0 20px #00fff7, 0 0 30px #00fff7, 0 0 40px #00fff7; }
                }
                @keyframes moveText {
                    0%   { transform: translateX(-50vw); }
                    50%  { transform: translateX(50vw); }
                    100% { transform: translateX(-50vw); }
                }
            </style>
        </head>
        <body>
            <div class="glow"> Powered by Dhairya</div>
        </body>
        </html>
        """

    @app.route("/status")
    def status():
        return {"status": "ok", "powered_by": "Dhairya"}

    return app


def run_flask():
    port = int(os.environ.get("PORT", 8000))
    app = create_app()
    app.run(host="0.0.0.0", port=port)
