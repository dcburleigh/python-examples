
import sys
import os
import getopt
import argparse

action = None
name = None

def cli2():
    # https://docs.python.org/3.6/howto/argparse.html?highlight=argparse
    #
    parser = argparse.ArgumentParser()

    #parser.add_argument("echo")

    parser.add_argument("-a", help="activate", action="store_true")
    parser.add_argument("-b", help="bonus")
    parser.add_argument("--name", help="item name")

    parser.add_argument("-l", "--list", help="list items", action="store_true")
    parser.add_argument("-s",   "--show", help="show a specified item", action="store_true")

    args = parser.parse_args()
    if args.list:
        print("list")
    elif args.show:
        print("show")

    if args.a:
        print("activate")

    if args.b:
        print("got b=%s" % args.b )

    if args.name:
        print("got name=%s" % name)




def cli1():
    # https://docs.python.org/3.6/library/getopt.html?highlight=getopt#module-getopt
    #
    print("cli1")
    action = None
    show_help = False
    try:
        opts,args = getopt.getopt(sys.argv[1:], 'ab:', ['help', 'name=',  'list', 'show'])
    except getopt.GetoptError as err:
        raise Exception("invalid arguments " + str(err) )

    for o,a in opts:
        if o == '-a':
            print("got a")
        elif o == '-b':
            b = a
            print("got b=%s" % b)
        elif o == '--name':
            name = b
            print("got name='%s' " % name )
        elif o == '--list':
            action = 'list'
        elif o == '--show':
            action = 'show'
        elif o == '--help':
            show_help = True


        if show_help:
            print("Help for %s" % action )

def main():
    #cli1()
    cli2()

if __name__ == '__main__':
    sys.exit(main())
