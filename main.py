import yoskPY as yp
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Bu araç, belirtilen dosyaları işlemek ve gerekli dosyaları indirmek için kullanılır."
    )
    
    # Argümanlar ekleme
    parser.add_argument(
        '--downloads',
        action='store_true',
        help="Gerekli dosyaları indirir. Örnek: pyinstaller kurulumu ve diğer bağımlılıklar."
    )
    parser.add_argument(
        '--file',
        type=str,
        help="İşlenecek dosya adını belirtin. Örnek: --file myscript (uzantısı olmadan)"
    )
    
    # Argümanları parse et
    args = parser.parse_args()
    
    # İndirme işlemi
    if args.downloads:
        print("Bağımlılıklar indiriliyor...")
        yp.run_command(
            "pip uninstall pyinstaller -y && pip install pyinstaller",
            new_terminal=True,
            os='windows'
        )
    
    # Dosya işleme
    if args.file:
        file_name = args.file
        print(f"{file_name}.py dosyası işleniyor...")
        yp.run_command(
            f"pyinstaller --onefile {file_name}.py && cd dist && {file_name}.exe",
            new_terminal=True,
            os='windows'
        )

if __name__ == "__main__":
    main()
