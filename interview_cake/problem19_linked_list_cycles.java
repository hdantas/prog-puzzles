// You have a singly-linked list and want to check if it contains a cycle.
// A singly-linked list is built with Nodes, where each node has:

// node.next-the next node in the list.
// node.data-the data held in the node. For example, if our linked list stores people in line at the movies, node.data might be the person's name.
// A cycle occurs when a node's next points back to a previous node in the list. The linked list is no longer linear with a beginning and end-instead, it cycles through a loop of nodes.

// Write a function contains_cycle() that takes the first node in a singly-linked list and returns a boolean indicating whether the list contains a cycle.

// For this problem, you cannot make any changes to the Node class.

// src: https://www.interviewcake.com/question/linked-list-cycles?utm_source=weekly_email


public class problem19_linked_list_cycles {
	public static void main(String[] args) {
		Node[] chain = create_chain();
		System.out.println("answer me: " + contains_cycle(chain[0]));
	}

	public static boolean contains_cycle(Node first_node) {
		Node slow_runner = first_node;
		Node fast_runner = first_node;
		
		while(true) {
			try {
				slow_runner = slow_runner.next;
				fast_runner = fast_runner.next.next;
				if(slow_runner == fast_runner){
					return true;
				}
			} catch (NullPointerException e) {
				break;
			}
		}
		return false;
	}

	public static Node[] create_chain() {
		Node[] chain =  new Node[20];
		chain[0] = new Node();
		for (int i = 0; i < 19; i++) {
			chain[i + 1] = new Node();
			chain[i].next = chain[i + 1];
		}
		chain[19].next = new Node();//chain[0];
		return chain;
	}
}

class Node {
	Node next = null;
	String data = "";
}