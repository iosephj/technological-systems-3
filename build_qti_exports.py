from pathlib import Path
import shutil

export_dir = Path("exports")
export_dir.mkdir(exist_ok=True)  # Crea la carpeta 'exports' si no existe

# Busca recursivamente todos los archivos llamados qti.md
for file_path in Path(".").rglob("qti.md"):
    parts = file_path.parts  # Obtiene cada parte de la ruta como una tupla

    # Construye el nuevo nombre usando las carpetas contenedoras
    if len(parts) >= 3:
        parent1 = parts[-2]      # Carpeta inmediata
        parent2 = parts[-3]      # Carpeta superior
        new_name = f"{parent2}_{parent1}_{file_path.name}"
    elif len(parts) >= 2:
        parent1 = parts[-2]
        new_name = f"{parent1}_{file_path.name}"
    else:
        new_name = file_path.name  # Si no hay carpetas, solo el nombre original

    # Copia el archivo a la carpeta exports con el nuevo nombre
    shutil.copy(file_path, export_dir / new_name)

