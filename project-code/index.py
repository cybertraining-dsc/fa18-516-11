import sys
from resnet_predefined_classify import handler

def get_stdin():
    buf = ""
    for line in sys.stdin:
        buf = buf + line
    return buf

if(__name__ == "__main__"):
    st = get_stdin()
    handler.handle(st)