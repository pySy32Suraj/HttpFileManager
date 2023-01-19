import sys
import traceback



def format_exc() -> str:
    e = sys.exc_info()
    # print(e)
    # return "error"
    exc_type, value, tb = e
    return f"{''.join(traceback.format_tb(tb))}\n{exc_type.__name__}: {value}"