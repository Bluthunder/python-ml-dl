
def ksmallest(root, k):

    stack = []
    count = 0
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        count += 1

        if count == k : return curr.val

        curr = curr.right
        
