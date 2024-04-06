import os


def main():
    print("hello from my_app.core")
    config_arg = os.getenv("MY_APP_CONFIG")
    print("using config for {}".format(config_arg))
