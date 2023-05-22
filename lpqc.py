from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


livre = input("Entrer le livre voulu: ")

# Chemin vers le pilote Chrome WebDriver
chromedriver_path = "chromedriver_win32\\chromedriver.exe"

# Configuration des options du navigateur
options = Options()
options.add_argument("--headless")  # Exécution sans interface graphique

# Création de l'instance du navigateur
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

# Charger la page Web
driver.get("https://www.laparolequichange.org/")


search_input = driver.find_element(By.CSS_SELECTOR, 'input[type="search"]')

search_input.send_keys(livre)



# Trouver le <tbody> contenant les éléments souhaités
tbody_elements = driver.find_elements(By.XPATH, "//tbody")

# Iterate over the tbody elements
for tbody_element in tbody_elements:
    # Find all the tr elements within the tbody
    tr_elements = tbody_element.find_elements(By.XPATH, "./tr")
    
    # Iterate over the tr elements
    for tr_element in tr_elements:
        # Print the text content of each tr element

        link_element = tr_element.find_element(By.XPATH, ".//a[contains(@href, '.mp3')]")
        href = link_element.get_attribute("href")

        print(href)

        # print(tr_element.text)

# Fermer le navigateur
driver.quit()

# Traitez le contenu récupéré selon vos besoins
# print("tbody: ", tbody_element.text)
