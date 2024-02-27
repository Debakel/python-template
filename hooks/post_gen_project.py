
SUCCESS = "\x1b[1;32m"
INFO = "\x1b[1;33m"
TERMINATOR = "\x1b[0m"


def main():
    print(SUCCESS + "Project successfully initialized" + TERMINATOR)
    print(INFO + "Next steps:" + TERMINATOR)
    print(f"""
    
    # Enter project directory
    cd <repo_name>
        
    # Install dependencies
    pipenv install --dev
    
    # Initialise git repo
    git init
    
    # Setup pre-commit and pre-push hooks
    pipenv run pre-commit install
    """)


if __name__ == "__main__":
    main()
