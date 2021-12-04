from time import strftime,localtime

def time_stamp():
    time_stamp = strftime("%Y%m%d%H%M%S",localtime())
    return time_stamp

if __name__ == "__main__":
    print(time_stamp())
