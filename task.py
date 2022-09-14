import argparse

from src.ranking import Ranking


def entrypoint() -> None:
    """Main entry point for the hockey ranker CLI.

    Raises:
        FileNotFoundError: If the input_file argument points to a file that does not exist.
        TypeError: If the input_file argument points to a non-file (eg, a directory).
    """
    parser = argparse.ArgumentParser(
        description="CLI to rank teams from a list of game results"
    )
    parser.add_argument("input_file", help="Location of input CSV")
    parser.add_argument("output_file", help="Location to write output CSV")

    # Parse out the input file
    args = parser.parse_args()

    # Here are your two arguments: the input CSV and the output CSV
    input_file = args.input_file
    output_file = args.output_file

    # TODO: Add your code here
    # (you may modify the line below)
    my_ranking = Ranking(input_file, output_file)


if __name__ == "__main__":
    entrypoint()
