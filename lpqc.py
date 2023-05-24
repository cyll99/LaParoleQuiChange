import getpass
import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Download each audio
def download_audio(page_audio, book):

    current_user = getpass.getuser() #get current user

    directory = f'C:\\Users\\{current_user}\\Downloads\\audio_files\\{book}'
 

    file_name = page_audio.split('/')[-1]
    file_path = os.path.join(directory, file_name)
    

        # Check if the file already exists
    if os.path.exists(file_path):
        print(f'Skipped {file_name} - File already exists')
        return


    try:
        with open(file_path, 'wb') as file:
                print(f"Downloadind {file_name}....")
                response = requests.get(page_audio)
                file.write(response.content)
                
                print(f'{file_name} downloaded')
    except:
        print("Somethings went wrong. File not downloaded")


# Process data from table
def process_data(tbody_elements, book):
    for tbody_element in tbody_elements:

        # Find all the tr elements within the tbody
        tr_elements = tbody_element.find_elements(By.XPATH, "./tr")

        
        # Iterate over the tr elements
        for tr_element in tr_elements:
            # Print the text content of each tr element

            link_element = tr_element.find_element(By.XPATH, ".//a[contains(@href, '.mp3')]")
            href = link_element.get_attribute("href")

            download_audio(href, book)


def main():
    while True:
        print("Press q to exit")
        book = input("Enter the book you want to download: ")

        if book.lower() == 'q':
            break

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

        search_input.send_keys(book)
        # Trouver le <tbody> contenant les éléments souhaités
        tbody_elements = driver.find_elements(By.XPATH, "//tbody")

        process_data(tbody_elements, book)
        # Continue to click the "Next" button until it is no longer available
        while True:
            # Find the "Next" link
            next_link = driver.find_element(By.ID, "idLivres_next")

            # Check if the "Next" link is disabled
            tabindex = next_link.get_attribute("tabindex")
            if tabindex == "-1":
                break
            # Click the "Next" link
            next_link.click()



            # Locate the updated table tbody element
            tbody_elements = driver.find_elements(By.XPATH, "//tbody")



            # Retrieve and process the data from the updated page
            process_data(tbody_elements, book)


        # Fermer le navigateur
        driver.quit()


if __name__ == "__main__":
    main()