import sys, os
from dotenv import load_dotenv

def show_args():
    pass

def show_args_env_file(env_file):
    load_dotenv(env_file, verbose=True)
    host = os.environ.get('HOST')
    print(f"got host={host}")

def main():
    show_args_env_file('example.env')

if __name__ == '__main__':
    sys.exit(main())
