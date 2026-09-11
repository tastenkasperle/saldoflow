from src.web import create_app

app = create_app()

if __name__ == '__main__':
    # Flask_Server starten - Debug modus
    app.run(debug=True, port=5000)
    