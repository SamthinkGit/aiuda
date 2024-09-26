import argparse
import importlib


def main():
    parser = argparse.ArgumentParser(
        description="Call another module with specific arguments."
    )
    parser.add_argument(
        "-module", type=str, required=True, help="Name of the module to call"
    )
    parser.add_argument(
        "args", nargs=argparse.REMAINDER, help="Arguments for the specified module"
    )

    args = parser.parse_args()

    # Load the specified module
    try:
        module = importlib.import_module(f"aiuda.core.{args.module}")
    except ModuleNotFoundError:
        print(f"The module '{args.module}' could not be found.")
        return

    # Call the main function of the module with the remaining arguments
    if hasattr(module, "main"):
        module.main(args.args)
    else:
        print(f"The module '{args.module}' does not have a 'main' function.")


if __name__ == "__main__":
    main()
