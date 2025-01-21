package 이진트리구현;

import java.util.ArrayList;
class Node{
	Node left = null;
	Node right = null;
	String data;
	Node(){}
	Node(String data){
		this.data = data;
	}
}

class binaryTree{
	Node root;
	Node[] arr = new Node[215];
	
	binaryTree() {
		root = new Node();
		arr[1] = root;
	}
	
	void insert(int parent, String data) {
		if(arr[2*parent]!=null) {
			if(arr[2*parent+1]!=null) return;
			else {
				Node newNode = new Node(data);
				arr[2*parent+1]= newNode;
				arr[parent].right = newNode;
			}
		} else {
			Node newNode = new Node(data);
			arr[2*parent]=newNode;
			arr[parent].left = newNode;
		}
	}
	
	void delete(int child) {
		if (arr[child]==null) return;
		if(child%2==0) arr[child/2].left = null;
		else arr[child/2].right = null;
	}
}

public class Solution {
	
	static binaryTree tree = new binaryTree();
	
	public static void main(String[] args) {
		tree.root.data = "A";
		tree.insert(1, "B");
		tree.insert(1, "C");
		tree.insert(2, "D");
		tree.insert(2, "E");
		tree.insert(3, "F");
		tree.insert(3, "G");
		tree.insert(5, "H");
		tree.insert(5, "I");
		
		preorder(1);
		System.out.println();
		inorder(1);
		System.out.println();
		postorder(1);
	}
	
	static void preorder(int root) {
		if(root>=tree.arr.length || tree.arr[root]==null) return;
		System.out.print(tree.arr[root].data+"->");
		preorder(root*2);
		preorder(root*2+1);
	}
	static void inorder(int root) {
		if(root>=tree.arr.length || tree.arr[root]==null) return;
		inorder(root*2);
		System.out.print(tree.arr[root].data+"->");
		inorder(root*2+1);
	}
	static void postorder(int root) {
		if(root>=tree.arr.length || tree.arr[root]==null) return;
		postorder(root*2);
		postorder(root*2+1);
		System.out.print(tree.arr[root].data+"->");
	}
}

