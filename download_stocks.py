#! /usr/bin/python

import investpy
import click
from datetime import datetime 
from dateutil.relativedelta import relativedelta

@click.command()
@click.option("--years", default=1, help="Data of the last years")
@click.option("--index", default="MSCI World", help="Name of the stock index")
@click.option("--country", default="world", help="Country of the stock index")
def download_stocks(years, index, country):
    
    to_date = datetime.now() - relativedelta(days=1)
    from_date = datetime.now() - relativedelta(years=years)
    to_date_str = to_date.strftime("%d/%m/%Y")
    from_date_str = from_date.strftime("%d/%m/%Y")

    print(f"From: {from_date_str}, To: {to_date_str}")
    
    data = investpy.get_index_historical_data(index=index,
                                          country=country,
                                          from_date=from_date_str,
                                          to_date=to_date_str)
    
    print(data.head)

if __name__ == '__main__':
    download_stocks()

