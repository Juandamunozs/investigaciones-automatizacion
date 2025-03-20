import os

# Ruta del directorio actual - directorio donde se encuentra el archivo 'env.py'
dir_proyect = os.path.dirname(os.path.abspath(__file__))

# Ruta de los directorios principales
dir_assets = os.path.join(dir_proyect, '..', 'assets')
dir_module = os.path.join(dir_proyect, '..', 'module')
dir_res = os.path.join(dir_proyect, '..', 'res')
dir_service = os.path.join(dir_proyect, '..', 'service')
dir_db = os.path.join(dir_proyect, '..', 'db')

# Ruta de los subdirectorios
dir_imagen_catpcha = r"C:\Users\juand\Downloads\captcha_image.png" 
dir_logo = os.path.join(dir_assets, 'image', 'logo.jpg')
dir_screnshots = os.path.join(dir_res, 'screenshots')
dir_pdf = os.path.join(dir_module, 'email', 'files')
dir_db_json = os.path.join(dir_db, 'db.json')
dir_token = os.path.join(dir_module, 'token')

# Ruta de ejecutables como ChromeDriver
dir_chromedriver = r"C:\\selenium\\chromedriver.exe"

# Lista de las rutas de carpetas para verificar y crear si no existen
directories_to_create = [
    dir_res,
    dir_screnshots,
    dir_assets,
    os.path.join(dir_assets, 'image'),  
    dir_pdf,
    dir_db,
    dir_token,
]

# Verificar si las carpetas existen; si no, crearlas
for directory in directories_to_create:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Configuración del token
SECRET_KEY = "9955ea8e1c6ce8cb33cc9e1dddba65c729078dd4ff9ff04936ee6af14bfc1cbb"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

email = "lifesnapco@gmail.com"
email_password = "bhcf jhfk jvkw ibro"  