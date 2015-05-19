from web import app
from config.settings import get_easy_settings

#app.config.from_object(get_easy_settings())

server_settings = get_easy_settings()

app.run(debug=server_settings.DEBUG, port=server_settings.PORT)
