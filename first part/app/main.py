import sys
from classes import DirectoryHandler


def main():
    if len(sys.argv) < 2:
        print(
            "Usage: python main.py <source_directory> " +
            "<destination_directory_or_nothing>")
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2] if len(sys.argv) > 2 else None
    dh = DirectoryHandler(source, destination)
    dh.process_directory(dh.src_dir)


if __name__ == '__main__':
    main()
