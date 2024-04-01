import os
import pprint

import typer


cli = typer.Typer()


@cli.command()
def run_volumetry_ingest():
    """Run volumetry ingest
    """
    print("Not yet implemented")



@cli.command()
def about():
    """CLI description

    Various lab related toolw.
    """
    print(f"CLI tool to help with science 👩‍🔬")