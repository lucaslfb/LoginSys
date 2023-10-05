import re
from datetime import datetime
import smtplib
import email.message
import bcrypt
import PySimpleGUI as sg


# funções de criação dos layouts de login

def generate_initial_screen():
    sg.theme('DarkBlue4')
    initial_layout = [
        [sg.Text('Username')],
        [sg.Input(key='username')],
        [sg.Text('Password')],
        [sg.Input(key='password', password_char='*')],
        [sg.Button('Login'), sg.Button('Register')],
    ]
    return sg.Window('LoginPy', layout=initial_layout, finalize=True)


def generate_registration_screen():
    sg.theme('DarkBlue4')
    register_layout = [
        [sg.Text('Username')],
        [sg.Input(key='username')],
        [sg.Text('Email')],
        [sg.Input(key='email')],
        [sg.Text('Password')],
        [sg.Input(key='password', password_char='*')],
        [sg.Text('Password confirm')],
        [sg.Input(key='password_confirm', password_char='*')],
        [sg.Button('Register')],
    ]
    return sg.Window('LoginPy', layout=register_layout, finalize=True)


# gerar os layouts na tela

login_window, register_window = generate_initial_screen(), None


# função de enviar a confirmação de usuário pelo email com smtp google

def send_email(mail):
    email_body = f"""
    <h1>Congratulation on your new account!</h1>
    <h2>Welcome!</h2>
    <p>Hello, thank you for creating your account with us!</p>
    """
    msg = email.message.Message()
    msg['Subject'] = "Welcome to LoginPy"
    msg['From'] = 'from'
    msg['To'] = mail
    password = 'password'  # substitua pela senha ou utilize opções mais seguras como variáveis de ambiente.
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_body)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # credencial de login para enviar o email
    s.login(msg['From'], password)

    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print(f"Email sent. {datetime.now()}")


# função para fazer login

def do_login():
    username = values['username']
    password = values['password']

    auth_validation = user_authentication(username, password)

    if auth_validation:
        login_window.close()
        sg.popup(f'Welcome {username}!\nThis program was developed by Lucas Bezerra.\nThanks for testing!')
        with open('log_register', 'a+', encoding='Utf-8', newline='') as archive:
            archive.writelines(f'{datetime.now()} | {username}\n')
        exit()
    elif not username or not password:
        sg.popup('Name or password required!')
    elif ' ' in username or ' ' in password:
        sg.popup('Make sure there are no spaces in the fields!')
    else:
        sg.popup(f'Wrong username or password!')


# função para registrar novos usuários

def do_register():
    username = values['username']
    password = values['password']
    password_confirm = values['password_confirm']
    mail = values['email']

    user_exists = search_user(username)
    pattern = r'^(?=.*[A-Z])(?=.*[\W_]).*$'
    password_size = len(password)

    if user_exists:
        sg.popup('This username is already being used!')
    elif not username or not password:
        sg.popup('Name or password required!')
    elif ' ' in username or ' ' in password:
        sg.popup('Make sure there are no spaces in the fields!')
    elif re.match(pattern, password) == None or password_size < 7:
        sg.popup('Your password must contain 8 digits, an uppercase character and a special character.')
    elif username == password:
        sg.popup('Your password must be different of the username!')
    elif password != password_confirm:
        sg.popup('You must write the same passwords!')
    else:
        salt = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        register_window.close()
        sg.popup('Your account has been created successfully.\nCheck your mail box!')

        with open('users.txt', 'a+', encoding='Utf-8', newline='') as archive:
            archive.writelines(f'{username} | {salt.decode("utf-8")} | {hash_password.decode("utf-8")} | {mail}\n')
            send_email(mail)
        return True


# função para verificar se o usuário já existe

def search_user(username):
    try:
        with open('users.txt', 'r', encoding='utf-8') as archive:
            for line in archive:
                line = line.strip()
                parts = line.split('|')
                if len(parts) == 4:
                    stored_username = parts[0].strip()
                if username == stored_username:
                    return True
    except FileNotFoundError:
        return False

    return False


# função para autenticar o usuário

def user_authentication(username, password):
    try:
        with open('users.txt', 'r', encoding='Utf-8') as archive:
            for line in archive:
                line = line.strip()
                parts = line.split('|')
                if len(parts) == 4:
                    stored_username = parts[0].strip()
                    stored_salt = parts[1].strip()
                    stored_hash = parts[2].strip()
                    if username == stored_username and bcrypt.checkpw(password.encode('utf-8'), stored_salt.encode('utf-8') and stored_hash.encode('utf-8')):
                        return True
    except FileNotFoundError:
        return False

    return False


# loop que roda a aplicação

while True:
    window, event, values = sg.read_all_windows()
    if window == login_window and event == sg.WINDOW_CLOSED:
        exit()
    elif window == login_window and event == 'Login':
        do_login()
    elif window == login_window and event == 'Register':
        login_window.close()
        register_window = generate_registration_screen()
    elif window == register_window and event == sg.WINDOW_CLOSED:
        register_window.hide()
        login_window = generate_initial_screen()
    elif window == register_window and event == 'Register':
        valid_register = do_register()
        if valid_register:
            login_window = generate_initial_screen()