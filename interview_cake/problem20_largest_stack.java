// You've implemented a Stack class, but you want to be able to access the largest element in a stack.
// Here's the Stack class you have:

  // class Stack:

  //   # intialize an empty list
  //   def __init__(self):
  //       self.items = []

  //   # push a new item to the last index
  //   def push(self, item):
  //       self.items.append(item)

  //   # remove the last item
  //   def pop(self):
  //       # if the stack is empty, return None
  //       # (it would also be reasonable to throw an exception)
  //       if not self.items: return None

  //       return self.items.pop()

  //   # see what the last item is
  //   def peek(self):
  //       # if the stack is empty, return None
  //       if not self.items: return None

  //       return self.items[len(self.items)-1]


// Use your Stack class to implement a new class MaxStack with a function get_max() that returns the largest element in the stack. get_max() should not remove the item.

// Your stacks will contain only integers.

// src: https://www.interviewcake.com/question/largest-stack?utm_source=weekly_email


class MaxStack extends Stack {
    Stack max_stack = new Stack();

    public void push(int item){
        items[size] = item;
        if (item >= max_stack.peek())
            max_stack.push(item);
        size += 1;
    }

    public int pop(){
        if (size == 0)
            return -1;
        int val = items[size - 1];
        if (val == max_stack.peek())
            max_stack.pop();
        size -= 1;
        return val;
    }

    public int get_max() {
        return max_stack.peek();
    }

}

public class problem20_largest_stack {
    public static void main(String[] args) {
        MaxStack stack = new MaxStack();
        stack.push(1);
        System.out.println("get_max: " + stack.get_max());
        stack.push(5);
        stack.push(2);
        stack.push(3);
        System.out.println("get_max: " + stack.get_max());
        System.out.println("pop: " + stack.pop());
        System.out.println("peek: " + stack.peek());
        stack.push(5);
        System.out.println("pop: " + stack.pop());
        System.out.println("pop: " + stack.pop());
        System.out.println("pop: " + stack.pop());
        System.out.println("pop: " + stack.pop());
        System.out.println("peek: " + stack.peek());
        System.out.println("get_max: " + stack.get_max());
    }
}