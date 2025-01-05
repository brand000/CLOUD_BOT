from scraping.dailyfx_com import dailyfx_com
from scraping.investing_com import get_pair
from scraping.bloomberg_com import bloomberg_com
from scraping.fx_calendar import get_fx_calendar

from dateutil import parser


if __name__ == "__main__":
    print("\ndailyfx_com()")
    print(dailyfx_com())
    
    print("\ninvesting_com()")
    print(get_pair("EUR_USD", "H1"))
    
    print("\nbloomberg_com")
    print(bloomberg_com())
    
    print("\nfx_calendar")
    print(get_fx_calendar(parser.parse("2022-04-11 00:00:00")))
    
