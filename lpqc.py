from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

def process_data(tbody_element):
    for tbody_element in tbody_elements:
                
        if len(tbody_element.text) == 0:
            break
        # Find all the tr elements within the tbody
        tr_elements = tbody_element.find_elements(By.XPATH, "./tr")

        
        # Iterate over the tr elements
        for tr_element in tr_elements:
            # Print the text content of each tr element

            link_element = tr_element.find_element(By.XPATH, ".//a[contains(@href, '.mp3')]")
            href = link_element.get_attribute("href")

            print(href)



# Trouver le <tbody> contenant les éléments souhaités
tbody_elements = driver.find_elements(By.XPATH, "//tbody")

process_data(tbody_elements)
# Continue to click the "Next" button until it is no longer available
while True:
     # Find the "Next" link
    next_link = driver.find_element(By.ID, "idLivres_next")

    # Check if the "Next" link is disabled
    is_disabled = next_link.get_attribute("disabled") == "true"
    if is_disabled:
        break

    # Click the "Next" link
    next_link.click()

    # Wait for the table to update
    # WebDriverWait(driver, 10).until(EC.staleness_of(tbody_elements))

    # Locate the updated table tbody element
    tbody_elements = driver.find_elements(By.XPATH, "//tbody")



    # Retrieve and process the data from the updated page
    process_data(tbody_elements)
      # Check if there are more elements in the table
    # rows = tbody_elements.find_elements(By.TAG_NAME, "tr")
    # if len(rows) == 0:
    #     break




# Fermer le navigateur
driver.quit()

# Traitez le contenu récupéré selon vos besoins
# print("tbody: ", tbody_element.text)
