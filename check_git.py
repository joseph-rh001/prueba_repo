# check_git.py

# Este script primero verifica si Git está instalado ejecutando el comando git --version. 
# Si el comando se ejecuta correctamente, se considera que Git está instalado y no hace mas. 
# Si el comando devuelve error, se asume que Git no está instalado y el script ofrece la opción de instalarlo.
# Si se elige instalar Git, el script abrirá la página de descargas de Git en el navegador web predeterminado. 
# Una vez descargado el paquete de instalacion se procede a a instalar Git automáticamente después de descargarlo en Windows, utilizando el módulo requests para descargar el instalador de Git y luego ejecutar el instalador descargado.
# Es posible que la libreria "request" marque el error  "Import 'requests' could not be resolved", esto indica que el módulo 'requests' no está disponible en el entorno de Python. Este módulo es comúnmente utilizado para hacer solicitudes HTTP en Python. Para solucionar este problema, necesitas instalar el módulo 'requests'. Puedes hacerlo utilizando pip, el administrador de paquetes de Python. Ejecutando el siguiente comando dentro de un entorno virtual: pip install requests

import os
import time
import subprocess
import platform
import requests
import tempfile

def is_git_installed():
    print("Comprobando si Git se encuentra instalado...")
    try:
        subprocess.check_output("git --version", shell=True)
        time.sleep(2)  # Espera de 2 segundos
        return True
    except subprocess.CalledProcessError:
        time.sleep(2)  # Espera de 2 segundos
        return False

def install_git():
    print("Git no se encuentra instalado.")
    install = input("Deseas instalar Git? (si/no): ").lower()
    if install == "si" or install == "s":
        install_git_windows()
    else:
        print("Git no se instalara.")

def install_git_windows():
    if platform.system() == "Windows":
        git_download_url = "https://git-scm.com/download/win"
        temp_dir = tempfile.gettempdir()
        git_installer_path = os.path.join(temp_dir, "GitInstaller.exe")

        try:
            # Download Git installer
            print("Descargando el instalador Git...")
            response = requests.get(git_download_url)
            response.raise_for_status()  # Comprobar si la descarga fue exitosa

            # Comprobar si el contenido de la respuesta no está vacío
            if not response.content:
                print("Error: El contenido del instalador Git está vacío.")
                return False

            with open(git_installer_path, "wb") as installer_file:
                installer_file.write(response.content)

            time.sleep(2)  # Espera de 2 segundos

            # Comprobar si el archivo se ha descargado correctamente
            if not os.path.exists(git_installer_path):
                print("Error: El archivo del instalador Git no se ha descargado correctamente.")
                return False

            # Run Git installer
            print("Ejecutando el instalador Git...")
            return_code = os.system(git_installer_path)
            if return_code != 0:
                print("Error: No se pudo ejecutar el instalador de Git.")
                return False
            else:
                return True

        except Exception as e:
            print(f"Error: {e}")
            return False

    else:
        print("Lo siento, tu sistema operativo no es compatible.")
        return False

def main():
    if is_git_installed():
        print("Git ya instalado.")
    else:
        install_git()

if __name__ == "__main__":
    main()
