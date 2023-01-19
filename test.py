from decoratorPattern import *
from multiprocessing import Process


def deployProxyRetrieverBot():
    bot = ProxyRetrieverBot()
    bot.setDriver()
    bot.getPage()
    bot.getProxies()

def main():
    procs = [Process(target=deployProxyRetrieverBot) for x in range(0,5)]
    for proc in procs:
        proc.start()

if __name__ == '__main__':
    main()
