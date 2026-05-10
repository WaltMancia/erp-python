class AppError(Exception):
    """Error base de aplicación"""
    pass


class ValidationError(AppError):
    """Errores de validación"""
    pass


class AuthenticationError(AppError):
    """Errores autenticación"""
    pass


class DatabaseError(AppError):
    """Errores base de datos"""
    pass
