class Config:
    def __init__(self, env):
        SUPPORTED_ENVS: list
        SUPPORTED_ENVS = ['dev', 'qa']

        if env.lower() not in SUPPORTED_ENVS:
            raise Exception(f'{env} is not a supported environment (supported envs: {SUPPORTED_ENVS}')

        self.base_url = {
            'dev': 'https://www.uala.com.ar/',
            'qa': 'https://www.uala.com.co/'
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa': 80
        }[env]