def AllParenthesis(n):
    #code here
    def combinePar(o, c, oc, output):
        if o == 0 and c == 0:
            output.append(oc)
            return
        if o != 0:
            combinePar(o - 1, c, oc + '(', output)
        if c > o and c != 0:
            combinePar(o, c - 1, oc + ')', output)
        
    output = []
    combinePar(n, n, "", output)
    print(output)
    return output

AllParenthesis(2)