from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USUARIO = "coservicios7@gmail.com"
PASSWORD = "Pedriño132*"

FACEBOOK_URL = "https://www.facebook.com"
FACEBOOK_MARKETPLACE_VENTA_URL = "https://www.facebook.com/marketplace/you/selling?locale=es_LA"


# Configuración de las opciones de Chrome
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# Inicia el WebDriver de Chrome
driver = webdriver.Chrome(options=options)

# Abre Facebook y haz login (como en tu código original)
driver.get(FACEBOOK_URL)
time.sleep(3)
driver.find_element(By.ID, "email").send_keys(USUARIO)
driver.find_element(By.ID, "pass").send_keys(PASSWORD)
driver.find_element(By.ID, "pass").send_keys(Keys.RETURN)
time.sleep(3) #ACa te espera para que puedas iniciar sesion tranquilamente
old_url = driver.current_url
WebDriverWait(driver, 30).until(EC.url_changes(old_url))
print("La pantalla cambió, continuando ejecución...")
time.sleep(2)
# Abre Marketplace
driver.get(FACEBOOK_MARKETPLACE_VENTA_URL)
time.sleep(5)

# # Busca el botón 'Publicar en más lugares' por su clase
        # publish_button = self.driver.find_element(By.XPATH, "//span[contains(@class, 'x193iq5w') and text()='Publicar en más lugares']")
        
        # # Hace clic en el botón
        # publish_button.click()
# Realiza alguna acción en la nueva pestaña (por ejemplo, clic en un botón)
clasesMenuDesplegable = ["x1ja2u2z", "x78zum5", "x2lah0s", "x1n2onr6", "xl56j7k",
    "x6s0dn4", "xozqiw3", "x1q0g3np", "xi112ho", "x17zwfj4",
    "x585lrc", "x1403ito", "x972fbf", "xcfux6l", "x1qhh985",
    "xm0m39n", "x9f619", "x1qhmfi1", "x1r1pt67", "x1jdnuiz", "x1x99re3"]



# Define las clases en una lista
clasesPublicarEnMasLugares = [
    "x1i10hfl", "xjbqb8w", "x1ejq31n", "xd10rxx", "x1sy0etr", "x17r0tee", "x972fbf",
    "xcfux6l", "x1qhh985", "xm0m39n", "xe8uvvx", "x1hl2dhg", "xggy1nq", "x1o1ewxj",
    "x3x9cwd", "x1e5q0jg", "x13rtm0m", "x87ps6o", "x1lku1pv", "x1a2a7pz", "xjyslct",
    "x9f619", "x1ypdohk", "x78zum5", "x1q0g3np", "x2lah0s", "x1i6fsjq", "xfvfia3",
    "xnqzcj9", "x1gh759c", "x1n2onr6", "x16tdsg8", "x1ja2u2z", "x6s0dn4", "x1y1aw1k",
    "xwib8y2", "x1q8cg2c", "xnjli0"
]

clasesPublicar = [
    "x9f619", "x1n2onr6", "x1ja2u2z", "x78zum5", "xdt5ytf",
    "x193iq5w", "xeuugli", "x1iyjqo2", "xs83m0k", "x150jy0e",
    "x1e558r4", "xjkvuk6", "x1iorvi4", "xdl72j9"
]


# Crea la expresión XPath con las clases
pathPublicarEnMasLugares = "//div[" + " and ".join([f"contains(@class, '{clase}')" for clase in clasesPublicarEnMasLugares]) + "]"
pathMenuDesplegable = "//div[" + " and ".join([f"contains(@class, '{clase}')" for clase in clasesMenuDesplegable]) + "]"
pathPublicar = "//div[" + " and ".join([f"contains(@class, '{clase}')" for clase in clasesPublicar]) + "]"

botonesMenuDesplegable = driver.find_elements(By.XPATH, pathMenuDesplegable)
i = 0
while i < len(botonesMenuDesplegable):
    time.sleep(5)
    # print("indice i al comenzar el ciclo: ",i)
    # print("largo del botonesMenuDesplegable", len(botonesMenuDesplegable))
    print("Falta ", i+1, "/", len(botonesMenuDesplegable), "para que finalize el script")
    if i < len(botonesMenuDesplegable):
        botonesMenuDesplegable[i].click()
        
    time.sleep(5)
    botonesPublicarEnMasLugares = driver.find_elements(By.XPATH, pathPublicarEnMasLugares)  # Encuentra todos los elementos que coincidan con el XPath
    botonesPublicarEnMasLugares[1].click()  # El indice 1 pertenece al boton "publicar en mas lugares"
    time.sleep(5)
    

    botonesSeleccionGrupos = driver.find_elements(By.XPATH, "//div[contains(@class, 'x9f619') and contains(@class, 'x1n2onr6') and contains(@class, 'x1ja2u2z') and contains(@class, 'x78zum5') and contains(@class, 'xdt5ytf') and contains(@class, 'x2lah0s') and contains(@class, 'x193iq5w') and contains(@class, 'xeuugli') and contains(@class, 'xsyo7zv') and contains(@class, 'x16hj40l') and contains(@class, 'x10b6aqq') and contains(@class, 'x1yrsyyn')]/i")
    if len(botonesSeleccionGrupos) >= 10:
        botonesSeleccionGrupos[0].click()
        botonesSeleccionGrupos[1].click()
        botonesSeleccionGrupos[2].click()
        botonesSeleccionGrupos[3].click()
        botonesSeleccionGrupos[4].click()
        botonesSeleccionGrupos[5].click()
        botonesSeleccionGrupos[6].click()
        botonesSeleccionGrupos[7].click()
        botonesSeleccionGrupos[8].click()
        botonesSeleccionGrupos[9].click()
    elif len(botonesSeleccionGrupos) >= 5:
        botonesSeleccionGrupos[0].click()
        botonesSeleccionGrupos[1].click()
        botonesSeleccionGrupos[2].click()
        botonesSeleccionGrupos[3].click()
        botonesSeleccionGrupos[4].click()
    elif len(botonesSeleccionGrupos) >= 3:
        botonesSeleccionGrupos[0].click()
        botonesSeleccionGrupos[1].click()
        botonesSeleccionGrupos[2].click()
    elif len(botonesSeleccionGrupos) >= 1:
        botonesSeleccionGrupos[0].click()
        
    # for boton in botonesSeleccionGrupos:
    #   print(boton.get_attribute("outerHTML"))  # Verifica el contenido de cada elemento
    
    # time.sleep(3)
    
    # botonesPublicar = driver.find_elements(By.XPATH, pathPublicar)
    # for boton in botonesPublicar:
    #     print(boton.text)
    # botonesPublicar[2].click() # el indice 2 pertenece al boton Publicar
    print("indice i antes del ++ :",i) 
    i += 1
    print("indice i despues del ++ :",i) 
    time.sleep(10)


print("Si llegaste hasta aca es porque finalizo el script y se ejecuto correctamente todas las acciones")
time.sleep(10)