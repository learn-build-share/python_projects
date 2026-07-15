# Streamlit entry point for the certificate generator app.
try:
    from app import main
except ImportError:
    from certificate_generator.app import main


if __name__ == "__main__":
    main()
