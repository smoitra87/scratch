import java.util.*;


public class SymmetricTree {

	public static void main(String[] args) {
		Node root = new Node();		
		System.out.println(checkSymmetric(root));
	}

	public static boolean checkSymmetric(Node root) { 
		if (root == null || root.left == root.right 
			&& root.left == null) {
			return true;
		}
	
		if(root.left == null || root.right == null)  { 
			return false;
		}

		Stack<Integer> lst = new Stack<>();
		Stack<Integer> rst = new Stack<>();
		lst.push(root.left);
		rst.push(root.right);	

		while(true) { 
			Node lNode = lst.pop();
			Node rNode = rst.pop();
			if(lNode == null || rNode == null) { 
				return false;
			}
			
			

		}
		return true;
	
	}

	private static class Node {
		public Node left, right;
		public int val;

	}

}
