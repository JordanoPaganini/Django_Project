from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions = {
        'Cadastrar_produto': True,
        'Liberar_desconto': True,
        'Cadastar_vendedor': True,
    }

class Vendedor(AbstractUserRole):
    available_permissions = {
        'realizar_venda': True
    }