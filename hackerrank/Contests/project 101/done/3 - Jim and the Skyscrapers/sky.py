import sys
import logging

def do_work(heights):
    logging.debug("%s", heights)
    response = 0
    l = len(heights)
    max_h = max(heights)
    min_h = min(heights)
    delta = max_h - min_h
    
    tmp = [0] * (delta + 1)
    logging.debug("%s", range(min_h, min_h + delta + 1))
    
    stack = [heights[0]]

    for i in xrange(l):
        h = heights[i]
        index = h - min_h
        response += tmp[index]
        
        if h > stack[-1]:
            old_h = stack[-1]
            while h > old_h:
                stack.pop()
                tmp[old_h - min_h] = 0
                logging.debug("Clear %s", old_h)
                if len(stack) == 0:
                    break;
                old_h = stack[-1]
        
        if len(stack) == 0 or h < stack[-1]:
            stack.append(h)
        
        tmp[index] += 1
        logging.debug("tmp[%d]: %s\th: %s\tresponse: %s\tstack: %s", h, tmp[index], h, response, stack)

    print 2 * response

if sys.platform == 'darwin':
    # logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    # val = [782, 1296, 1039, 1466, 129, 1898, 1766, 261, 1134, 51, 3250, 3208, 4414]
    # do_work(val)
    # exit()

    logging.basicConfig(stream=sys.stdout, level=logging.ERROR)
    myfile = open("sky-input08.txt")
    n = int(myfile.readline())
    val = myfile.readline().split();
    do_work(map(int, val))

else:
    n = int(raw_input())
    string = raw_input()
    val = string.split();
    do_work(map(int, val))
