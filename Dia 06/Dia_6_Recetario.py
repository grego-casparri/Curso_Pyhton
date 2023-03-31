from pathlib import Path
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_menu():
    print("¡Bienvenido al administrador de recetas!")
    print("La ruta de acceso al directorio de recetas es:", recipe_directory)
    print("Hay un total de", total_recipes, "recetas en el directorio.")
    print("Por favor, seleccione una opción:")
    print("1. Leer una receta.")
    print("2. Crear una nueva receta.")
    print("3. Crear una nueva categoría.")
    print("4. Eliminar una receta.")
    print("5. Eliminar una categoría.")
    print("6. Salir del programa.")
    user_choice = input("Opción elegida: ")
    return user_choice


def select_category():
    clear_screen()
    recipe_dir = Path("Recetas")
    categories = [category.name for category in recipe_dir.iterdir() if category.is_dir()]
    print("Categorías de recetas disponibles:")
    for i, category in enumerate(categories):
        print(f"{i+1}. {category}")
    while True:
        try:
            selection = int(input("Seleccione una categoría: "))
            if selection < 1 or selection > len(categories):
                print("Selección inválida. Intente de nuevo.")
            else:
                return categories[selection - 1]
        except ValueError:
            print("Selección inválida. Intente de nuevo.")


def read_recipe(category):
    clear_screen()
    recipe_path = Path.cwd() / "Recetas" / category
    recipe_files = sorted(recipe_path.glob("*.txt"))
    if not recipe_files:
        print("No hay recetas en esta categoría")
        return
    print(f"Hay {len(recipe_files)} recetas en la categoría {category}")
    print("Estas son las recetas disponibles:")
    for i, file in enumerate(recipe_files):
        print(f"{i+1}. {file.stem}")
    recipe_number = input("¿Qué receta quieres leer? (Ingresa el número): ")
    try:
        recipe_number = int(recipe_number)
        if recipe_number < 1 or recipe_number > len(recipe_files):
            raise ValueError
    except ValueError:
        print("Opción inválida, por favor ingresa un número válido")
        return
    selected_recipe = recipe_files[recipe_number-1]
    with open(selected_recipe, "r", encoding="utf-8") as f:
        recipe_content = f.read()
    input(recipe_content)


def create_recipe():
    category = select_category()  # Obtiene la categoría elegida por el usuario
    recipe_name = input("Ingrese el nombre de la receta: ")
    recipe_content = input("Ingrese el contenido de la receta: ")
    recipe_path = Path("recetas") / category / f"{recipe_name}.txt"
    # Si el archivo ya existe, pedimos confirmación para sobreescribirlo
    if recipe_path.exists():
        overwrite = input(f"El archivo {recipe_name}.txt ya existe. ¿Desea sobreescribirlo? (S/N)").lower()
        if overwrite != "s":
            print("No se ha creado la receta.")
            return
    with open(recipe_path, "w") as f:
        f.write(recipe_content)
        print(f"La receta '{recipe_name}' se ha creado en la categoría '{category}'.")

def select_recipe(category):
    """
    Muestra al usuario las recetas en la categoría dada y le pide que elija una de ellas.

    Parameters:
    category (str): El nombre de la categoría de recetas.

    Returns:
    (str, str): Una tupla con el nombre y contenido del archivo de la receta seleccionada.
    """

    # Obtener la ruta de la carpeta de la categoría y listar los archivos en ella
    clear_screen()
    category_folder = recipe_directory / category
    recipe_files = list(category_folder.glob('*.txt'))

    # Mostrar al usuario las recetas disponibles en la categoría
    print(f"Recetas disponibles en la categoría {category}:")
    for i, file in enumerate(recipe_files):
        print(f"{i+1}. {file.stem}")

    # Pedir al usuario que elija una receta por número
    while True:
        try:
            recipe_num = int(input("Seleccione una receta por número: "))
            if recipe_num < 1 or recipe_num > len(recipe_files):
                raise ValueError
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # Obtener el nombre y contenido del archivo de la receta seleccionada
    recipe_file = recipe_files[recipe_num-1]
    with open(recipe_file, 'r') as file:
        recipe_name = recipe_file.stem
        recipe_content = file.read()

    return recipe_name, recipe_content


def create_category():
    while True:
        category_name = input("Ingrese el nombre de la nueva categoría: ")
        category_path = Path.cwd() / "recetas" / category_name
        if category_path.exists():
            print("Esa categoría ya existe. Intente con otro nombre.")
        else:
            category_path.mkdir()
            print(f"La categoría '{category_name}' ha sido creada exitosamente.")
            break


def delete_recipe():
    clear_screen()
    category = select_category()
    recipe_name, recipe_content = select_recipe(category)
    recipe_path = Path(f"Recetas/{category}/{recipe_name}.txt")
    confirm = input(f"¿Está seguro que desea eliminar la receta {recipe_name}? (S/N): ")
    if confirm.lower() == "s":
        recipe_path.unlink()
        print(f"La receta {recipe_name} ha sido eliminada.")
    else:
        print("No se eliminó la receta.")
    input("Presione cualquier tecla para continuar...")


def delete_category():
    category = select_category()
    category_path = recipe_directory / category

    try:
        category_path.rmdir()
        print(f"La categoría {category} ha sido eliminada exitosamente.")
    except OSError as e:
        print(f"No se pudo eliminar la categoría {category}. Error: {e}")


# Definimos la ruta de acceso al directorio de recetas.
recipe_directory = Path.cwd() / "Recetas"

# Contamos el número de archivos de recetas en la carpeta.
total_recipes = len(list(recipe_directory.glob("*/*.txt")))

# Bucle principal del programa.
while True:
    clear_screen()
    user_choice = show_menu()
    if user_choice == "1":
        clear_screen()
        category = select_category()
        read_recipe(category)
    elif user_choice == "2":
        create_recipe()
    elif user_choice == "3":
        create_category()
    elif user_choice == "4":
        delete_recipe()
    elif user_choice == "5":
        delete_category()
    elif user_choice == "6":
        break
    else:
        input("Opción no válida. Presione Enter para continuar.")




