import os
import base64

def generate_secret_key():
    secret_bytes = os.urandom(32)
    secret_key = base64.urlsafe_b64encode(secret_bytes).rstrip(b'=').decode('utf-8')
    return secret_key

def add_secret_key_to_env():
    secret_key = generate_secret_key()

    key_exists = False
    with open('.env', 'r') as env_file:
        for line in env_file:
            if line.startswith("SECRET_KEY="):
                key_exists = True
                break

    if not key_exists:
        with open('.env', 'a') as env_file:
            env_file.write(f"SECRET_KEY={secret_key}\n")
    else:
        with open('.env', 'r') as env_file:
            lines = env_file.readlines()
        with open('.env', 'w') as env_file:
            for line in lines:
                if line.startswith("SECRET_KEY="):
                    line = f"SECRET_KEY={secret_key}\n"
                env_file.write(line)

if __name__ == "__main__":
    add_secret_key_to_env()
