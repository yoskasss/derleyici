import subprocess
import platform

def hello_world(message):
    """Konsola bir mesaj yazdırır."""
    print(message)

def yosk(prompt):
    """Kullanıcıdan girdi alır."""
    return input(prompt)

def greet_user(name):
    """Kullanıcıya kişisel bir selam verir."""
    print(f"Merhaba, {name}! Hoş geldiniz!")

def calculate_sum(a, b):
    """İki sayının toplamını döndürür."""
    return a + b

def save_to_file(filename, content):
    """Verilen içeriği belirtilen dosyaya kaydeder."""
    with open(filename, 'w') as file:
        file.write(content)
    print(f"İçerik '{filename}' dosyasına kaydedildi.")

def read_from_file(filename):
    """Belirtilen dosyadan içeriği okur ve döndürür."""
    with open(filename, 'r') as file:
        content = file.read()
    return content

def repeat_message(message, times):
    """Bir mesajı belirtilen sayıda tekrarlar."""
    return message * times

def run_command(command, new_terminal=False, os=None):
    try:
        # Determine the operating system if not specified
        if os is None:
            os = platform.system().lower()

        if new_terminal:
            if os == 'windows':
                # Windows için yeni terminalde komut çalıştır
                command = f'start cmd /k "{command}"'
            elif os == 'linux':
                # Linux için yeni terminalde komut çalıştır (gnome-terminal, konsole, etc. kullanılabilir)
                command = f'gnome-terminal -- {command}'
            elif os == 'darwin':
                # macOS için yeni terminalde komut çalıştır
                command = f'osascript -e \'tell application "Terminal" to do script "{command}"\''
            else:
                print("Bilinmeyen işletim sistemi. Yeni terminal açma özelliği desteklenmiyor.")
                return
        
        # Komutu çalıştır
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        
        # Komutun çıktısını ve hatasını yazdır
        if result.stdout:
            print('Çıktı:', result.stdout)
        if result.stderr:
            print('Hata:', result.stderr)
        print('Çıkış kodu:', result.returncode)
    except subprocess.CalledProcessError as e:
        print('Komut çalıştırılırken hata oluştu:', e)
        if e.stdout:
            print('Çıktı:', e.stdout)
        if e.stderr:
            print('Hata:', e.stderr)

def open_app(app_name, os=None):
    try:
        # Determine the operating system if not specified
        if os is None:
            os = platform.system().lower()

        if os == 'windows':
            # Windows için uygulama başlat
            command = f'start {app_name}'
        elif os == 'linux':
            # Linux için uygulama başlat (xdg-open, gnome-open, or the application name directly)
            command = f'{app_name}'
        elif os == 'darwin':
            # macOS için uygulama başlat
            command = f'open -a "{app_name}"'
        else:
            print("Bilinmeyen işletim sistemi. Uygulama açma özelliği desteklenmiyor.")
            return
        
        # Komutu çalıştır
        subprocess.run(command, shell=True, check=True)
        print(f'{app_name} başarıyla başlatıldı.')
    except subprocess.CalledProcessError as e:
        print(f'{app_name} başlatılırken hata oluştu:', e)
        if e.stdout:
            print('Çıktı:', e.stdout)
        if e.stderr:
            print('Hata:', e.stderr)

def text_to_binary(text):
    """Verilen metni ikilik (binary) kodlara çevirir."""
    binary_text = ''
    for char in text:
        binary_text += format(ord(char), '08b') + ' '
    return binary_text

