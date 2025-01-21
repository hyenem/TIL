package Tree;

public class Tree_순회 {
	
	static char[] tree = {0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 0, 0, 'H','I'};
	
	public static void main(String[] args) {
		preorder(1);
		System.out.println();
		inorder(1);
		System.out.println();
		postorder(1);
		
		
	}
	
	// 매개변수로 트리의 루트 index 받기
	public static void preorder(int root) {
		if(root>=tree.length || tree[root]==0) {
			return;
		}
		System.out.print(tree[root]+"->");
		preorder(2*root);
		preorder(2*root+1);
	}
	public static void inorder(int root) {
		if(root>=tree.length || tree[root]==0) {
			return;
		}
		inorder(2*root);
		System.out.print(tree[root]+"->");
		inorder(2*root+1);
	}
	public static void postorder(int root) {
		if(root>=tree.length || tree[root]==0) {
			return;
		}
		postorder(2*root);
		postorder(2*root+1);
		System.out.print(tree[root]+"->");
	}
}
