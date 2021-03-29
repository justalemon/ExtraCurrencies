from pathlib import Path

from .arguments import args
from .currencies import compile_currencies
from .processing import process_files


def main():
    if hasattr(args, "help"):
        return

    for game in args.games:
        Path("build/" + game + "/universal/def").mkdir(parents=True, exist_ok=True)

        currencies = compile_currencies(game)

        process_files(["source/base.json", f"source/base_{game}.json"],
                      output="/universal/def/economy_data.sii",
                      stype="economy_data", sname="economy.data.storage",
                      extra=currencies)
        process_files(["source/manifest.json"],
                      output="/universal/manifest.sii",
                      stype="mod_package", sname=".universal")
        process_files(["source/versions.json"],
                      output="/versions.sii",
                      stype="package_version_info", sname=".universal")


if __name__ == "__main__":
    main()
