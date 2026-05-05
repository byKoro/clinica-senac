import utilidades.cores as cor
config_senha = {
    "min":4,
    "max":14,
    "message_min":cor.vermelho("Erro! A senha deve conter mais de 04 caracteres!"),
    "message_max":cor.vermelho("Erro! A senha deve ter menos que 14 caracteres!"),
    "message_pass_error": cor.vermelho("Erro! Senha ou usuário incorreto!")
}