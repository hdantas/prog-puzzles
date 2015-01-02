# http://www.codewars.com/kata/542ea700734f7daff80007fc

def processes(start, end, original_processes, solution_candidate=[]):
    # uses recursion to greedily explore trees, then returns the shortest tree of those with the correct start and end node
    if (start == end): return solution_candidate # found a possible solution

    tmp_result = []
    matched_processes = [] # nodes traversed
    non_matched_processes = [] # nodes to traverse in the recursion
    for p in original_processes:
        if p[1] == start:
            matched_processes += [p]
        else:
            non_matched_processes += [p]
    for m in matched_processes:
        tmp_result += [processes(m[2], end, non_matched_processes, solution_candidate + [m[0]])]

    clean_tmp_result = [item for item in tmp_result if len(item) > 0] # remove empty solution candidates
    if clean_tmp_result == []:
        result = []
    else:
        result = min(clean_tmp_result, key=len) # off the possible solutions pick the one with the smallest length
    return result