// Implement a queue with 2 stacks. Your queue should have an enqueue and a dequeue function and it should be "first in first out" (FIFO).
// Optimize for the time cost of m function calls on your queue. These can be any mix of enqueue and dequeue calls.

// Assume you already have a stack implementation and it gives O(1) time push and pop.

// src: https://www.interviewcake.com/question/queue-two-stacks?utm_source=weekly_email
import java.util.Stack;

class Queue {
	Stack<Integer> in_stack = new Stack<Integer>();
	Stack<Integer> out_stack = new Stack<Integer>();

	void enqueue(int item) {	
		in_stack.push(item);
	}

	int dequeue() {
		if (out_stack.empty()) {
			while(!in_stack.empty())
				out_stack.push(in_stack.pop());
			
			return out_stack.pop();
		}

		return out_stack.pop();
	}

}

public class problem21_queue_two_stacks {
	public static void main(String[] args) {
		Queue queue = new Queue();
		queue.enqueue(1);
		queue.enqueue(5);
		queue.enqueue(2);
		queue.enqueue(3);
		System.out.println("dequeue: " + queue.dequeue());
		queue.enqueue(5);
		System.out.println("dequeue: " + queue.dequeue());
		System.out.println("dequeue: " + queue.dequeue());
		System.out.println("dequeue: " + queue.dequeue());
		System.out.println("dequeue: " + queue.dequeue());
	}
}