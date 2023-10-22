from selenium.webdriver import Chrome
import time

def buscar_ofertas_linkedin():
    # Iniciar el navegador
    driver = Chrome()

    # Definir criterios de búsqueda
    palabras_clave = ["python", "java"]
    urls = []

    for palabra in palabras_clave:
        # Ir a la página de búsqueda de LinkedIn con los criterios especificados
        url = f"https://www.linkedin.com/jobs/search/?f_TPR=r86400&f_WRA=true&keywords={palabra}"
        driver.get(url)
        driver.find_element_by_xpath("//a[@class='result-card__full-card-link']")
        time.sleep(5) # Esperar a que se cargue la página

        # Recopilar los enlaces de las ofertas de trabajo
        ofertas = driver.find_element_by_css_selector(".result-card__full-card-link")
        print(oferta.get_attribute("href"))
        for oferta in ofertas:
            urls.append(oferta.get_attribute("href"))

    # Cierra el navegador
    driver.quit()

    return urls

if __name__ == "__main__":
    enlaces = buscar_ofertas_linkedin()
    for enlace in enlaces:
        print(enlace)
