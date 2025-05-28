from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

def hash_password(password):
    """
    Gera um hash seguro para a senha.
    """
    return generate_password_hash(password)

def verify_password(password_hash, password):
    """
    Verifica se a senha corresponde ao hash armazenado.
    """
    return check_password_hash(password_hash, password)

def format_datetime(dt):
    """
    Formata datetime para string ISO.
    """
    return dt.isoformat() if isinstance(dt, datetime) else dt
