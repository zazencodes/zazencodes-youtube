def main(config_arg):

    print("hello from my_app.core")
    print("using config for {}".format(config_arg))

    if config_arg == "client_1":
        from config.client_1 import CLIENT_NAME
    else:
        raise ValueError(f"Bad client ID: {config_arg}")

    print(CLIENT_NAME)
