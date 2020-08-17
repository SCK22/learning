import click

@click.command()
@click.option("--requests", "-r", default = 500, help = "number of requests")
@click.option("--concurrency", "-c", default = 1, help = "number of concurrent requests")
@click.option("--json-file", "-j", default = None , help = "Path to the output JSON file")
@click.argument("url")

def cli(requests, concurrency, json_file, url):
    print("requests", requests)
    print("concurrency", concurrency)
    print("json_file", json_file)
    print("url", url)


if __name__ == "__main__":
    cli()