def basic_encrypt_text(text):
    """Verilen metni harflerin yerine sayılarla değiştirerek şifreler."""
    encryption_dict = {
        'a': '1', 'b': '2', 'c': '3', 'ç': '4', 'd': '5', 'e': '6', 'f': '7', 'g': '8', 'ğ': '9', 'h': '10',
        'ı': '11', 'i': '12', 'j': '13', 'k': '14', 'l': '15', 'm': '16', 'n': '17', 'o': '18', 'ö': '19', 'p': '20',
        'r': '21', 's': '22', 'ş': '23', 't': '24', 'u': '25', 'ü': '26', 'v': '27', 'y': '28', 'z': '29',
        'A': '1', 'B': '2', 'C': '3', 'Ç': '4', 'D': '5', 'E': '6', 'F': '7', 'G': '8', 'Ğ': '9', 'H': '10',
        'I': '11', 'İ': '12', 'J': '13', 'K': '14', 'L': '15', 'M': '16', 'N': '17', 'O': '18', 'Ö': '19', 'P': '20',
        'R': '21', 'S': '22', 'Ş': '23', 'T': '24', 'U': '25', 'Ü': '26', 'V': '27', 'Y': '28', 'Z': '29'
    }
    encrypted_text = ''
    for char in text:
        encrypted_text += encryption_dict.get(char, char) + ' '
    return encrypted_text.strip()

def encrypt_text(text):
    encryption_dict = {
        'a': '219', 'b': '228', 'c': '237', 'ç': '246', 'd': '255', 'e': '264', 'f': '273', 'g': '282', 'ğ': '291', 'h': '2010',
        'ı': '1119', 'i': '1128', 'j': '1137', 'k': '1146', 'l': '1155', 'm': '1164', 'n': '1173', 'o': '1182', 'ö': '1191', 'p': '1200',
        'r': '1209', 's': '1218', 'ş': '1227', 't': '1236', 'u': '1245', 'ü': '1254', 'v': '1263', 'y': '1272', 'z': '1281',
        'A': '219', 'B': '228', 'C': '237', 'Ç': '246', 'D': '255', 'E': '264', 'F': '273', 'G': '282', 'Ğ': '291', 'H': '2010',
        'I': '1119', 'İ': '1128', 'J': '1137', 'K': '1146', 'L': '1155', 'M': '1164', 'N': '1173', 'O': '1182', 'Ö': '1191', 'P': '1200',
        'R': '1209', 'S': '1218', 'Ş': '1227', 'T': '1236', 'U': '1245', 'Ü': '1254', 'V': '1263', 'Y': '1272', 'Z': '1281'
    }
    encrypted_text = ''
    for char in text:
        encrypted_text += encryption_dict.get(char, char) + ' '
    return encrypted_text.strip()

def decrypt_text(encrypted_text):
    """Şifrelenmiş metni çözer."""
    decryption_dict = {
        '219': 'a', '228': 'b', '237': 'c', '246': 'ç', '255': 'd', '264': 'e', '273': 'f', '282': 'g', '291': 'ğ', '2010': 'h',
        '1119': 'ı', '1128': 'i', '1137': 'j', '1146': 'k', '1155': 'l', '1164': 'm', '1173': 'n', '1182': 'o', '1191': 'ö', '1200': 'p',
        '1209': 'r', '1218': 's', '1227': 'ş', '1236': 't', '1245': 'u', '1254': 'ü', '1263': 'v', '1272': 'y', '1281': 'z',
        '219': 'A', '228': 'B', '237': 'C', '246': 'Ç', '255': 'D', '264': 'E', '273': 'F', '282': 'G', '291': 'Ğ', '2010': 'H',
        '1119': 'I', '1128': 'İ', '1137': 'J', '1146': 'K', '1155': 'L', '1164': 'M', '1173': 'N', '1182': 'O', '1191': 'Ö', '1200': 'P',
        '1209': 'R', '1218': 'S', '1227': 'Ş', '1236': 'T', '1245': 'U', '1254': 'Ü', '1263': 'V', '1272': 'Y', '1281': 'Z'
    }
    decrypted_text = ''
    encrypted_parts = encrypted_text.split(' ')
    for part in encrypted_parts:
        decrypted_text += decryption_dict.get(part, part)
    return decrypted_text