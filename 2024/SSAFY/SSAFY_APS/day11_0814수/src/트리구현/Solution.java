package 트리구현;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

class Node{
	int idx;
	Node parent;
	LinkedList<Node> child = new LinkedList<>();
	Node(int idx){
		this.idx = idx;
	}
}

class Tree {
	Node root;
	int idx = 1;
	Map<Integer, Node> indexMap = new HashMap<Integer,Node>();

	Tree(){
		root = new Node(1);
		indexMap.put(1, root);
	}

	void insert(int parent) {
		Node parentNode = indexMap.get(parent);
		Node newNode = new Node(++idx);
		newNode.parent = parentNode;
		parentNode.child.add(newNode);
	}

	void delete(int child) {
		Node nowNode = indexMap.get(child);
		nowNode.parent.child.remove(nowNode);
	}
}

public class Solution {

}